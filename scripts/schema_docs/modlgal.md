# modlgal — Database Schema

**2 tables, 63 columns total**

### Tables

- [modlgal_reps](#modlgal_reps) (57,902 rows)
- [modlgal_reps_save](#modlgal_reps_save) (817 rows)

---

## modlgal_reps

mod-ell Galois reps

**Rows:** 57,902

**API:** https://www.lmfdb.org/api/modlgal_reps/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `algebraic_group` | `text` | The type of algebraic group of the codomain (e.g. "GL", "GSp") | text |
| `base_ring_characteristic` | `integer` | Characteristic of the base ring (the value of $\ell$). | prime ell |
| `base_ring_is_field` | `boolean` |  true iff base ring is a field | boolean |
| `base_ring_order` | `integer` | Order of the base ring. | integer |
| `conductor` | `bigint` | conductor of the Artin rep | Artin conductor |
| `conductor_is_squarefree` | `boolean` | True iff the conductor is squarefree. | boolean |
| `conductor_num_primes` | `integer` | Number of prime divisors of the conductor. | integer |
| `conductor_primes` | `integer[]` | Sorted list of primes dividing the conductor. | list of integers |
| `cyclotomic_exponent` | `integer` | Exponent of the cyclotomic character of the representation in the determinant of the representation, an integer betwe... | integer |
| `determinant_index` | `integer` | The index of the image of the determinant in $\GL_1$ | integer |
| `determinant_label` | `text` | Label of the 1-dimensional mod-$\ell$ Galois representation given by the determinant. | string label (cross-reference) |
| `dimension` | `integer` | Dimension of the representation. | dimension of the representation over F_ell |
| `dual_pair_of_algebras` | `jsonb` | List of [A,B,Phi] computed by the [dual_pairs](https://gitlab.com/pbruin/dual-pairs/) package, where A and B are list... | List of [A,B,Phi] computed by the [dual_pairs](https://gitlab.com/pbruin/dual-pa (JSON array) |
| `frobenius_matrices` | `integer[]` | list of Frobenius matrices for (at least) all good primes $p < 100$.  The nth entry corresponds to the nth prime $p$ ... | list of integers |
| `generating_primes` | `integer[]` | List of good primes whose Frobenius classes generate the image of the representation (equivalently, the Galois group ... | list of integers |
| `good_primes` | `integer[]` | List of unramified primes $p\nmid \ell$ less than 100, corresponding to the list of Frobenius matrices stored in {{KN... | list of integers |
| `image_abstract_group` | `text` | Label of the abstract group isomorphic to the image | text |
| `image_index` | `integer` | Index of the image in the codomain. | integer |
| `image_label` | `text` | Label of group. For character "Cn" where n is the order, for dimension 2 over prime field use Sutherland's label, "C1... | label of the image group |
| `image_order` | `integer` | Size of the image. | |im(rho)| |
| `image_type` | `text` | Human sensible descriptor of the image, e.g "big" = contains SL_n; "Borel", "cyclic" etc. | text |
| `is_absolutely_irreducible` | `boolean` | True iff the representation is absolutely irreducible. | boolean |
| `is_irreducible` | `boolean` | True iff the representation is irreducible (currently always True). | boolean |
| `is_solvable` | `boolean` | True iff the image is solvable. | boolean |
| `is_surjective` | `boolean` | True iff the representation is surjective (image=codomain). | boolean |
| `kernel_polynomial` | `numeric[]` | List of integer coefficients of defining polynomial for the canonical sibling field (the stem field that would be use... | polynomial defining the kernel (fixed) field |
| `label` | `text` | Label of the representation.  When the number field is Q (currently always true) this has the format dimension.base_r... | representation label: dim.ell.conductor.order[.twist] |
| `num` | `integer` | The positive integer that is the last part of the label, used to break ties. | integer |
| `original_polynomial` | `integer[]` | Normalized defining polynomial for Sp(4,2) representations | list of integers |
| `projective_image_abstract_group` | `text` | Label of the abstract group isomorphic to the projective image | text |
| `projective_is_surjective` | `boolean` | True iff the projective representation is surjective. | boolean |
| `projective_kernel_polynomial` | `numeric[]` | List of integer coefficients of the defining polynomial for the canonical sibling whose Galois closure is the fixed f... | list of arbitrary-precision integers |
| `projective_type` | `text` | Type of projective representation (for dim=2 this can be Dn, A4, S4, A5). | text |
| `related_objects` | `text[]` | List of pairs of strings [object_type, object_label] where object_type is one of Dirichlet, MF, ECQ, G2C, ... (as for... | list of strings |
| `top_slope_rational` | `text` | The {{KNOWL('lf.top_slope','top slope')}} of the $\Q_\ell$-algebra defined by the kernel polynomial, stored as a text... | text |
| `top_slope_real` | `real` | The {{KNOWL('lf.top_slope','top slope')}} of the $\Q_\ell$-algebra defined by the kernel polynomial, stored as floati... | floating-point approximation |
| `traces` | `integer[]` | List of traces of Frobenius.  Value -1 is used for ell and bad primes | list of integers |
| `weight` | `integer` | Weight of the representation (currenly for dimension 2 only) | positive integer (weight) |

---

## modlgal_reps_save

Mod-ell Galois representations

**Rows:** 817

**API:** https://www.lmfdb.org/api/modlgal_reps_save/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `abs_irr` | `smallint` | 1 if representation is absolutely irreducible, 0 if not, -1 if unknown | integer |
| `bad_prime_list` | `jsonb` | (description not yet updated on this server) | JSON list of [prime, field1, field2, field3, field4] tuples for bad primes (primes dividing ell*conductor), with Frobenius data |
| `base_field` | `text` | (description not yet updated on this server) | text |
| `base_label` | `text` | LMFDB label of the field whose absolute Galois group is being represented. | string label (cross-reference) |
| `conductor` | `integer` | conductor of the Artin rep | positive integer |
| `degree_proj_field` | `smallint` | The degree of the extension cut out by the projective image of this representation over the base field. | integer |
| `dim` | `smallint` | The dimension of the representation | non-negative integer |
| `field` | `jsonb` | Definining polynomial of the finite field that is the field of definition of the representation. This is the  Conway ... | Definining polynomial of the finite field that is the field of definition of the (JSON array) |
| `field_char` | `smallint` | Characteristic of the finite field that is the field of definition of the representation. | integer |
| `field_deg` | `smallint` | Degree of the finite field that is the field of definition of the representation. | integer |
| `field_order` | `smallint` | Order of the finite field that is the field of definition of the representation. | integer |
| `good_prime_list` | `jsonb` | (description not yet updated on this server) | JSON list of [prime, trace_vector, factored_charpoly_string, image_order, image_index] tuples for unramified primes p < 100 |
| `image_at` | `text` | (description not yet updated on this server) | text |
| `image_label` | `text` | Label of group. For character "Cn" where n is the order, for dimension 2 over prime field use Sutherland's label, "C1... | string label (cross-reference) |
| `image_order` | `integer` | Size of the image. | integer |
| `image_type` | `text` | Human sensible descriptor of the image, e.g "big" = contains SL_n; "Borel", "cyclic" etc. | text |
| `index` | `smallint` | The counter used as the final component of the representations label. | integer |
| `label` | `text` | (description not yet updated on this server) | string label |
| `poly_ker` | `text` | polynomial whose splitting field is the fixed field of the kernel of the representation | text |
| `poly_proj_ker` | `text` | polynomial whose splitting field is the fixed field of the kernel of the projective representation | text |
| `primes_conductor` | `jsonb` | List of primes dividing the conductor | List of primes dividing the conductor (JSON array) |
| `projective_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `projective_type` | `text` | (description not yet updated on this server) | text |
| `rep_type` | `text` | (description not yet updated on this server) | text |
| `weight` | `smallint` | (description not yet updated on this server) | positive integer (weight) |

---
