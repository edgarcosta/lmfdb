# hgcwa — Database Schema

**6 tables, 84 columns total**

### Tables

- [hgcwa_complete](#hgcwa_complete) (14 rows)
- [hgcwa_genvectors](#hgcwa_genvectors) (2,108 rows)
- [hgcwa_passports](#hgcwa_passports) (335,012 rows)
- [hgcwa_per_genus_stats](#hgcwa_per_genus_stats) (0 rows)
- [hgcwa_per_group_stats](#hgcwa_per_group_stats) (0 rows)
- [hgcwa_unique_groups](#hgcwa_unique_groups) (1,299 rows)

---

## hgcwa_complete

**Rows:** 14

**API:** https://www.lmfdb.org/api/hgcwa_complete/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `g0_gt0_compute` | `boolean` | whether quotient genus >0 data has been computed for this genus | boolean |
| `genus` | `smallint` | genus | non-negative integer (genus) |
| `num_families` | `integer[]` | 1st entry is number of distinct families for this genus total, nth entry is for quotient genus n-2 | list of integers |
| `num_gen_vectors` | `integer[]` | 1st entry is number of distinct generating vectors for this genus, nth entry is for quotient genus n-2 | list of integers |
| `num_refined_pp` | `integer[]` | 1st entry is number of distinct refined passports for this genus, nth entry is for quotient genus n-2 | list of integers |
| `num_unique_groups` | `integer` | number of distinct groups of this genus | non-negative integer (count) |
| `top_braid_compute` | `boolean` | whether topological and braid equivalences have been computed for this genus and g0=0 | boolean |
| `top_braid_g0_gt0` | `boolean` | False for now (whether topological and braid equivalences have been computed for g0>0) | boolean |

---

## hgcwa_genvectors

**Rows:** 2,108

**API:** https://www.lmfdb.org/api/hgcwa_genvectors/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `braid` | `integer[]` | (description not yet updated on this server) | list of integers |
| `cc` | `integer[]` | (description not yet updated on this server) | list of integers |
| `cinv` | `numeric` | (description not yet updated on this server) | arbitrary-precision integer |
| `con` | `text[]` | (description not yet updated on this server) | list of strings |
| `connected_genvec` | `text[]` | (description not yet updated on this server) | list of strings |
| `cyclic_trigonal` | `boolean` | (description not yet updated on this server) | boolean |
| `dim` | `smallint` | (description not yet updated on this server) | non-negative integer |
| `eqn` | `text[]` | (description not yet updated on this server) | list of strings |
| `full_auto` | `text` | (description not yet updated on this server) | text |
| `full_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `g0` | `smallint` | (description not yet updated on this server) | integer |
| `genus` | `smallint` | (description not yet updated on this server) | non-negative integer (genus) |
| `genvec` | `numeric[]` | (description not yet updated on this server) | list of arbitrary-precision integers |
| `group` | `text` | (description not yet updated on this server) | text |
| `group_order` | `integer` | (description not yet updated on this server) | integer |
| `hyp_involution` | `numeric` | (description not yet updated on this server) | arbitrary-precision integer |
| `hyperelliptic` | `boolean` | (description not yet updated on this server) | boolean |
| `jacobian_decomp` | `jsonb` | (description not yet updated on this server) | JSON list of [dim, mult, char_index] triples: Jacobian decomposition (same as hgcwa_passports) |
| `label` | `text` | (description not yet updated on this server) | string label |
| `min_deg` | `integer` | (description not yet updated on this server) | integer |
| `passport_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `r` | `smallint` | (description not yet updated on this server) | integer |
| `signH` | `integer[]` | (description not yet updated on this server) | list of integers |
| `signature` | `integer[]` | (description not yet updated on this server) | list of integers |
| `topological` | `integer[]` | (description not yet updated on this server) | list of integers |
| `total_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `trans_group` | `text` | (description not yet updated on this server) | text |

---

## hgcwa_passports

Group actions on higher genus curves

**Rows:** 335,012

**API:** https://www.lmfdb.org/api/hgcwa_passports/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `braid` | `integer[]` | ordered pair of positive integers designating the "cc" entry for the generating vector which is the representative fo... | list of integers |
| `cc` | `jsonb` | ordered pair of positive integers where first number is which refined passport and second is which generating vector ... | ordered pair of positive integers where first number is which refined passport a (JSON array) |
| `cinv` | `jsonb` | trigonal automorphism (if cyclic trigonal), sotred as a list of positive intgers representing a permutation | trigonal automorphism (if cyclic trigonal), sotred as a list of positive intgers (JSON array) |
| `con` | `text` | list of conjugacy classes where the action for this particular refined passport occurs, stored as a string representi... | text |
| `cyclic_trigonal` | `boolean` | True/False whether curve is cyclic trigonal | boolean, family contains cyclic trigonal curves |
| `dim` | `smallint` | dimension of the family of curves, this is a non-negative integer | dimension of the family (moduli space) |
| `eqn` | `jsonb` | string representing an equation for the family, given in LaTeX notation | string representing an equation for the family, given in LaTeX notation (JSON array) |
| `full_auto` | `text` | group id for the full automorphism group for this family, as string representing a pair of integers encoding the GAP/... | text |
| `full_label` | `text` | label for full automorphism group, in same form as label but for full automorphism group data | string label (cross-reference) |
| `g0` | `smallint` | quotient genus, this is a non-negative integer | genus of the quotient curve C/G |
| `gen_vectors` | `jsonb` | generating vector for this action, stored as r lists of positive integers representing permutations | generating vector for this action, stored as r lists of positive integers repres (JSON array) |
| `genus` | `smallint` | genus of the family of curves, this is a positive integer > 1 | genus g of the curve |
| `group` | `text` | automorphism group, string representing a pair of integers encoding the GAP/Magma group id | text |
| `group_order` | `integer` | order of the group | order of the automorphism group |
| `hyp_involution` | `jsonb` | hyperelliptic involution (if hyperelliptic), stored as list of positive integers representing a permutation | hyperelliptic involution (if hyperelliptic), stored as list of positive integers |
| `hyperelliptic` | `boolean` | True/False whether curve is hyperelliptic | boolean, family contains hyperelliptic curves |
| `jacobian_decomp` | `jsonb` | a list consisting of lists of integers, each one of which codes a factor in a Jacobian variety decomposition. An entr... | JSON list of [dim, multiplicity, char_index] triples: Jacobian decomposes as product of A_dim^mult for each character. E.g. [3,1,2] means one copy of a 3-dimensional abelian variety from character #2 |
| `label` | `text` | label for whole family, string of form 'g.a-b.g0.m1-m2-...-mr' where g is genus, a-b is group, g0 is quotient genus, ... | family label: genus.g0.signature_str.group_label |
| `ndim` | `smallint` | Not visible and will be deleted in new versions of the database | integer |
| `passport_label` | `text` | label for the passport (numbered by conjugacy class), string of form 'g.a-b.g0.m1-m2-...-mr.x' where x is a positive ... | string label (cross-reference) |
| `r` | `smallint` | number of branch points of the cover, non-negative integer | integer |
| `realcc` | `integer[]` | cc but as a pair of integers | list of integers |
| `signH` | `text` | signature of full action, a string representing a list of positive integers for the action of the full automorphism g... | text |
| `signature` | `text` | a string representing a list of non-negative integers [g0,m1,...,mr] where g0 is the quotient genus, and the mi repre... | text |
| `topological` | `integer[]` | ordered pair of positive integers designating the "cc" entry for the generating vector which is the representative fo... | list of integers |
| `total_label` | `text` | label including which generating vector, string of form 'g.a-b.g0.m1-m2-...-mr.x.y' where y is a positive integer rep... | string label (cross-reference) |

---

## hgcwa_per_genus_stats

**Rows:** 0

**API:** https://www.lmfdb.org/api/hgcwa_per_genus_stats/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `g0_gt0_compute` | `boolean` | (description not yet updated on this server) | boolean |
| `genus` | `smallint` | (description not yet updated on this server) | non-negative integer (genus) |
| `nonabelian_only` | `boolean` | (description not yet updated on this server) | boolean |
| `num_families` | `integer[]` | (description not yet updated on this server) | list of integers |
| `num_gen_vectors` | `integer[]` | (description not yet updated on this server) | list of integers |
| `num_refined_pp` | `integer[]` | (description not yet updated on this server) | list of integers |
| `num_unique_groups` | `integer` | (description not yet updated on this server) | non-negative integer (count) |
| `top_braid_compute` | `boolean` | (description not yet updated on this server) | boolean |
| `top_braid_g0_gt0` | `boolean` | (description not yet updated on this server) | boolean |

---

## hgcwa_per_group_stats

**Rows:** 0

**API:** https://www.lmfdb.org/api/hgcwa_per_group_stats/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `braid` | `integer` | (description not yet updated on this server) | integer |
| `g0_gt0_list` | `integer[]` | (description not yet updated on this server) | list of integers |
| `g0_is_gt0` | `boolean` | (description not yet updated on this server) | boolean |
| `gen_vectors` | `integer` | (description not yet updated on this server) | integer |
| `genus` | `smallint` | (description not yet updated on this server) | non-negative integer (genus) |
| `group` | `text` | (description not yet updated on this server) | text |
| `topological` | `integer` | (description not yet updated on this server) | integer |

---

## hgcwa_unique_groups

**Rows:** 1,299

**API:** https://www.lmfdb.org/api/hgcwa_unique_groups/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `braid` | `integer` | number of distinct generating vectors, up to braid equivalence, for this genus and group (if g0_is_gt0 is false) | integer |
| `g0_gt0_list` | `integer[]` | list of g0 values this group appears for, if greater than 0 | list of integers |
| `g0_is_gt0` | `boolean` | whether the group is for quotient genus 0 or quotient genus >= 1 | boolean |
| `gen_vectors` | `integer` | number of distinct generating vectors, up to simultaneous conjugation, for this genus and group | integer |
| `genus` | `smallint` | genus | non-negative integer (genus) |
| `group` | `integer[]` | GAP ID encoded as a pair of integers [N,i], where N is the order of the group and i distinguishes groups of the same ... | list of integers |
| `topological` | `integer` | number of distinct generating vectors, up to topological equivalence, for this genus and group (if g0_is_gt0 is false) | integer |

---
