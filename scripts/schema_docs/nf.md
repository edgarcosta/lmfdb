# nf — Database Schema

**3 tables, 62 columns total**

### Tables

- [nf_fields](#nf_fields) (22,174,050 rows)
- [nf_fields_extra](#nf_fields_extra) (22,174,050 rows)
- [nf_fields_reflex](#nf_fields_reflex) (2,865,131 rows)

---

## nf_fields

Number fields

**Rows:** 22,174,050

**API:** https://www.lmfdb.org/api/nf_fields/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `class_group` | `jsonb` | invariant factors for the class group, in descending order | invariant factors of class group as text, e.g. '[2,4]' or '[]' |
| `class_number` | `numeric` | class number | class number h(K) |
| `cm` | `boolean` | whether or not the field is a CM field | boolean, true if K is a CM field |
| `coeffs` | `numeric[]` | coefficients of our defining polynomial starting with the constant term. | polynomial coefficients of defining polredabs polynomial. Sage ordering: [a_n, a_{n-1}, ..., a_1, a_0] (leading coeff first) |
| `conductor` | `numeric` | if the field is abelian, its conductor | positive integer |
| `degree` | `smallint` | degree of the field over *Q* | degree [K:Q] |
| `disc_abs` | `numeric` | the absolute value of the discriminant | absolute value of discriminant |D_K| |
| `disc_rad` | `numeric` | the radical of the absolute value of the discriminant | arbitrary-precision integer |
| `disc_sign` | `smallint` | 1 or -1 depending on the sign of the discriminant | +1 or -1, sign of discriminant |
| `embeddings_gen_imag` | `double precision[]` | list of imaginary parts of embeddings of generator | list of floats |
| `embeddings_gen_real` | `double precision[]` | list of real parts of embeddings of generator | list of floats |
| `gal_is_abelian` | `boolean` | true if the Galois group is abelian | boolean |
| `gal_is_cyclic` | `boolean` | true if the Galois group is cyclic | boolean |
| `gal_is_solvable` | `boolean` | true if the Galois group is solvable | boolean |
| `galois_disc_exponents` | `numeric[]` | If there are n ramifying primes, a list of n integers which are the corresponding exponents in the discriminant of th... | list of integers (length 0 in sample) |
| `galois_label` | `text` | the label of the Galois group | transitive group label nTt, e.g. '5T3' |
| `galt` | `integer` | the T-number of the Galois group | integer |
| `grd` | `double precision` | Root discriminant of the Galois closure | Galois root discriminant |D_K|^(1/|Gal|) |
| `index` | `integer` | Index of the number field | integer |
| `inessentialp` | `integer[]` | List of inessential primes | list of integers |
| `is_galois` | `boolean` | true if the field is Galois over Q | boolean, true if K/Q is Galois |
| `is_minimal_sibling` | `boolean` | is this its own minimal sibling | boolean |
| `iso_number` | `smallint` | the last number in the label, which is just a counter | integer |
| `label` | `text` | LMFDB label, formed by joining the degree, number of real places, absolute discriminant, and index with '.'. The inde... | label d.r.D.i: degree.r2.abs_disc.index, e.g. '2.2.5.1' |
| `local_algs` | `text[]` | Local algebras for ramified primes.  If a factor is in the local field database, we give its label.  If not, it is gi... | list of strings |
| `maximal_cm_subfield` | `numeric[]` | coefficients of the maximal CM subfield.  If this does not exist, then None | list of arbitrary-precision integers |
| `minimal_sibling` | `numeric[]` | Coefficients for the minimal sibling of this field if it is a different field | list of arbitrary-precision integers |
| `monogenic` | `smallint` | Is the field monogenic: 1 for yes, -1 for no, 0 for not computed | boolean or null: true if O_K = Z[alpha] for some alpha |
| `narrow_class_group` | `bigint[]` | Invariant factors of the narrow class of the field in ascending order | list of integers |
| `narrow_class_number` | `bigint` | Narrow class number of the field | narrow class number h+(K) |
| `num_ram` | `smallint` | the number of ramified primes | count of ramified primes |
| `r2` | `smallint` | number of pairs of complex places | number of pairs of complex embeddings: r2 = (deg - r1)/2 |
| `ramps` | `numeric[]` | the ramified primes in a list. Stored as strings because they may be too big | primes dividing discriminant (ramified primes), sorted |
| `rd` | `double precision` | root discriminant | root discriminant |D|^(1/d) |
| `regulator` | `numeric` | regulator of the field | regulator R(K), floating-point |
| `relative_class_number` | `numeric` | The relative class number if the field is CM | arbitrary-precision integer |
| `subfield_mults` | `integer[]` | Parallel to the list of subfields, the number of subfields isomorphic to one defined by the polynomial in the subfiel... | list of integers |
| `subfields` | `text[]` | List of coefficients of defining polynomials, which are polredabs'ed for subfields | list of strings |
| `torsion_order` | `smallint` | the order of the torsion subgroup of the unit group | integer |
| `used_grh` | `boolean` | True if class group/unit computation assumed GRH. If missing, assume false | boolean, true if computations assume GRH |

---

## nf_fields_extra

Additional data for displaying number field pages (not searchable)

**Rows:** 22,174,050

**API:** https://www.lmfdb.org/api/nf_fields_extra/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `dirichlet_group` | `bigint[]` | For an abelian field, the list of Dirichlet characters corresponding to this field given in Conrey numbering with mod... | list of integers |
| `frobs` | `jsonb` | List of Frobenius cycle types for the first few primes.  For ramified primes, we just give [0]. | List of Frobenius cycle types for the first few primes.  For ramified primes, we (JSON array) |
| `label` | `text` | LMFDB label, formed by joining the degree, number of real places, absolute discriminant, and index with '.'. The inde... | string label |
| `res` | `jsonb` | Resolvent information. Currently, only certain types of siblings are represented. Each key is a type and the value is... | Resolvent information. Currently, only certain types of siblings are represented (JSON object) |
| `source` | `text` | Knowl, possibly with parameters, which describe the source of the field | text |
| `subfield_inclusions` | `smallint[]` | inclusions for subfields; values are the order they appear in subfields;inclusions to Q and top field not give | list of small integers |
| `torsion_gen` | `text` | A generator of the torsion subgroup of the unit group as a latex string | text |
| `torsion_gen_coeffs` | `numeric[]` | Generator of the torsion part of the unit group given as a vector of coefficients with respect to the integral basis | list of arbitrary-precision integers |
| `unit_signature_rank` | `smallint` | Unit signature rank of the field | integer |
| `units` | `jsonb` | list of generators of the units modulo torsion, stored as latex ready strings. If there is no class number, assume un... | list of generators of the units modulo torsion, stored as latex ready strings. I (JSON array) |
| `unitsGmodule` | `jsonb` | in some cases we have data on the units modulo torsion as an integral Galois module. In each pair, the first coordina... | in some cases we have data on the units modulo torsion as an integral Galois mod |
| `unitsType` | `text` | Type of unit group, modulo torsion, as a G-module where G is the Galois group | text |
| `units_coeffs` | `numeric[]` | List of fundamental units given as vectors of coefficients with respect to the integral basis | list of arbitrary-precision integers |
| `zk` | `jsonb` | an integral basis in terms of 'a', a root of the defining polynomial | an integral basis in terms of 'a', a root of the defining polynomial (JSON array) |

---

## nf_fields_reflex

Reflex fields of CM fields

**Rows:** 2,865,131

**API:** https://www.lmfdb.org/api/nf_fields_reflex/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `CM_types` | `text[]` | list of CM types | list of strings |
| `galois_orbits` | `smallint[]` | An identifier indicating in which Galois orbit a CM type is | list of small integers |
| `multiplicity` | `smallint` | The number of CM types that give rise to this reflex field | integer |
| `nf_label` | `text` | Label of the CM number field | string label (cross-reference) |
| `rf_coeffs` | `numeric[]` | Coefficients of the equation defining one of the reflex fields | list of arbitrary-precision integers |
| `rf_emb_imag` | `double precision[]` | list of imaginary parts of embedded reflex field generator | list of floats |
| `rf_emb_real` | `double precision[]` | list of real parts of embedded reflex field generator | list of floats |
| `rf_rf` | `text[]` | A list of reflex fields of the reflex fields, one for each Galois orbit | list of strings |

---
