# hmf — Database Schema

**4 tables, 43 columns total**

### Tables

- [hmf_fields](#hmf_fields) (400 rows)
- [hmf_forms](#hmf_forms) (368,356 rows)
- [hmf_forms_temp](#hmf_forms_temp) (0 rows)
- [hmf_hecke](#hmf_hecke) (368,356 rows)

---

## hmf_fields

Information on base fields for Hilbert modular forms

**Rows:** 400

**API:** https://www.lmfdb.org/api/hmf_fields/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `degree` | `smallint` | field degree | positive integer |
| `discriminant` | `bigint` | field discriminant | integer (discriminant) |
| `ideals` | `jsonb` | fixed ordered list of ideals | fixed ordered list of ideals (JSON array) |
| `label` | `text` | field label | string label |
| `narrow_class_no` | `smallint` | narrow class number | integer |
| `primes` | `jsonb` | fixed ordered list of primes | fixed ordered list of primes (JSON array) |

---

## hmf_forms

**Rows:** 368,356

**API:** https://www.lmfdb.org/api/hmf_forms/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `deg` | `smallint` | degree of base field | degree [F:Q] of base field |
| `dimension` | `integer` | dimension of the newform (the absolute degree of its Hecke field) | dimension of the eigenspace |
| `disc` | `bigint` | discriminant of base field | discriminant of base field |
| `field_bad_primes` | `integer[]` | ramified primes of base field | list of integers |
| `field_label` | `text` | LMFDB label of base field | base totally real number field label |
| `is_CM` | `text` | CM flag | boolean, has complex multiplication |
| `is_base_change` | `text` | base-change flag | boolean, arises as base change from Q or smaller field |
| `label` | `text` | form label | HMF label: field_label-level_label-label_suffix |
| `label_nsuffix` | `smallint` | label numerical suffix | integer |
| `label_suffix` | `text` | label (alpha) suffix | text |
| `level_bad_primes` | `integer[]` | primes dividing level norm | list of integers |
| `level_ideal` | `text` | level ideal definition | text |
| `level_label` | `text` | level ideal label | level ideal label |
| `level_norm` | `integer` | level ideal norm | norm of level ideal |
| `parallel_weight` | `smallint` | parallel weight | common weight k if all weights equal (parallel weight) |
| `short_label` | `text` | form short label | string label (cross-reference) |
| `weight` | `text` | weight | weight vector [k1,...,kd] (one weight per real embedding) |

---

## hmf_forms_temp

**Rows:** 0

**API:** https://www.lmfdb.org/api/hmf_forms_temp/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `deg` | `smallint` | (description not yet updated on this server) | positive integer |
| `dimension` | `integer` | (description not yet updated on this server) | non-negative integer |
| `disc` | `bigint` | (description not yet updated on this server) | integer (discriminant) |
| `field_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `hecke_field` | `jsonb` | (description not yet updated on this server) | JSON (unpopulated staging column, table has 0 rows): intended to store Hecke eigenvalue field polynomial |
| `is_CM` | `text` | (description not yet updated on this server) | text |
| `is_base_change` | `text` | (description not yet updated on this server) | text |
| `label` | `text` | (description not yet updated on this server) | string label |
| `label_nsuffix` | `smallint` | (description not yet updated on this server) | integer |
| `label_suffix` | `text` | (description not yet updated on this server) | text |
| `level_ideal` | `text` | (description not yet updated on this server) | text |
| `level_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `level_norm` | `integer` | (description not yet updated on this server) | integer |
| `parallel_weight` | `smallint` | (description not yet updated on this server) | integer |
| `short_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `weight` | `text` | (description not yet updated on this server) | positive integer (weight) |

---

## hmf_hecke

**Rows:** 368,356

**API:** https://www.lmfdb.org/api/hmf_hecke/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `AL_eigenvalues` | `jsonb` | Atkin-Lehner eigenvalues | Atkin-Lehner eigenvalues (JSON array) |
| `hecke_eigenvalues` | `jsonb` | Hecke eigenvalues | Hecke eigenvalues (JSON array) |
| `hecke_polynomial` | `text` | defining polynomial for Hecke field | text |
| `label` | `text` | form label | string label |

---
