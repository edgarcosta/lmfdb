# shimcurve — Database Schema

**3 tables, 27 columns total**

### Tables

- [shimcurve_models](#shimcurve_models) (1 rows)
- [shimcurve_pictures](#shimcurve_pictures) (304 rows)
- [shimcurve_points](#shimcurve_points) (0 rows)

---

## shimcurve_models

Models for modular curves

**Rows:** 1

**API:** https://www.lmfdb.org/api/shimcurve_models/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `dont_display` | `boolean` | (description not yet updated on this server) | boolean |
| `equation` | `text[]` | (description not yet updated on this server) | list of strings |
| `model_type` | `smallint` | (description not yet updated on this server) | integer |
| `number_variables` | `smallint` | (description not yet updated on this server) | integer |
| `shimcurve` | `text` | (description not yet updated on this server) | text |
| `smooth` | `boolean` | (description not yet updated on this server) | boolean |

---

## shimcurve_pictures

Profile pictures for modular curves

**Rows:** 304

**API:** https://www.lmfdb.org/api/shimcurve_pictures/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `image` | `text` | (description not yet updated on this server) | text |
| `psl2label` | `text` | (description not yet updated on this server) | text |

---

## shimcurve_points

Rational points on modular curves

**Rows:** 0

**API:** https://www.lmfdb.org/api/shimcurve_points/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `Clabel` | `text` | Label in the LMFDB of the genus 2 curve corresponding to this point, if it exists | text |
| `Igusa_invs` | `text` | The Igusa invariants of the point | text |
| `cardinality` | `integer` | (description not yet updated on this server) | integer |
| `cm` | `smallint` | (description not yet updated on this server) | integer |
| `conductor_norm` | `numeric` | The norm of the conductor of the minimal twist of an elliptic curve corrsponding to this point | arbitrary-precision integer |
| `coordinates` | `jsonb` | A dictionary with keys the different model types and values a list of coordinates as strings with coordinates in term... | A dictionary with keys the different model types and values a list of coordinate |
| `curve_genus` | `integer` | The genus of the modular curve on which this point lies | integer |
| `curve_index` | `integer` | The index in GL(2,Z/N) of the modular curve on which this point lies | integer |
| `curve_label` | `text` | The label of the modular curve | string label (cross-reference) |
| `curve_level` | `integer` | The level of the modular curve on which this point lies | integer |
| `curve_name` | `text` | If applicable, the name of the modular curve such as X_0(N) | text |
| `degree` | `smallint` | (description not yet updated on this server) | positive integer |
| `isolated` | `smallint` | Whether the point is isolated (not in a family parameterized by a P1 or abelian variety) | integer |
| `j_field` | `text` | (description not yet updated on this server) | text |
| `j_height` | `double precision` | The height of the j-invariant | floating-point approximation |
| `jinv` | `text` | (description not yet updated on this server) | text |
| `jorig` | `text` | A comma separated list of rationals giving coordinates of the j-invariant in the residue field, when not rational and... | text |
| `quo_info` | `smallint[]` | (description not yet updated on this server) | list of small integers |
| `residue_field` | `text` | (description not yet updated on this server) | text |

---
