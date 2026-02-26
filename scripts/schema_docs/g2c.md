# g2c — Database Schema

**12 tables, 175 columns total**

### Tables

- [g2c_curves](#g2c_curves) (66,158 rows)
- [g2c_curves_new](#g2c_curves_new) (6,216,959 rows)
- [g2c_endomorphisms](#g2c_endomorphisms) (66,158 rows)
- [g2c_endomorphisms_new](#g2c_endomorphisms_new) (0 rows)
- [g2c_galrep](#g2c_galrep) (51,890 rows)
- [g2c_galrep_new](#g2c_galrep_new) (0 rows)
- [g2c_plots](#g2c_plots) (66,158 rows)
- [g2c_plots_new](#g2c_plots_new) (0 rows)
- [g2c_ratpts](#g2c_ratpts) (66,158 rows)
- [g2c_ratpts_new](#g2c_ratpts_new) (6,216,959 rows)
- [g2c_tamagawa](#g2c_tamagawa) (172,938 rows)
- [g2c_tamagawa_new](#g2c_tamagawa_new) (0 rows)

---

## g2c_curves

Genus 2 curves over *Q*

**Rows:** 66,158

**API:** https://www.lmfdb.org/api/g2c_curves/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `Lhash` | `text` | the value of the hash function defined in Section 4.3 of https://arxiv.org/abs/1602.03715 | text |
| `abs_disc` | `bigint` | absolute discriminant | absolute value of discriminant |
| `analytic_rank` | `smallint` | analytic rank upper bound that is believed to be tight (known for rank 0 or 1) | analytic rank of L(J,s) |
| `analytic_rank_proved` | `boolean` | true if the analytic rank upper bound is provably equal to the analytic rank | boolean |
| `analytic_sha` | `smallint` | conjectural order of Sha obtained from the other terms in the BSD formula | analytic order of Sha from BSD |
| `aut_grp_id` | `text` | (description not yet updated on this server) | text |
| `aut_grp_label` | `text` | (description not yet updated on this server) | automorphism group label, e.g. '2.1' |
| `aut_grp_tex` | `text` | (description not yet updated on this server) | text |
| `bad_lfactors` | `text` | bad primes and the corresponding L-factors | text repr of [[p, [coeffs]], ...]: bad Euler factors as lists of (prime, polynomial coefficients) |
| `bad_primes` | `integer[]` | bad primes | primes dividing conductor |
| `class` | `text` | isogeny class | isogeny class label: cond.alpha |
| `cond` | `bigint` | conductor | positive integer, conductor |
| `disc_sign` | `smallint` | sign of the discriminant | +1 or -1 |
| `end_alg` | `text` | endomorphism algebra | End^0(J) tensor Q: 'Q', 'RM', 'CM', 'QxQ', 'M_2(Q)' |
| `eqn` | `text` | coefficients of minimal equation y^2+h(x)y=f(x) | text representation of [f(x), h(x)] defining y^2 + h(x)*y = f(x). Stored as string of nested integer lists, e.g. '[[0,0,0,0,1,1],[1,1,0,1]]' |
| `g2_inv` | `text` | G2 invariants | G2 invariants [g1,g2,g3] as text repr of rationals |
| `geom_aut_grp_id` | `text` | (description not yet updated on this server) | text |
| `geom_aut_grp_label` | `text` | (description not yet updated on this server) | geometric automorphism group label |
| `geom_aut_grp_tex` | `text` | (description not yet updated on this server) | text |
| `geom_end_alg` | `text` | geometric endomorphism algebra | End^0(J_Qbar) tensor Q: 'Q', 'RM', 'CM', 'QxQ', 'M_2(Q)', etc. |
| `globally_solvable` | `smallint` | 1 if known to have rational points, 0 if known to have no rational points, -1 if unknown | integer |
| `has_square_sha` | `boolean` | assuming Sha is finite, true if the order of Sha is a square, false otherwise (in which case it is 2 times a square, ... | boolean, Sha is a perfect square |
| `hasse_weil_proved` | `boolean` | true if the Hasse-Weil conjecture is known to hold for the L-function of this curve | boolean |
| `igusa_clebsch_inv` | `text` | Igusa-Clebsch invariants | Igusa-Clebsch invariants [I2,I4,I6,I10] as text repr of integer list |
| `igusa_inv` | `text` | Igusa invariants | Igusa invariants [J2,J4,J6,J8,J10] as text repr |
| `is_gl2_type` | `boolean` | whether the curve is of GL2-type over its base field | boolean, Jacobian isogenous to product of elliptic curves |
| `is_simple_base` | `boolean` | whether the curve is simple over the base field | boolean, J is Q-simple |
| `is_simple_geom` | `boolean` | whether the curve is simple over the algebraic closure | boolean, J is geometrically simple (over Qbar) |
| `label` | `text` | LMFDB label | label: cond.alpha.disc.num, e.g. '169.a.169.1' |
| `leading_coeff` | `numeric` | leading coefficients | arbitrary-precision integer |
| `locally_solvable` | `boolean` | true if the curve has rational points locally everywhere (i.e. over every completion of Q, including R) | boolean, C has points in Q_v for all v |
| `modell_images` | `text[]` | list of labels of mod=ell Galois images | list of strings |
| `mw_rank` | `smallint` | rank of the Mordell-Weil group | proved Mordell-Weil rank of J(Q), or null |
| `mw_rank_proved` | `boolean` | true if the rank of the Mordell-Weil group is provably correct | boolean |
| `non_maximal_primes` | `integer[]` | the primes p for which the mod-p Galois representation is not surjective | list of integers |
| `non_solvable_places` | `jsonb` | List of integers p for which curve has no Q_p points, with 0 denoting the infinite place | List of integers p for which curve has no Q_p points, with 0 denoting the infini (JSON array) |
| `num_rat_pts` | `smallint` | number of rational points | count of rational points on C |
| `num_rat_wpts` | `smallint` | number of rational Weierstrass points | count of rational Weierstrass points |
| `real_geom_end_alg` | `text` | endomorphism ring over base field tensored with RR | End^0(J) tensor R: 'R', 'C', 'RxR', 'M_2(R)', 'M_2(C)' |
| `real_period` | `numeric` | real period | real period Omega(C/R) |
| `regulator` | `numeric` | regulator | height regulator of J(Q) |
| `root_number` | `smallint` | root number | global root number +1 or -1 |
| `st_group` | `text` | Sato-Tate group over base field | Sato-Tate group name, e.g. 'USp(4)' |
| `st_label` | `text` | Label of the Sato-Tate group | Sato-Tate group label |
| `st_label_components` | `integer[]` | Integer components of the Sato-Tate group label for sorting | list of integers |
| `tamagawa_product` | `smallint` | product of the Tamagawa numbers | product of local Tamagawa numbers |
| `torsion_order` | `smallint` | rational torsion order of the Jacobian | |J(Q)_tors| |
| `torsion_subgroup` | `text` | rational torsion group of the Jacobian, represented by the invariant factors [d_1, d_2, ...] for which this torsion g... | invariant factors of J(Q)_tors as text, e.g. '[2,2]' |
| `two_selmer_rank` | `smallint` | 2-Selmer rank | rank of 2-Selmer group Sel_2(J/Q) |
| `two_torsion_field` | `jsonb` | 2-torsion field | 2-torsion field (JSON array) |

---

## g2c_curves_new

Genus 2 curves over *Q*

**Rows:** 6,216,959

**API:** https://www.lmfdb.org/api/g2c_curves_new/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `Lhash` | `text` | the value of the hash function defined in Section 4.3 of https://arxiv.org/abs/1602.03715 | text |
| `abs_disc` | `numeric` | absolute discriminant | arbitrary-precision integer |
| `analytic_rank` | `smallint` | analytic rank upper bound that is believed to be tight (known for rank 0 or 1) | integer |
| `analytic_rank_proved` | `boolean` | true if the analytic rank upper bound is provably equal to the analytic rank | boolean |
| `analytic_sha` | `smallint` | conjectural order of Sha obtained from the other terms in the BSD formula | integer |
| `aut_grp` | `text` | automorphism group id n.m | text |
| `bad_lfactors` | `text` | bad primes and the corresponding L-factors | text |
| `bad_primes` | `bigint[]` | bad primes | list of integers |
| `class` | `text` | isogeny class | text |
| `cond` | `bigint` | conductor | integer |
| `disc_sign` | `smallint` | sign of the discriminant | integer |
| `end_alg` | `text` | endomorphism algebra | text |
| `eqn` | `text` | coefficients of minimal equation y^2+h(x)y=f(x) | text |
| `g2_inv` | `text` | G2 invariants | text |
| `geom_aut_grp` | `text` | geometric automorphism group id n.m | text |
| `geom_end_alg` | `text` | geometric endomorphism algebra | text |
| `globally_solvable` | `smallint` | 1 if known to have rational points, 0 if known to have no rational points, -1 if unknown | integer |
| `has_square_sha` | `boolean` | assuming Sha is finite, true if the order of Sha is a square, false otherwise (in which case it is 2 times a square, ... | boolean |
| `hasse_weil_proved` | `boolean` | true if the Hasse-Weil conjecture is known to hold for the L-function of this curve | boolean |
| `igusa_clebsch_inv` | `text` | Igusa-Clebsch invariants | text |
| `igusa_inv` | `text` | Igusa invariants | text |
| `is_gl2_type` | `boolean` | whether the curve is of GL2-type over its base field | boolean |
| `is_simple_base` | `boolean` | whether the curve is simple over the base field | boolean |
| `is_simple_geom` | `boolean` | whether the curve is simple over the algebraic closure | boolean |
| `label` | `text` | LMFDB label | string label |
| `leading_coeff` | `numeric` | leading coefficients | arbitrary-precision integer |
| `locally_solvable` | `boolean` | true if the curve has rational points locally everywhere (i.e. over every completion of Q, including R) | boolean |
| `modell_images` | `text[]` | list of labels of mod=ell Galois images | list of strings |
| `mw_rank` | `smallint` | rank of the Mordell-Weil group | integer |
| `mw_rank_proved` | `boolean` | true if the rank of the Mordell-Weil group is provably correct | boolean |
| `non_maximal_primes` | `integer[]` | the primes p for which the mod-p Galois representation is not surjective | list of integers |
| `non_solvable_places` | `jsonb` | List of integers p for which curve has no Q_p points, with 0 denoting the infinite place | List of integers p for which curve has no Q_p points, with 0 denoting the infini (JSON array) |
| `num` | `smallint` | (description not yet updated on this server) | integer |
| `num_rat_pts` | `smallint` | number of rational points | non-negative integer (count) |
| `num_rat_wpts` | `smallint` | number of rational Weierstrass points | non-negative integer (count) |
| `real_geom_end_alg` | `text` | endomorphism ring over base field tensored with RR | text |
| `real_period` | `numeric` | real period | arbitrary-precision integer |
| `regulator` | `numeric` | regulator | arbitrary-precision integer |
| `root_number` | `smallint` | root number | integer |
| `st_group` | `text` | Sato-Tate group over base field | text |
| `st_label` | `text` | Label of the Sato-Tate group | string label (cross-reference) |
| `st_label_components` | `integer[]` | Integer components of the Sato-Tate group label for sorting | list of integers |
| `tamagawa_product` | `smallint` | product of the Tamagawa numbers | integer |
| `torsion_order` | `smallint` | rational torsion order of the Jacobian | integer |
| `torsion_subgroup` | `text` | rational torsion group of the Jacobian, represented by the invariant factors [d_1, d_2, ...] for which this torsion g... | text |
| `two_selmer_rank` | `smallint` | 2-Selmer rank | integer |
| `two_torsion_field` | `jsonb` | 2-torsion field | 2-torsion field |

---

## g2c_endomorphisms

Endomorphism data for genus 2 curves over QQ.

**Rows:** 66,158

**API:** https://www.lmfdb.org/api/g2c_endomorphisms/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `factorsQQ_base` | `jsonb` | description of endomorphism algebra factors over the base field | text: factorization of End^0(J) tensor Q as list of [label, poly, disc] triples |
| `factorsQQ_geom` | `jsonb` | description of endomorphism algebra factors over the algebraic closure | geometric version of factorsQQ_base |
| `factorsRR_base` | `jsonb` | endomorphism algebra factors over the base field tensored with RR | text: real factors, list of 'R' or 'C' strings |
| `factorsRR_geom` | `jsonb` | endomorphism algebra factors over the algebraic closure tensored with RR | geometric version of factorsRR_base |
| `fod_coeffs` | `jsonb` | defining polynomial of the smallest field over which all endomorphisms are defined | defining polynomial coefficients of field of definition |
| `fod_label` | `text` | LMFDB label of the smallest field over which all endomorphisms are defined | number field label of field of definition of all endomorphisms |
| `is_simple_base` | `boolean` | whether the curve is simple over the base field | boolean |
| `is_simple_geom` | `boolean` | whether the curve is simple over the algebraic closure | boolean |
| `label` | `text` | LMFDB label of the genus 2 curve | curve label |
| `lattice` | `jsonb` | endomorphism lattice. See notes section | endomorphism lattice. See notes section (JSON array) |
| `ring_base` | `jsonb` | endomorphism ring over the base field as a subring of the endomorphism algebra | text: [index, is_eichler] for endomorphism ring order |
| `ring_geom` | `jsonb` | endomorphism ring over the algebraic closure as a subring of the endomorphism algebra | geometric version of ring_base |
| `spl_facs_coeffs` | `jsonb` | defining coefficients of the elliptic curves obtained by splitting the Jacobian | defining coefficients of the elliptic curves obtained by splitting the Jacobian |
| `spl_facs_condnorms` | `jsonb` | conductor norms of the elliptic curves obtained by splitting the Jacobian | conductor norms of the elliptic curves obtained by splitting the Jacobian |
| `spl_facs_labels` | `jsonb` | LMFDB labels of the elliptic curves obtained by splitting the Jacobian | LMFDB labels of the elliptic curves obtained by splitting the Jacobian |
| `spl_fod_coeffs` | `jsonb` | defining polynomial of a field of minimal degree over which a splitting of the Jacobian is defined | defining polynomial of a field of minimal degree over which a splitting of the J (JSON array) |
| `spl_fod_gen` | `jsonb` | generator of a field of minimal degree over which a splitting of the Jacobian is defined, as a subfield of the smalle... | generator of a field of minimal degree over which a splitting of the Jacobian is (JSON array) |
| `spl_fod_label` | `text` | LMFDB label of a field of minimal degree over which a splitting of the Jacobian is defined | string label (cross-reference) |
| `st_group_base` | `text` | Sato-Tate group over the base field | text |
| `st_group_geom` | `text` | Sato-Tate group over the algebraic closure (equivalently, its identity component) | text |

---

## g2c_endomorphisms_new

Endomorphism data for genus 2 curves over QQ.

**Rows:** 0

**API:** https://www.lmfdb.org/api/g2c_endomorphisms_new/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `factorsQQ_base` | `jsonb` | description of endomorphism algebra factors over the base field | description of endomorphism algebra factors over the base field |
| `factorsQQ_geom` | `jsonb` | description of endomorphism algebra factors over the algebraic closure | description of endomorphism algebra factors over the algebraic closure |
| `factorsRR_base` | `jsonb` | endomorphism algebra factors over the base field tensored with RR | endomorphism algebra factors over the base field tensored with RR |
| `factorsRR_geom` | `jsonb` | endomorphism algebra factors over the algebraic closure tensored with RR | endomorphism algebra factors over the algebraic closure tensored with RR |
| `fod_coeffs` | `jsonb` | defining polynomial of the smallest field over which all endomorphisms are defined | defining polynomial of the smallest field over which all endomorphisms are defin |
| `fod_label` | `text` | LMFDB label of the smallest field over which all endomorphisms are defined | string label (cross-reference) |
| `is_simple_base` | `boolean` | whether the curve is simple over the base field | boolean |
| `is_simple_geom` | `boolean` | whether the curve is simple over the algebraic closure | boolean |
| `label` | `text` | LMFDB label of the genus 2 curve | string label |
| `lattice` | `jsonb` | endomorphism lattice. See notes section | endomorphism lattice. See notes section |
| `ring_base` | `jsonb` | endomorphism ring over the base field as a subring of the endomorphism algebra | endomorphism ring over the base field as a subring of the endomorphism algebra |
| `ring_geom` | `jsonb` | endomorphism ring over the algebraic closure as a subring of the endomorphism algebra | endomorphism ring over the algebraic closure as a subring of the endomorphism al |
| `spl_facs_coeffs` | `jsonb` | defining coefficients of the elliptic curves obtained by splitting the Jacobian | defining coefficients of the elliptic curves obtained by splitting the Jacobian |
| `spl_facs_condnorms` | `jsonb` | conductor norms of the elliptic curves obtained by splitting the Jacobian | conductor norms of the elliptic curves obtained by splitting the Jacobian |
| `spl_facs_labels` | `jsonb` | LMFDB labels of the elliptic curves obtained by splitting the Jacobian | LMFDB labels of the elliptic curves obtained by splitting the Jacobian |
| `spl_fod_coeffs` | `jsonb` | defining polynomial of a field of minimal degree over which a splitting of the Jacobian is defined | defining polynomial of a field of minimal degree over which a splitting of the J |
| `spl_fod_gen` | `jsonb` | generator of a field of minimal degree over which a splitting of the Jacobian is defined, as a subfield of the smalle... | generator of a field of minimal degree over which a splitting of the Jacobian is |
| `spl_fod_label` | `text` | LMFDB label of a field of minimal degree over which a splitting of the Jacobian is defined | string label (cross-reference) |
| `st_group_base` | `text` | Sato-Tate group over the base field | text |
| `st_group_geom` | `text` | Sato-Tate group over the algebraic closure (equivalently, its identity component) | text |

---

## g2c_galrep

Images of Galois representations of genus $2$ Jacobians

**Rows:** 51,890

**API:** https://www.lmfdb.org/api/g2c_galrep/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `conductor` | `integer` | Conductor of the genus 2 curve. | positive integer |
| `lmfdb_label` | `text` | LMFDB label of the genus 2 curve. | string label |
| `modell_image` | `text` | Image inside GSp(4,Z/$\ell$) of the mod-$\ell$ Galois representation of the Jacobian of the curve. | text |
| `prime` | `smallint` | A prime $\ell$ for which the mod-$\ell$ Galois representation is not surjective | integer |

---

## g2c_galrep_new

Images of Galois representations of genus $2$ Jacobians

**Rows:** 0

**API:** https://www.lmfdb.org/api/g2c_galrep_new/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `conductor` | `integer` | Conductor of the genus 2 curve. | positive integer |
| `lmfdb_label` | `text` | LMFDB label of the genus 2 curve. | string label |
| `modell_image` | `text` | Image inside GSp(4,Z/$\ell$) of the mod-$\ell$ Galois representation of the Jacobian of the curve. | text |
| `prime` | `smallint` | A prime $\ell$ for which the mod-$\ell$ Galois representation is not surjective | integer |

---

## g2c_plots

**Rows:** 66,158

**API:** https://www.lmfdb.org/api/g2c_plots/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `label` | `text` | LMFDB label of the genus 2 curve | string label |
| `plot` | `text` | base-64 encoded png | text |

---

## g2c_plots_new

**Rows:** 0

**API:** https://www.lmfdb.org/api/g2c_plots_new/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `label` | `text` | LMFDB label of the genus 2 curve | string label |
| `plot` | `text` | base-64 encoded png | text |

---

## g2c_ratpts

**Rows:** 66,158

**API:** https://www.lmfdb.org/api/g2c_ratpts/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `label` | `text` | LMFDB label of the genus 2 curve | curve label |
| `mw_gens` | `jsonb` | list of generators of the Mordell-Weil group of the Jacobian (assuming mw_gens_v is true) | text: Mordell-Weil generators as divisor classes |
| `mw_gens_v` | `boolean` | true if mw_gens is known to be correct | boolean |
| `mw_heights` | `numeric[]` | heights of Mordell-Weil generators (in order matching mw_gens) | text: canonical heights of MW generators |
| `mw_invs` | `smallint[]` | Invariants of the Mordell-Weil group as an abelian group, [0,0,2,4] is Z x Z x Z/2 x Z/4 | list of small integers |
| `num_rat_pts` | `smallint` | number of known rational points | non-negative integer (count) |
| `rat_pts` | `jsonb` | list of known rational points | text: list of projective rational points [[x,y,z],...] |
| `rat_pts_v` | `boolean` | true if all rational points are known | boolean |

---

## g2c_ratpts_new

**Rows:** 6,216,959

**API:** https://www.lmfdb.org/api/g2c_ratpts_new/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `label` | `text` | LMFDB label of the genus 2 curve | string label |
| `mw_gens` | `jsonb` | list of generators of the Mordell-Weil group of the Jacobian (assuming mw_gens_v is true) | list of generators of the Mordell-Weil group of the Jacobian (assuming mw_gens_v (JSON array) |
| `mw_gens_v` | `boolean` | true if mw_gens is known to be correct | boolean |
| `mw_heights` | `numeric[]` | heights of Mordell-Weil generators (in order matching mw_gens) | list of integers (length 0 in sample) |
| `mw_invs` | `smallint[]` | Invariants of the Mordell-Weil group as an abelian group, [0,0,2,4] is Z x Z x Z/2 x Z/4 | list of small integers |
| `num_rat_pts` | `smallint` | number of known rational points | non-negative integer (count) |
| `rat_pts` | `jsonb` | list of known rational points | list of known rational points (JSON array) |
| `rat_pts_v` | `boolean` | true if all rational points are known | boolean |

---

## g2c_tamagawa

**Rows:** 172,938

**API:** https://www.lmfdb.org/api/g2c_tamagawa/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `cluster_label` | `text` | cluster picture label | string label (cross-reference) |
| `label` | `text` | genus 2 curve label | curve label |
| `local_root_number` | `numeric` | The local root number (plus or minus 1) | arbitrary-precision integer |
| `p` | `bigint` | a prime p of bad reduction | bad prime p |
| `tamagawa_number` | `smallint` | tamagawa number at p | local Tamagawa number c_p |

---

## g2c_tamagawa_new

**Rows:** 0

**API:** https://www.lmfdb.org/api/g2c_tamagawa_new/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `cluster_label` | `text` | cluster picture label | string label (cross-reference) |
| `label` | `text` | genus 2 curve label | string label |
| `local_root_number` | `numeric` | The local root number (plus or minus 1) | arbitrary-precision integer |
| `p` | `bigint` | a prime p of bad reduction | integer |
| `tamagawa_number` | `smallint` | tamagawa number at p | integer |

---
