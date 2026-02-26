# hecke — Database Schema

**3 tables, 28 columns total**

### Tables

- [hecke_algebras](#hecke_algebras) (1,421 rows)
- [hecke_ladic](#hecke_ladic) (3,771 rows)
- [hecke_orbits](#hecke_orbits) (454 rows)

---

## hecke_algebras

**Rows:** 1,421

**API:** https://www.lmfdb.org/api/hecke_algebras/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `label` | `text` | (description not yet updated on this server) | Hecke algebra label |
| `level` | `integer` | (description not yet updated on this server) | positive integer level |
| `num_orbits` | `smallint` | (description not yet updated on this server) | number of Hecke orbits |
| `weight` | `integer` | (description not yet updated on this server) | positive integer weight |

---

## hecke_ladic

**Rows:** 3,771

**API:** https://www.lmfdb.org/api/hecke_ladic/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `ell` | `smallint` | (description not yet updated on this server) | integer |
| `field` | `jsonb` | (description not yet updated on this server) | JSON [index, degree, poly_string, index2]: l-adic coefficient field. field[1]=degree, field[2]=defining polynomial as string |
| `idempotent` | `text` | (description not yet updated on this server) | text |
| `index` | `smallint` | (description not yet updated on this server) | integer |
| `label_l` | `text` | (description not yet updated on this server) | text |
| `level` | `integer` | (description not yet updated on this server) | positive integer |
| `num_charpoly_ql` | `smallint` | (description not yet updated on this server) | non-negative integer (count) |
| `operators` | `jsonb` | (description not yet updated on this server) | JSON list of Hecke operators T_p mod l. Each entry = flat list of dim^2 integers (row-major matrix over Z/lZ) |
| `orbit_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `properties` | `jsonb` | (description not yet updated on this server) | JSON [grading_list, gorenstein_defect]: grading_list = list of ints, gorenstein_defect = int (0 means Gorenstein) |
| `structure` | `jsonb` | (description not yet updated on this server) | JSON [dim, num_gens, gens_sage_str, rels_sage_str]: dimension, number of generators, SageMath-evaluable strings for generators and relations |
| `weight` | `smallint` | (description not yet updated on this server) | positive integer (weight) |

---

## hecke_orbits

**Rows:** 454

**API:** https://www.lmfdb.org/api/hecke_orbits/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `Qalg_gen` | `jsonb` | (description not yet updated on this server) | JSON list of integers: indices of Hecke operators T_n generating the Hecke algebra over Q |
| `Qbasis` | `jsonb` | (description not yet updated on this server) | JSON list of integers: indices for a Q-basis of the Hecke algebra as a Q-vector space |
| `Zbasis` | `jsonb` | (description not yet updated on this server) | JSON list of flattened square matrices (each inner list has dim^2 entries as strings): Z-basis elements for the Hecke order, each stored row-major |
| `disc_fac` | `jsonb` | (description not yet updated on this server) | JSON list of [prime, exponent] pairs (as strings): prime factorization of the discriminant of the Hecke Z-order |
| `discriminant` | `numeric` | (description not yet updated on this server) | integer (discriminant) |
| `hecke_op` | `text` | (description not yet updated on this server) | text |
| `level` | `integer` | (description not yet updated on this server) | positive integer |
| `num_hecke_op` | `integer` | (description not yet updated on this server) | non-negative integer (count) |
| `orbit` | `smallint` | (description not yet updated on this server) | integer |
| `orbit_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `parent_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `weight` | `smallint` | (description not yet updated on this server) | positive integer (weight) |

---
