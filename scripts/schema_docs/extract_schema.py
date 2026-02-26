#!/usr/bin/env python3
"""
Extract LMFDB database table schemas into JSON files grouped by module prefix.

Usage:
    sage -python scripts/schema_docs/extract_schema.py

Output:
    scripts/schema_docs/json/<prefix>.json  — one file per module prefix
"""

import json
import os
import sys
from collections import defaultdict
from decimal import Decimal

# Ensure the LMFDB root (parent of scripts/) is on the path
_lmfdb_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _lmfdb_root not in sys.path:
    sys.path.insert(0, _lmfdb_root)


def json_serializer(obj):
    """Handle types that aren't JSON-serializable."""
    if isinstance(obj, Decimal):
        if obj == int(obj):
            return int(obj)
        return float(obj)
    if isinstance(obj, bytes):
        return f"<bytes: {len(obj)} bytes>"
    if isinstance(obj, memoryview):
        return f"<bytes: {len(obj)} bytes>"
    if isinstance(obj, set):
        return sorted(obj)
    return str(obj)


def extract_sample_row(table):
    """Get a sample row from a table, returning None on failure."""
    try:
        row = table.lucky({}, projection=2)
        if row is None:
            return None
        # Convert to JSON-safe dict
        safe = {}
        for k, v in row.items():
            try:
                json.dumps(v)
                safe[k] = v
            except (TypeError, ValueError):
                safe[k] = json_serializer(v)
        return safe
    except Exception as e:
        return {"_error": str(e)}


def get_table_prefix(table_name):
    """Extract module prefix from table name (part before first underscore)."""
    i = table_name.find('_')
    if i == -1:
        return table_name
    return table_name[:i]


def extract_all_schemas(output_dir):
    from lmfdb import db

    os.makedirs(output_dir, exist_ok=True)

    grouped = defaultdict(dict)
    total_tables = 0
    total_cols = 0

    for table_name in sorted(db.tablenames):
        table = db[table_name]
        prefix = get_table_prefix(table_name)

        # Get column info
        search_cols = sorted(table.search_cols)
        extra_cols = sorted(table.extra_cols)
        col_types = dict(table.col_type)

        # Get descriptions (may fail if knowl db is not populated)
        try:
            table_desc = table.description()
        except Exception:
            table_desc = "(unavailable)"

        try:
            col_descs = table.column_description()
        except Exception:
            col_descs = {}

        # Get row count
        try:
            count = table.count()
        except Exception:
            count = -1

        # Get a sample row
        sample = extract_sample_row(table)

        # Build column list
        columns = []
        for col in search_cols:
            columns.append({
                "name": col,
                "type": col_types.get(col, "unknown"),
                "category": "search",
                "description": col_descs.get(col, ""),
            })
        for col in extra_cols:
            columns.append({
                "name": col,
                "type": col_types.get(col, "unknown"),
                "category": "extra",
                "description": col_descs.get(col, ""),
            })

        table_info = {
            "name": table_name,
            "prefix": prefix,
            "description": table_desc,
            "count": count,
            "columns": columns,
            "sample_row": sample,
        }

        grouped[prefix][table_name] = table_info
        total_tables += 1
        total_cols += len(columns)
        print(f"  {table_name}: {len(columns)} columns, {count} rows")

    # Write one JSON file per prefix
    for prefix, tables in sorted(grouped.items()):
        outpath = os.path.join(output_dir, f"{prefix}.json")
        with open(outpath, 'w') as f:
            json.dump(tables, f, indent=2, default=json_serializer)

    print(f"\nDone: {total_tables} tables, {total_cols} columns across {len(grouped)} prefixes")
    print(f"Output in: {output_dir}")
    return grouped


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "json")
    extract_all_schemas(output_dir)
