# test — Database Schema

**3 tables, 10 columns total**

### Tables

- [test_rewrite](#test_rewrite) (1 rows)
- [test_table](#test_table) (16 rows)
- [test_xyz](#test_xyz) (100,000 rows)

---

## test_rewrite

**Rows:** 1

**API:** https://www.lmfdb.org/api/test_rewrite/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `label` | `text` | (description not yet updated on this server) | string label |
| `x` | `numeric` | (description not yet updated on this server) | arbitrary-precision integer |

---

## test_table

test table

**Rows:** 16

**API:** https://www.lmfdb.org/api/test_table/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `label` | `text` | Label of the test entry | string label |
| `tex_name` | `text` | Latex form | text |

---

## test_xyz

**Rows:** 100,000

**API:** https://www.lmfdb.org/api/test_xyz/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `bar` | `bigint` | bar | integer |
| `col1` | `text` | (description not yet updated on this server) | text |
| `col2` | `text` | (description not yet updated on this server) | text |
| `foo` | `bigint` | foo | integer |
| `col3` | `text` | (description not yet updated on this server) | text |
| `col4` | `text` | (description not yet updated on this server) | text |

---
