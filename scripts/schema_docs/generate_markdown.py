#!/usr/bin/env python3
"""
Generate markdown documentation from extracted LMFDB table schemas.

Usage:
    sage -python scripts/schema_docs/generate_markdown.py

Reads from:  scripts/schema_docs/json/*.json
Writes to:   scripts/schema_docs/<prefix>.md, index.md
"""

import json
import os
import glob

from annotations import MATH_TYPES


def escape_md(text):
    """Escape pipe characters for markdown table cells."""
    if not text:
        return ""
    return text.replace("|", "\\|").replace("\n", " ")


def infer_math_type(table_name, col_name, pg_type, description, sample_value):
    """
    Infer the mathematical type from column metadata and sample data.
    Returns a string description or "**TODO**" if unknown.
    """
    # Check hand-curated annotations first
    key = f"{table_name}.{col_name}"
    if key in MATH_TYPES:
        return MATH_TYPES[key]

    # Common patterns based on column name and type
    name_lower = col_name.lower()

    # Label columns
    if name_lower in ("label", "lmfdb_label", "cremona_label"):
        return "string label"
    if name_lower.endswith("_label"):
        return "string label (cross-reference)"
    if name_lower.endswith("_url") or name_lower == "url":
        return "URL string"

    # Known integer semantics
    if name_lower == "conductor":
        return "positive integer"
    if name_lower == "rank":
        return "non-negative integer"
    if name_lower in ("degree", "deg"):
        return "positive integer"
    if name_lower == "genus" or name_lower == "g":
        return "non-negative integer (genus)"
    if name_lower == "level":
        return "positive integer"
    if name_lower == "weight" or name_lower == "k":
        return "positive integer (weight)"
    if name_lower == "dimension" or name_lower == "dim":
        return "non-negative integer"
    if name_lower == "class_number":
        return "positive integer"
    if name_lower == "discriminant" or name_lower == "disc":
        return "integer (discriminant)"

    # Array types with known semantics
    if name_lower == "jinv" and "numeric" in pg_type:
        return "rational number as [numerator, denominator]"
    if name_lower == "ainvs":
        return "list of 5 integers [a1, a2, a3, a4, a6]"
    if name_lower in ("coefficients", "coeffs"):
        return "polynomial coefficients"

    # Boolean
    if pg_type == "boolean":
        return "boolean"

    # Portrait / image
    if name_lower == "portrait" or pg_type == "bytea":
        return "binary image data (PNG)"

    # Infer from PostgreSQL type
    if pg_type in ("integer", "bigint", "smallint"):
        if "count" in name_lower or name_lower.startswith("num_"):
            return "non-negative integer (count)"
        return "integer"
    if pg_type == "numeric":
        return "arbitrary-precision integer"
    if pg_type in ("double precision", "real"):
        return "floating-point approximation"
    if pg_type == "text":
        return "text"
    if pg_type == "text[]":
        return "list of strings"

    # Array types — try to use sample data
    if pg_type == "numeric[]":
        if sample_value is not None and isinstance(sample_value, list):
            if len(sample_value) == 2:
                return "rational as [num, den] or list of 2 integers (**TODO**: verify)"
            return f"list of integers (length {len(sample_value)} in sample)"
        return "list of arbitrary-precision integers"
    if pg_type in ("integer[]", "bigint[]"):
        return "list of integers"
    if pg_type == "smallint[]":
        return "list of small integers"
    if pg_type == "double precision[]":
        return "list of floats"

    if pg_type == "jsonb":
        # Use the knowl description if informative
        desc_lower = (description or "").lower()
        if desc_lower and "not yet updated" not in desc_lower and len(description) > 5:
            shape = ""
            if sample_value is not None:
                if isinstance(sample_value, list):
                    shape = " (JSON array)"
                elif isinstance(sample_value, dict):
                    shape = " (JSON object)"
            return escape_md(description)[:80] + shape
        if sample_value is not None:
            if isinstance(sample_value, list):
                return "JSON array (**TODO**: describe structure)"
            if isinstance(sample_value, dict):
                return "JSON object (**TODO**: describe structure)"
        return "JSON (**TODO**: describe structure)"

    return "**TODO**"


def generate_table_md(table_name, table_info):
    """Generate markdown for a single table."""
    lines = []
    lines.append(f"## {table_name}")
    lines.append("")

    desc = table_info.get("description", "")
    if desc and desc != "(unavailable)" and "not yet updated" not in desc:
        lines.append(f"{desc}")
        lines.append("")

    count = table_info.get("count", -1)
    if count >= 0:
        lines.append(f"**Rows:** {count:,}")
        lines.append("")

    lines.append(f"**API:** https://www.lmfdb.org/api/{table_name}/")
    lines.append("")

    columns = table_info.get("columns", [])
    if not columns:
        lines.append("*(no columns)*")
        lines.append("")
        return "\n".join(lines)

    sample = table_info.get("sample_row") or {}

    # Table header
    lines.append("| Column | Type | Description | Mathematical Type |")
    lines.append("|--------|------|-------------|-------------------|")

    for col in columns:
        name = col["name"]
        pg_type = col["type"]
        desc = col.get("description", "")
        sample_val = sample.get(name)

        math_type = infer_math_type(table_name, name, pg_type, desc, sample_val)

        # Truncate long descriptions for the table
        desc_short = escape_md(desc)
        if len(desc_short) > 120:
            desc_short = desc_short[:117] + "..."

        lines.append(f"| `{name}` | `{pg_type}` | {desc_short} | {math_type} |")

    lines.append("")
    return "\n".join(lines)


