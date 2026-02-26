# hmsurfaces — Database Schema

**4 tables, 37 columns total**

### Tables

- [hmsurfaces_cusps](#hmsurfaces_cusps) (30,918 rows)
- [hmsurfaces_elliptic_pts](#hmsurfaces_elliptic_pts) (21,856 rows)
- [hmsurfaces_invs](#hmsurfaces_invs) (9,034 rows)
- [hmsurfaces_pictures](#hmsurfaces_pictures) (0 rows)

---

## hmsurfaces_cusps

Cusps on Hilbert modular surfaces

**Rows:** 30,918

**API:** https://www.lmfdb.org/api/hmsurfaces_cusps/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `M_label` | `text` | LMFDB label of the ideal M attached to the cusp | string label (cross-reference) |
| `coordinates` | `bigint[]` | [[a1,a2],[b1,b2]] indicate the cusp (a_1 + a_2 w : b_1 + b_2 w) as a point in P^1(F), where F = Q(w) | list of integers |
| `label` | `text` | Label of the Hilbert modular surface | string label |
| `repetition` | `integer` | Number of times self_intersections_minimal should be repeated to obtain the sequence of self-intersection numbers | integer |
| `self_intersections_minimal` | `integer[]` | Periodic part of the associated Hirzebruch-Jung continued fraction | list of integers |

---

## hmsurfaces_elliptic_pts

Elliptic points on Hilbert modular surfaces

**Rows:** 21,856

**API:** https://www.lmfdb.org/api/hmsurfaces_elliptic_pts/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `label` | `text` | Label of the Hilbert modular surface | string label |
| `nb` | `integer` | Number of elliptic points | integer |
| `rotation_type` | `integer[]` | Rotation type [n; a,b] | list of integers |

---

## hmsurfaces_invs

Invariants of Hilbert modular surfaces

**Rows:** 9,034

**API:** https://www.lmfdb.org/api/hmsurfaces_invs/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `K2` | `integer` | Self-intersection number of the canonical divisor | integer |
| `chi` | `integer` | Holomorphic Euler characteristic | integer |
| `comp_gens` | `bigint[]` | Coordinates for generators of component ideal | list of integers |
| `component_label` | `text` | Label of component as an ideal | string label (cross-reference) |
| `euler_nb` | `integer` | Euler number | integer |
| `field_discr` | `integer` | Discriminant of the number field | integer |
| `field_label` | `text` | Label of totally real field | string label (cross-reference) |
| `gamma_type` | `text` | Gamma type (0, 1 or f) | text |
| `group_type` | `text` | Group type (sl or gl) | text |
| `h11` | `integer` | Hodge number h^{1,1} | integer |
| `h20` | `integer` | Hodge number h^{2,0} | integer |
| `is_pp` | `boolean` | True iff the Hilbert surface classifies principally polarized abelian surfaces | boolean |
| `kodaira_dims` | `integer[]` | Possibilities for the Kodaira dimension | list of integers |
| `label` | `text` | Label | string label |
| `len_cusp_res` | `integer` | Number of curves in cusp resolutions | integer |
| `len_ell_res` | `integer` | Number of curves in elliptic point resolutions | integer |
| `len_res` | `integer` | Number of curves added to resolve singularities | integer |
| `level_gens` | `bigint[]` | Coordinates for generators of level ideal | list of integers |
| `level_label` | `text` | Label of level as an ideal | string label (cross-reference) |
| `level_norm` | `integer` | Norm of level | integer |
| `narrow_class_nb` | `integer` | Narrow class number of the number field | integer |
| `nb_cusps` | `integer` | Number of cusps on the Hilbert surface | integer |
| `nb_ell` | `integer` | Number of elliptic points on the Hilbert surface | integer |
| `nb_ell2` | `integer` | Number of elliptic points of order 2 | integer |
| `nb_ell3` | `integer` | Number of elliptic points of order 3 | integer |
| `nb_ell4` | `integer` | Number of elliptic points of order 4 | integer |
| `nb_ell5` | `integer` | Number of elliptic points of order 5 | integer |
| `nb_ell6` | `integer` | Number of elliptic points of order 6 | integer |

---

## hmsurfaces_pictures

Pictures attached to Hilbert modular surfaces

**Rows:** 0

**API:** https://www.lmfdb.org/api/hmsurfaces_pictures/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `label` | `text` | Label of the Hilbert modular surface | string label |

---
