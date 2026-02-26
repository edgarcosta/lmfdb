# LMFDB Type Conventions

How PostgreSQL storage types map to mathematical objects in the LMFDB.

## Scalar Types

| PostgreSQL Type | Mathematical Meaning | Notes |
|----------------|---------------------|-------|
| `smallint` | Small integer (−32768 to 32767) | Degrees, weights, genus, small counts |
| `integer` | Integer (−2^31 to 2^31−1) | Conductors, levels, moderate-sized invariants |
| `bigint` | Large integer (−2^63 to 2^63−1) | Internal IDs, very large counts |
| `numeric` | Arbitrary-precision integer | Discriminants, large conductors, exact large values |
| `double precision` | Floating-point approximation | Analytic conductors, heights, L-function zeros, analytic rank |
| `real` | Single-precision float | Less common; some approximations |
| `boolean` | True/false flag | CM indicator, self-dual, parity |
| `text` | String | Labels, latex strings, polynomial representations, string keys |
| `bytea` | Binary data | Portraits (PNG images) |

## Array Types

| PostgreSQL Type | Common Mathematical Meanings | Examples |
|----------------|------------------------------|----------|
| `smallint[]` | Partition, torsion invariants, short integer tuples | Torsion structure `[2,4]`, cycle type `[3,2,1]` |
| `integer[]` | Lists of moderate integers | Euler factor coefficients, Hecke eigenvalues |
| `bigint[]` | Lists of large integers | — |
| `numeric[]` | **Multiple conventions** (see below) | a-invariants, j-invariant, polynomial coefficients |
| `double precision[]` | List of floating-point values | Embeddings, approximate zeros |
| `text[]` | List of strings | Friend URLs, related labels |
| `boolean[]` | List of flags | — |

### `numeric[]` Conventions

This is the most overloaded type. Common conventions:

1. **Rational number as `[numerator, denominator]`**
   - Example: `jinv` in `ec_curvedata` — j-invariant stored as `[num, den]`
   - Example: `analytic_conductor` in some tables

2. **Polynomial coefficients**
   - Example: `coeffs` in `nf_fields` — defining polynomial of a number field
   - Convention: usually `[a0, a1, ..., an]` for a0 + a1*x + ... + an*x^n

3. **List of arbitrary-precision integers**
   - Example: `ainvs` in `ec_curvedata` — Weierstrass a-invariants `[a1, a2, a3, a4, a6]`
   - Example: `base_field` in `belyi_galmaps` — polredabs coefficients

4. **Number field element as list of rationals**
   - Each rational may itself be a pair `[num, den]` in a nested structure
   - Sometimes stored flat: `[c0, c1, ..., cn-1]` for c0 + c1*α + ... in the number field

## Structured Types

| PostgreSQL Type | Common Usage | Structure |
|----------------|-------------|-----------|
| `jsonb` | Complex nested data | Varies per column — see table-specific docs |

### Common `jsonb` Patterns

1. **List of lists** — e.g., Hecke eigenvalue data, embeddings per conjugate
2. **Dictionary/object** — e.g., specialization data, additional invariants
3. **Nested list of integers** — e.g., permutation triples in cycle notation
4. **Heterogeneous list** — e.g., `[integer, string, list]` tuples

## Label Conventions

Labels are stored as `text` and follow module-specific conventions:

| Module | Label Format | Example |
|--------|-------------|---------|
| `ec` (Q) | `conductor.isogeny_class.curve_number` | `11.a1` |
| `ecnf` | `field-conductor_norm-conductor_label-isogeny_class-curve_number` | `2.0.4.1-100.1-a1` |
| `nf` | `degree.r1.discriminant_abs.index` | `2.2.5.1` |
| `mf` | `level.weight.char_orbit.hecke_orbit` | `1.12.a.a` |
| `g2c` | `conductor.isogeny_class.curve_number` | `169.a.169.1` |
| `gps` | `order.counter` | `12.4` |
| `gg` | `degree.counter` | `5T3` (also uses nTt format) |
| `belyi` | `degTgroup-partition1_partition2_partition3-orbit` | `6T7-4.2_3.3_4.2-a` |

## Search vs Extra Columns

- **Search columns** (`search`): Indexed in PostgreSQL, usable in queries. These are the columns users can search on.
- **Extra columns** (`extra`): Stored in a separate table (`_extras`), not indexed. Retrieved only when displaying individual records, not during search.

This distinction affects performance: search columns have B-tree or GIN indexes; extra columns are fetched via a JOIN on the internal `id`.
