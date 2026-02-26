# maass — Database Schema

**6 tables, 31 columns total**

### Tables

- [maass_newforms](#maass_newforms) (14,995 rows)
- [maass_newforms_coefficients](#maass_newforms_coefficients) (14,995 rows)
- [maass_portraits](#maass_portraits) (14,995 rows)
- [maass_rigor](#maass_rigor) (35,416 rows)
- [maass_rigor_coefficients](#maass_rigor_coefficients) (35,416 rows)
- [maass_rigor_portraits](#maass_rigor_portraits) (35,416 rows)

---

## maass_newforms

**Rows:** 14,995

**API:** https://www.lmfdb.org/api/maass_newforms/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `conrey_index` | `smallint` | second number in the Conrey label q.n for the character of this newform | integer |
| `contributor` | `text` | name of the person or persons who contributed the data | text |
| `error` | `numeric` | size of the error interval on the coefficients (not always set and not rigorous) | arbitrary-precision integer |
| `fricke_eigenvalue` | `smallint` | the sign of the Fricke involution +/-1 | integer |
| `level` | `smallint` | the level of the newform (a positive integer) | positive integer |
| `maass_id` | `text` | unique identifier which serves as the label of the Maass newform | text |
| `spectral_parameter` | `numeric` | the real number R such that the Laplace eignvalue is lambda = 1/4 + R^2 | arbitrary-precision integer |
| `symmetry` | `smallint` | odd=-1, even=+1 | integer |
| `weight` | `smallint` | weight of the newform (0 or 1, currently always 0) | positive integer (weight) |
| `coefficients` | `numeric[]` | list of real numbers giving the Fourier coefficients of the newform | polynomial coefficients |

---

## maass_newforms_coefficients

Fourier coefficients for Maass forms (matching the maass_newforms table)

**Rows:** 14,995

**API:** https://www.lmfdb.org/api/maass_newforms_coefficients/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `coefficients` | `numeric[]` | list of real numbers giving the Fourier coefficients of the newform | polynomial coefficients |
| `maass_id` | `text` | unique identifier which serves as the label of the Maass newform | text |

---

## maass_portraits

**Rows:** 14,995

**API:** https://www.lmfdb.org/api/maass_portraits/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `maass_id` | `text` | unique identifier which serves as the label of the Maass newform | text |
| `portrait` | `text` | base-64 encoded gif containing a plot of the newform shown in the properties box | binary image data (PNG) |

---

## maass_rigor

Rigorous Maass forms

**Rows:** 35,416

**API:** https://www.lmfdb.org/api/maass_rigor/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `conrey_index` | `smallint` | (description not yet updated on this server) | integer |
| `fricke_eigenvalue` | `smallint` | (description not yet updated on this server) | +1 or -1 (or 0 if unknown) |
| `level` | `smallint` | (description not yet updated on this server) | positive integer level |
| `maass_index` | `text` | (description not yet updated on this server) | text |
| `maass_label` | `text` | (description not yet updated on this server) | Maass form label: level.weight.conrey.spectral_index |
| `nspec` | `smallint` | (description not yet updated on this server) | integer |
| `spectral_error` | `numeric` | (description not yet updated on this server) | arbitrary-precision integer |
| `spectral_parameter` | `numeric` | (description not yet updated on this server) | eigenvalue R of Laplacian: lambda = 1/4 + R^2. High-precision real |
| `symmetry` | `smallint` | (description not yet updated on this server) | 0 = even, 1 = odd |
| `weight` | `smallint` | (description not yet updated on this server) | integer weight (currently always 0) |
| `coefficient_errors` | `numeric[]` | (description not yet updated on this server) | list of arbitrary-precision integers |
| `coefficients` | `numeric[]` | (description not yet updated on this server) | Fourier coefficients a_n as list of real numbers |

---

## maass_rigor_coefficients

Fourier coefficients for Maass forms (matching the maass_rigor table)

**Rows:** 35,416

**API:** https://www.lmfdb.org/api/maass_rigor_coefficients/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `coefficient_errors` | `numeric[]` | radii for balls around the corresponding entry in coefficients so that the actual value is contained in the ball | list of arbitrary-precision integers |
| `coefficients` | `numeric[]` | Fourier coefficients | polynomial coefficients |
| `maass_label` | `text` | the label for the Maass form | string label (cross-reference) |

---

## maass_rigor_portraits

Portraits for Maass forms

**Rows:** 35,416

**API:** https://www.lmfdb.org/api/maass_rigor_portraits/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `maass_label` | `text` | the label for the Maass form | string label (cross-reference) |
| `portrait` | `text` | base64 encoded png of the Maass form | binary image data (PNG) |

---
