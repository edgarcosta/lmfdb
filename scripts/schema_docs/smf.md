# smf — Database Schema

**13 tables, 227 columns total**

### Tables

- [smf_dims](#smf_dims) (72 rows)
- [smf_ev](#smf_ev) (3,094 rows)
- [smf_families](#smf_families) (14 rows)
- [smf_fc](#smf_fc) (26,212 rows)
- [smf_hecke_newspace_traces](#smf_hecke_newspace_traces) (84,483 rows)
- [smf_hecke_nf](#smf_hecke_nf) (8,173 rows)
- [smf_hecke_traces](#smf_hecke_traces) (0 rows)
- [smf_newforms](#smf_newforms) (11,632 rows)
- [smf_newspaces](#smf_newspaces) (28,497 rows)
- [smf_qexp_coeffs](#smf_qexp_coeffs) (10,114 rows)
- [smf_qexp_reduction](#smf_qexp_reduction) (2,556 rows)
- [smf_qexp_short](#smf_qexp_short) (0 rows)
- [smf_samples](#smf_samples) (129 rows)

---

## smf_dims

Siegel modular forms

**Rows:** 72

**API:** https://www.lmfdb.org/api/smf_dims/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `111111` | `text` | string encoding a rational function in Q(t) | text |
| `21111` | `text` | string encoding a rational function in Q(t) | text |
| `2211` | `text` | string encoding a rational function in Q(t) | text |
| `222` | `text` | string encoding a rational function in Q(t) | text |
| `3111` | `text` | string encoding a rational function in Q(t) | text |
| `321` | `text` | string encoding a rational function in Q(t) | text |
| `33` | `text` | string encoding a rational function in Q(t) | text |
| `411` | `text` | string encoding a rational function in Q(t) | text |
| `42` | `text` | string encoding a rational function in Q(t) | text |
| `51` | `text` | string encoding a rational function in Q(t) | text |
| `6` | `text` | string encoding a rational function in Q(t) | text |
| `author` | `text` | string naming the author(s) | text |
| `description` | `text` | string describing the space | text |
| `group` | `text` | name of the modular group, string (currently always 'Gamma(2)') | text |
| `note` | `jsonb` | string containing a latex note | string containing a latex note (JSON array) |
| `space` | `text` | string describing the type of the space (either "total" or "cusp") | text |
| `sym_power` | `numeric` | string encoding a nonnegative even integer (currently in [0,100]) | arbitrary-precision integer |
| `title` | `text` | string (currently always set to "Hilbert Poincare series") | text |

---

## smf_ev

Siegel modular forms

**Rows:** 3,094

**API:** https://www.lmfdb.org/api/smf_ev/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `data` | `jsonb` | string encoding the eigenvalue as an element of the number field Q(a) of the sample (as defined by field_poly) | string encoding the eigenvalue as an element of the number field Q(a) of the sam |
| `index` | `smallint` | string encoding the integer index of the eigenvalue (currently an integer in [2..100]). This uniquely identifies the ... | integer |
| `owner_id` | `integer` | Object(id) equal to the _id attribute of the sample to which this eigenvalue data belongs | integer |

---

## smf_families

Siegel modular forms

**Rows:** 14

**API:** https://www.lmfdb.org/api/smf_families/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `degree` | `smallint` | integer degree of the famly (currently 2, 3, or 4) | positive integer |
| `dim_args_default` | `jsonb` | for families with dimension formulas, a dictionary with default values for k and j | for families with dimension formulas, a dictionary with default values for k and (JSON object) |
| `latex_name` | `text` | latex string for displaying the name | text |
| `name` | `text` | string identifying the family (e.g. "Sp4Z") | text |
| `order` | `integer` | integer used to control the ordering of the families for display purposes | integer |
| `plain_name` | `text` | string describing family in plain text | text |

---

## smf_fc

Siegel modular forms

**Rows:** 26,212

**API:** https://www.lmfdb.org/api/smf_fc/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `data` | `jsonb` | dictionary whose keys are strings encoding integer vectors and whose values are strings encoding (possibly constant) ... | dictionary whose keys are strings encoding integer vectors and whose values are  (JSON object) |
| `det` | `smallint` | string encoding an integer that uniquely identifies this Fourier coefficient data record among others with the same o... | integer |
| `owner_id` | `integer` | Object(id) equal to the _id attribute of the sample to which this eigenvalue data belongs | integer |

---

## smf_hecke_newspace_traces

Traces of Hecke operators on spaces of Siegel modular forms over number fields

**Rows:** 84,483

**API:** https://www.lmfdb.org/api/smf_hecke_newspace_traces/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `hecke_orbit_code` | `bigint` | encoding of the tuple (g.C.N.w.i) into 64 bits, used in eigenvalue tables.  g + (ord(C)<<8) + (N<<12) + (k<<20) + (j<... | integer |
| `n` | `integer` | index n of a_n | integer |
| `trace_an` | `numeric` | integer containing the nth coefficient of the trace form for the entire newspace (sum of trace forms) | arbitrary-precision integer |

---

## smf_hecke_nf

Hecke eigenvalues of Siegel modular forms over number fields

**Rows:** 8,173

**API:** https://www.lmfdb.org/api/smf_hecke_nf/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `an` | `jsonb` | list of lists encoding the coefficients of the L-series a_1,a_2,...,a_100 either as a linear combination of the basis... | list of lists encoding the coefficients of the L-series a_1,a_2,...,a_100 either (JSON array) |
| `char_orbit_index` | `smallint` | ordinal i identifying the Galois orbit of the characterof this newform (base26 encoded in the newform label / charact... | integer |
| `degree` | `smallint` | Degree g (automorphic with repsect to Sp(2g, Q)) | positive integer |
| `family` | `text` | Family of arithmetic subgroups ('K' = paramodular, 'S' = Siegel, 'P' =  principal) | text |
| `field_poly` | `numeric[]` | list of integer coefficients of a defining polynomial for the Hecke field | list of arbitrary-precision integers |
| `hecke_orbit_code` | `bigint` | encoding of the tuple (g.C.N.w.i.x) into 64 bits, used in eigenvalue tables.  g + (ord(C)<<8) + (N<<12) + (k<<20) + (... | integer |
| `hecke_ring_character_values` | `jsonb` | list of pairs [[m1,[a11,...,a1n]],...[mr,[a1r,...,arn]]] where mi are generators of (Z/NZ)* and [ai1,...,ain] is the ... | list of pairs [[m1,[a11,...,a1n]],...[mr,[a1r,...,arn]]] where mi are generators |
| `hecke_ring_cyclotomic_generator` | `integer` | zero or an integer m suth that an and ap are encoded as sparse integer polynomials in zeta_m (typically zeta_m is a r... | integer |
| `hecke_ring_denominators` | `numeric[]` | List of integers giving denominators of the basis for the hecke ring in terms of the power basis (if hecke_ring_power... | list of arbitrary-precision integers |
| `hecke_ring_inverse_denominators` | `numeric[]` | List of integers giving denominators of the inverse basis that represents power basis in terms of the basis for the h... | list of arbitrary-precision integers |
| `hecke_ring_inverse_numerators` | `numeric[]` | List of lists of integers giving numerators of the inverse basis that represents power basis in terms of the basis fo... | list of arbitrary-precision integers |
| `hecke_ring_numerators` | `numeric[]` | List of lists of integers giving numerators of the basis for the hecke ring in terms of the power basis (if hecke_rin... | list of arbitrary-precision integers |
| `hecke_ring_power_basis` | `boolean` | True if we are using the power basis specified by field_poly as the basis for the hecke ring | boolean |
| `hecke_ring_rank` | `integer` | rank of Hecke ring as a free Z-module = dimension of newform = degree of field_lpoly | integer |
| `label` | `text` | Label g.C.N.w.a.x of this newform | string label |
| `lambda_p` | `jsonb` | list of lists encoding Hecke eigenvalues a_p (same format as a_n) for primes p up to maxp | list of lists encoding Hecke eigenvalues a_p (same format as a_n) for primes p u (JSON array) |
| `lambda_p_square` | `jsonb` | list of lists encoding Hecke eigenvalues of a_{p^2} (same format as a_n) for primes p up to maxp_square | list of lists encoding Hecke eigenvalues of a_{p^2} (same format as a_n) for pri (JSON array) |
| `lambda_p_square_0` | `jsonb` | list of lists encoding Hecke eigenvalues of a_{p^2,0} (same format as a_n) for primes p up to maxp_square | list of lists encoding Hecke eigenvalues of a_{p^2,0} (same format as a_n) for p (JSON array) |
| `lambda_p_square_1` | `jsonb` | list of lists encoding Hecke eigenvalues of a_{p^2,1} (same format as a_n) for primes p up to maxp_square | list of lists encoding Hecke eigenvalues of a_{p^2,1} (same format as a_n) for p (JSON array) |
| `lambda_p_square_2` | `jsonb` | list of lists encoding Hecke eigenvalues of a_{p^2,2} (same format as a_n) for primes p up to maxp_square | list of lists encoding Hecke eigenvalues of a_{p^2,2} (same format as a_n) for p (JSON array) |
| `level` | `integer` | Level N in the family | positive integer |
| `maxp` | `integer` | largest prime for which a_p appears in the list ap | integer |
| `maxp_square` | `integer` | largest prime p for which lambda_p_square appears in the list lambdap_square | integer |
| `qexp` | `jsonb` | a dictionary - keys are exponents, values are coefficients, for the q-expansion | a dictionary - keys are exponents, values are coefficients, for the q-expansion |
| `weight` | `smallint[]` | Weight (k,j) | positive integer (weight) |

---

## smf_hecke_traces

Traces of Hecke eigenvalues of Siegel modular forms over number fields

**Rows:** 0

**API:** https://www.lmfdb.org/api/smf_hecke_traces/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `hecke_orbit_code` | `bigint` | encoding of the tuple (g.C.N.w.i.x) into 64 bits, used in eigenvalue tables.  g + (ord(C)<<8) + (N<<12) + (k<<20) + (... | integer |
| `n` | `integer` | index n of a_n | integer |
| `trace_an` | `numeric` | integer containing the nth coefficient of the trace form for this newform | arbitrary-precision integer |

---

## smf_newforms

Siegel modular forms

**Rows:** 11,632

**API:** https://www.lmfdb.org/api/smf_newforms/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `analytic_rank` | `smallint` | the analytic rank of the L-function of the embedded newforms in this newform orbit | integer |
| `analytic_rank_proved` | `boolean` | true if the analytic rank has been proved | boolean |
| `atkin_lehner_eigenvals` | `integer[]` | a list of pairs [p, ev] where ev is 1 or -1, the Atkin-Lehner eigenvalue for each p dividing N (NULL overall if nontr... | list of integers |
| `atkin_lehner_string` | `text` | list of signs +/- of Atkin-Lehner eigenvalues ordered by p (facilitates lookups) | text |
| `aut_rep_type` | `text` | Type of the automorphic representation corresponding to this form - one of (F, B, P, Q, Y, G) according to the classi... | text |
| `char_conductor` | `integer` | Conductor of the Dirichlet character chi of this newform | integer |
| `char_degree` | `integer` | Degree of the (cyclotomic) character field | integer |
| `char_is_minimal` | `boolean` | true if the character chi is {{KNOWL('character.dirichlet.minimal','minimal')}} | boolean |
| `char_is_real` | `boolean` | true if the character takes only real values (trivial or quadratic) | boolean |
| `char_orbit_index` | `smallint` | ordinal i identifying the Galois orbit of the character of this newform (base26 encoded in the newform label / charac... | integer |
| `char_orbit_label` | `text` | base26-encoding of char_orbit_index-1 | string label (cross-reference) |
| `char_order` | `integer` | the order of the character chi | integer |
| `char_parity` | `smallint` | 1 for even, -1 for odd | integer |
| `char_values` | `jsonb` | quadruple <N,n,u,v> where N is the level, n is the order of the character, u is a list of generators for the unit gro... | quadruple <N,n,u,v> where N is the level, n is the order of the character, u is  |
| `conrey_indexes` | `integer[]` | Sorted list of Conrey indexes of characters in this Galois orbit | list of integers |
| `degree` | `smallint` | Degree g of this newform (automorphic with repsect to Sp(2g, Q)) | degree of the Siegel modular form (e.g. 2 for Sp(4)) |
| `dim` | `integer` | the dimension of this newform | dimension of eigenspace |
| `embedded_related_objects` | `text[]` | list of lists of text URLs of related objects (e.g. Artin reps), indexed by embedding_m (so first entry is a list of ... | list of strings |
| `family` | `text` | Family of arithmetic subgroups (paramodular, Siegel, principal) | text |
| `field_disc` | `numeric` | discriminant of the coefficient field, if known | arbitrary-precision integer |
| `field_disc_factorization` | `numeric[]` | factorization of field discriminant stored as ordered list of pairs [p,e] | list of integers (length 0 in sample) |
| `field_poly` | `numeric[]` | list of integers giving defining polynomial for the Hecke field (standard Sage order of coefficients) | list of arbitrary-precision integers |
| `field_poly_is_cyclotomic` | `boolean` | true if field_poly is a cylcotomic polynomial (the field might be Q(zeta_n) even when this flage is not set if we hav... | boolean |
| `field_poly_is_real_cyclotomic` | `boolean` | true if field_poly is the minimal polynomial of zeta_n + zeta_n^-1 for some n (the field might be Q(zeta_n)^+ even wh... | boolean |
| `field_poly_root_of_unity` | `integer` | the value of n if either field_poly_is_cylotomic of field_poly_is_real_cyclotomic is set | integer |
| `fricke_eigenval` | `smallint` | product of the Atkin-Lehner eigenvalues (NULL if nontrivial character) | integer |
| `hecke_orbit` | `integer` | (X) An integer that is encoded into x in the label via 1=a, 2=b, 26=z, 27=ba, 28=bb.  Note the shift: the letter is t... | integer |
| `hecke_orbit_code` | `bigint` | encoding of the tuple (g.C.N.w.i.x) into 64 bits, used in eigenvalue tables.  g + ((C-1)<<8) + (N<<12) + (w[0]<<20) +... | integer |
| `hecke_ring_generator_nbound` | `integer` | minimal integer m such that a_1,...,a_m generate the Hecke ring | integer |
| `hecke_ring_index_factorization` | `numeric[]` | Factorization of hecke_ring_index stored as ordered list of pairs [p,e]. | list of integers (length 0 in sample) |
| `hecke_ring_index_proved` | `boolean` | whether the index has been proved correct (computing the maximal order may not be possible) | boolean |
| `is_cuspidal` | `boolean` | true if this is a cusp form | boolean |
| `label` | `text` | Label g.C.N.w.a.x of this newform | Siegel modular form label |
| `level` | `integer` | Level N in the family | level N |
| `level_is_prime` | `boolean` | true if N is prime (1 is not prime) | boolean |
| `level_is_prime_power` | `boolean` | true if N is a prime power (1 is not a prime power) | boolean |
| `level_is_square` | `boolean` | true if N is square | boolean |
| `level_is_squarefree` | `boolean` | true if N is squarefree | boolean |
| `level_primes` | `integer[]` | sorted list of prime divisors of N | list of integers |
| `level_radical` | `integer` | product of prime divisors of N | integer |
| `nf_label` | `text` | LMFDB label for the corresponding number field (can be NULL) | string label (cross-reference) |
| `prim_orbit_index` | `smallint` | char_orbit for the primitive version of this character | integer |
| `qexp_display` | `text` | latexed string for display on search page results | text |
| `related_objects` | `text[]` | list of text URLs of related objects (e.g. elliptic curve isogeny class, Artin rep, ...), e.g. ["EllipticCurve/Q/11/a"] | list of strings |
| `relative_dim` | `integer` | the Q(chi)-dimension of this Hecke orbit (=dim/char_degree) | integer |
| `space_label` | `text` | label g.C.N.w.a of the newspace containing this newform | string label (cross-reference) |
| `trace_display` | `numeric[]` | list of the first four a_{p,1} traces for display on search page results | list of arbitrary-precision integers |
| `trace_hash` | `bigint` | appropriate linear combination of the a_{p,i} between 2^12 and 2^13 | integer |
| `trace_lambda_p` | `numeric[]` | List of traces of Hecke operators T_p on the Galois orbit corresponding to the values up to 200 | list of arbitrary-precision integers |
| `trace_lambda_p_square` | `numeric[]` | List of traces of Hecke operators T_p_square on the Galois orbit corresponding to the values up to 200 | list of arbitrary-precision integers |
| `trace_lambda_p_square_0` | `numeric[]` | List of traces of Hecke operators T_p_square_0 on the Galois orbit corresponding to the values up to 200 | list of arbitrary-precision integers |
| `trace_lambda_p_square_1` | `numeric[]` | List of traces of Hecke operators T_p_square_1 on the Galois orbit corresponding to the values up to 200 | list of arbitrary-precision integers |
| `trace_lambda_p_square_2` | `numeric[]` | List of traces of Hecke operators T_p_square_2 on the Galois orbit corresponding to the values up to 200 | list of arbitrary-precision integers |
| `traces` | `numeric[]` | full list of integer traces tr(a_{n,1}) for n from 1 to 1000 (or more) | list of arbitrary-precision integers |
| `weight` | `smallint[]` | Weight of this newform (highest weight of the corresponding irreducible representation of GL(g)) | weight k |
| `weight_parity` | `smallint` | (-1)^j | integer |

---

## smf_newspaces

Spaces of Siegel modular forms

**Rows:** 28,497

**API:** https://www.lmfdb.org/api/smf_newspaces/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `ALdims` | `integer[]` | Dimensions of Atkin-Lehner subspaces | list of integers |
| `ALdims_G` | `integer[]` | Dimensions of Atkin-Lehner subspaces of type (G) | list of integers |
| `ALdims_P` | `integer[]` | Dimensions of Atkin-Lehner subspaces of type (P) | list of integers |
| `char_conductor` | `integer` | Conductor of the Dirichlet character chi of this newform | integer |
| `char_degree` | `integer` | Degree of the (cyclotomic) character field | integer |
| `char_is_minimal` | `boolean` | true if the character chi is {{KNOWL('character.dirichlet.minimal','minimal')}} | boolean |
| `char_is_real` | `boolean` | true if the character takes only real values (trivial or quadratic) | boolean |
| `char_orbit_index` | `smallint` | ordinal i identifying the Galois orbit of the character of this newform (base26 encoded in the newform label / charac... | integer |
| `char_orbit_label` | `text` | base26-encoding of char_orbit_index-1 | string label (cross-reference) |
| `char_order` | `integer` | the order of the character chi | integer |
| `char_parity` | `smallint` | 1 for even, -1 for odd | integer |
| `char_values` | `jsonb` | quadruple <N,n,u,v> where N is the level, n is the order of the character, u is a list of generators for the unit gro... | quadruple <N,n,u,v> where N is the level, n is the order of the character, u is  |
| `conrey_indexes` | `integer[]` | Sorted list of Conrey indexes of characters in this Galois orbit | list of integers |
| `cusp_G_dim` | `integer` | Dimension of the space of  cuspforms of general type | integer |
| `cusp_G_lambda_p` | `numeric[]` | List of traces of Hecke operators T_p on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `cusp_G_lambda_p_square` | `numeric[]` | List of traces of Hecke operators T_p_square on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `cusp_G_lambda_p_square_0` | `numeric[]` | List of traces of Hecke operators T_p_square_0 on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `cusp_G_lambda_p_square_1` | `numeric[]` | List of traces of Hecke operators T_p_square_1 on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `cusp_G_lambda_p_square_2` | `numeric[]` | List of traces of Hecke operators T_p_square_2 on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `cusp_P_dim` | `integer` | Dimension of the space of  Saito-Kurokawa lifts | integer |
| `cusp_P_lambda_p` | `numeric[]` | List of traces of Hecke operators T_p on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `cusp_P_lambda_p_square` | `numeric[]` | List of traces of Hecke operators T_p_square on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `cusp_P_lambda_p_square_0` | `numeric[]` | List of traces of Hecke operators T_p_square_0 on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `cusp_P_lambda_p_square_1` | `numeric[]` | List of traces of Hecke operators T_p_square_1 on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `cusp_P_lambda_p_square_2` | `numeric[]` | List of traces of Hecke operators T_p_square_2 on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `cusp_Y_dim` | `integer` | Dimension of the space of  Yoshida lifts | integer |
| `cusp_Y_lambda_p` | `numeric[]` | List of traces of Hecke operators T_p on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `cusp_Y_lambda_p_square` | `numeric[]` | List of traces of Hecke operators T_p_square on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `cusp_Y_lambda_p_square_0` | `numeric[]` | List of traces of Hecke operators T_p_square_0 on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `cusp_Y_lambda_p_square_1` | `numeric[]` | List of traces of Hecke operators T_p_square_1 on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `cusp_Y_lambda_p_square_2` | `numeric[]` | List of traces of Hecke operators T_p_square_2 on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `cusp_dim` | `integer` | the Q-dimension of the space of cusp forms of this level, weight and character | integer |
| `degree` | `smallint` | Degree g of this newform (automorphic with repsect to Sp(2g, Q)) | positive integer |
| `eis_F_dim` | `integer` | Dimension of the space of  Siegel-Eisenstein series | integer |
| `eis_F_lambda_p` | `numeric[]` | List of traces of Hecke operators T_p on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `eis_F_lambda_p_square` | `numeric[]` | List of traces of Hecke operators T_p_square on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `eis_F_lambda_p_square_0` | `numeric[]` | List of traces of Hecke operators T_p_square_0 on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `eis_F_lambda_p_square_1` | `numeric[]` | List of traces of Hecke operators T_p_square_1 on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `eis_F_lambda_p_square_2` | `numeric[]` | List of traces of Hecke operators T_p_square_2 on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `eis_Q_dim` | `integer` | Dimension of the space of  Klingen-Eisenstein series | integer |
| `eis_Q_lambda_p` | `numeric[]` | List of traces of Hecke operators T_p on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `eis_Q_lambda_p_square` | `numeric[]` | List of traces of Hecke operators T_p_square on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `eis_Q_lambda_p_square_0` | `numeric[]` | List of traces of Hecke operators T_p_square_0 on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `eis_Q_lambda_p_square_1` | `numeric[]` | List of traces of Hecke operators T_p_square_1 on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `eis_Q_lambda_p_square_2` | `numeric[]` | List of traces of Hecke operators T_p_square_2 on the Siegel-Eisenstein (F) space corresponding to the values up to 200 | list of arbitrary-precision integers |
| `eis_dim` | `integer` | the Q-dimension of the space of Eisenstein forms of this level, weight and character | integer |
| `family` | `text` | Family of arithmetic subgroups ('F' = full, 'K' = paramodular, 'S' = Siegel, 'C' - principal) | text |
| `hecke_orbit_code` | `bigint` | encoding of the tuple (g.C.N.w.i) into 64 bits, used in eigenvalue tables.  g + (ord(C)<<8) + (N<<12) + (k<<20) + (j<... | integer |
| `label` | `text` | Label g.C.N.w.a of this newspace | string label |
| `level` | `integer` | Level N in the family | positive integer |
| `level_is_prime` | `boolean` | true if N is prime (1 is not prime) | boolean |
| `level_is_prime_power` | `boolean` | true if N is a prime power (1 is not a prime power) | boolean |
| `level_is_square` | `boolean` | true if N is square | boolean |
| `level_is_squarefree` | `boolean` | true if N is squarefree | boolean |
| `level_primes` | `integer[]` | sorted list of prime divisors of N | list of integers |
| `level_radical` | `integer` | product of prime divisors of N | integer |
| `new_cusp_G_dim` | `integer` | Dimension of the space of new cuspforms of general type | integer |
| `new_cusp_P_dim` | `integer` | Dimension of the space of new Saito-Kurokawa lifts | integer |
| `new_cusp_Y_dim` | `integer` | Dimension of the space of new Yoshida lifts | integer |
| `new_cusp_dim` | `integer` | Dimension of the space of new cusp forms | integer |
| `new_eis_F_dim` | `integer` | Dimension of the space of new Siegel-Eisenstein series | integer |
| `new_eis_Q_dim` | `integer` | Dimension of the space of new Klingen-Eisenstein series | integer |
| `new_eis_dim` | `integer` | Dimension of the space of new Eisenstein series | integer |
| `new_total_dim` | `integer` | Total dimension of the space of new modular forms | integer |
| `num_forms` | `integer` | number of Hecke orbits (each corresponds to a Galois conjugacy class of modular forms) | non-negative integer (count) |
| `old_cusp_G_dim` | `integer` | Dimension of the space of old cuspforms of general type | integer |
| `old_cusp_P_dim` | `integer` | Dimension of the space of old Saito-Kurokawa lifts | integer |
| `old_cusp_Y_dim` | `integer` | Dimension of the space of old Yoshida lifts | integer |
| `old_cusp_dim` | `integer` | Dimension of the space of old cusp forms | integer |
| `old_eis_F_dim` | `integer` | Dimension of the space of old Siegel-Eisenstein series | integer |
| `old_eis_Q_dim` | `integer` | Dimension of the space of old Klingen-Eisenstein series | integer |
| `old_eis_dim` | `integer` | Dimension of the space of old Eisenstein series | integer |
| `old_total_dim` | `integer` | Total dimension of the space of old modular forms | integer |
| `prim_orbit_index` | `smallint` | char_orbit for the primitive version of this character | integer |
| `total_dim` | `integer` | Total dimension of the space of  modular forms | integer |
| `traces` | `integer[]` | integer coefficients a_n of the trace form (sum of all newforms in the space) for n from 1 to 1000, only set when dim... | list of integers |
| `weight` | `smallint[]` | Weight of this newform (highest weight of the corresponding irreducible representation of GL(g)) | positive integer (weight) |
| `weight_parity` | `smallint` | (-1)^j | integer |

---

## smf_qexp_coeffs

Coefficients in q-expansions of Siegel modular forms indexed by orbits of quadratic forms

**Rows:** 10,114

**API:** https://www.lmfdb.org/api/smf_qexp_coeffs/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `coeff` | `integer[]` | Coordinates of the coefficient in integral basis of the Hecke ring | list of integers |
| `hecke_orbit_code` | `bigint` | Hecke orbit code identifying the newform | integer |
| `qf_legendre` | `integer[]` | Legendre-reduced quadratic form | list of integers |
| `qf_tag` | `integer[]` | Tag attached to Legendre-reduced quadratic form | list of integers |

---

## smf_qexp_reduction

Reduction of quadratic forms in q-expansions for Siegel modular forms

**Rows:** 2,556

**API:** https://www.lmfdb.org/api/smf_qexp_reduction/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `family` | `text` | Family of arithmetic subgroups ('F' = full, 'K' = paramodular, 'S' = Siegel, 'C' = principal) | text |
| `index` | `bigint` | Index of this quadratic form in the display ordering | integer |
| `is_minimal` | `boolean` | True iff the orbit representative is minimal | boolean |
| `level` | `integer` | Level of the newspace | positive integer |
| `qf_legendre` | `integer[]` | Legendre-reduced quadratic form | list of integers |
| `qf_orbit_rep` | `integer[]` | Orbit representative | list of integers |
| `qf_tag` | `integer[]` | Tag attached to Legendre-reduced quadratic form | list of integers |

---

## smf_qexp_short

Short, fully expanded q-expansions of Siegel modular forms

**Rows:** 0

**API:** https://www.lmfdb.org/api/smf_qexp_short/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `coeff` | `integer[]` | Coordinates of the coefficient in integral basis of the Hecke ring | list of integers |
| `hecke_orbit_code` | `bigint` | Hecke orbit code identifying the newform | integer |
| `index` | `smallint` | Index of coefficient in case of vector-valued forms | integer |
| `qf` | `integer[]` | Quadratic form encoded as a triple of integers | list of integers |
| `trace` | `smallint` | Trace of the 2*2 matrix representing the quadratic form | integer |

---

## smf_samples

Siegel modular forms

**Rows:** 129

**API:** https://www.lmfdb.org/api/smf_samples/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `Fourier_coefficients` | `jsonb` | dictionary whose keys are tuples encoding binary quadratic forms and whose values are strings encoding coefficients | dictionary whose keys are tuples encoding binary quadratic forms and whose value |
| `collection` | `jsonb` | array of strings identifying families of spaces of Siegel modular forms that contain this sample (the families curren... | array of strings identifying families of spaces of Siegel modular forms that con (JSON array) |
| `courtesy_of` | `text` | string identifying the source of the sample (e.g. authors and date) | text |
| `degree` | `smallint` | integer degree (same as in smf_families, 2, 3, or 4) | positive integer |
| `eigenvalues` | `jsonb` | delete | delete |
| `explicit_formula` | `text` | string encoding a polynomial in Q(a)[A,B,C,D] | text |
| `fdeg` | `smallint` | integer degree of field_poly (current an integer in [1..29]) | integer |
| `field` | `text` | string encoding sage command to load the number field containing the Fourier coefficients | text |
| `field_poly` | `text` | string encoding a monic polynomial f(x) in Z[x] defining a number field Q(a):=Q[x]/(f(x)) (x is used for Q) | text |
| `id_link` | `integer` | integer | integer |
| `is_eigenform` | `boolean` | boolean if an eigenform | boolean |
| `is_integral` | `boolean` | boolean if the coefficients are algebraic integers | boolean |
| `name` | `text` | name uniquely identifying the sample within any of the collections it belongs to | text |
| `representation` | `smallint` | string encoding an integer (currently an element of {0,2}) | integer |
| `type` | `text` | string describing the type of sample (e.g. 'Ikeda lift, cusp form') | text |
| `weight` | `smallint` | integer weight of the form | positive integer (weight) |

---