def generate_prefix_md(prefix, tables):
    """Generate the full markdown file for a module prefix."""
    lines = []
    lines.append(f"# {prefix} — Database Schema")
    lines.append("")

    table_count = len(tables)
    total_cols = sum(len(t.get("columns", [])) for t in tables.values())
    lines.append(f"**{table_count} tables, {total_cols} columns total**")
    lines.append("")

    # Table of contents
    lines.append("### Tables")
    lines.append("")
    for tname in sorted(tables.keys()):
        count = tables[tname].get("count", -1)
        count_str = f" ({count:,} rows)" if count >= 0 else ""
        lines.append(f"- [{tname}](#{tname}){count_str}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Each table
    for tname in sorted(tables.keys()):
        lines.append(generate_table_md(tname, tables[tname]))
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def generate_index_md(all_data):
    """Generate the top-level index.md."""
    lines = []
    lines.append("# LMFDB Database Schema Documentation")
    lines.append("")
    lines.append("Comprehensive documentation of all database tables in the LMFDB.")
    lines.append("")

    total_tables = sum(len(tables) for tables in all_data.values())
    total_cols = sum(
        sum(len(t.get("columns", [])) for t in tables.values())
        for tables in all_data.values()
    )
    lines.append(f"**{total_tables} tables across {len(all_data)} module prefixes, {total_cols} columns total**")
    lines.append("")
    lines.append("## Reference")
    lines.append("")
    lines.append("- [Type Conventions](type_conventions.md) — how PostgreSQL types map to mathematical objects")
    lines.append("")

    lines.append("## Modules")
    lines.append("")
    lines.append("| Prefix | Tables | Columns | Description |")
    lines.append("|--------|--------|---------|-------------|")

    prefix_descriptions = {
        "ec": "Elliptic curves over Q",
        "mf": "Modular forms",
        "nf": "Number fields",
        "g2c": "Genus 2 curves",
        "gps": "Finite groups",
        "lfunc": "L-functions",
        "modcurve": "Modular curves",
        "belyi": "Belyi maps",
        "av": "Abelian varieties over finite fields",
        "lf": "Local fields (p-adic fields)",
        "hgm": "Hypergeometric motives",
        "hmf": "Hilbert modular forms",
        "artin": "Artin representations",
        "bmf": "Bianchi modular forms",
        "smf": "Siegel modular forms",
        "hecke": "Hecke algebras",
        "lat": "Lattices",
        "halfmf": "Half-integral weight modular forms",
        "hgcwa": "Higher genus curves with automorphisms",
        "char": "Dirichlet characters",
        "st": "Sato-Tate groups",
        "cluster": "Cluster pictures",
        "ecnf": "Elliptic curves over number fields",
        "modlgal": "Mod-ell Galois representations",
        "modlmf": "Mod-ell modular forms",
        "gg": "Galois groups (transitive groups)",
        "fq": "Isogeny classes over finite fields",
        "maass": "Maass forms",
        "lfunc": "L-functions",
        "crystals": "Crystals",
    }

    for prefix in sorted(all_data.keys()):
        tables = all_data[prefix]
        n_tables = len(tables)
        n_cols = sum(len(t.get("columns", [])) for t in tables.values())
        desc = prefix_descriptions.get(prefix, "")
        lines.append(f"| [{prefix}]({prefix}.md) | {n_tables} | {n_cols} | {desc} |")

    lines.append("")
    return "\n".join(lines)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_dir = os.path.join(script_dir, "json")

    if not os.path.exists(json_dir):
        print(f"Error: {json_dir} does not exist. Run extract_schema.py first.")
        sys.exit(1)

    json_files = sorted(glob.glob(os.path.join(json_dir, "*.json")))
    if not json_files:
        print(f"Error: No JSON files found in {json_dir}. Run extract_schema.py first.")
        sys.exit(1)

    all_data = {}
    for jf in json_files:
        prefix = os.path.splitext(os.path.basename(jf))[0]
        with open(jf) as f:
            all_data[prefix] = json.load(f)

    # Generate per-prefix markdown files
    for prefix, tables in sorted(all_data.items()):
        md = generate_prefix_md(prefix, tables)
        outpath = os.path.join(script_dir, f"{prefix}.md")
        with open(outpath, 'w') as f:
            f.write(md)
        print(f"  {prefix}.md: {len(tables)} tables")

    # Generate index
    index_md = generate_index_md(all_data)
    with open(os.path.join(script_dir, "index.md"), 'w') as f:
        f.write(index_md)
    print("  index.md")

    total_tables = sum(len(t) for t in all_data.values())
    print(f"\nDone: {total_tables} tables documented in {len(all_data)} files + index.md")


if __name__ == "__main__":
    import sys
    main()
