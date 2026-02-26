# hgm — Database Schema

**4 tables, 148 columns total**

### Tables

- [hgm_euler_survey](#hgm_euler_survey) (97,527 rows)
- [hgm_families](#hgm_families) (61,063 rows)
- [hgm_monodromy](#hgm_monodromy) (137,565 rows)
- [hgm_motives](#hgm_motives) (285 rows)

---

## hgm_euler_survey

**Rows:** 97,527

**API:** https://www.lmfdb.org/api/hgm_euler_survey/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `A` | `integer[]` | (description not yet updated on this server) | list of integers |
| `B` | `integer[]` | (description not yet updated on this server) | list of integers |
| `d` | `integer` | (description not yet updated on this server) | integer |
| `eulers` | `numeric[]` | (description not yet updated on this server) | Euler factor data at prime p |
| `label` | `text` | (description not yet updated on this server) | motive label |
| `p` | `integer` | (description not yet updated on this server) | prime |

---

## hgm_families

Families of hypergeometric motives

**Rows:** 61,063

**API:** https://www.lmfdb.org/api/hgm_families/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `A` | `jsonb` | List of a_i | list of alpha parameters (cyclotomic orders defining the hypergeometric datum) |
| `A2` | `jsonb` | 2-part of A after cancellation | 2-part of A after prime cancellation |
| `A2rev` | `jsonb` | 2-part of B after cancellation | 2-part of B after cancellation |
| `A3` | `jsonb` | 3-part of A after cancellation | 3-part of A |
| `A3rev` | `jsonb` | 3-part of B after cancellation | 3-part of B |
| `A5` | `jsonb` | 5-part of A after cancellation | 5-part of A |
| `A5rev` | `jsonb` | 5-part of B after cancellation | 5-part of B |
| `A7` | `jsonb` | 7-part of A after cancellation | 7-part of A |
| `A7rev` | `jsonb` | 7-part of B after cancellation | 7-part of B |
| `Arev` | `jsonb` | List of b_i | reversed/complementary alpha parameters |
| `Au2` | `jsonb` | Prime-to-2-part of A after cancellation | prime-to-2-part of A |
| `Au2rev` | `jsonb` | Prime-to-2-part of B after cancellation | prime-to-2-part of B |
| `Au3` | `jsonb` | Prime-to-3-part of A after cancellation | prime-to-3-part of A |
| `Au3rev` | `jsonb` | Prime-to-3-part of B after cancellation | prime-to-3-part of B |
| `Au5` | `jsonb` | Prime-to-5-part of A after cancellation | prime-to-5-part of A |
| `Au5rev` | `jsonb` | Prime-to-5-part of B after cancellation | prime-to-5-part of B |
| `Au7` | `jsonb` | Prime-to-7-part of A after cancellation | prime-to-7-part of A |
| `Au7rev` | `jsonb` | Prime-to-7-part of B after cancellation | prime-to-7-part of B |
| `B` | `jsonb` | List of b_i | list of beta parameters (cyclotomic orders) |
| `B2` | `jsonb` | 2-part of B after cancellation | 2-part of B after cancellation (JSON array) |
| `B2rev` | `jsonb` | 2-part of A after cancellation | 2-part of A after cancellation (JSON array) |
| `B3` | `jsonb` | 3-part of B after cancellation | 3-part of B after cancellation (JSON array) |
| `B3rev` | `jsonb` | 3-part of A after cancellation | 3-part of A after cancellation (JSON array) |
| `B5` | `jsonb` | 5-part of B after cancellation | 5-part of B after cancellation (JSON array) |
| `B5rev` | `jsonb` | 5-part of A after cancellation | 5-part of A after cancellation (JSON array) |
| `B7` | `jsonb` | 7-part of B after cancellation | 7-part of B after cancellation (JSON array) |
| `B7rev` | `jsonb` | 7-part of A after cancellation | 7-part of A after cancellation (JSON array) |
| `Brev` | `jsonb` | List of a_i | reversed/complementary beta parameters |
| `Bu2` | `jsonb` | Prime-to-2-part of B after cancellation | Prime-to-2-part of B after cancellation (JSON array) |
| `Bu2rev` | `jsonb` | Prime-to-2-part of A after cancellation | Prime-to-2-part of A after cancellation (JSON array) |
| `Bu3` | `jsonb` | Prime-to-3-part of B after cancellation | Prime-to-3-part of B after cancellation (JSON array) |
| `Bu3rev` | `jsonb` | Prime-to-3-part of A after cancellation | Prime-to-3-part of A after cancellation (JSON array) |
| `Bu5` | `jsonb` | Prime-to-5-part of B after cancellation | Prime-to-5-part of B after cancellation (JSON array) |
| `Bu5rev` | `jsonb` | Prime-to-5-part of A after cancellation | Prime-to-5-part of A after cancellation (JSON array) |
| `Bu7` | `jsonb` | Prime-to-7-part of B after cancellation | Prime-to-7-part of B after cancellation (JSON array) |
| `Bu7rev` | `jsonb` | Prime-to-7-part of A after cancellation | Prime-to-7-part of A after cancellation (JSON array) |
| `C2` | `jsonb` | Cancelled 2-part | Cancelled 2-part (JSON array) |
| `C3` | `jsonb` | Cancelled 3-part | Cancelled 3-part (JSON array) |
| `C5` | `jsonb` | Cancelled 5-part | Cancelled 5-part (JSON array) |
| `C7` | `jsonb` | Cancelled 7-part | Cancelled 7-part (JSON array) |
| `Cu2` | `jsonb` | Cancelled prime-to-2-part | Cancelled prime-to-2-part (JSON array) |
| `Cu3` | `jsonb` | Cancelled prime-to-3-part | Cancelled prime-to-3-part (JSON array) |
| `Cu5` | `jsonb` | Cancelled prime-to-5-part | Cancelled prime-to-5-part (JSON array) |
| `Cu7` | `jsonb` | Cancelled prime-to-7-part | Cancelled prime-to-7-part (JSON array) |
| `bezout` | `jsonb` | Matrix giving bilinear pairing | Matrix giving bilinear pairing (JSON array) |
| `degree` | `smallint` | Degree of the motive | degree of the motive |
| `det` | `jsonb` | Determinant | Determinant (JSON array) |
| `famhodge` | `jsonb` | Hodge vector of the family | Hodge vector of the hypergeometric family |
| `h0` | `integer[]` | Matrix giving monodromy at 0 | list of integers |
| `h1` | `integer[]` | Matrix giving monodromy at 1 | list of integers |
| `hinf` | `integer[]` | Matrix giving monodromy at infinity | list of integers |
| `imprim` | `smallint` | GCD of gamma vector | integer |
| `label` | `text` | Label | family label |
| `mono` | `jsonb` | Monodromy groups mod 2, 3, 5, 7: list of pairs of a prime and a list of the order, 'index', group name, prime-to-ell-... | Monodromy groups mod 2, 3, 5, 7: list of pairs of a prime and a list of the orde (JSON array) |
| `snf` | `jsonb` | Smith normal form of Bezout matrix | Smith normal form of Bezout matrix (JSON array) |
| `variety_dim` | `smallint` | Dimension of canonical variety | integer |
| `weight` | `smallint` | Weight | motivic weight |

---

## hgm_monodromy

**Rows:** 137,565

**API:** https://www.lmfdb.org/api/hgm_monodromy/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `A` | `integer[]` | The {{KNOWL('hgm.defining_parameters', 'defining parameter')}} $A$, matching the {{KNOWL('columns.hgm_families.A', 'c... | list of integers |
| `Au` | `integer[]` | The {{KNOWL('hgm.defining_parameter_primetoppart', 'prime-to-$\ell$ part')}} of {{KNOWL('columns.hgm_monodromy.A', 'A... | list of integers |
| `B` | `integer[]` | The {{KNOWL('hgm.defining_parameters', 'defining parameter')}} $B$, matching the {{KNOWL('columns.hgm_families.B', 'c... | list of integers |
| `Bu` | `integer[]` | The {{KNOWL('hgm.defining_parameter_primetoppart', 'prime-to-$\ell$ part')}} of {{KNOWL('columns.hgm_monodromy.B', 'B... | list of integers |
| `Cu` | `integer[]` | The canceled terms in computing the {{KNOWL('hgm.defining_parameter_primetoppart', 'prime-to-$\ell$ part')}}. | list of integers |
| `ambient_factored_order` | `integer[]` | The factored order of the ambient group, as a list of pairs $[p,e]$. | list of integers |
| `ambient_gens` | `integer[]` | The generators of the ambient group, as a list of matrices (each represented as a list of lists of integers). | list of integers |
| `ambient_group_label` | `text` | The label of the ambient isometry group (either a symplectic or orthogonal group), as a finite abstract group. | string label (cross-reference) |
| `ambient_matrix_group_label` | `text` | The label of the ambient group as a finite matrix group, currently always null. | string label (cross-reference) |
| `ambient_name` | `text` | The name of the ambient group, of the form $\operatorname{Sp}_d(\mathbb{F}_{\ell})_{\operatorname{rad}}^{\operatornam... | text |
| `ambient_order` | `numeric` | The order of the ambient isometry group (either a symplectic or orthogonal group). | arbitrary-precision integer |
| `bezout_det` | `integer` | The determinant of the {{KNOWL('hgm.bezout_matrix', 'Bezout matrix')}} for the family. | integer |
| `degree` | `integer` | The {{KNOWL('hgm.weight', 'degree')}} of the family. | positive integer |
| `ell` | `integer` | The prime $\ell$, a {{KNOWL('hgm.wild', 'wild')}} prime for the family. | integer |
| `family` | `text` | The {{KNOWL('hgm.field.label', 'label')}} for the family. | text |
| `isotropic_dim` | `integer` | The dimension of the maximal totally isotropic subspace inside the orthogonal complement of the radical, for the ambi... | integer |
| `monodromy_factored_index` | `integer[]` | The factored index of the {{KNOWL('hgm.monodromy', 'monodromy group')}} inside the ambient group (either a symplectic... | list of integers |
| `monodromy_factored_order` | `integer[]` | The factored order of the {{KNOWL('hgm.monodromy', 'monodromy group')}}, as a list of pairs $[p,e]$. | list of integers |
| `monodromy_gens` | `integer[]` | The generators of the {{KNOWL('hgm.monodromy', 'monodromy group')}}, as a list of matrices (each represented as a lis... | list of integers |
| `monodromy_group_label` | `text` | The label of the {{KNOWL('hgm.monodromy', 'monodromy group')}}, as a finite abstract group. | string label (cross-reference) |
| `monodromy_index` | `numeric` | The index of the {{KNOWL('hgm.monodromy', 'monodromy group')}} inside the ambient group (either a symplectic or ortho... | arbitrary-precision integer |
| `monodromy_matrix_group_label` | `text` | The label of the monodromy group as a finite matrix group, currently always null. | string label (cross-reference) |
| `monodromy_order` | `numeric` | The order of the {{KNOWL('hgm.monodromy', 'monodromy group')}}. | arbitrary-precision integer |
| `radical_dim` | `integer` | The dimension of the radical, for the ambient isotropic space. | integer |
| `type` | `integer` | 1 if symplectic, 0 if orthogonal | integer |
| `weight` | `integer` | The {{KNOWL('hgm.weight', 'weight')}} of the family. | positive integer (weight) |
| `witt_index` | `integer` | The Witt index of the ambient isotropic group. | integer |

---

## hgm_motives

Hypergeometric motives

**Rows:** 285

**API:** https://www.lmfdb.org/api/hgm_motives/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `A` | `jsonb` | List of a_i | alpha parameters |
| `A2` | `jsonb` | 2-part of A after cancellation | 2-part of A after cancellation (JSON array) |
| `A2rev` | `jsonb` | 2-part of B after cancellation | 2-part of B after cancellation (JSON array) |
| `A3` | `jsonb` | 3-part of A after cancellation | 3-part of A after cancellation (JSON array) |
| `A3rev` | `jsonb` | 3-part of B after cancellation | 3-part of B after cancellation (JSON array) |
| `A5` | `jsonb` | 5-part of A after cancellation | 5-part of A after cancellation (JSON array) |
| `A5rev` | `jsonb` | 5-part of B after cancellation | 5-part of B after cancellation (JSON array) |
| `A7` | `jsonb` | 7-part of A after cancellation | 7-part of A after cancellation (JSON array) |
| `A7rev` | `jsonb` | 7-part of B after cancellation | 7-part of B after cancellation (JSON array) |
| `Arev` | `jsonb` | List of b_i | reversed alpha |
| `Au2` | `jsonb` | Prime-to-2-part of A after cancellation | Prime-to-2-part of A after cancellation (JSON array) |
| `Au2rev` | `jsonb` | Prime-to-2-part of B after cancellation | Prime-to-2-part of B after cancellation (JSON array) |
| `Au3` | `jsonb` | Prime-to-3-part of A after cancellation | Prime-to-3-part of A after cancellation (JSON array) |
| `Au3rev` | `jsonb` | Prime-to-3-part of B after cancellation | Prime-to-3-part of B after cancellation (JSON array) |
| `Au5` | `jsonb` | Prime-to-5-part of A after cancellation | Prime-to-5-part of A after cancellation (JSON array) |
| `Au5rev` | `jsonb` | Prime-to-5-part of B after cancellation | Prime-to-5-part of B after cancellation (JSON array) |
| `Au7` | `jsonb` | Prime-to-7-part of A after cancellation | Prime-to-7-part of A after cancellation (JSON array) |
| `Au7rev` | `jsonb` | Prime-to-7-part of B after cancellation | Prime-to-7-part of B after cancellation (JSON array) |
| `B` | `jsonb` | List of b_i | beta parameters |
| `B2` | `jsonb` | 2-part of B after cancellation | 2-part of B after cancellation (JSON array) |
| `B2rev` | `jsonb` | 2-part of A after cancellation | 2-part of A after cancellation (JSON array) |
| `B3` | `jsonb` | 3-part of B after cancellation | 3-part of B after cancellation (JSON array) |
| `B3rev` | `jsonb` | 3-part of A after cancellation | 3-part of A after cancellation (JSON array) |
| `B5` | `jsonb` | 5-part of B after cancellation | 5-part of B after cancellation (JSON array) |
| `B5rev` | `jsonb` | 5-part of A after cancellation | 5-part of A after cancellation (JSON array) |
| `B7` | `jsonb` | 7-part of B after cancellation | 7-part of B after cancellation (JSON array) |
| `B7rev` | `jsonb` | 7-part of A after cancellation | 7-part of A after cancellation (JSON array) |
| `Brev` | `jsonb` | List of a_i | reversed beta |
| `Bu2` | `jsonb` | Prime-to-2-part of B after cancellation | Prime-to-2-part of B after cancellation (JSON array) |
| `Bu2rev` | `jsonb` | Prime-to-2-part of A after cancellation | Prime-to-2-part of A after cancellation (JSON array) |
| `Bu3` | `jsonb` | Prime-to-3-part of B after cancellation | Prime-to-3-part of B after cancellation (JSON array) |
| `Bu3rev` | `jsonb` | Prime-to-3-part of A after cancellation | Prime-to-3-part of A after cancellation (JSON array) |
| `Bu5` | `jsonb` | Prime-to-5-part of B after cancellation | Prime-to-5-part of B after cancellation (JSON array) |
| `Bu5rev` | `jsonb` | Prime-to-5-part of A after cancellation | Prime-to-5-part of A after cancellation (JSON array) |
| `Bu7` | `jsonb` | Prime-to-7-part of B after cancellation | Prime-to-7-part of B after cancellation (JSON array) |
| `Bu7rev` | `jsonb` | Prime-to-7-part of A after cancellation | Prime-to-7-part of A after cancellation (JSON array) |
| `C2` | `jsonb` | Cancelled 2-part | Cancelled 2-part (JSON array) |
| `C3` | `jsonb` | Cancelled 3-part | Cancelled 3-part (JSON array) |
| `C5` | `jsonb` | Cancelled 5-part | Cancelled 5-part (JSON array) |
| `C7` | `jsonb` | Cancelled 7-part | Cancelled 7-part (JSON array) |
| `Cu2` | `jsonb` | Cancelled prime-to-2-part | Cancelled prime-to-2-part (JSON array) |
| `Cu3` | `jsonb` | Cancelled prime-to-3-part | Cancelled prime-to-3-part (JSON array) |
| `Cu5` | `jsonb` | Cancelled prime-to-5-part | Cancelled prime-to-5-part (JSON array) |
| `Cu7` | `jsonb` | Cancelled prime-to-7-part | Cancelled prime-to-7-part (JSON array) |
| `centralval` | `smallint` | Not yet implemented | central L-value (real number) |
| `coeffs` | `jsonb` | Coefficients for the L-function's Dirichlet series | polynomial coefficients |
| `cond` | `bigint` | Conductor | integer |
| `degree` | `smallint` | Degree of motive | degree of the motive |
| `famhodge` | `jsonb` | Hodge vector for the family | Hodge vector of parent family |
| `hodge` | `jsonb` | Hodge vector for the motive | Hodge numbers of the specialization |
| `label` | `text` | Label | motive label (specialization of a family at parameter t) |
| `lcms` | `jsonb` | List of least common multiples of Frobenius orders in mod-ell Galois representations for ell=2, 3, 5, 7 | List of least common multiples of Frobenius orders in mod-ell Galois representat (JSON array) |
| `locinfo` | `jsonb` | List of lists over small primes p.  Each is the conductor exponent, Frobenius polynomial coefficient list, semi-simpl... | local L-factor data at bad primes (JSON) |
| `req` | `bigint` | Difficulty | integer |
| `sig` | `smallint` | Signature of the motive | integer |
| `sign` | `smallint` | Sign in the functional equation | root number +1 or -1 |
| `t` | `text` | Specialization point | specialization parameter t (rational as [num, den]) |
| `weight` | `smallint` | Weight of motive | motivic weight |

---
