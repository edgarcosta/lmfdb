# mf — Database Schema

**24 tables, 553 columns total**

### Tables

- [mf_boxes](#mf_boxes) (12 rows)
- [mf_gamma1](#mf_gamma1) (1,161,064 rows)
- [mf_gamma1_eis](#mf_gamma1_eis) (1,163,555 rows)
- [mf_gamma1_portraits](#mf_gamma1_portraits) (27,801 rows)
- [mf_hecke_cc](#mf_hecke_cc) (14,417,694 rows)
- [mf_hecke_cc_eis](#mf_hecke_cc_eis) (187,911 rows)
- [mf_hecke_charpolys](#mf_hecke_charpolys) (5,472,725 rows)
- [mf_hecke_lpolys](#mf_hecke_lpolys) (5,472,725 rows)
- [mf_hecke_lpolys_eis](#mf_hecke_lpolys_eis) (6,354,800 rows)
- [mf_hecke_nf](#mf_hecke_nf) (218,909 rows)
- [mf_hecke_nf_eis](#mf_hecke_nf_eis) (254,192 rows)
- [mf_hecke_traces](#mf_hecke_traces) (184,889,242 rows)
- [mf_hecke_traces_eis](#mf_hecke_traces_eis) (224,730,242 rows)
- [mf_newform_portraits](#mf_newform_portraits) (281,965 rows)
- [mf_newform_portraits_test](#mf_newform_portraits_test) (2,055 rows)
- [mf_newforms](#mf_newforms) (1,141,510 rows)
- [mf_newforms_eis](#mf_newforms_eis) (1,181,351 rows)
- [mf_newspace_portraits](#mf_newspace_portraits) (338,553 rows)
- [mf_newspaces](#mf_newspaces) (2,471,024 rows)
- [mf_newspaces_al](#mf_newspaces_al) (2,471,024 rows)
- [mf_newspaces_eis](#mf_newspaces_eis) (2,514,785 rows)
- [mf_stark](#mf_stark) (2,556 rows)
- [mf_twists_cc](#mf_twists_cc) (49,165,089 rows)
- [mf_twists_nf](#mf_twists_nf) (1,622,040 rows)

---

## mf_boxes

**Rows:** 12

**API:** https://www.lmfdb.org/api/mf_boxes/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `Dmax` | `integer` | upper bound on the Q-dimension of newspaces in this box | integer |
| `Dmin` | `integer` | lower bound on the Q-dimension of newspaces in this box | integer |
| `Nk2max` | `integer` | upper bound on level*weight^2 for newspaces in this box | integer |
| `Nk2min` | `integer` | lower bound on level*weight^2 for newspaces in this box | integer |
| `Nk_count` | `integer` | count of (N,k) pairs (number of S_k(Gamma_1(N)) spaces) | non-negative integer (count) |
| `Nmax` | `integer` | upper bound on level | integer |
| `Nmin` | `integer` | lower bound on level | integer |
| `eigenvalues` | `boolean` | true if eigenvalue data is available for embedded newforms of small dimension in this box | boolean |
| `embedding_count` | `bigint` | total number of embedded newforms in this box | non-negative integer (count) |
| `embeddings` | `boolean` | true if eigenvalue data is available for embedded newforms in this box | boolean |
| `kmax` | `integer` | upper bound on weight | integer |
| `kmin` | `integer` | lower bound on weight | integer |
| `lfunctions` | `boolean` | true if L-functions have been computed for newforms in this box | boolean |
| `newform_count` | `integer` | number of newforms (Galois orbits) in this box | non-negative integer (count) |
| `newspace_count` | `integer` | number of newspaces S_k^new(N,chi) in this box | non-negative integer (count) |
| `nonzero_Nk_count` | `integer` | number of S_k(Gamma_1(N) spaces) in this box that have positive dimension | non-negative integer (count) |
| `nonzero_newspace_count` | `integer` | number of newspaces S_k^new(N,chi) in this box that have positive dimension | non-negative integer (count) |
| `omax` | `integer` | upper bound on the order of chi for newspaces S_k^new(N,chi) in this box | integer |
| `omin` | `integer` | lower bound on the order of chi for newspaces S_k^new(N,chi) in this box | integer |
| `split` | `boolean` | true if the newspaces in this box have been decomposed into newforms | boolean |
| `straces` | `boolean` | true if traces for the newspaces in this box have been computed | boolean |
| `traces` | `boolean` | true if traces for the newforms in this box have been computed | boolean |

---

## mf_gamma1

**Rows:** 1,161,064

**API:** https://www.lmfdb.org/api/mf_gamma1/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `Nk2` | `bigint` | level*weight^2 | integer |
| `a4_dim` | `integer` | sum of the dimensions of the A4 newforms in this newspace (always 0 for k > 1) | integer |
| `a5_dim` | `integer` | sum of the dimensions of the A5 newforms in this newspace (always 0 for k > 1) | integer |
| `analytic_conductor` | `double precision` | the {{KNOWL('analytic_conductor', 'analytic conductor')}} of this newspace | floating-point approximation |
| `cusp_dim` | `bigint` | Q-dimension of the cuspidal space S_k(Gamma1(N)) | integer |
| `dihedral_dim` | `integer` | sum of the dimensions of the dihedral newforms in this newspace (always 0 for k > 1) | integer |
| `dim` | `bigint` | Q-dimension of S_k^new(Gamma1(N)) | non-negative integer |
| `eis_dim` | `bigint` | Q-dimension of the Eisenstein subspace of M_k(Gamma1(N)) | integer |
| `eis_new_dim` | `bigint` | Q-dimension of the new part of the Eisenstein subspace of M_k(Gamma1(N)) | integer |
| `hecke_orbit_dims` | `bigint[]` | list of Q-dimensions of newforms in S_k(Gamma1(N)) (ordered by label) if known | list of integers |
| `label` | `text` | label N.k of this newspace | string label |
| `level` | `integer` | level N | positive integer |
| `level_is_powerful` | `boolean` | True if level is divisible by the square of every prime divisor. | boolean |
| `level_is_prime` | `boolean` | true if level is prime | boolean |
| `level_is_prime_power` | `boolean` | true if level is a prime power | boolean |
| `level_is_prime_square` | `boolean` | True if the level is the square of a prime. | boolean |
| `level_is_square` | `boolean` | true if level is square | boolean |
| `level_is_squarefree` | `boolean` | true if level is squarefree | boolean |
| `level_primes` | `integer[]` | prime divisors of the level | list of integers |
| `level_radical` | `integer` | product of prime divisors of the level | integer |
| `mf_dim` | `bigint` | Q-dimension of M_k(Gamma1(N)) | integer |
| `mf_new_dim` | `bigint` | Q-dimension of M_k^new(Gamma1(N) | integer |
| `newspace_dims` | `bigint[]` | list of Q-dimension of newspaces S_k^new(N,chi) in S_k^new(Gamma1(N)) orderd by label | list of integers |
| `num_forms` | `integer` | number of newforms (Galois orbits) in S_k^new(Gamma1(N)) | non-negative integer (count) |
| `num_spaces` | `integer` | number of newspaces S_k^new(N,chi) in S_k^new(Gamma1(N)) | non-negative integer (count) |
| `s4_dim` | `integer` | sum of the dimensions of the S4 newforms in this newspace (always 0 for k > 1) | integer |
| `sturm_bound` | `bigint` | floor(k*Index(Gamma1(N))/12) | integer |
| `trace_bound` | `integer` | least nonnegative n such that traces from 1 to n uniquely distinguish all newforms in this newspace (0 if there is on... | integer |
| `trace_display` | `numeric[]` | list of the four traces tr(a2), tr(a3), tr(a5), tr(a7) of the traceform for S_k^new(Gamma1(N)), not computed in all c... | list of arbitrary-precision integers |
| `traces` | `numeric[]` | integer coefficients of the trace form for S_k^new(Gamma1(N)) | list of integers (length 0 in sample) |
| `weight` | `smallint` | weight k | positive integer (weight) |
| `weight_parity` | `smallint` | (-1)^k | integer |

---

## mf_gamma1_eis

**Rows:** 1,163,555

**API:** https://www.lmfdb.org/api/mf_gamma1_eis/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `Nk2` | `bigint` | level*weight^2 | integer |
| `a4_dim` | `integer` | sum of the dimensions of the A4 newforms in this newspace (always 0 for k > 1) | integer |
| `a5_dim` | `integer` | sum of the dimensions of the A5 newforms in this newspace (always 0 for k > 1) | integer |
| `analytic_conductor` | `double precision` | the {{KNOWL('analytic_conductor', 'analytic conductor')}} of this newspace | floating-point approximation |
| `cusp_dim` | `bigint` | Q-dimension of the cuspidal space S_k(Gamma1(N)) | integer |
| `dihedral_dim` | `integer` | sum of the dimensions of the dihedral newforms in this newspace (always 0 for k > 1) | integer |
| `dim` | `bigint` | Q-dimension of S_k^new(Gamma1(N)) | non-negative integer |
| `eis_dim` | `bigint` | Q-dimension of the Eisenstein subspace of M_k(Gamma1(N)) | integer |
| `eis_new_dim` | `bigint` | Q-dimension of the new part of the Eisenstein subspace of M_k(Gamma1(N)) | integer |
| `hecke_orbit_dims` | `bigint[]` | list of Q-dimensions of newforms in S_k(Gamma1(N)) (ordered by label) if known | list of integers |
| `is_cuspidal` | `boolean` | True if this is a cuspidal subspace | boolean |
| `label` | `text` | label N.k of this newspace | string label |
| `level` | `integer` | level N | positive integer |
| `level_is_powerful` | `boolean` | True if level is divisible by the square of every prime divisor. | boolean |
| `level_is_prime` | `boolean` | true if level is prime | boolean |
| `level_is_prime_power` | `boolean` | true if level is a prime power | boolean |
| `level_is_prime_square` | `boolean` | True if the level is the square of a prime. | boolean |
| `level_is_square` | `boolean` | true if level is square | boolean |
| `level_is_squarefree` | `boolean` | true if level is squarefree | boolean |
| `level_primes` | `integer[]` | prime divisors of the level | list of integers |
| `level_radical` | `integer` | product of prime divisors of the level | integer |
| `mf_dim` | `bigint` | Q-dimension of M_k(Gamma1(N)) | integer |
| `mf_new_dim` | `bigint` | Q-dimension of M_k^new(Gamma1(N) | integer |
| `newspace_dims` | `bigint[]` | list of Q-dimension of newspaces S_k^new(N,chi) in S_k^new(Gamma1(N)) orderd by label | list of integers |
| `num_forms` | `integer` | number of newforms (Galois orbits) in S_k^new(Gamma1(N)) | non-negative integer (count) |
| `num_spaces` | `integer` | number of newspaces S_k^new(N,chi) in S_k^new(Gamma1(N)) | non-negative integer (count) |
| `s4_dim` | `integer` | sum of the dimensions of the S4 newforms in this newspace (always 0 for k > 1) | integer |
| `sturm_bound` | `bigint` | floor(k*Index(Gamma1(N))/12) | integer |
| `trace_bound` | `integer` | least nonnegative n such that traces from 1 to n uniquely distinguish all newforms in this newspace (0 if there is on... | integer |
| `trace_display` | `numeric[]` | list of the four traces tr(a2), tr(a3), tr(a5), tr(a7) of the traceform for S_k^new(Gamma1(N)), not computed in all c... | list of arbitrary-precision integers |
| `traces` | `numeric[]` | integer coefficients of the trace form for S_k^new(Gamma1(N)) | list of arbitrary-precision integers |
| `weight` | `smallint` | weight k | positive integer (weight) |
| `weight_parity` | `smallint` | (-1)^k | integer |

---

## mf_gamma1_portraits

**Rows:** 27,801

**API:** https://www.lmfdb.org/api/mf_gamma1_portraits/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `label` | `text` | label N.k of the newspace S_k(Gamma1(N)) | string label |
| `level` | `integer` | level N | positive integer |
| `portrait` | `text` | base-64 encoded png to display in the properties box | binary image data (PNG) |
| `weight` | `smallint` | weight k | positive integer (weight) |

---

## mf_hecke_cc

**Rows:** 14,417,694

**API:** https://www.lmfdb.org/api/mf_hecke_cc/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `an_normalized` | `double precision[]` | list of pairs [x,y] such that a_n = n^{(k-1)/2)*(x+iy) | double precision[]: flat pairs [x1,y1, x2,y2,...] where a_n = n^((k-1)/2) * (x_n + i*y_n) |
| `angles` | `double precision[]` | list of pairs [p, `\theta_p`] where `a_p = p^{(k-1)/2} (e^{2\pi i \theta_p} + chi(p)e^{-2\pi i \theta_p})`; it will r... | double precision[]: Sato-Tate angles theta_p. a_p = 2*p^((k-1)/2)*cos(2*pi*theta_p) for good primes; NULL for bad primes |
| `char_orbit_index` | `smallint` | ordinal identifying the Galois orbit of the character of this embedded newform (base26 encoded as a in the label) | integer |
| `conrey_index` | `integer` | the integer n in the Conrey label N.n identifying the element of (Z/NZ)* that corresponds to the character | Conrey label of the character used for this embedding |
| `dual_conrey_index` | `integer` | the Conrey index n of the dual (complex conjugate) character | Conrey label of complex conjugate character |
| `dual_embedding_index` | `integer` | the embedding index for the dual (complex conjugate) embedded newform | integer |
| `dual_embedding_m` | `integer` | ordinal identifying the dual (complex conjugate) embedding in the list of all embeddings of this newform when ordered... | integer |
| `embedding_index` | `integer` | ordinal identify the embedding among those with the same Conrey label | index among embeddings with same conrey_index |
| `embedding_m` | `integer` | ordinal identifying the embedding in the list of all embeddings of this newform when ordered lexicographically by con... | global index among all embeddings of this newform |
| `embedding_root_imag` | `double precision` | imaginary part of the root corresponding to this embedding | imaginary part of the root defining this embedding |
| `embedding_root_real` | `double precision` | real part of the root corresponding to this embedding | real part of the root defining this embedding |
| `hecke_orbit` | `integer` | ordinal x identifying the newform in the newspace (when lex-ordered by traces), starting from 1. | integer |
| `hecke_orbit_code` | `bigint` | encoding of the newform label (N.k.i.x) into 64 bits via N + (k<<24) + ((i-1)<<36) + ((x-1)<<52) | 64-bit encoding |
| `label` | `text` | label N.k.a.x.n.i of the embedded newform, where N.a is the character orbit label and n distinguishes the Conrey labe... | embedded label N.k.a.x.n.i (includes Conrey index and embedding index) |
| `level` | `integer` | level N | positive integer |
| `weight` | `smallint` | weight k | positive integer (weight) |

---

## mf_hecke_cc_eis

**Rows:** 187,911

**API:** https://www.lmfdb.org/api/mf_hecke_cc_eis/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `an_normalized` | `double precision[]` | list of pairs [x,y] such that a_n = n^{(k-1)/2)*(x+iy) | list of floats |
| `angles` | `double precision[]` | list of pairs [p, `\theta_p`] where `a_p = p^{(k-1)/2} (e^{2\pi i \theta_p} + chi(p)e^{-2\pi i \theta_p})`; it will r... | list of floats |
| `char_orbit_index` | `smallint` | ordinal identifying the Galois orbit of the character of this embedded newform (base26 encoded as a in the label) | integer |
| `conrey_index` | `integer` | the integer n in the Conrey label N.n identifying the element of (Z/NZ)* that corresponds to the character | integer |
| `dual_conrey_index` | `integer` | the Conrey index n of the dual (complex conjugate) character | integer |
| `dual_embedding_index` | `integer` | the embedding index for the dual (complex conjugate) embedded newform | integer |
| `dual_embedding_m` | `integer` | ordinal identifying the dual (complex conjugate) embedding in the list of all embeddings of this newform when ordered... | integer |
| `embedding_index` | `integer` | ordinal identify the embedding among those with the same Conrey label | integer |
| `embedding_m` | `integer` | ordinal identifying the embedding in the list of all embeddings of this newform when ordered lexicographically by con... | integer |
| `embedding_root_imag` | `double precision` | imaginary part of the root corresponding to this embedding | floating-point approximation |
| `embedding_root_real` | `double precision` | real part of the root corresponding to this embedding | floating-point approximation |
| `hecke_orbit` | `integer` | ordinal x identifying the newform in the newspace (when lex-ordered by traces), starting from 1. | integer |
| `hecke_orbit_code` | `bigint` | encoding of the newform label (N.k.i.x) into 64 bits via N + (k<<24) + ((i-1)<<36) + ((x-1)<<52) | integer |
| `label` | `text` | label N.k.a.x.n.i of the embedded newform, where N.a is the character orbit label and n distinguishes the Conrey labe... | string label |
| `level` | `integer` | level N | positive integer |
| `weight` | `smallint` | weight k | positive integer (weight) |

---

## mf_hecke_charpolys

**Rows:** 5,472,725

**API:** https://www.lmfdb.org/api/mf_hecke_charpolys/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `charpoly_factorization` | `jsonb` | a pair [coeffs,e] where coeffs is a list of coefficients of the minpoly of a_p and e is [Q(f):Q(a_p)] | JSON: [[coeffs1, e1], [coeffs2, e2], ...] factored characteristic polynomial det(T-a_p). Each coeffs is polynomial coefficients (constant first) |
| `hecke_orbit_code` | `bigint` | encoding of the newform label (N.k.i.x) into 64 bits | 64-bit encoding |
| `p` | `integer` | prime p for which this row gives the factorization of the charpoly of a_p | prime p |

---

## mf_hecke_lpolys

**Rows:** 5,472,725

**API:** https://www.lmfdb.org/api/mf_hecke_lpolys/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `hecke_orbit_code` | `bigint` | encoding of the newform label (N.k.i.x) into 64 bits | 64-bit encoding |
| `lpoly` | `numeric[]` | L-polynomial of the rational L-function of the newform at the prime p | L-polynomial coefficients at p (constant term first) |
| `lpoly_factorization` | `jsonb` | list of pairs [c,e] such that Lp(T) = f(T)^e where f is a polynomial with coefficient list c | JSON: factorization of L-polynomial over Q |
| `p` | `integer` | prime p for which this row gives the L-polynomial of L(f,s) at the prime p | prime p |

---

## mf_hecke_lpolys_eis

**Rows:** 6,354,800

**API:** https://www.lmfdb.org/api/mf_hecke_lpolys_eis/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `hecke_orbit_code` | `bigint` | encoding of the newform label (N.k.i.x) into 64 bits | integer |
| `lpoly` | `numeric[]` | L-polynomial of the rational L-function of the newform at the prime p | list of arbitrary-precision integers |
| `lpoly_factorization` | `jsonb` | list of pairs [c,e] such that Lp(T) = f(T)^e where f is a polynomial with coefficient list c | list of pairs [c,e] such that Lp(T) = f(T)^e where f is a polynomial with coeffi (JSON array) |
| `p` | `integer` | prime p for which this row gives the L-polynomial of L(f,s) at the prime p | integer |

---

## mf_hecke_nf

**Rows:** 218,909

**API:** https://www.lmfdb.org/api/mf_hecke_nf/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `an` | `jsonb` | list of lists encoding Hecke eigenvalues a_1,a_2,...,a_100 either as a linear combination of the basis specified in t... | JSON: first 100 eigenvalues. If cyclotomic_generator=0: each a_n = [c0,...,cd-1] in Hecke ring basis. If cyclotomic_generator=m: each a_n = [[c1,e1],...,[ck,ek]] sparse polynomial in zeta_m |
| `ap` | `jsonb` | list of lists encoding Hecke eigenvalues of a_p (same format as a_n) for primes p up to maxp | JSON: eigenvalues a_p for primes p up to maxp, same format as an |
| `char_orbit_index` | `smallint` | ordinal i identifying the Galois orbit of the character of this newform (base26 encoded in the newform label / charac... | integer |
| `field_poly` | `numeric[]` | list of integer coefficients of a defining polynomial for the Hecke field | defining polynomial of Hecke field, coefficient ordering matches Sage (high degree first) |
| `hecke_orbit_code` | `bigint` | encoding of the tuple (N.k.i.x) into 64 bits | 64-bit encoding (same as mf_newforms) |
| `hecke_ring_character_values` | `jsonb` | list of pairs [[m1,[a11,...,a1n]],...[mr,[a1r,...,arn]]] where mi are generators of (Z/NZ)* and [ai1,...,ain] is the ... | JSON [[g1,[a11,...,a1d]],[g2,...]] character values on generators of (Z/NZ)* |
| `hecke_ring_cyclotomic_generator` | `integer` | zero or an integer m suth that an and ap are encoded as sparse integer polynomials in zeta_m (typically zeta_m is a r... | m if field is Q(zeta_m) and using cyclotomic basis; 0 otherwise |
| `hecke_ring_denominators` | `numeric[]` | List of integers giving denominators of the basis for the hecke ring in terms of the power basis (if hecke_ring_power... | denominators corresponding to hecke_ring_numerators entries |
| `hecke_ring_inverse_denominators` | `numeric[]` | List of integers giving denominators of the inverse basis that represents power basis in terms of the basis for the h... | inverse basis change denominators |
| `hecke_ring_inverse_numerators` | `numeric[]` | List of lists of integers giving numberators of the inverse basis that represents power basis in terms of the basis f... | inverse basis change matrix numerators |
| `hecke_ring_numerators` | `numeric[]` | List of lists of integers giving numberators of the basis for the hecke ring in terms of the power basis (if hecke_ri... | basis change matrix numerators: list of integer lists, each row = basis element as linear combination of power basis. Flattened for storage |
| `hecke_ring_power_basis` | `boolean` | True if we are using the power basis specified by field_poly as the basis for the hecke ring | boolean, true if using {1, alpha, alpha^2, ...} basis |
| `hecke_ring_rank` | `integer` | rank of Hecke ring as a free Z-module = dimension of newform = degree of field_lpoly | dim(newform) = degree of field_poly |
| `label` | `text` | label N.k.a.x | newform label N.k.a.x |
| `level` | `integer` | level N | positive integer |
| `maxp` | `integer` | larges prime for which a_p appears in the list ap | largest prime for which a_p is stored |
| `weight` | `smallint` | weight k | positive integer (weight) |

---

## mf_hecke_nf_eis

**Rows:** 254,192

**API:** https://www.lmfdb.org/api/mf_hecke_nf_eis/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `a0_denom` | `numeric` | the denominator of the constant term in the q-expansion of the Eisenstein series | arbitrary-precision integer |
| `a0_num` | `numeric[]` | the numerator of the constant term in the q-expansion of the Eisenstein series | list of arbitrary-precision integers |
| `an` | `jsonb` | list of lists encoding Hecke eigenvalues a_1,a_2,...,a_100 either as a linear combination of the basis specified in t... | list of lists encoding Hecke eigenvalues a_1,a_2,...,a_100 either as a linear co (JSON array) |
| `ap` | `jsonb` | list of lists encoding Hecke eigenvalues of a_p (same format as a_n) for primes p up to maxp | list of lists encoding Hecke eigenvalues of a_p (same format as a_n) for primes  (JSON array) |
| `char_orbit_index` | `smallint` | ordinal i identifying the Galois orbit of the character of this newform (base26 encoded in the newform label / charac... | integer |
| `field_poly` | `numeric[]` | list of integer coefficients of a defining polynomial for the Hecke field | list of arbitrary-precision integers |
| `hecke_orbit_code` | `bigint` | encoding of the tuple (N.k.i.x) into 64 bits | integer |
| `hecke_ring_character_values` | `jsonb` | list of pairs [[m1,[a11,...,a1n]],...[mr,[a1r,...,arn]]] where mi are generators of (Z/NZ)* and [ai1,...,ain] is the ... | list of pairs [[m1,[a11,...,a1n]],...[mr,[a1r,...,arn]]] where mi are generators |
| `hecke_ring_cyclotomic_generator` | `integer` | zero or an integer m suth that an and ap are encoded as sparse integer polynomials in zeta_m (typically zeta_m is a r... | integer |
| `hecke_ring_denominators` | `numeric[]` | List of integers giving denominators of the basis for the hecke ring in terms of the power basis (if hecke_ring_power... | list of arbitrary-precision integers |
| `hecke_ring_inverse_denominators` | `numeric[]` | List of integers giving denominators of the inverse basis that represents power basis in terms of the basis for the h... | list of arbitrary-precision integers |
| `hecke_ring_inverse_numerators` | `numeric[]` | List of lists of integers giving numberators of the inverse basis that represents power basis in terms of the basis f... | list of arbitrary-precision integers |
| `hecke_ring_numerators` | `numeric[]` | List of lists of integers giving numberators of the basis for the hecke ring in terms of the power basis (if hecke_ri... | list of arbitrary-precision integers |
| `hecke_ring_power_basis` | `boolean` | True if we are using the power basis specified by field_poly as the basis for the hecke ring | boolean |
| `hecke_ring_rank` | `integer` | rank of Hecke ring as a free Z-module = dimension of newform = degree of field_lpoly | integer |
| `label` | `text` | label N.k.a.x | string label |
| `level` | `integer` | level N | positive integer |
| `maxp` | `integer` | larges prime for which a_p appears in the list ap | integer |
| `weight` | `smallint` | weight k | positive integer (weight) |

---

## mf_hecke_traces

**Rows:** 184,889,242

**API:** https://www.lmfdb.org/api/mf_hecke_traces/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `hecke_orbit_code` | `bigint` | encoding of the newform label (N.k.i.x) into 64 bits via N + (k<<24) + ((i-1)<<36) + ((x-1)<<52) | 64-bit encoding |
| `n` | `integer` | index n of a_n | index n of the eigenvalue a_n |
| `trace_an` | `numeric` | integer containing the nth coefficient of the trace form for this newform | tr(a_n) as arbitrary-precision integer |

---

## mf_hecke_traces_eis

**Rows:** 224,730,242

**API:** https://www.lmfdb.org/api/mf_hecke_traces_eis/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `hecke_orbit_code` | `bigint` | encoding of the newform label (N.k.i.x) into 64 bits via N + (k<<24) + ((i-1)<<36) + ((x-1)<<52) | integer |
| `n` | `integer` | index n of a_n | integer |
| `trace_an` | `numeric` | integer containing the nth coefficient of the trace form for this newform | arbitrary-precision integer |

---

## mf_newform_portraits

**Rows:** 281,965

**API:** https://www.lmfdb.org/api/mf_newform_portraits/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `char_orbit_index` | `smallint` | ordinal i identifying the Galois orbit of the character of this newform (base26 encoded in the newform label / charac... | integer |
| `hecke_orbit` | `integer` | ordinal x identifying the newform in the newspace (when lex-ordered by traces), starting from 1. | integer |
| `label` | `text` | label N.k.a.x of the newform | newform label |
| `level` | `integer` | level N | positive integer |
| `portrait` | `text` | base-64 encoded image of the newform (plot created by portrait.sage) to display in the properties box | base64-encoded PNG image |
| `weight` | `smallint` | weight k | positive integer (weight) |

---

## mf_newform_portraits_test

**Rows:** 2,055

**API:** https://www.lmfdb.org/api/mf_newform_portraits_test/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `char_orbit_index` | `smallint` | (description not yet updated on this server) | integer |
| `hecke_orbit` | `integer` | (description not yet updated on this server) | integer |
| `label` | `text` | (description not yet updated on this server) | string label |
| `level` | `integer` | (description not yet updated on this server) | positive integer |
| `portrait` | `text` | (description not yet updated on this server) | binary image data (PNG) |
| `weight` | `smallint` | (description not yet updated on this server) | positive integer (weight) |

---

## mf_newforms

**Rows:** 1,141,510

**API:** https://www.lmfdb.org/api/mf_newforms/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `Nk2` | `integer` | N*k^2 | N * k^2 (used for ordering and search) |
| `analytic_conductor` | `double precision` | N*(Exp(Psi((k)/2))/(2*pi))^2 where Psi(t) := Gamma'(t)/Gamma(t) | floating-point, analytic conductor |
| `analytic_rank` | `smallint` | the analytic rank of the L-function of the embedded newforms in this newform orbit | non-negative integer, order of vanishing of L(f,s) at center |
| `analytic_rank_proved` | `boolean` | true if the analytic rank has been proved | boolean |
| `artin_degree` | `integer` | degree of the Artin rep corresponding to this newform (set only if k=1) | integer |
| `artin_field` | `numeric[]` | list of coefficients of a polynomial whose splitting field is the fixed field of the Artin rep corresponding to this ... | list of arbitrary-precision integers |
| `artin_field_label` | `text` | LMFDB label of artin_field (set only if k=1) | string label (cross-reference) |
| `artin_image` | `text` | GAP id N.n of the image of the Artin rep corresponding to the newform (set only if k=1) | text |
| `atkin_lehner_eigenvals` | `integer[]` | a list of pairs [p, ev] where ev is 1 or -1, the Atkin-Lehner eigenvalue for each p dividing N (NULL overall if nontr... | JSON list of [p, eigenvalue] pairs: [[p1,+/-1], [p2,+/-1],...] for primes p | N |
| `atkin_lehner_string` | `text` | list of signs +/- of Atkin-Lehner eigenvalues ordered by p (facilitates lookups) | string of +/- chars for quick search, e.g. '+-+' |
| `char_conductor` | `integer` | Conductor of the Dirichlet character chi of this newform | conductor of the character chi |
| `char_degree` | `integer` | Degree of the (cyclotomic) character field | degree [Q(chi):Q] |
| `char_is_minimal` | `boolean` | true if the character chi is {{KNOWL('character.dirichlet.minimal','minimal')}} | boolean |
| `char_is_real` | `boolean` | true if the character takes only real values (trivial or quadratic) | boolean, true if chi is real-valued (trivial or quadratic) |
| `char_orbit_index` | `smallint` | ordinal i identifying the Galois orbit of the character of this newform (base26 encoded in the newform label / charac... | 1-indexed ordinal of Galois orbit of Dirichlet character |
| `char_orbit_label` | `text` | base26-encoding of char_orbit_index-1 | base-26 encoded character orbit (a=1, b=2, ...) |
| `char_order` | `integer` | the order of the character chi | multiplicative order of chi |
| `char_parity` | `smallint` | 1 for even, -1 for odd | 1 = even, -1 = odd |
| `char_values` | `jsonb` | quadruple <N,n,u,v> where N is the level, n is the order of the character, u is a list of generators for the unit gro... | JSON: [[m1,[a11,...,a1d]], [m2,[a21,...,a2d]], ...] character values on generators of (Z/NZ)*. Each value is an element of Q(zeta_n) expressed as integer vector in power basis |
| `cm_discs` | `integer[]` | list of CM discriminants (the negative discriminants listed in self_twist_discs | negative discriminants from self_twist_discs (CM twists) |
| `conrey_index` | `integer` | Index `n` of the first Conrey label `N.n` in the Galois orbit of the character for this newform. | Conrey label n of first character in the Galois orbit |
| `dim` | `integer` | the dimension of this newform | non-negative integer, absolute dimension [Q(f):Q] |
| `embedded_related_objects` | `text[]` | list of lists of text URLs of related objects (e.g. Artin reps), indexed by embedding_m (so first entry is a list of ... | list of URL strings indexed by embedding_m |
| `field_disc` | `numeric` | discriminant of the coefficient field, if known | discriminant of Hecke field Q(f), arbitrary-precision |
| `field_disc_factorization` | `numeric[]` | factorization of field discriminant stored as ordered list of pairs [p,e] | factorization as flat list [p1,e1, p2,e2,...] of (prime, exponent) pairs |
| `field_poly` | `numeric[]` | list of integers giving defining polynomial for the Hecke field (standard Sage order of coefficients) | coefficients of defining polynomial of Hecke field Q(f), Sage ordering (high degree first). E.g. [1,0,-5,0,1] for x^4-5x^2+1 |
| `field_poly_is_cyclotomic` | `boolean` | true if field_poly is a cylcotomic polynomial (the field might be Q(zeta_n) even when this flage is not set if we hav... | boolean |
| `field_poly_is_real_cyclotomic` | `boolean` | true if field_poly is the minimal polynomial of zeta_n + zeta_n^-1 for some n (the field might be Q(zeta_n)^+ even wh... | boolean |
| `field_poly_root_of_unity` | `integer` | the value of n if either field_poly_is_cylotomic of field_poly_is_real_cyclotomic is set | m if Q(f) = Q(zeta_m) or Q(zeta_m)+, else NULL |
| `fricke_eigenval` | `smallint` | product of the Atkin-Lehner eigenvalues (NULL if nontrivial character) | product of all Atkin-Lehner eigenvalues, +1 or -1 (trivial char only) |
| `has_non_self_twist` | `smallint` | 1 if form admits a non-trivial inner twist, 0 if it does not, -1 if unknown | integer |
| `hecke_cutters` | `jsonb` | a list of pairs [p, F_p] where F_p is a list of integers encoding a polynomial; the intersection of the kernels of F_... | a list of pairs [p, F_p] where F_p is a list of integers encoding a polynomial;  |
| `hecke_orbit` | `integer` | (X) An integer that is encoded into x in the label via 1=a, 2=b, 26=z, 27=ba, 28=bb.  Note the shift: the letter is t... | index of Hecke orbit within the newspace |
| `hecke_orbit_code` | `bigint` | encoding of the tuple (N.k.i.x) into 64 bits, used in eigenvalue tables.  N + (k<<24) + ((i-1)<<36) + ((X-1)<<52). | 64-bit packed int: N + (k<<24) + ((char_orbit_index-1)<<36) + ((hecke_orbit-1)<<52) |
| `hecke_ring_generator_nbound` | `integer` | minimal integer m such that a_1,...,a_m generate the Hecke ring | minimal m such that a_1,...,a_m generate the Hecke ring |
| `hecke_ring_index` | `numeric` | (a divisor of) the index of the order generated by the Hecke eigenvalues in the maximal order.  Stored as its factori... | index [O_max : O_Hecke] of Hecke order in maximal order, arbitrary-precision |
| `hecke_ring_index_factorization` | `numeric[]` | Factorization of hecke_ring_index stored as ordered list of pairs [p,e]. | factorization as flat [p1,e1, p2,e2,...] |
| `hecke_ring_index_proved` | `boolean` | whether the index has been proved correct (computing the maximal order may not be possible) | boolean |
| `inner_twist_count` | `integer` | number of inner twists (includes proved and unproved), -1 if inner twists have not been computed (this applies to all... | number of inner twists, -1 if unknown |
| `inner_twists` | `integer[]` | List of septuples of integers [b,m,M,o,parity,order,disc] where <M,o> identifies the Galois orbit of a Dirichlet char... | list of integers |
| `is_cm` | `boolean` | whether there is cm.  1=yes, -1=no, 0=unknown | boolean |
| `is_largest` | `boolean` | True if the dimension of this newform is strictly larger than that of any other newforms in its newspace or Atkin-Leh... | boolean |
| `is_maximal` | `boolean` | True if the dimension of this newform is equal to the dimension of the newspace or AL-subspace that contains it | boolean |
| `is_polredabs` | `boolean` | whether the polynomial has been reduced by Pari's `polredabs` | boolean, true if field_poly is polredabs-reduced |
| `is_rm` | `boolean` | whether the form has RM | boolean |
| `is_self_dual` | `boolean` | true if L-func is self-dual (coeff field is totally real) | boolean, true if coefficient field is totally real |
| `is_self_twist` | `boolean` | whether this form has a nontrivial a self twist (CM or RM) | boolean |
| `is_twist_minimal` | `boolean` | true if level N is the same as the level of minimal_twist | boolean, true if this is the twist-minimal form |
| `label` | `text` | Label N.k.a.x of this newform | label N.k.a.x: level.weight.char_orbit.hecke_orbit, e.g. '1.12.a.a' |
| `level` | `integer` | level N | positive integer N (level of Gamma_0(N)) |
| `level_is_powerful` | `boolean` | True if level is divisible by the square of every prime divisor. | boolean |
| `level_is_prime` | `boolean` | true if N is prime (1 is not prime) | boolean |
| `level_is_prime_power` | `boolean` | true if N is a prime power (1 is not a prime power) | boolean |
| `level_is_prime_square` | `boolean` | True if the level is the square of a prime. | boolean |
| `level_is_square` | `boolean` | true if N is square | boolean |
| `level_is_squarefree` | `boolean` | true if N is squarefree | boolean |
| `level_primes` | `integer[]` | sorted list of prime divisors of N | list of integers |
| `level_radical` | `integer` | product of prime divisors of N | integer |
| `minimal_twist` | `text` | label of the designated twist-minimal rep of the twist-class of this newform | label of the twist-minimal form in the twist class |
| `nf_label` | `text` | LMFDB label for the corresponding number field (can be NULL) | LMFDB number field label (only for dim <= 20) |
| `prim_orbit_index` | `smallint` | char_orbit for the primitive version of this character | integer |
| `projective_field` | `numeric[]` | for weight 1 forms, list of integer coefficients of polynomial whose splitting field is the fixed field of the kernel... | list of arbitrary-precision integers |
| `projective_field_label` | `text` | LMFDB label of projective field (if present | string label (cross-reference) |
| `projective_image` | `text` | for weight 1 forms, isomorphism class of project image (e.g. which Dn | label of projective image: Dn, A4, S4, A5 (weight 1 only) |
| `projective_image_type` | `text` | for weight 1 forms, one of "Dn", "A4", "S4", "A5" | type name: 'Dn', 'A4', 'S4', 'A5' (weight 1 only) |
| `qexp_display` | `text` | latexed string for display on search page results | LaTeX string of q-expansion for display |
| `related_objects` | `text[]` | list of text URLs of related objects (e.g. elliptic curve isogeny class, Artin rep, ...), e.g. ["EllipticCurve/Q/11/a"] | list of URL strings to related LMFDB objects |
| `relative_dim` | `integer` | the Q(chi)-dimension of this Hecke orbit (=dim/char_degree) | dimension over character field, dim / char_degree |
| `rm_discs` | `integer[]` | list of RM discriminants (the positive discriminants listed in self_twist_discs) | positive discriminants from self_twist_discs (RM twists) |
| `sato_tate_group` | `text` | LMFDB label of Sato-Tate group (currently only present for weight k > 1) | text |
| `self_twist_discs` | `integer[]` | list of discriminants giving self twists (either 0,1,or 3 quadratic discriminants) | list of discriminants d for self-twists chi_d. CM: d<0. RM: d>0. Empty if no self-twist |
| `self_twist_type` | `smallint` | 0=none, 1=cm, 2=rm, 3=both | 0=none, 1=CM, 2=RM, 3=both |
| `space_label` | `text` | label N.k.a of the newspace containing this newform | parent newspace label N.k.a |
| `trace_display` | `numeric[]` | list of the first four a_n traces for display on search page results | first four traces [tr(a_2), tr(a_3), tr(a_5), tr(a_7)] |
| `trace_hash` | `bigint` | appropriate linear combination of the a_p between 2^12 and 2^13 | 64-bit hash for fast trace-based lookup |
| `trace_moments` | `numeric[]` | list of moments of a_p/p^((k-1)/2) computed over p <= 2^13 (rounded to three decimal places) | list of arbitrary-precision integers |
| `trace_zratio` | `numeric` | proportion of zero a_p values for p <= 2^13 (rounded to three decimal places) | arbitrary-precision integer |
| `traces` | `numeric[]` | full list of integer traces tr(a_n) for n from 1 to 1000 (or more) | integer trace values tr(a_n) for n=1 to ~1000, arbitrary-precision |
| `weight` | `smallint` | weight k | positive integer k (weight of modular form) |
| `weight_parity` | `smallint` | (-1)^k | integer |

---

## mf_newforms_eis

**Rows:** 1,181,351

**API:** https://www.lmfdb.org/api/mf_newforms_eis/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `Nk2` | `integer` | N*k^2 | integer |
| `a0_denom` | `numeric` | denominator of the constant term in the q-expansion | arbitrary-precision integer |
| `analytic_conductor` | `double precision` | N*(Exp(Psi((k)/2))/(2*pi))^2 where Psi(t) := Gamma'(t)/Gamma(t) | floating-point approximation |
| `analytic_rank` | `smallint` | the analytic rank of the L-function of the embedded newforms in this newform orbit | integer |
| `analytic_rank_proved` | `boolean` | true if the analytic rank has been proved | boolean |
| `artin_degree` | `integer` | degree of the Artin rep corresponding to this newform (set only if k=1) | integer |
| `artin_field` | `numeric[]` | list of coefficients of a polynomial whose splitting field is the fixed field of the Artin rep corresponding to this ... | list of arbitrary-precision integers |
| `artin_field_label` | `text` | LMFDB label of artin_field (set only if k=1) | string label (cross-reference) |
| `artin_image` | `text` | GAP id N.n of the image of the Artin rep corresponding to the newform (set only if k=1) | text |
| `atkin_lehner_eigenvals` | `integer[]` | a list of pairs [p, ev] where ev is 1 or -1, the Atkin-Lehner eigenvalue for each p dividing N (NULL overall if nontr... | list of integers |
| `atkin_lehner_string` | `text` | list of signs +/- of Atkin-Lehner eigenvalues ordered by p (facilitates lookups) | text |
| `char_conductor` | `integer` | Conductor of the Dirichlet character chi of this newform | integer |
| `char_degree` | `integer` | Degree of the (cyclotomic) character field | integer |
| `char_is_minimal` | `boolean` | true if the character chi is {{KNOWL('character.dirichlet.minimal','minimal')}} | boolean |
| `char_is_real` | `boolean` | true if the character takes only real values (trivial or quadratic) | boolean |
| `char_orbit_index` | `smallint` | ordinal i identifying the Galois orbit of the character of this newform (base26 encoded in the newform label / charac... | integer |
| `char_orbit_label` | `text` | base26-encoding of char_orbit_index-1 | string label (cross-reference) |
| `char_order` | `integer` | the order of the character chi | integer |
| `char_parity` | `smallint` | 1 for even, -1 for odd | integer |
| `char_values` | `jsonb` | quadruple <N,n,u,v> where N is the level, n is the order of the character, u is a list of generators for the unit gro... | quadruple <N,n,u,v> where N is the level, n is the order of the character, u is  (JSON array) |
| `cm_discs` | `integer[]` | list of CM discriminants (the negative discriminants listed in self_twist_discs | list of integers |
| `conrey_index` | `integer` | Index `n` of the first Conrey label `N.n` in the Galois orbit of the character for this newform. | integer |
| `dim` | `integer` | the dimension of this newform | non-negative integer |
| `embedded_related_objects` | `text[]` | list of lists of text URLs of related objects (e.g. Artin reps), indexed by embedding_m (so first entry is a list of ... | list of strings |
| `field_disc` | `numeric` | discriminant of the coefficient field, if known | arbitrary-precision integer |
| `field_disc_factorization` | `numeric[]` | factorization of field discriminant stored as ordered list of pairs [p,e] | list of integers (length 0 in sample) |
| `field_poly` | `numeric[]` | list of integers giving defining polynomial for the Hecke field (standard Sage order of coefficients) | list of arbitrary-precision integers |
| `field_poly_is_cyclotomic` | `boolean` | true if field_poly is a cylcotomic polynomial (the field might be Q(zeta_n) even when this flage is not set if we hav... | boolean |
| `field_poly_is_real_cyclotomic` | `boolean` | true if field_poly is the minimal polynomial of zeta_n + zeta_n^-1 for some n (the field might be Q(zeta_n)^+ even wh... | boolean |
| `field_poly_root_of_unity` | `integer` | the value of n if either field_poly_is_cylotomic of field_poly_is_real_cyclotomic is set | integer |
| `fricke_eigenval` | `smallint` | product of the Atkin-Lehner eigenvalues (NULL if nontrivial character) | integer |
| `has_non_self_twist` | `smallint` | 1 if form admits a non-trivial inner twist, 0 if it does not, -1 if unknown | integer |
| `hecke_cutters` | `jsonb` | a list of pairs [p, F_p] where F_p is a list of integers encoding a polynomial; the intersection of the kernels of F_... | a list of pairs [p, F_p] where F_p is a list of integers encoding a polynomial;  (JSON array) |
| `hecke_orbit` | `integer` | (X) An integer that is encoded into x in the label via 1=a, 2=b, 26=z, 27=ba, 28=bb.  Note the shift: the letter is t... | integer |
| `hecke_orbit_code` | `bigint` | encoding of the tuple (N.k.i.x) into 64 bits, used in eigenvalue tables.  N + (k<<24) + ((i-1)<<36) + ((X-1)<<52). | integer |
| `hecke_ring_generator_nbound` | `integer` | minimal integer m such that a_1,...,a_m generate the Hecke ring | integer |
| `hecke_ring_index` | `numeric` | (a divisor of) the index of the order generated by the Hecke eigenvalues in the maximal order.  Stored as its factori... | arbitrary-precision integer |
| `hecke_ring_index_factorization` | `numeric[]` | Factorization of hecke_ring_index stored as ordered list of pairs [p,e]. | list of integers (length 0 in sample) |
| `hecke_ring_index_proved` | `boolean` | whether the index has been proved correct (computing the maximal order may not be possible) | boolean |
| `inner_twist_count` | `integer` | number of inner twists (includes proved and unproved), -1 if inner twists have not been computed (this applies to all... | non-negative integer (count) |
| `inner_twists` | `integer[]` | List of septuples of integers [b,m,M,o,parity,order,disc] where <M,o> identifies the Galois orbit of a Dirichlet char... | list of integers |
| `is_cm` | `boolean` | whether there is cm.  1=yes, -1=no, 0=unknown | boolean |
| `is_cuspidal` | `boolean` | true if the form is a cusp form | boolean |
| `is_largest` | `boolean` | True if the dimension of this newform is strictly larger than that of any other newforms in its newspace or Atkin-Leh... | boolean |
| `is_maximal` | `boolean` | True if the dimension of this newform is equal to the dimension of the newspace or AL-subspace that contains it | boolean |
| `is_polredabs` | `boolean` | whether the polynomial has been reduced by Pari's `polredabs` | boolean |
| `is_rm` | `boolean` | whether the form has RM | boolean |
| `is_self_dual` | `boolean` | true if L-func is self-dual (coeff field is totally real) | boolean |
| `is_self_twist` | `boolean` | whether this form has a nontrivial a self twist (CM or RM) | boolean |
| `is_twist_minimal` | `boolean` | true if level N is the same as the level of minimal_twist | boolean |
| `label` | `text` | Label N.k.a.x of this newform | string label |
| `level` | `integer` | level N | positive integer |
| `level_is_powerful` | `boolean` | True if level is divisible by the square of every prime divisor. | boolean |
| `level_is_prime` | `boolean` | true if N is prime (1 is not prime) | boolean |
| `level_is_prime_power` | `boolean` | true if N is a prime power (1 is not a prime power) | boolean |
| `level_is_prime_square` | `boolean` | True if the level is the square of a prime. | boolean |
| `level_is_square` | `boolean` | true if N is square | boolean |
| `level_is_squarefree` | `boolean` | true if N is squarefree | boolean |
| `level_primes` | `integer[]` | sorted list of prime divisors of N | list of integers |
| `level_radical` | `integer` | product of prime divisors of N | integer |
| `minimal_twist` | `text` | label of the designated twist-minimal rep of the twist-class of this newform | text |
| `nf_label` | `text` | LMFDB label for the corresponding number field (can be NULL) | string label (cross-reference) |
| `prim_orbit_index` | `smallint` | char_orbit for the primitive version of this character | integer |
| `projective_field` | `numeric[]` | for weight 1 forms, list of integer coefficients of polynomial whose splitting field is the fixed field of the kernel... | list of arbitrary-precision integers |
| `projective_field_label` | `text` | LMFDB label of projective field (if present | string label (cross-reference) |
| `projective_image` | `text` | for weight 1 forms, isomorphism class of project image (e.g. which Dn | text |
| `projective_image_type` | `text` | for weight 1 forms, one of "Dn", "A4", "S4", "A5" | text |
| `qexp_display` | `text` | latexed string for display on search page results | text |
| `related_objects` | `text[]` | list of text URLs of related objects (e.g. elliptic curve isogeny class, Artin rep, ...), e.g. ["EllipticCurve/Q/11/a"] | list of strings |
| `relative_dim` | `integer` | the Q(chi)-dimension of this Hecke orbit (=dim/char_degree) | integer |
| `rm_discs` | `integer[]` | list of RM discriminants (the positive discriminants listed in self_twist_discs) | list of integers |
| `sato_tate_group` | `text` | LMFDB label of Sato-Tate group (currently only present for weight k > 1) | text |
| `self_twist_discs` | `integer[]` | list of discriminants giving self twists (either 0,1,or 3 quadratic discriminants) | list of integers |
| `self_twist_type` | `smallint` | 0=none, 1=cm, 2=rm, 3=both | integer |
| `space_label` | `text` | label N.k.a of the newspace containing this newform | string label (cross-reference) |
| `trace_a0_num` | `numeric` | trace of the numerators of the constant term in the q-expansion | arbitrary-precision integer |
| `trace_display` | `numeric[]` | list of the first four a_n traces for display on search page results | list of arbitrary-precision integers |
| `trace_hash` | `bigint` | appropriate linear combination of the a_p between 2^12 and 2^13 | integer |
| `trace_moments` | `numeric[]` | list of moments of a_p/p^((k-1)/2) computed over p <= 2^13 (rounded to three decimal places) | list of arbitrary-precision integers |
| `trace_zratio` | `numeric` | proportion of zero a_p values for p <= 2^13 (rounded to three decimal places) | arbitrary-precision integer |
| `traces` | `numeric[]` | full list of integer traces tr(a_n) for n from 1 to 1000 (or more) | list of arbitrary-precision integers |
| `weight` | `smallint` | weight k | positive integer (weight) |
| `weight_parity` | `smallint` | (-1)^k | integer |

---

## mf_newspace_portraits

**Rows:** 338,553

**API:** https://www.lmfdb.org/api/mf_newspace_portraits/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `char_orbit_index` | `smallint` | ordinal i identifying the Galois orbit of the character of this newspace (base26 encoded in the newform label / chara... | integer |
| `label` | `text` | label N.k.a of this newspace | newspace label |
| `level` | `integer` | level N | positive integer |
| `portrait` | `text` | base-64 encoded image of the newform (plot created by portrait.sage) to display in the properties box | base64-encoded PNG image |
| `weight` | `smallint` | weight k | positive integer (weight) |

---

## mf_newspaces

**Rows:** 2,471,024

**API:** https://www.lmfdb.org/api/mf_newspaces/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `ALdims` | `integer[]` | For newspaces with trivial character a list of the dimensions of the Atkin-Lehner subspaces: if $q_0,\ldots,q_{w-1}$ ... | Atkin-Lehner eigenspace dimensions (trivial char only). List indexed by subsets of bad primes |
| `ALdims_eis_new` | `integer[]` | For Eisenstein newspaces with trivial character a list of the dimensions of the Atkin-Lehner subspaces: if $q_0,\ldot... | list of integers |
| `ALdims_eis_old` | `integer[]` | For Eisenstein oldspaces with trivial character a list of the dimensions of the Atkin-Lehner subspaces: if $q_0,\ldot... | list of integers |
| `ALdims_old` | `integer[]` | For oldspaces with trivial character a list of the dimensions of the Atkin-Lehner subspaces: if $q_0,\ldots,q_{w-1}$ ... | list of integers |
| `Nk2` | `integer` | N*k^2 | N * k^2 |
| `a4_dim` | `integer` | total dimension of A4 Hecke orbits (only set for weight 1 | integer |
| `a5_dim` | `integer` | total dimension of A5 Hecke orbits (only set for weight 1 | integer |
| `analytic_conductor` | `double precision` | N*(Exp(Psi((k)/2))/(2*pi))^2 where Psi(t) := Gamma'(t)/Gamma(t) | analytic conductor N * (psi(k/2) / (2*pi))^2, floating-point |
| `char_conductor` | `integer` | Conductor of the Dirichlet character | conductor of chi |
| `char_degree` | `integer` | the degree of the (cyclotomic) character field | [Q(chi):Q] |
| `char_is_real` | `boolean` | whether the character takes only real values (trivial or quadratic) | boolean |
| `char_orbit_index` | `smallint` | ordinal i identifying the Galois orbit of the character chi of this newspace (base26 encoded in the newform label / c... | 1-indexed ordinal of character orbit |
| `char_orbit_label` | `text` | base26 encoding of char_orbit_index-1 | base-26 label (a=1, b=2, ...) |
| `char_order` | `integer` | the order of the character | multiplicative order of chi |
| `char_parity` | `smallint` | 1 or -1, depending on the parity of the character | 1 = even, -1 = odd |
| `char_values` | `jsonb` | quadruple <N,n,u,v> where N is the level, n is the order of the character, u is a list of generators for the unit gro... | quadruple <N,n,u,v> where N is the level, n is the order of the character, u is  (JSON array) |
| `conrey_index` | `integer` | The integer $n$ for which $N.n$ is the label of the first Conrey character in the Galois orbit of the character of th... | Conrey label of first character in orbit |
| `cusp_dim` | `integer` | Q-dimension of the cuspidal space `S_k(N, \chi)` | Q-dimension of full cuspidal space S_k(N,chi) |
| `dihedral_dim` | `integer` | total dimension of dihedral Hecke orbits (only set for weight 1) | integer |
| `dim` | `integer` | Q-dimension of this newspace | Q-dimension of S_k^new(N,chi) |
| `eis_dim` | `integer` | Q-dimension of the eisenstein subspace of the corresponding M_k(N,chi) | Q-dimension of Eisenstein subspace of M_k(N,chi) |
| `eis_new_dim` | `integer` | Q-dimension of the new eisenstein subspace of the corresponding M_k(N,chi) | Q-dimension of new Eisenstein part |
| `hecke_cutter_primes` | `integer[]` | list of primes that appear in the hecke cutters for the newforms in this space (empty list if num_forms=1, not set fo... | list of integers |
| `hecke_orbit_code` | `bigint` | Encoding of the tuple (N.k.i) into 64 bits, used as a key in mf_hecke_newspace_traces. N + (k<<24) + ((i-1)<<36) this... | 64-bit encoding N + (k<<24) + ((char_orbit_index-1)<<36) |
| `hecke_orbit_dims` | `integer[]` | Sorted list of dimensions of Hecke orbits (irreducible Galois stable subspaces) | sorted list of dimensions of Hecke orbits, ascending |
| `label` | `text` | Label N.k.a of this newspace | label N.k.a: level.weight.char_orbit |
| `level` | `integer` | level N | positive integer N |
| `level_is_powerful` | `boolean` | True if level is divisible by the square of every prime divisor. | boolean |
| `level_is_prime` | `boolean` | true if N is prime (1 is not prime) | boolean |
| `level_is_prime_power` | `boolean` | true if N is a prime power (1 is not a prime power) | boolean |
| `level_is_prime_square` | `boolean` | True if the level is the square of a prime. | boolean |
| `level_is_square` | `boolean` | true if N is square | boolean |
| `level_is_squarefree` | `boolean` | true if N is squarefree | boolean |
| `level_primes` | `integer[]` | sorted list of prime divisors of N | prime divisors of N, sorted |
| `level_radical` | `integer` | product of the prime divisors of N | product of prime divisors of N (radical) |
| `mf_dim` | `integer` | Q-dimension of M_k(N, \chi) | Q-dimension of M_k(N,chi) |
| `mf_new_dim` | `integer` | Q-dimension of M_k(N, chi) | Q-dimension of M_k^new(N,chi) |
| `num_forms` | `smallint` | number of Hecke orbits (each corresponds to a Galois conjugacy class of modular forms) | count of Hecke orbits (newforms) in this space |
| `plus_dim` | `integer` | For spaces with tirival character, dimension of the subspace with Fricke-eigevalue +1 | dimension of Fricke eigenvalue +1 subspace (trivial char only) |
| `prim_orbit_index` | `smallint` | char_orbit for the primitive version of this character | integer |
| `relative_dim` | `integer` | Q(chi)-dimension of the newspace S_k^new(N,[chi]), equal to dim/degree(chi) | dim / char_degree |
| `s4_dim` | `integer` | total dimension of S4 Hecke orbits (only set for weight 1 | integer |
| `sturm_bound` | `integer` | floor(k*Index(Gamma0(N))/12) | floor(k * [SL2(Z):Gamma0(N)] / 12) |
| `trace_bound` | `integer` | the integer n so that the traces from 1 up to n distinguish all forms in this space (e.g. 1 if the dimensions are all... | minimal n such that tr(a_1),...,tr(a_n) distinguish all forms in the space |
| `trace_display` | `numeric[]` | list of integer traces tr(a_2), tr(a_3), tr(a_5), tr(a_7), only set when dim > 0 and not yet computed in every case. | [tr(a_2), tr(a_3), tr(a_5), tr(a_7)] |
| `traces` | `numeric[]` | integer coefficients a_n of the trace form (sum of all newforms in the space) for n from 1 to 1000, only set when dim... | integer trace form coefficients tr(a_n) for n=1 to ~1000 |
| `weight` | `smallint` | weight k | positive integer k |
| `weight_parity` | `smallint` | (-1)^k | integer |

---

## mf_newspaces_al

**Rows:** 2,471,024

**API:** https://www.lmfdb.org/api/mf_newspaces_al/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `ALdims` | `integer[]` | For newspaces with trivial character a list of the dimensions of the Atkin-Lehner subspaces: if $q_0,\ldots,q_{w-1}$ ... | list of integers |
| `ALdims_eis_new` | `integer[]` | For Eisenstein newspaces with trivial character a list of the dimensions of the Atkin-Lehner subspaces: if $q_0,\ldot... | list of integers |
| `ALdims_eis_old` | `integer[]` | For Eisenstein oldspaces with trivial character a list of the dimensions of the Atkin-Lehner subspaces: if $q_0,\ldot... | list of integers |
| `ALdims_old` | `integer[]` | For oldspaces with trivial character a list of the dimensions of the Atkin-Lehner subspaces: if $q_0,\ldots,q_{w-1}$ ... | list of integers |
| `Nk2` | `integer` | N*k^2 | integer |
| `a4_dim` | `integer` | total dimension of A4 Hecke orbits (only set for weight 1 | integer |
| `a5_dim` | `integer` | total dimension of A5 Hecke orbits (only set for weight 1 | integer |
| `analytic_conductor` | `double precision` | N*(Exp(Psi((k)/2))/(2*pi))^2 where Psi(t) := Gamma'(t)/Gamma(t) | floating-point approximation |
| `char_conductor` | `integer` | Conductor of the Dirichlet character | integer |
| `char_degree` | `integer` | the degree of the (cyclotomic) character field | integer |
| `char_is_real` | `boolean` | whether the character takes only real values (trivial or quadratic) | boolean |
| `char_orbit_index` | `smallint` | ordinal i identifying the Galois orbit of the character chi of this newspace (base26 encoded in the newform label / c... | integer |
| `char_orbit_label` | `text` | base26 encoding of char_orbit_index-1 | string label (cross-reference) |
| `char_order` | `integer` | the order of the character | integer |
| `char_parity` | `smallint` | 1 or -1, depending on the parity of the character | integer |
| `char_values` | `jsonb` | quadruple <N,n,u,v> where N is the level, n is the order of the character, u is a list of generators for the unit gro... | quadruple <N,n,u,v> where N is the level, n is the order of the character, u is  (JSON array) |
| `conrey_index` | `integer` | The integer $n$ for which $N.n$ is the label of the first Conrey character in the Galois orbit of the character of th... | integer |
| `cusp_dim` | `integer` | Q-dimension of the cuspidal space `S_k(N, \chi)` | integer |
| `dihedral_dim` | `integer` | total dimension of dihedral Hecke orbits (only set for weight 1) | integer |
| `dim` | `integer` | Q-dimension of this newspace | non-negative integer |
| `eis_dim` | `integer` | Q-dimension of the eisenstein subspace of the corresponding M_k(N,chi) | integer |
| `eis_new_dim` | `integer` | Q-dimension of the new eisenstein subspace of the corresponding M_k(N,chi) | integer |
| `hecke_cutter_primes` | `integer[]` | list of primes that appear in the hecke cutters for the newforms in this space (empty list if num_forms=1, not set fo... | list of integers |
| `hecke_orbit_code` | `bigint` | Encoding of the tuple (N.k.i) into 64 bits, used as a key in mf_hecke_newspace_traces. N + (k<<24) + ((i-1)<<36) this... | integer |
| `hecke_orbit_dims` | `integer[]` | Sorted list of dimensions of Hecke orbits (irreducible Galois stable subspaces) | list of integers |
| `label` | `text` | Label N.k.a of this newspace | string label |
| `level` | `integer` | level N | positive integer |
| `level_is_powerful` | `boolean` | True if level is divisible by the square of every prime divisor. | boolean |
| `level_is_prime` | `boolean` | true if N is prime (1 is not prime) | boolean |
| `level_is_prime_power` | `boolean` | true if N is a prime power (1 is not a prime power) | boolean |
| `level_is_prime_square` | `boolean` | True if the level is the square of a prime. | boolean |
| `level_is_square` | `boolean` | true if N is square | boolean |
| `level_is_squarefree` | `boolean` | true if N is squarefree | boolean |
| `level_primes` | `integer[]` | sorted list of prime divisors of N | list of integers |
| `level_radical` | `integer` | product of the prime divisors of N | integer |
| `mf_dim` | `integer` | Q-dimension of M_k(N, \chi) | integer |
| `mf_new_dim` | `integer` | Q-dimension of M_k(N, chi) | integer |
| `num_forms` | `smallint` | number of Hecke orbits (each corresponds to a Galois conjugacy class of modular forms) | non-negative integer (count) |
| `plus_dim` | `integer` | For spaces with tirival character, dimension of the subspace with Fricke-eigevalue +1 | integer |
| `prim_orbit_index` | `smallint` | char_orbit for the primitive version of this character | integer |
| `relative_dim` | `integer` | Q(chi)-dimension of the newspace S_k^new(N,[chi]), equal to dim/degree(chi) | integer |
| `s4_dim` | `integer` | total dimension of S4 Hecke orbits (only set for weight 1 | integer |
| `sturm_bound` | `integer` | floor(k*Index(Gamma0(N))/12) | integer |
| `trace_bound` | `integer` | the integer n so that the traces from 1 up to n distinguish all forms in this space (e.g. 1 if the dimensions are all... | integer |
| `trace_display` | `numeric[]` | list of integer traces tr(a_2), tr(a_3), tr(a_5), tr(a_7), only set when dim > 0 and not yet computed in every case. | list of arbitrary-precision integers |
| `traces` | `numeric[]` | integer coefficients a_n of the trace form (sum of all newforms in the space) for n from 1 to 1000, only set when dim... | list of arbitrary-precision integers |
| `weight` | `smallint` | weight k | positive integer (weight) |
| `weight_parity` | `smallint` | (-1)^k | integer |

---

## mf_newspaces_eis

**Rows:** 2,514,785

**API:** https://www.lmfdb.org/api/mf_newspaces_eis/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `ALdims` | `integer[]` | For newspaces with trivial character a list of the dimensions of the Atkin-Lehner subspaces: if $q_0,\ldots,q_{w-1}$ ... | list of integers |
| `ALdims_eis_new` | `integer[]` | For Eisenstein newspaces with trivial character a list of the dimensions of the Atkin-Lehner subspaces: if $q_0,\ldot... | list of integers |
| `ALdims_eis_old` | `integer[]` | For Eisenstein oldspaces with trivial character a list of the dimensions of the Atkin-Lehner subspaces: if $q_0,\ldot... | list of integers |
| `ALdims_old` | `integer[]` | For oldspaces with trivial character a list of the dimensions of the Atkin-Lehner subspaces: if $q_0,\ldots,q_{w-1}$ ... | list of integers |
| `Nk2` | `integer` | N*k^2 | integer |
| `a4_dim` | `integer` | total dimension of A4 Hecke orbits (only set for weight 1 | integer |
| `a5_dim` | `integer` | total dimension of A5 Hecke orbits (only set for weight 1 | integer |
| `analytic_conductor` | `double precision` | N*(Exp(Psi((k)/2))/(2*pi))^2 where Psi(t) := Gamma'(t)/Gamma(t) | floating-point approximation |
| `char_conductor` | `integer` | Conductor of the Dirichlet character | integer |
| `char_degree` | `integer` | the degree of the (cyclotomic) character field | integer |
| `char_is_real` | `boolean` | whether the character takes only real values (trivial or quadratic) | boolean |
| `char_orbit_index` | `smallint` | ordinal i identifying the Galois orbit of the character chi of this newspace (base26 encoded in the newform label / c... | integer |
| `char_orbit_label` | `text` | base26 encoding of char_orbit_index-1 | string label (cross-reference) |
| `char_order` | `integer` | the order of the character | integer |
| `char_parity` | `smallint` | 1 or -1, depending on the parity of the character | integer |
| `char_values` | `jsonb` | quadruple <N,n,u,v> where N is the level, n is the order of the character, u is a list of generators for the unit gro... | quadruple <N,n,u,v> where N is the level, n is the order of the character, u is  (JSON array) |
| `conrey_index` | `integer` | The integer $n$ for which $N.n$ is the label of the first Conrey character in the Galois orbit of the character of th... | integer |
| `cusp_dim` | `integer` | Q-dimension of the cuspidal space `S_k(N, \chi)` | integer |
| `dihedral_dim` | `integer` | total dimension of dihedral Hecke orbits (only set for weight 1) | integer |
| `dim` | `integer` | Q-dimension of this newspace | non-negative integer |
| `eis_dim` | `integer` | Q-dimension of the eisenstein subspace of the corresponding M_k(N,chi) | integer |
| `eis_new_dim` | `integer` | Q-dimension of the new eisenstein subspace of the corresponding M_k(N,chi) | integer |
| `hecke_cutter_primes` | `integer[]` | list of primes that appear in the hecke cutters for the newforms in this space (empty list if num_forms=1, not set fo... | list of integers |
| `hecke_orbit_code` | `bigint` | Encoding of the tuple (N.k.i) into 64 bits, used as a key in mf_hecke_newspace_traces. N + (k<<24) + ((i-1)<<36) this... | integer |
| `hecke_orbit_dims` | `integer[]` | Sorted list of dimensions of Hecke orbits (irreducible Galois stable subspaces) | list of integers |
| `is_cuspidal` | `boolean` | True if this is a cuspidal subspace | boolean |
| `label` | `text` | Label N.k.a of this newspace | string label |
| `level` | `integer` | level N | positive integer |
| `level_is_powerful` | `boolean` | True if level is divisible by the square of every prime divisor. | boolean |
| `level_is_prime` | `boolean` | true if N is prime (1 is not prime) | boolean |
| `level_is_prime_power` | `boolean` | true if N is a prime power (1 is not a prime power) | boolean |
| `level_is_prime_square` | `boolean` | True if the level is the square of a prime. | boolean |
| `level_is_square` | `boolean` | true if N is square | boolean |
| `level_is_squarefree` | `boolean` | true if N is squarefree | boolean |
| `level_primes` | `integer[]` | sorted list of prime divisors of N | list of integers |
| `level_radical` | `integer` | product of the prime divisors of N | integer |
| `mf_dim` | `integer` | Q-dimension of M_k(N, \chi) | integer |
| `mf_new_dim` | `integer` | Q-dimension of M_k(N, chi) | integer |
| `num_forms` | `smallint` | number of Hecke orbits (each corresponds to a Galois conjugacy class of modular forms) | non-negative integer (count) |
| `plus_dim` | `integer` | For spaces with tirival character, dimension of the subspace with Fricke-eigevalue +1 | integer |
| `prim_orbit_index` | `smallint` | char_orbit for the primitive version of this character | integer |
| `relative_dim` | `integer` | Q(chi)-dimension of the newspace S_k^new(N,[chi]), equal to dim/degree(chi) | integer |
| `s4_dim` | `integer` | total dimension of S4 Hecke orbits (only set for weight 1 | integer |
| `sturm_bound` | `integer` | floor(k*Index(Gamma0(N))/12) | integer |
| `trace_bound` | `integer` | the integer n so that the traces from 1 up to n distinguish all forms in this space (e.g. 1 if the dimensions are all... | integer |
| `trace_display` | `numeric[]` | list of integer traces tr(a_2), tr(a_3), tr(a_5), tr(a_7), only set when dim > 0 and not yet computed in every case. | list of arbitrary-precision integers |
| `traces` | `numeric[]` | integer coefficients a_n of the trace form (sum of all newforms in the space) for n from 1 to 1000, only set when dim... | list of arbitrary-precision integers |
| `weight` | `smallint` | weight k | positive integer (weight) |
| `weight_parity` | `smallint` | (-1)^k | integer |

---

## mf_stark

Stark units for weight 1 newforms

**Rows:** 2,556

**API:** https://www.lmfdb.org/api/mf_stark/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `b` | `text` | Element of coefficient field parameterizing Stark units | text |
| `m` | `integer` | Scaling factor for unit | integer |
| `mf_dim` | `integer` | dimension of modular form | integer |
| `mf_label` | `text` | Label for the modular form | string label (cross-reference) |
| `mf_level` | `integer` | level of modular form | integer |
| `stark_minpoly` | `numeric[]` | The minimal polynomial for the Stark unit | list of arbitrary-precision integers |

---

## mf_twists_cc

**Rows:** 49,165,089

**API:** https://www.lmfdb.org/api/mf_twists_cc/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `conductor` | `integer` | conductor of psi (equal to the modulus M in its label since psi is primitive) | positive integer |
| `degree` | `integer` | degree of psi = [Q(psi):Q] = phi(order) = cardinality of character orbit [psi] | positive integer |
| `order` | `integer` | order of psi | integer |
| `parity` | `smallint` | parity of psi | integer |
| `source_conrey_index` | `integer` | Conrey index of source newform (numeric value of n in source_label) | integer |
| `source_dim` | `integer` | dimension of the source newform orbit | integer |
| `source_embedding_index` | `integer` | (description not yet updated on this server) | integer |
| `source_hecke_orbit_code` | `bigint` | Hecke orbit code of source newform (64-bit encoding of N.k.a.x in source label) | integer |
| `source_is_minimal` | `boolean` | true if source newform is twist-minimal and has minimal character | boolean |
| `source_label` | `text` | label (N.k.a.x.n.i) of the embedded newform being twisted | string label (cross-reference) |
| `source_level` | `integer` | level of the source newform | integer |
| `target_conrey_index` | `integer` | Conrey index of target newform character (numeric value of n in target_label) | integer |
| `target_dim` | `integer` | dimension of the target newform orbit | integer |
| `target_embedding_index` | `integer` | (description not yet updated on this server) | integer |
| `target_hecke_orbit_code` | `bigint` | Hecke orbit code of target newform (64-bit encoding of N.k.a.x in target label) | integer |
| `target_is_minimal` | `boolean` | true if target newform is twist-minimal and has minimal character | boolean |
| `target_label` | `text` | label (N.k.a.x.n.i) of the twisted embedded newform | string label (cross-reference) |
| `target_level` | `integer` | level of the target newform | integer |
| `twist_class_label` | `text` | embedded newform label N.k.a.x.n.i of the designated twist class representative (of minimal level and character) | string label (cross-reference) |
| `twist_class_level` | `integer` | level of the minimal twist equivalent embedded newform | integer |
| `twisting_char_label` | `text` | Conrey label M.n of the twisting character psi (psi is always primitive) | string label (cross-reference) |
| `twisting_conrey_index` | `integer` | Conrey index of twisting character psi (numeric value of n in twisting_char_label) | integer |
| `weight` | `smallint` | weight k of source and target newforms (and all newforms in the twist equivalence class) | positive integer (weight) |

---

## mf_twists_nf

**Rows:** 1,622,040

**API:** https://www.lmfdb.org/api/mf_twists_nf/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `conductor` | `integer` | conductor of psi (equal to the modulus M in its label since psi is primitive) | positive integer |
| `degree` | `integer` | degree of psi = [Q(psi):Q] = phi(order) = cardinality of character orbit [psi] | positive integer |
| `multiplicity` | `smallint` | # of twists by distinct psi in [psi] for each embedded newform | count of distinct twists by same character orbit |
| `order` | `integer` | order of psi | integer |
| `parity` | `smallint` | parity of psi | integer |
| `self_twist_disc` | `integer` | for self twists the discriminant of the Kronecker character (1 for trivial char), 0 otherwise | integer |
| `source_char_orbit` | `smallint` | character orbit index of source newform (numeric value of i in source_label) | integer |
| `source_dim` | `integer` | dimension of the source newform | integer |
| `source_hecke_orbit` | `integer` | Hecke orbit index of source newform (numeric value of x in source label) | integer |
| `source_is_minimal` | `boolean` | true if source newform is twist-minimal and has minimal character | boolean |
| `source_label` | `text` | label (N.k.a.x) of the newform being twisted | source newform label |
| `source_level` | `integer` | level of the source newform | integer |
| `target_char_orbit` | `smallint` | (description not yet updated on this server) | integer |
| `target_dim` | `integer` | dimension of the target newform | integer |
| `target_hecke_orbit` | `integer` | Hecke orbit index of target newform (numeric value of x in target label) | integer |
| `target_is_minimal` | `boolean` | true if target newform is twist-minimal and has minimal character | boolean |
| `target_label` | `text` | label (N.k.a.x) of the twisted newform | twisted newform label |
| `target_level` | `integer` | level of the target newform | integer |
| `twist_class_label` | `text` | newform label N.k.a.x of the designated twist class representative (of minimal level and character) | label of twist-minimal representative |
| `twist_class_level` | `integer` | level of the twist-minimal newforms in this twist class (N in twist_class_label) | integer |
| `twisting_char_label` | `text` | label M.a of the twisting character orbit [psi] (psi is always primitive) | character orbit label of the twisting character |
| `twisting_char_orbit` | `smallint` | character orbit index of target newform (numeric value of i in target_label) | integer |
| `weight` | `smallint` | weight k of source and target newforms (and all newforms in the twist equivalence class) | positive integer (weight) |

---
