# ec — Database Schema

**13 tables, 223 columns total**

### Tables

- [ec_classdata](#ec_classdata) (2,917,287 rows)
- [ec_curvedata](#ec_curvedata) (3,824,372 rows)
- [ec_galrep](#ec_galrep) (5,482,562 rows)
- [ec_iqf_labels](#ec_iqf_labels) (46,358 rows)
- [ec_iwasawa](#ec_iwasawa) (974,104 rows)
- [ec_localdata](#ec_localdata) (13,178,234 rows)
- [ec_mwbsd](#ec_mwbsd) (3,824,372 rows)
- [ec_nfcurves](#ec_nfcurves) (767,518 rows)
- [ec_nfcurves_test](#ec_nfcurves_test) (687,520 rows)
- [ec_nfportraits](#ec_nfportraits) (170,119 rows)
- [ec_padic](#ec_padic) (6,819,842 rows)
- [ec_sympow](#ec_sympow) (23,338,296 rows)
- [ec_torsion_growth](#ec_torsion_growth) (16,491,706 rows)

---

## ec_classdata

**Rows:** 2,917,287

**API:** https://www.lmfdb.org/api/ec_classdata/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `anlist` | `smallint[]` | L-series coefficients. a_n for 0 <= n < 20 | L-series coefficients a_n for n=0..19. a_0=0, a_1=1, then a_2,...,a_19 |
| `aplist` | `smallint[]` | Traces of Frobenius. a_p for p < 100 | traces of Frobenius a_p for first 25 primes (p=2,3,5,...,97). Index 0 = a_2 |
| `class_deg` | `smallint` | LCM of isogeny degrees in the isogeny class | positive integer, LCM of isogeny degrees |
| `class_size` | `smallint` | Number of curves in the isogeny class | positive integer, number of curves in class |
| `conductor` | `integer` | Conductor | positive integer |
| `isogeny_matrix` | `smallint[]` | Matric of isogeny degrees | flattened row-major N x N matrix of cyclic isogeny degrees. For class_size=N, has N^2 entries. Symmetric. M[i][j] = degree of cyclic isogeny from curve i to curve j (LMFDB ordering) |
| `lmfdb_iso` | `text` | LMFDB isogeny class code | isogeny class label, e.g. '11.a' |
| `trace_hash` | `bigint` | Trace hash | 64-bit hash of Frobenius traces for fast isogeny class lookup |

---

## ec_curvedata

**Rows:** 3,824,372

**API:** https://www.lmfdb.org/api/ec_curvedata/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `Ciso` | `text` | Cremona label of isogeny class | Cremona isogeny class label, e.g. '11a' |
| `Clabel` | `text` | Cremona label of curve | Cremona label, e.g. '11a1' |
| `Cnumber` | `smallint` | Cremona index of curve in its isogeny class | 1-indexed position in isogeny class (Cremona ordering) |
| `abc_quality` | `double precision` | quality of the abc-triple associated to the j-invariant | floating-point, quality q(a,b,c) of the abc-triple for the j-invariant |
| `absD` | `numeric` | Absolute value of discriminant | absolute value of minimal discriminant, arbitrary-precision |
| `adelic_genus` | `integer` | The genus of the modular curve on which this elliptic curve is a canonical rational point | non-negative integer, genus of the modular curve X_H where H = rho_E(Gal) |
| `adelic_index` | `integer` | The index in $\GL_2(\widehat{\mathbb{Z}})$ of the adelic image of this elliptic curve. | positive integer, index [GL2(Z-hat) : rho_E(Gal)] |
| `adelic_level` | `bigint` | The level of the maximal modular curve on which this elliptic curve defines a rational point. | positive integer, level M of adelic image (largest level of a modular curve with rational point) |
| `ainvs` | `numeric[]` | a-invariants | Weierstrass a-invariants [a1,a2,a3,a4,a6] as numeric[5]. Defines y^2+a1*xy+a3*y = x^3+a2*x^2+a4*x+a6 |
| `analytic_rank` | `smallint` | analytic rank | non-negative integer, order of vanishing of L(E,s) at s=1 |
| `bad_primes` | `integer[]` | primes of bad reduction | sorted list of primes of bad reduction |
| `class_deg` | `smallint` | LCM of degrees of isogenies | positive integer, LCM of isogeny degrees in the class |
| `class_size` | `smallint` | Size of isogeny class | positive integer, number of curves in the isogeny class |
| `cm` | `smallint` | CM discriminant, or 0 | CM discriminant (negative integer) or 0 if no CM. E.g. -3, -4, -7, ..., 0 |
| `conductor` | `integer` | Conductor | positive integer, conductor of the curve |
| `degree` | `bigint` | Degree of modular parametrization | positive integer, degree of modular parametrization X_0(N) -> E |
| `elladic_images` | `text[]` | List of Sutherland labels of subgroups of $\GL_2(\Z/\ell\Z)$. | Sutherland labels of ell-adic Galois images in GL2(Z_ell), format 'ell.index.surjdet.label' |
| `faltings_height` | `numeric` | Faltings height | real (arbitrary-precision), Faltings height |
| `faltings_index` | `smallint` | index of curve in its isogeny class, sorted by Faltings height | 1-indexed position in isogeny class sorted by Faltings height |
| `faltings_ratio` | `smallint` | integer ratio of period area to that of the curve with minimal Faltings height in its isogeny class | integer ratio of period area to that of minimal-Faltings-height curve in class |
| `intrinsic_torsion` | `smallint` | Order of intrinsic torsion subgroup | positive integer, order of intrinsic torsion subgroup |
| `iso_nlabel` | `smallint` | numerical version of the LMFDB isogeny class label | numerical encoding of isogeny class letter (a=0, b=1, ...) |
| `isogeny_degrees` | `smallint[]` | Degrees of cyclic isogenies for this curve | sorted list of degrees of cyclic isogenies from this curve, e.g. [1, 5, 25] |
| `jinv` | `numeric[]` | j-invariant [numerator,denominator] | j-invariant as numeric[2]: [numerator, denominator]. Reconstruct via QQ(tuple(jinv)) |
| `lmfdb_iso` | `text` | LMFDB isogeny class code | isogeny class label: N.c, e.g. '11.a' |
| `lmfdb_label` | `text` | LMFDB label | LMFDB label: N.c.n (conductor.isogeny_class.curve_number), e.g. '11.a1' |
| `lmfdb_number` | `smallint` | LMFDB index of curve in its isogeny class | 1-indexed position within isogeny class (LMFDB ordering) |
| `manin_constant` | `smallint` | Manin constant | positive integer, Manin constant c_E |
| `min_quad_twist_ainvs` | `numeric[]` | a-invariants of minimal quadratic twist | a-invariants of minimal quadratic twist, same format as ainvs |
| `min_quad_twist_disc` | `smallint` | discriminant of twist to minimal quadratic twist | discriminant d of the quadratic twist E_d that is minimal |
| `modell_images` | `text[]` | List of {{KNOWL('modcurve.other_labels', 'Sutherland labels')}} of mod-$\ell$ {{KNOWL('ec.galois_rep','Galois images'... | Sutherland labels of mod-ell Galois images in GL2(F_ell) |
| `modm_images` | `text[]` | Sorted list of RSZB labels (or partial labels) $\texttt{N.i.g.n}$ of subgroups of $\GL(2,\widehat \Z)$ that correspon... | RSZB labels of mod-m Galois images, format 'N.M.d.label' |
| `nonmax_primes` | `smallint[]` | primes for which the mod-p Galois representation has non-maximal image | primes ell where mod-ell Galois image is not maximal in GL2(F_ell) |
| `nonmax_rad` | `integer` | product of non-maximal primes | product of nonmax_primes |
| `num_bad_primes` | `smallint` | number of primes of bad reduction | count of primes of bad reduction |
| `num_int_pts` | `integer` | number of integral points | non-negative integer, count of integral points on minimal model |
| `optimality` | `smallint` | optimality code (0=no, 1=yes, n>0 if one of n possibles) | 0 = not optimal, 1 = optimal (Gamma_0(N)-optimal), n>1 = n candidates |
| `potential_good_reduction` | `boolean` | potential good reduction flag | boolean, true if E has potential good reduction at all primes |
| `rank` | `smallint` | Mordell-Weil rank | non-negative integer, Mordell-Weil rank |
| `regulator` | `numeric` | Regulator | positive real (arbitrary-precision), regulator of Mordell-Weil group |
| `semistable` | `boolean` | Semistable flag | boolean, true if all bad reduction is multiplicative |
| `serre_invariants` | `integer[]` | list of triples (p,w,n) for each prime p where the mod-p Serre weight w and conductor n are not (2,N) | flat triples [p1,w1,n1, p2,w2,n2,...]: prime, Serre weight, conductor exponent |
| `sha` | `integer` | Analytic order of Sha (rounded) | positive integer, analytic order of Sha (Tate-Shafarevich group), rounded |
| `sha_primes` | `smallint[]` | Primes dividing Sha | prime divisors of the analytic order of Sha |
| `signD` | `smallint` | Sign of discriminant | +1 or -1, sign of minimal discriminant |
| `squarefree_disc` | `boolean` | Squarefree discriminant flag | boolean, true if discriminant is squarefree |
| `stable_faltings_height` | `numeric` | Stable Faltings height | real (arbitrary-precision), stable Faltings height (isogeny-invariant) |
| `szpiro_ratio` | `double precision` | Szpiro ratio | floating-point, Szpiro ratio log|Delta|/log(N) |
| `torsion` | `smallint` | Torsion order | positive integer, order of torsion subgroup E(Q)_tors |
| `torsion_primes` | `smallint[]` | Primes dividing torsion order | prime divisors of torsion order |
| `torsion_structure` | `smallint[]` | Structure constants of torsion subgroup | invariant factors of E(Q)_tors in ascending order, e.g. [2,4] means Z/2 x Z/4. Empty [] for trivial |

---

## ec_galrep

**Rows:** 5,482,562

**API:** https://www.lmfdb.org/api/ec_galrep/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `adelic_gens` | `bigint[]` | List of generating matrices that define the adelic image of this elliptic curve. | generating matrices as flat 4-tuples [a,b,c,d, a,b,c,d,...] for 2x2 matrices mod M |
| `adelic_image` | `text` | The {{KNOWL('gl2.label','label')}} of the adelic image of this elliptic curve. | RSZB label of adelic image in GL2(Z-hat), only for prime=0 |
| `conductor` | `integer` | Conductor | positive integer |
| `elladic_image` | `text` | Sutherland code for the $\ell$-adic Galois image | Sutherland label of ell-adic image in GL2(Z_ell) |
| `lmfdb_label` | `text` | LMFDB label of curve | curve label |
| `modell_image` | `text` | Sutherland code for the mod-$\ell$ Galois image | Sutherland label of mod-ell image in GL2(F_ell) |
| `prime` | `smallint` | Prime with non-maximal Galois image | prime ell for ell-adic data; 0 = adelic data |

---

## ec_iqf_labels

Lookup table for converting old to new labels for ideals in imaginary quadratic fields

**Rows:** 46,358

**API:** https://www.lmfdb.org/api/ec_iqf_labels/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `fld` | `text` | Field label (for an imaginary quadratic field) | imaginary quadratic field label |
| `new` | `text` | Standard ideal label | standard ideal label |
| `old` | `text` | Old-style ideal label | old-style ideal label |

---

## ec_iwasawa

**Rows:** 974,104

**API:** https://www.lmfdb.org/api/ec_iwasawa/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `conductor` | `integer` | Conductor | positive integer |
| `iwdata` | `jsonb` | Iwasawa invariants. Keys are primes, including all bad multiplicative primes and all primes up to some bound. Values ... | JSON object: keys = prime strings, values = [lambda,mu] (ordinary) or [lambda0,lambda1,mu] (supersingular) or 'o?'/'ss?' (unknown) |
| `iwp0` | `smallint` | Iwasawa prime. if nonzero, a prime p0 such that lambda=mu=0 for all good p>=p0 | smallest prime p0 such that lambda=mu=0 for all good primes p >= p0. NULL if unknown |
| `lmfdb_label` | `text` | LMFDB label of curve | curve label |

---

## ec_localdata

**Rows:** 13,178,234

**API:** https://www.lmfdb.org/api/ec_localdata/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `conductor` | `integer` | Conductor | positive integer |
| `conductor_valuation` | `smallint` | Conductor valuation | v_p(N), exponent of p in conductor |
| `discriminant_valuation` | `smallint` | Discriminant valuation | v_p(Delta), exponent of p in discriminant |
| `j_denominator_valuation` | `smallint` | j-invariant denominator valuation | v_p(denominator of j-invariant) |
| `kodaira_symbol` | `smallint` | Kodaira symbol (PARI encoded) | PARI encoding: 1..10 = I_0..I_10; -1 = I*_0; <= -14: I*_m where m = -(code+4) |
| `lmfdb_label` | `text` | LMFDB label of curve | curve label |
| `prime` | `integer` | Prime (of bad reduction) | prime p of bad reduction |
| `reduction_type` | `smallint` | Type of bad reduction (0 additive, +1 split multiplicative, -1 non-split multiplicative) | -1 = nonsplit multiplicative, 0 = additive, +1 = split multiplicative |
| `root_number` | `smallint` | (local) root number | local root number epsilon_p in {0, 1} |
| `tamagawa_number` | `smallint` | Tamagawa number | positive integer c_p, local Tamagawa number at p |

---

## ec_mwbsd

**Rows:** 3,824,372

**API:** https://www.lmfdb.org/api/ec_mwbsd/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `area` | `numeric` | Area (covolume) of period lattice | covolume of period lattice, arbitrary-precision positive real |
| `conductor` | `integer` | Conductor | positive integer |
| `gens` | `numeric[]` | Generators (modulo torsion) | free generators in weighted projective coords, flat: [a1,b1,c1, a2,b2,c2,...]. Point = (a/c^2, b/c^3) |
| `heights` | `numeric[]` | Heights of generators | Neron-Tate canonical heights of generators, arbitrary-precision reals |
| `lmfdb_label` | `text` | LMFDB label of curve | curve label |
| `ngens` | `smallint` | Number of generators | non-negative integer, number of stored free generators (= rank) |
| `rank_bounds` | `smallint[]` | Lower and upper bounds for rank | [lower, upper] bounds for rank when exact rank unknown |
| `real_period` | `numeric` | Real Period | positive real (arbitrary-precision), real period Omega_E |
| `sha_an` | `numeric` | Analytic order of Sha | analytic order of Sha from BSD formula, arbitrary-precision |
| `special_value` | `numeric` | Leading coefficient of L-series | L^(r)(E,1)/r! where r = analytic rank, arbitrary-precision |
| `tamagawa_product` | `integer` | Product of Tamagawa numbers | positive integer, product of local Tamagawa numbers prod_p c_p |
| `torsion_generators` | `numeric[]` | Generators of torsion subgroup | torsion generators in weighted projective coords [a,b,c], flat like gens |
| `xcoord_integral_points` | `numeric[]` | x-coordinates of integral points | x-coordinates of integral points on minimal model |

---

## ec_nfcurves

Elliptic curves over *Q* and other number fields

**Rows:** 767,518

**API:** https://www.lmfdb.org/api/ec_nfcurves/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `Lvalue` | `numeric` | leading coefficient of L-series | L(E,1) or L^(r)(E,1)/r!, arbitrary-precision |
| `abs_disc` | `bigint` | absolute value of discriminant of base field | |N(discriminant ideal)| |
| `ainvs` | `text` | 5 Weierstrass coefficients (a-invariants) as a single string | text: 5 a-invariants as semicolon-separated field elements. Each element = comma-separated coefficients in power basis {1,alpha,alpha^2,...}. E.g. '0,0;-1,0;1,0;0,-1;0,-1' |
| `analytic_rank` | `smallint` | analytic rank | non-negative integer |
| `bad_primes` | `jsonb` | primes of bad reduction | JSON list of prime ideal strings in w-generator notation, e.g. ['(2,w+1)', '(3)'] |
| `base_change` | `jsonb` | labels of base change source curves | JSON list of curve labels this is a base change of. Labels without '-' = curves over Q (Cremona labels), with '-' = curves over number fields (ECNF labels). Empty [] = not a base change |
| `class_deg` | `integer` | LCM of isogeny degrees within this class | positive integer, LCM of isogeny degrees |
| `class_label` | `text` | full label of the isogeny class | string label (cross-reference) |
| `class_size` | `smallint` | Number of curves in the isogeny class | positive integer, curves in isogeny class |
| `cm` | `integer` | CM code. Either 0 for no CM, or a negative discriminant. | CM discriminant or 0 |
| `cm_type` | `smallint` | potential/actual CM | 0 = no CM, 1 = potential CM, 2 = actual CM over K |
| `conductor_ideal` | `text` | data defining the conductor | human-readable ideal representation |
| `conductor_label` | `text` | label of the conductor | label of conductor ideal, e.g. '100.1' |
| `conductor_norm` | `bigint` | norm of the conductor | positive integer, norm N(conductor ideal) |
| `conductor_norm_factors` | `integer[]` | Prime factors of conductor norm | list of integers |
| `degree` | `smallint` | Base field degree | degree [K:Q] |
| `disc` | `text` | Discriminant | discriminant as text (ideal or integer) |
| `equation` | `text` | Weierstrass equation (LaTeX) | Weierstrass equation as LaTeX string |
| `field_label` | `text` | Base field label | number field label d.r1.disc.index, e.g. '2.0.4.1' |
| `galois_images` | `jsonb` | Sutherland codes for non-maximal mod p Galois images | JSON list of Sutherland GL2(F_p) subgroup labels for non-maximal images, parallel to nonmax_primes. E.g. ['2B', '3Cs.1.1'] |
| `gens` | `jsonb` | generators of infinite order | JSON list of strings, each a MW generator as projective point '[[c0,...],[d0,...],[e0,...]]' where each coord is rational coeffs in {1,alpha,...} basis. Affine point = (x,y) with x=a/c^2, y=b/c^3 |
| `heights` | `numeric[]` | heights of generators | Neron-Tate heights of generators |
| `iso_label` | `text` | isogeny class label | short isogeny class label (without field prefix) |
| `iso_nlabel` | `smallint` | isogeny class index | numerical isogeny class index (a=0, b=1, ...) |
| `isodeg` | `integer[]` | Degrees of cyclic isogenies | degrees of cyclic isogenies from this curve |
| `isogeny_matrix` | `jsonb` | Matrix of isogeny degrees between curves in the isogeny class | JSON nested list [[d_ij,...],...] of isogeny degrees: M[i][j] = degree of cyclic isogeny from curve i to j. Symmetric, diagonal = 1 |
| `jinv` | `text` | j-invariant | j-invariant as text string (exact field element representation) |
| `label` | `text` | full label | full label: field-cond_norm-cond_label-class-number, e.g. '2.0.4.1-100.1-a1' |
| `local_data` | `jsonb` | List of local data at bad primes | JSON list of dicts per bad prime: keys {p (ideal string in w-notation), normp (int), ord_cond, ord_disc, ord_den_j, cp (Tamagawa number), kod (PARI Kodaira symbol int), red (0=additive, 1=split mult, -1=nonsplit mult), rootno (local root number)} |
| `minD` | `text` | minimal discriminant ideal | text |
| `n_bad_primes` | `integer` | Number of bad primes | integer |
| `ngens` | `smallint` | Number of generators of infinite order stored | number of stored Mordell-Weil generators |
| `non_min_p` | `jsonb` | Non-minimal primes | JSON list of prime ideal strings where the stored model is not minimal. Usually [] (globally minimal) or length 1 |
| `nonmax_primes` | `smallint[]` | List of nonmaximal primes | primes with non-maximal mod-p Galois image |
| `nonmax_rad` | `integer` | product of nonmaximal primes | product of nonmax_primes |
| `normdisc` | `numeric` | Norm of minimal discriminant | norm of minimal discriminant ideal, arbitrary-precision |
| `number` | `smallint` | index of curve in isogeny class. starts at 1 | 1-indexed curve number in isogeny class |
| `omega` | `numeric` | product of local periods | period (product of local periods), arbitrary-precision |
| `potential_good_reduction` | `boolean` | Potential good reduction flag | boolean |
| `q_curve` | `boolean` | Q-curve flag | boolean, true if E is isogenous to all its Galois conjugates |
| `rank` | `smallint` | rank | non-negative integer, Mordell-Weil rank over K |
| `rank_bounds` | `jsonb` | lower and upper rank bounds | JSON [lower, upper] bounds for Mordell-Weil rank, e.g. [0, 2] means 0 <= rank <= 2 |
| `reducible_primes` | `integer[]` | Reducible primes (at which Galois representation is non-maximal) | primes with reducible mod-p Galois representation |
| `reg` | `numeric` | regulator | regulator, arbitrary-precision |
| `root_analytic_conductor` | `double precision` | The {{KNOWL("lfunction.root_analytic_conductor", "root analytic conductor")}} of the associated L-function | floating-point, root analytic conductor |
| `semistable` | `boolean` | Semistable flag | boolean |
| `sha` | `integer` | Analytic order of Sha (rounded) | analytic order of Sha |
| `short_class_label` | `text` | short label of isogeny class (excludes field) | string label (cross-reference) |
| `short_label` | `text` | short label (excludes field) | string label (cross-reference) |
| `signature` | `jsonb` | Base field signature | JSON [r1, r2]: r1 = real embeddings, r2 = complex pairs. r1+2*r2 = [K:Q] |
| `tamagawa_product` | `integer` | Product of Tamagawa numbers | positive integer, product of Tamagawa numbers |
| `torsion_gens` | `jsonb` | torsion generators | JSON list of strings, each a torsion generator as projective point '[[c0,...],[d0,...],[e0,...]]' where each coord is coeffs in power basis of K/Q |
| `torsion_order` | `smallint` | torsion order | positive integer, |E(K)_tors| |
| `torsion_primes` | `integer[]` | primes dividing torsino order | prime divisors of torsion order |
| `torsion_structure` | `jsonb` | invariants of torsion subgroup | JSON list of invariant factors of E(K)_tors ascending, e.g. [2,4] = Z/2 x Z/4. Empty [] for trivial |
| `trace_hash` | `bigint` | Trace hash | 64-bit hash of traces for fast lookup |

---

## ec_nfcurves_test

**Rows:** 687,520

**API:** https://www.lmfdb.org/api/ec_nfcurves_test/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `Lvalue` | `numeric` | (description not yet updated on this server) | arbitrary-precision integer |
| `abs_disc` | `bigint` | (description not yet updated on this server) | integer |
| `ainvs` | `text` | (description not yet updated on this server) | list of 5 integers [a1, a2, a3, a4, a6] |
| `analytic_rank` | `smallint` | (description not yet updated on this server) | integer |
| `bad_primes` | `jsonb` | (description not yet updated on this server) | JSON list of prime ideal strings in w-generator notation (same as ec_nfcurves) |
| `base_change` | `jsonb` | (description not yet updated on this server) | JSON list of curve labels this is a base change of (same as ec_nfcurves) |
| `class_deg` | `integer` | (description not yet updated on this server) | integer |
| `class_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `class_size` | `smallint` | (description not yet updated on this server) | integer |
| `cm` | `integer` | (description not yet updated on this server) | integer |
| `cm_type` | `smallint` | (description not yet updated on this server) | integer |
| `conductor_ideal` | `text` | (description not yet updated on this server) | text |
| `conductor_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `conductor_norm` | `bigint` | (description not yet updated on this server) | integer |
| `conductor_norm_factors` | `integer[]` | (description not yet updated on this server) | list of integers |
| `degree` | `smallint` | (description not yet updated on this server) | positive integer |
| `disc` | `text` | (description not yet updated on this server) | integer (discriminant) |
| `equation` | `text` | (description not yet updated on this server) | text |
| `field_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `galois_images` | `jsonb` | (description not yet updated on this server) | JSON list of Sutherland GL2(F_p) subgroup labels (same as ec_nfcurves) |
| `gens` | `jsonb` | (description not yet updated on this server) | JSON list of MW generator strings as projective points over K (same as ec_nfcurves) |
| `heights` | `numeric[]` | (description not yet updated on this server) | list of integers (length 0 in sample) |
| `iso_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `iso_nlabel` | `smallint` | (description not yet updated on this server) | integer |
| `isodeg` | `integer[]` | (description not yet updated on this server) | list of integers |
| `isogeny_matrix` | `jsonb` | (description not yet updated on this server) | JSON nested list of isogeny degrees (same as ec_nfcurves) |
| `jinv` | `text` | (description not yet updated on this server) | text |
| `label` | `text` | (description not yet updated on this server) | string label |
| `local_data` | `jsonb` | (description not yet updated on this server) | JSON list of dicts per bad prime (same as ec_nfcurves) |
| `minD` | `text` | (description not yet updated on this server) | text |
| `n_bad_primes` | `integer` | (description not yet updated on this server) | integer |
| `ngens` | `smallint` | (description not yet updated on this server) | integer |
| `non_min_p` | `jsonb` | (description not yet updated on this server) | JSON list of prime ideal strings where model is not minimal (same as ec_nfcurves) |
| `nonmax_primes` | `smallint[]` | (description not yet updated on this server) | list of small integers |
| `nonmax_rad` | `integer` | (description not yet updated on this server) | integer |
| `normdisc` | `numeric` | (description not yet updated on this server) | arbitrary-precision integer |
| `number` | `smallint` | (description not yet updated on this server) | integer |
| `omega` | `numeric` | (description not yet updated on this server) | arbitrary-precision integer |
| `potential_good_reduction` | `boolean` | (description not yet updated on this server) | boolean |
| `q_curve` | `boolean` | (description not yet updated on this server) | boolean |
| `rank` | `smallint` | (description not yet updated on this server) | non-negative integer |
| `rank_bounds` | `jsonb` | (description not yet updated on this server) | JSON [lower, upper] bounds for rank (same as ec_nfcurves) |
| `reducible_primes` | `integer[]` | (description not yet updated on this server) | list of integers |
| `reg` | `numeric` | (description not yet updated on this server) | arbitrary-precision integer |
| `root_analytic_conductor` | `double precision` | (description not yet updated on this server) | floating-point approximation |
| `semistable` | `boolean` | (description not yet updated on this server) | boolean |
| `sha` | `integer` | (description not yet updated on this server) | integer |
| `short_class_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `short_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `signature` | `jsonb` | (description not yet updated on this server) | JSON [r1, r2] signature of base field K (same as ec_nfcurves) |
| `tamagawa_product` | `integer` | (description not yet updated on this server) | integer |
| `torsion_gens` | `jsonb` | (description not yet updated on this server) | JSON list of torsion generator strings as projective points (same as ec_nfcurves) |
| `torsion_order` | `smallint` | (description not yet updated on this server) | integer |
| `torsion_primes` | `integer[]` | (description not yet updated on this server) | list of integers |
| `torsion_structure` | `jsonb` | (description not yet updated on this server) | JSON list of invariant factors of E(K)_tors (same as ec_nfcurves) |
| `trace_hash` | `bigint` | (description not yet updated on this server) | integer |

---

## ec_nfportraits

Plots for elliptic curves over number fields of degree at least 3

**Rows:** 170,119

**API:** https://www.lmfdb.org/api/ec_nfportraits/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `label` | `text` | (description not yet updated on this server) | curve label |
| `portrait` | `text` | (description not yet updated on this server) | base64-encoded PNG image of curve portrait |

---

## ec_padic

p-adic data for elliptic curves over *Q*

**Rows:** 6,819,842

**API:** https://www.lmfdb.org/api/ec_padic/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `lmfdb_iso` | `text` | LMFDB label of isogeny class | isogeny class label |
| `p` | `smallint` | prime | prime p |
| `prec` | `smallint` | p-adic precision | p-adic precision of computation |
| `unit` | `numeric` | unit factor of regulator | unit part of p-adic regulator (coprime to p), arbitrary-precision |
| `val` | `smallint` | valuation of p-adic regulator | p-adic valuation v_p(R_p) of p-adic regulator |

---

## ec_sympow

**Rows:** 23,338,296

**API:** https://www.lmfdb.org/api/ec_sympow/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `conductor` | `numeric` | Conductor of the L-function of the symmetric power | conductor of Sym^k(E), arbitrary-precision |
| `lmfdb_iso` | `text` | Label of base isogeny class | isogeny class label |
| `power` | `smallint` | power | positive integer k, the symmetric power Sym^k |

---

## ec_torsion_growth

**Rows:** 16,491,706

**API:** https://www.lmfdb.org/api/ec_torsion_growth/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `conductor` | `integer` | Conductor | positive integer |
| `degree` | `smallint` | Degree of extension field | degree [K:Q] of extension field |
| `field` | `numeric[]` | Extension field (polynomial coefficients) | defining polynomial coefficients [a0,a1,...,an] of K/Q (constant term first) |
| `lmfdb_label` | `text` | LMFDB label | curve label over Q |
| `torsion` | `smallint[]` | Torsion structure over the extension field | torsion structure of E(K)_tors, invariant factors e.g. [2,8] |

---
