# fq — Database Schema

**1 tables, 4 columns total**

### Tables

- [fq_fields](#fq_fields) (35,352 rows)

---

## fq_fields

**Rows:** 35,352

**API:** https://www.lmfdb.org/api/fq_fields/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `characteristic` | `bigint` | The characteristic of the field | integer |
| `conway` | `smallint` | 1 if it is a Conway polynomial, 0 otherwise | integer |
| `degree` | `integer` | The degree of the field over its prime field | positive integer |
| `polynomial` | `jsonb` | Coefficients of the defining polynomial over the prime field | Coefficients of the defining polynomial over the prime field (JSON array) |

---
