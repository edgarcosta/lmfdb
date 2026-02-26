# quaternion — Database Schema

**2 tables, 19 columns total**

### Tables

- [quaternion_orders](#quaternion_orders) (578 rows)
- [quaternion_orders_polarized](#quaternion_orders_polarized) (377 rows)

---

## quaternion_orders

a table of quaternion orders

**Rows:** 578

**API:** https://www.lmfdb.org/api/quaternion_orders/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `area_denominator` | `integer` | Denominator of Area / (4 pi) where area is the area of the fundmaental domain for O^1 | integer |
| `area_numerator` | `integer` | Numerator of Area / (4 pi) where area is the area of the fundmaental domain for O^1 | integer |
| `discB` | `integer` | discriminant of B | integer |
| `discO` | `integer` | discriminant of O | integer |
| `gens_denominators` | `integer[]` | the LCMs of the denominators of the basis elements | list of integers |
| `gens_numerators` | `integer[]` | the numerators of the basis of O in terms of generators of B | list of integers |
| `i_square` | `integer` | $i^2$ | integer |
| `j_square` | `integer` | $j^2$ | integer |
| `label` | `text` | the label of the quaternion order, of the format discB.discO or just discB if O is maximal | string label |

---

## quaternion_orders_polarized

a table of polarized quaternion orders

**Rows:** 377

**API:** https://www.lmfdb.org/api/quaternion_orders_polarized/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `AutmuO_generators` | `integer[]` | generators of AutmuO, written in terms of the basis of O | list of integers |
| `AutmuO_is_cyclic` | `boolean` | whether AutmuO is cyclic | boolean |
| `AutmuO_label` | `text` | the group label of AutmuO | string label (cross-reference) |
| `AutmuO_size` | `integer` | the size of AutmuO | integer |
| `Gerby_gen` | `integer[]` | generators of the kernel of the full enhanced semidirect product acting on the upper and lowe half plane | list of integers |
| `deg_mu` | `integer` | the degree of the polarized element mu | integer |
| `label` | `text` | the label of the polarized quaternion order, of the format discB.discO.deg_mu or just discO.deg_mu if O is maximal | string label |
| `mu` | `integer[]` | the polarized element mu, written in terms of the basis of O | list of integers |
| `nrd_mu` | `integer` | the reduced norm of the polarized element mu | integer |
| `order_label` | `text` | the label of the quaternion order | string label (cross-reference) |

---
