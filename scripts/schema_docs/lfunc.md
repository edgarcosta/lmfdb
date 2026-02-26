# lfunc — Database Schema

**5 tables, 191 columns total**

### Tables

- [lfunc_data](#lfunc_data) (0 rows)
- [lfunc_instances](#lfunc_instances) (24,594,342 rows)
- [lfunc_lfunctions](#lfunc_lfunctions) (24,201,376 rows)
- [lfunc_rs_knowls](#lfunc_rs_knowls) (6 rows)
- [lfunc_search](#lfunc_search) (24,123,388 rows)

---

## lfunc_data

**Rows:** 0

**API:** https://www.lmfdb.org/api/lfunc_data/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `algebraic` | `boolean` | (description not yet updated on this server) | boolean |
| `analytic_conductor` | `double precision` | (description not yet updated on this server) | floating-point approximation |
| `bad_lfactors` | `jsonb` | (description not yet updated on this server) | JSON [[p,[c0,...]],...]: local L-factor at each bad prime (same as lfunc_lfunctions) |
| `bad_primes` | `bigint[]` | (description not yet updated on this server) | list of integers |
| `central_character` | `text` | (description not yet updated on this server) | text |
| `conductor` | `numeric` | (description not yet updated on this server) | positive integer |
| `conductor_radical` | `bigint` | (description not yet updated on this server) | integer |
| `conjugate` | `text` | (description not yet updated on this server) | text |
| `degree` | `smallint` | (description not yet updated on this server) | positive integer |
| `euler_factors` | `jsonb` | (description not yet updated on this server) | JSON list of Euler factor polynomial coefficients at primes (same as lfunc_lfunctions) |
| `euler_factors_factorization` | `jsonb` | (description not yet updated on this server) | JSON list of Euler factor factorizations (same as lfunc_lfunctions) |
| `factors` | `text[]` | (description not yet updated on this server) | list of strings |
| `index` | `smallint` | (description not yet updated on this server) | integer |
| `instance_types` | `text[]` | (description not yet updated on this server) | list of strings |
| `instance_urls` | `text[]` | (description not yet updated on this server) | list of strings |
| `label` | `text` | (description not yet updated on this server) | string label |
| `leading_term_mid` | `numeric` | (description not yet updated on this server) | arbitrary-precision integer |
| `leading_term_rad` | `double precision` | (description not yet updated on this server) | floating-point approximation |
| `load_key` | `text` | (description not yet updated on this server) | text |
| `motivic_weight` | `smallint` | (description not yet updated on this server) | integer |
| `mu_imag` | `numeric[]` | (description not yet updated on this server) | list of arbitrary-precision integers |
| `mu_real` | `smallint[]` | (description not yet updated on this server) | list of small integers |
| `nu_imag` | `numeric[]` | (description not yet updated on this server) | list of arbitrary-precision integers |
| `nu_real_doubled` | `smallint[]` | (description not yet updated on this server) | list of small integers |
| `order_of_vanishing` | `smallint` | (description not yet updated on this server) | integer |
| `origin` | `text` | (description not yet updated on this server) | text |
| `plot_delta` | `real` | (description not yet updated on this server) | floating-point approximation |
| `plot_values` | `real[]` | (description not yet updated on this server) | list of floats: values of Hardy Z-function Z(k*plot_delta) (same as lfunc_lfunctions) |
| `poles` | `double precision[]` | (description not yet updated on this server) | list of floats |
| `positive_zeros_extra` | `double precision[]` | (description not yet updated on this server) | list of floats |
| `positive_zeros_mid` | `numeric[]` | (description not yet updated on this server) | list of arbitrary-precision integers |
| `positive_zeros_rad` | `double precision[]` | (description not yet updated on this server) | list of floats |
| `prelabel` | `text` | (description not yet updated on this server) | text |
| `primitive` | `boolean` | (description not yet updated on this server) | boolean |
| `rational` | `boolean` | (description not yet updated on this server) | boolean |
| `root_analytic_conductor` | `double precision` | (description not yet updated on this server) | floating-point approximation |
| `root_angle_mid` | `numeric` | (description not yet updated on this server) | arbitrary-precision integer |
| `root_angle_rad` | `double precision` | (description not yet updated on this server) | floating-point approximation |
| `self_dual` | `boolean` | (description not yet updated on this server) | boolean |
| `special_values_at` | `double precision[]` | (description not yet updated on this server) | list of floats |
| `special_values_mid` | `numeric[]` | (description not yet updated on this server) | list of arbitrary-precision integers |
| `special_values_rad` | `double precision[]` | (description not yet updated on this server) | list of floats |
| `spectral_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `trace_hash` | `bigint` | (description not yet updated on this server) | integer |
| `z1` | `numeric` | (description not yet updated on this server) | arbitrary-precision integer |

---

## lfunc_instances

table for associating abstract L-functions with objects from which they arise

**Rows:** 24,594,342

**API:** https://www.lmfdb.org/api/lfunc_instances/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `Lhash` | `text` | lookup by L-function hash (used to find all objects with the same L-function) | L-function hash for cross-reference |
| `Lhash_array` | `text[]` | the Lhash of the factors known | list of strings |
| `factors` | `text[]` | the labels of the factors if known | list of strings |
| `label` | `text` | {{ KNOWL('lfunction.label', title='label')}} | string label |
| `type` | `text` | used to filter instances by type | type of source object |
| `url` | `text` | lookup by object homepage URL | URL of source mathematical object |

---

## lfunc_lfunctions

L-functions

**Rows:** 24,201,376

**API:** https://www.lmfdb.org/api/lfunc_lfunctions/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `A10` | `numeric` | the 10th {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coefficient')}} in arithmetic normalization for rational L-... | arbitrary-precision integer |
| `A2` | `numeric` | the 2nd {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coefficient')}} in arithmetic normalization for rational L-f... | arbitrary-precision integer |
| `A3` | `numeric` | the 3rd {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coefficient')}} in arithmetic normalization for rational L-f... | arbitrary-precision integer |
| `A4` | `numeric` | the 4th {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coefficient')}} in arithmetic normalization for rational L-f... | arbitrary-precision integer |
| `A5` | `numeric` | the 5th {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coefficient')}} in arithmetic normalization for rational L-f... | arbitrary-precision integer |
| `A6` | `numeric` | the 6th {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coefficient')}} in arithmetic normalization for rational L-f... | arbitrary-precision integer |
| `A7` | `numeric` | the 7th {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coefficient')}} in arithmetic normalization for rational L-f... | arbitrary-precision integer |
| `A8` | `numeric` | the 8th {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coefficient')}} in arithmetic normalization for rational L-f... | arbitrary-precision integer |
| `A9` | `numeric` | the 9th {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coefficient')}} in arithmetic normalization for rational L-f... | arbitrary-precision integer |
| `Lhash` | `text` | lookup by L-function hash (used to find all objects with the same L-function) | text |
| `a10` | `jsonb` | pair of floats (a complex number), the embedding of the 10th {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coeffic... | pair of floats (a complex number), the embedding of the 10th {{KNOWL('lfunction. (JSON array) |
| `a2` | `jsonb` | pair of floats (a complex number), the embedding of the 2nd {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coeffici... | pair of floats (a complex number), the embedding of the 2nd {{KNOWL('lfunction.d (JSON array) |
| `a3` | `jsonb` | pair of floats (a complex number), the embedding of the 3rd {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coeffici... | pair of floats (a complex number), the embedding of the 3rd {{KNOWL('lfunction.d (JSON array) |
| `a4` | `jsonb` | pair of floats (a complex number), the embedding of the 4th {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coeffici... | pair of floats (a complex number), the embedding of the 4th {{KNOWL('lfunction.d (JSON array) |
| `a5` | `jsonb` | pair of floats (a complex number), the embedding of the 5th {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coeffici... | pair of floats (a complex number), the embedding of the 5th {{KNOWL('lfunction.d (JSON array) |
| `a6` | `jsonb` | pair of floats (a complex number), the embedding of the 6th {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coeffici... | pair of floats (a complex number), the embedding of the 6th {{KNOWL('lfunction.d (JSON array) |
| `a7` | `jsonb` | pair of floats (a complex number), the embedding of the 7th {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coeffici... | pair of floats (a complex number), the embedding of the 7th {{KNOWL('lfunction.d (JSON array) |
| `a8` | `jsonb` | pair of floats (a complex number), the embedding of the 8th {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coeffici... | pair of floats (a complex number), the embedding of the 8th {{KNOWL('lfunction.d (JSON array) |
| `a9` | `jsonb` | pair of floats (a complex number), the embedding of the 5th {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coeffici... | pair of floats (a complex number), the embedding of the 5th {{KNOWL('lfunction.d (JSON array) |
| `accuracy` | `smallint` | bit accuracy (after the decimal point) of the nontrivial zeros | integer |
| `algebraic` | `boolean` | if the L-func is {{ KNOWL('lfunc.arithmetic', 'arithemetic') }}, i.e. normalized {{KNOWL('lfunction.dirichlet_series'... | boolean, true if Dirichlet coefficients are algebraic integers |
| `analytic_conductor` | `double precision` | the {{ KNOWL('lfunction.analytic_conductor', title='conductor') }} of the L-func | floating-point |
| `analytic_normalization` | `numeric` | a floating point number representing how to from the algebraic normalization to analytic {{KNOWL('lfunction.normaliza... | arbitrary-precision integer |
| `bad_lfactors` | `jsonb` | the euler factors for the bad primes as list of pairs (prime, list(polynomial)) | JSON list of [prime, [c0,...,cd]] pairs: local L-factor polynomial at each bad prime. E.g. [[3011,[1]]] means F_3011(T)=1 (fully ramified). Same coefficient conventions as euler_factors |
| `bad_primes` | `bigint[]` | the primes dividing the {{ KNOWL('lfunction.analytic_conductor', title='conductor') }} | list of ramified primes |
| `central_character` | `text` | the conrey label of a character that induces the {{ KNOWL('lfunction.central_character', title='central character')}}... | Dirichlet character label |
| `coeff_info` | `jsonb` | a triple of strings to help with | a triple of strings to help with (JSON array) |
| `coefficient_field` | `text` |  string identifying how | text |
| `conductor` | `numeric` | the {{ KNOWL('lfunction.conductor', title='conductor') }} of the L-func | conductor N, arbitrary-precision |
| `conductor_radical` | `integer` | the radical of the {{ KNOWL('lfunction.conductor', title='conductor') }} of the L-func | radical of conductor (product of distinct prime factors) |
| `conjugate` | `text` | the Lhash of the dual L-function, NULL if self-dual | text |
| `credit` | `text` | a string identifying who computed the entry, so far the options are NULL or 'Stefan Lemurell' | text |
| `degree` | `smallint` | {{ KNOWL('lfunction.degree', title='degree') }} | degree d of the L-function |
| `dirichlet_coefficients` | `jsonb` | list of {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coefficient')}} in arithmetic normalization, represented eit... | list of {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coefficient')}} in arit (JSON array) |
| `euler_factors` | `jsonb` | all the euler factors up to some bound, at least 100, represented as list of lists | JSON list of Euler factor polynomial coefficients at successive primes (2,3,5,7,...). Each entry = [c0,c1,...,cd] for F_p(T) = c0 + c1*T + ... + cd*T^d. c0=1 always. Coefficients are ints, or strings like 'a^k' for algebraic L-functions, or [Re,Im] pairs for CDF |
| `euler_factors_factorization` | `jsonb` | factorization of the euler factors, represented as lists of lists of pairs, where the first entry is a list represent... | JSON list (indexed by prime) of factorizations. Each = list of [factor_coeffs, exponent] pairs. factor_coeffs = [c0,...] for an irreducible factor, exponent = multiplicity |
| `gamma_factors` | `jsonb` | a pair of lists of numbers the first list being the gamma_R shifts, and the second list being the gamma_C shifts. sto... | a pair of lists of numbers the first list being the gamma_R shifts, and the seco (JSON array) |
| `group` | `text` | the codomain group of the galois representation | text |
| `index` | `smallint` | last component of  {{ KNOWL('lfunction.label', title='label')}} | integer |
| `label` | `text` | {{ KNOWL('lfunction.label', title='label')}} | L-function label |
| `leading_term` | `text` | leading term of the Taylor expansion of the L-function centered at t = 0 on the critical line | text |
| `load_key` | `text` | a string identifying a batch of lfuncions, it can be who uploaded it or in what workshop were these generated | text |
| `motivic_weight` | `smallint` | {{ KNOWL('lfunction.motivic_weight', 'motivic weight') }} | motivic weight w |
| `mu_imag` | `numeric[]` | the imaginary part of mus in the analytic normalization the [functional equation], where if possible Gamma_R factors ... | mu parameters (imaginary parts): numeric array |
| `mu_real` | `smallint[]` | the real part (in [0, 1]) of mus in the analytic normalization the [functional equation], where if possible Gamma_R f... | mu parameters (real parts): smallint array of floor(2*mu_j) values |
| `nu_imag` | `numeric[]` | the imaginary part of nus in the analytic normalization the [functional equation], where if possible Gamma_R factors ... | nu parameters (imaginary parts): numeric array |
| `nu_real_doubled` | `smallint[]` | the real part of nus doubled, so they are integers, in the analytic normalization the [functional equation], where if... | 2*nu parameters (real parts): smallint array |
| `order_of_vanishing` | `smallint` | the {{KNOWL('function.analytic_rank', 'analytic rank')}}, the order of vanishing at its central point | analytic rank (order of vanishing at center) |
| `origin` | `text` | url for the object that was use to generated this data | URL of source mathematical object |
| `plot_delta` | `numeric` | the spacing of the plot_values | arbitrary-precision integer |
| `plot_values` | `jsonb` | the values of the Z function spaced by plot_delta, i.e., plot_values = [Z(k*plot_delta) for k in range(len(plot_delta))] | JSON list of floats: values of the Hardy Z-function Z(k*plot_delta) for k=0,1,2,... Used to draw the L-function plot on the critical line |
| `positive_zeros` | `jsonb` | list of strictly positive zeros stored as strings, not all digits need to be correct, see accuracy | list of strictly positive zeros stored as strings, not all digits need to be cor (JSON array) |
| `precision` | `smallint` | to be deleted | integer |
| `prelabel` | `text` | the label {{ KNOWL('lfunction.label', title='label')}} without the last component | text |
| `primitive` | `boolean` | true if L-func is  {{ KNOWL('lfunction.primitive', title='primitive')}}, we use the second moment in many instances t... | boolean, true if L-function is primitive |
| `rational` | `boolean` | if the {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coefficients')}} in arithmetic normalisation are rational | boolean |
| `root_analytic_conductor` | `double precision` | the {{ KNOWL('lfunction.root_analytic_conductor', title='root analytic conductor')}} of the L-func | N^(1/d) * product of gamma factors |
| `root_angle` | `double precision` | the {{ KNOWL('lfunction.root_angle', title='root angle')}} of the L-func stored in the interval (-0.5, 0.5] | floating-point approximation |
| `root_number` | `text` | the {{ KNOWL('lfunction.sign', 'root number') }} as a string | text |
| `self_dual` | `boolean` | true if L-func is {{ KNOWL('lfunction.self-dual', title='self-dual')}} | boolean |
| `sign_arg` | `numeric` | the {{ KNOWL('lfunction.root_angle', title='root angle')}} of the L-func stored in the inerval (-0.5, 0.5] | arbitrary-precision integer |
| `spectral_label` | `text` | {{ KNOWL(' lfunction.spectral_label') }} | spectral parameter label |
| `st_group` | `text` | to be deleted | text |
| `symmetry_type` | `text` | to be deleted | text |
| `trace_hash` | `bigint` | linear combination of the a_p between 2^12 and 2^13 reduced mod 2^61-1 as defined in Section 4.3 of \cite{arXiv:1006.... | hash identifier for fast lookup |
| `types` | `jsonb` | to be deleted | to be deleted (JSON array) |
| `values` | `jsonb` | to be deleted | to be deleted (JSON array) |
| `z1` | `numeric` | imaginary part of the first zero where all the last digit may have an error of +-1, e.g., we could represent pi as 3.... | imaginary part of lowest nontrivial zero, floating-point |
| `z2` | `numeric` | imaginary part of the second zero where all the last digit may have an error of +-1, e.g., we could represent pi as 3... | arbitrary-precision integer |
| `z3` | `numeric` | imaginary part of the third zero where all the last digit may have an error of +-1, e.g., we could represent pi as 3.... | arbitrary-precision integer |

---

## lfunc_rs_knowls

**Rows:** 6

**API:** https://www.lmfdb.org/api/lfunc_rs_knowls/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `acknowledgments` | `text` | this table represents a map load_key -> knowls for compleness, reliability and source | text |
| `completeness` | `text` | this table represents a map load_key -> knowls for compleness, reliability and source | text |
| `load_key` | `text` | this table represents a map load_key -> knowls for compleness, reliability and source | text |
| `reliability` | `text` | this table represents a map load_key -> knowls for compleness, reliability and source | text |
| `source` | `text` | this table represents a map load_key -> knowls for compleness, reliability and source | text |

---

## lfunc_search

**Rows:** 24,123,388

**API:** https://www.lmfdb.org/api/lfunc_search/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `algebraic` | `boolean` | if the L-func is {{ KNOWL('lfunc.arithmetic', 'arithemetic') }}, i.e. normalized {{KNOWL('lfunction.dirichlet_series'... | boolean |
| `analytic_conductor` | `double precision` | the {{ KNOWL('lfunction.analytic_conductor', title='conductor') }} of the L-func | floating-point approximation |
| `bad_primes` | `bigint[]` | the primes dividing the {{ KNOWL('lfunction.analytic_conductor', title='conductor') }} | list of integers |
| `central_character` | `text` | the conrey label of the primitive character that induces the {{ KNOWL('lfunction.central_character', title='central c... | text |
| `conductor` | `numeric` | the {{ KNOWL('lfunction.conductor', title='conductor') }} of the L-func | positive integer |
| `conductor_radical` | `bigint` | the radical of the {{ KNOWL('lfunction.conductor', title='conductor') }} of the L-func | integer |
| `degree` | `smallint` | {{ KNOWL('lfunction.degree', title='degree') }} | positive integer |
| `dirichlet_coefficients` | `numeric[]` | list of {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coefficient')}} in arithmetic normalization, if rational | list of arbitrary-precision integers |
| `euler11` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler13` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler17` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler19` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler2` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler23` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler29` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler3` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler31` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler37` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler41` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler43` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler47` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler5` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler53` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler59` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler61` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler67` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler7` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler71` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler73` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler79` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler83` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler89` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler97` | `numeric[]` | arrays of length degree + 1 representing the euler factors at p, where p is the number at the end of the name column | list of arbitrary-precision integers |
| `euler_factors` | `numeric[]` | to be deleted | list of arbitrary-precision integers |
| `index` | `smallint` | the last component of {{ KNOWL('lfunction.label', title='label')}} | integer |
| `instance_types` | `text[]` | representing the keys of the multimap url(type) -> url(instance) | list of strings |
| `instance_urls` | `text[]` | representing the values of the multimap url(type) -> url(instance) | list of strings |
| `is_instance_Artin` | `boolean` | is_instance_X with X in {Artin,BMF,CMF,DIR,ECQ,ECQSymPower,ECNF,G2Q,HMF,MaassGL3,MaassGL4,MaassGSp4,NF}, represents i... | boolean |
| `is_instance_BMF` | `boolean` | is_instance_X with X in {Artin,BMF,CMF,DIR,ECQ,ECQSymPower,ECNF,G2Q,HMF,MaassGL3,MaassGL4,MaassGSp4,NF}, represents i... | boolean |
| `is_instance_CMF` | `boolean` | is_instance_X with X in {Artin,BMF,CMF,DIR,ECQ,ECQSymPower,ECNF,G2Q,HMF,MaassGL3,MaassGL4,MaassGSp4,NF}, represents i... | boolean |
| `is_instance_DIR` | `boolean` | is_instance_X with X in {Artin,BMF,CMF,DIR,ECQ,ECQSymPower,ECNF,G2Q,HMF,MaassGL3,MaassGL4,MaassGSp4,NF}, represents i... | boolean |
| `is_instance_ECNF` | `boolean` | is_instance_X with X in {Artin,BMF,CMF,DIR,ECQ,ECQSymPower,ECNF,G2Q,HMF,MaassGL3,MaassGL4,MaassGSp4,NF}, represents i... | boolean |
| `is_instance_ECQ` | `boolean` | is_instance_X with X in {Artin,BMF,CMF,DIR,ECQ,ECQSymPower,ECNF,G2Q,HMF,MaassGL3,MaassGL4,MaassGSp4,NF}, represents i... | boolean |
| `is_instance_G2Q` | `boolean` | is_instance_X with X in {Artin,BMF,CMF,DIR,ECQ,ECQSymPower,ECNF,G2Q,HMF,MaassGL3,MaassGL4,MaassGSp4,NF}, represents i... | boolean |
| `is_instance_HMF` | `boolean` | is_instance_X with X in {Artin,BMF,CMF,DIR,ECQ,ECQSymPower,ECNF,G2Q,HMF,MaassGL3,MaassGL4,MaassGSp4,NF}, represents i... | boolean |
| `is_instance_MaassGL3` | `boolean` | is_instance_X with X in {Artin,BMF,CMF,DIR,ECQ,ECQSymPower,ECNF,G2Q,HMF,MaassGL3,MaassGL4,MaassGSp4,NF}, represents i... | boolean |
| `is_instance_MaassGL4` | `boolean` | is_instance_X with X in {Artin,BMF,CMF,DIR,ECQ,ECQSymPower,ECNF,G2Q,HMF,MaassGL3,MaassGL4,MaassGSp4,NF}, represents i... | boolean |
| `is_instance_MaassGSp4` | `boolean` | is_instance_X with X in {Artin,BMF,CMF,DIR,ECQ,ECQSymPower,ECNF,G2Q,HMF,MaassGL3,MaassGL4,MaassGSp4,NF}, represents i... | boolean |
| `is_instance_NF` | `boolean` | is_instance_X with X in {Artin,BMF,CMF,DIR,ECQ,ECQSymPower,ECNF,G2Q,HMF,MaassGL3,MaassGL4,MaassGSp4,NF}, represents i... | boolean |
| `label` | `text` | {{ KNOWL('lfunction.label', title='label')}} | string label |
| `motivic_weight` | `smallint` | {{ KNOWL('lfunction.motivic_weight', 'motivic weight') }} | integer |
| `mu_imag` | `numeric[]` | the imaginary part of mus in the analytic normalization the [functional equation], where if possible Gamma_R factors ... | list of arbitrary-precision integers |
| `mu_real` | `smallint[]` | the real part (in [0, 1]) of mus in the analytic normalization the [functional equation], where if possible Gamma_R f... | list of small integers |
| `nu_imag` | `numeric[]` | the imaginary part of nus in the analytic normalization the [functional equation], where if possible Gamma_R factors ... | list of integers (length 0 in sample) |
| `nu_real_doubled` | `smallint[]` | the real part of nus doubled, so they are integers, in the analytic normalization the [functional equation], where if... | list of small integers |
| `order_of_vanishing` | `smallint` | the {{KNOWL('function.analytic_rank', 'analytic rank')}}, the order of vanishing at its central point | integer |
| `prelabel` | `text` | the label {{ KNOWL('lfunction.label', title='label')}} without the last component | text |
| `primitive` | `boolean` | true if L-func is {{ KNOWL('lfunction.primitive', title='primitive')}}, we use the second moment in many instances to... | boolean |
| `rational` | `boolean` | if the {{KNOWL('lfunction.dirichlet_series', 'Dirichlet coefficients')}} in arithmetic normalisation are rational | boolean |
| `root_analytic_conductor` | `double precision` | the {{ KNOWL('lfunction.root_analytic_conductor', title='root analytic conductor')}} of the L-func | floating-point approximation |
| `root_angle` | `double precision` | the {{ KNOWL('lfunction.root_angle', title='root angle')}} of the L-func stored in the inerval (-0.5, 0.5] | floating-point approximation |
| `self_dual` | `boolean` | true if L-func is {{ KNOWL('lfunction.self-dual', title='self-dual')}} | boolean |
| `spectral_label` | `text` | the {{ KNOWL('lfunction.spectral_label', title='spectral label') }} of the L-func | string label (cross-reference) |
| `trace_hash` | `bigint` | linear combination of the a_p between 2^12 and 2^13 reduced mod 2^61-1 as defined in Section 4.3 of \cite{arXiv:1006.... | integer |
| `z1` | `numeric` | the first zero where all the last digit may have an error of +-1, e.g., we could represent pi as 3.1416 | arbitrary-precision integer |

---
