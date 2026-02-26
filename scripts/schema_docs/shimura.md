# shimura — Database Schema

**1 tables, 6 columns total**

### Tables

- [shimura_curves](#shimura_curves) (236 rows)

---

## shimura_curves

table of Shimura curves

**Rows:** 236

**API:** https://www.lmfdb.org/api/shimura_curves/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `atkin_lehner` | `integer[]` | atkin-lehner involution | list of integers |
| `disc` | `integer` | discriminant | integer (discriminant) |
| `genus` | `smallint` | genus | non-negative integer (genus) |
| `label` | `text` | D<discriminant>N<level><atkin-lehner | string label |
| `level` | `integer` | level | positive integer |
| `model` | `text` | model of the curve | text |

---
