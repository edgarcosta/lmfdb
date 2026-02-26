# lat — Database Schema

**3 tables, 83 columns total**

### Tables

- [lat_genera](#lat_genera) (2,746,865 rows)
- [lat_lattices](#lat_lattices) (39,293 rows)
- [lat_lattices_new](#lat_lattices_new) (3,891,054 rows)

---

## lat_genera

This table stores lattices (free Z-modules with a nondegenerate symmetric inner product) up to local equivalence (also refered to as the genus of the lattice).

**Rows:** 2,746,865

**API:** https://www.lmfdb.org/api/lat_genera/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `adjacency_matrix` | `jsonb` | A dictionary with primes as keys and flattened p-neighbor multi-edge adjaceny matrix as values | A dictionary with primes as keys and flattened p-neighbor multi-edge adjaceny ma (JSON object) |
| `adjacency_polynomials` | `jsonb` | A dictionary with primes as keys and factored characteristic polynomials of adjacency matrices as values (as a list o... | A dictionary with primes as keys and factored characteristic polynomials of adja (JSON object) |
| `class_number` | `smallint` | size of the genus | positive integer |
| `conway_symbol` | `text` | the Conway symbol for the genus | text |
| `det` | `bigint` | determinant of Gram matrix | integer |
| `disc` | `bigint` | the discriminant (close to the determinant, but off by a factor of 2 in some cases) | integer (discriminant) |
| `discriminant_form` | `integer[]` | Quadratic form on the discriminant group, as a symmetric matrix | list of integers |
| `discriminant_group_invs` | `integer[]` | Smith-style invariants for the discriminant group | list of integers |
| `dual_conway_symbol` | `text` | Conway Symbol of the dual genus | text |
| `is_even` | `boolean` | whether the lattice is even | boolean |
| `label` | `text` | the part of the label that is constant across a genus | string label |
| `level` | `bigint` | level of lattice | positive integer |
| `mass` | `numeric[]` | numerator and denominator of the mass (sum of 1/Aut(L) for L in the genus) | list of arbitrary-precision integers |
| `nplus` | `smallint` | (description not yet updated on this server) | integer |
| `rank` | `smallint` | the rank of the lattice | non-negative integer |
| `rep` | `integer[]` | representative for the genus | list of integers |

---

## lat_lattices

Integral lattices

**Rows:** 39,293

**API:** https://www.lmfdb.org/api/lat_lattices/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `aut` | `numeric` | size of automorphism group | order of automorphism group |Aut(L)| |
| `base_label` | `text` | part of the *label* which is completely deterministic | string label (cross-reference) |
| `class_number` | `smallint` | class number or genus of a lattice | positive integer |
| `comments` | `text` | comments and historical remarks | text |
| `density` | `numeric` | density of a lattice | arbitrary-precision integer |
| `det` | `bigint` | determinant of a lattice | determinant of the Gram matrix |
| `dim` | `smallint` | dimension of a lattice | dimension of the lattice |
| `genus_reps` | `jsonb` | list of genus representatives (matrices) | list of genus representatives (matrices) (JSON array) |
| `gram` | `jsonb` | Gram matrix of a lattice | Gram matrix as upper-triangular integer list (row-major upper triangle) |
| `hermite` | `numeric` | Hermite number of a lattice | arbitrary-precision integer |
| `index` | `smallint` | index of a lattice | integer |
| `kissing` | `bigint` | Kissing number of a lattice | integer |
| `label` | `text` | LMFDB label of a lattice | lattice label: dim.det.level.class.number |
| `level` | `bigint` | level of a lattice | level of the lattice (= det/gcd for certain normalizations) |
| `minimum` | `integer` | length of the shortest vector | minimal nonzero norm in the lattice |
| `name` | `jsonb` | list of known names of a given lattice | common name if known, e.g. 'E8', 'Leech' |
| `shortest` | `jsonb` | list of shortest vectors (for the Leech lattice it is a list of strings) | list of shortest vectors (for the Leech lattice it is a list of strings) (JSON array) |
| `theta_series` | `jsonb` | coefficients of the q-expansion of the theta series associated to a lattice (for the Leech lattice it is a list of st... | coefficients of theta function sum_{v in L} q^{v.v} |

---

## lat_lattices_new

This table stores lattices (free Z-modules with a nondegenerate symmetric inner product) up to isomorphism.

**Rows:** 3,891,054

**API:** https://www.lmfdb.org/api/lat_lattices_new/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `Zn_complement` | `text` | the orthogonal complement of the maximal sublattice whose Gram matrix is diagonal | text |
| `aut_group` | `text` | string describing the automorphism group using GroupToString | text |
| `aut_label` | `text` | label for the automorphism group as an abstract group | string label (cross-reference) |
| `aut_size` | `numeric` | size of automorphism group | arbitrary-precision integer |
| `class_number` | `smallint` | size of the genus | positive integer |
| `conway_symbol` | `text` | the Conway symbol for the genus | text |
| `density` | `numeric` | center density of the lattice centered sphere packing (only for definite lattices) | arbitrary-precision integer |
| `det_abs` | `bigint` | absolute value of determinant of Gram matrix | integer |
| `det_radical` | `bigint` | radical of determinant of Gram matrix | integer |
| `det_sign` | `smallint` | sign of determinant of Gram matrix | integer |
| `disc` | `bigint` | the discriminant (close to the determinant, but off by a factor of 2 in some cases) | integer (discriminant) |
| `discriminant_group_invs` | `integer[]` | Smith-style invariants for the discriminant group | list of integers |
| `dual_density` | `numeric` | the center density of the dual lattice (only for definite lattices) | arbitrary-precision integer |
| `dual_det` | `numeric` | the determinant of the dual lattice | arbitrary-precision integer |
| `dual_hermite` | `numeric` | the Hermite number of the dual lattice (only for definite lattices) | arbitrary-precision integer |
| `dual_kissing` | `bigint` | the kissing number of the dual lattice (only for definite lattices) | integer |
| `dual_label` | `text` | the label for the minimal integral scaling of the dual lattice (may be null if the discriminant is too large) | string label (cross-reference) |
| `dual_theta_series` | `numeric[]` | the theta series of the dual lattice | list of arbitrary-precision integers |
| `even_complement` | `text` | the label for the orthogonal complement of the even sublattice | text |
| `even_sublattice` | `text` | the label for the sublattice generated by vectors of even norm | text |
| `festi_veniani_index` | `numeric` | the index of the lattice automorphism group within the automorphism group of the discriminant group | arbitrary-precision integer |
| `genus_label` | `text` | The part of the label that is constant across a genus | string label (cross-reference) |
| `gram` | `integer[]` | A list of human-preferred gram matrices; often there will only be one, but for E8 for example we want to include mult... | list of integers |
| `gram_is_canonical` | `boolean` | whether the gram matrix is in canonical form | boolean |
| `gram_others` | `integer[]` | A list of human-preferred gram matrices; often there will only be one, but for E8 for example we want to include mult... | list of integers |
| `hermite` | `numeric` | Hermite number (only for definite lattices) | arbitrary-precision integer |
| `is_additively_indecomposable` | `boolean` | whether the lattice is additively indecomposable | boolean |
| `is_even` | `boolean` | whether the lattice is even | boolean |
| `is_indecomposable` | `boolean` | whether the lattice is (orthogonally) indecomposable | boolean |
| `is_tensor_product` | `boolean` | whether this lattice has a nontrivial decomposition as a tensor product | boolean |
| `kissing` | `bigint` | kissing number (only for definite lattices) | integer |
| `label` | `text` |  `dimension.signature.determinant.genus_spec.tiebreaker` where  - `genus_spec` is    - ommitted if determinant is 1 a... | string label |
| `level` | `bigint` | level of lattice | positive integer |
| `minimum` | `integer` | length of shortest vector (only for definite lattices) | integer |
| `name` | `text` | an identifier string like 'E8', often null | text |
| `norm1_complement` | `text` | the label for the complement of the norm 1 sublattice | text |
| `norm1_sublattice` | `text` | the label for the sublattice generated by vectors of norm 1 | text |
| `nplus` | `smallint` | (description not yet updated on this server) | integer |
| `orthogonal_factors` | `text[]` | the orthogonal decomposition of the lattice (given as a duplicate-free list of lattice labels, sorted in reverse by m... | list of strings |
| `orthogonal_multiplicities` | `smallint[]` | multiplicities of the lattices in the orthogonal decomposition (a list of integers of the same length as orthogonal_f... | list of small integers |
| `pneighbors` | `jsonb` | a dictionary with primes as keys and a list of labels as values (the p-neighbors) | a dictionary with primes as keys and a list of labels as values (the p-neighbors |
| `rank` | `smallint` | the rank of the lattice | non-negative integer |
| `root_complement` | `text` | the label for the orthogonal complement of the root sublattice | text |
| `root_sublattice` | `text` | the label for the root sublattice | text |
| `shortest` | `integer[]` | A list of orbit representatives (under the action of the automorphism group) for the shortest vectors | list of integers |
| `successive_minima` | `integer[]` | the sequence of successive minima, of length equal to the rank | list of integers |
| `tensor_decompositions` | `jsonb` | A list of lists of pairs. The overall list contains different decompositions as a tensor product; the first entry of ... | A list of lists of pairs. The overall list contains different decompositions as  |
| `theta_prec` | `smallint` | Absolute precision of the theta series and dual theta series | integer |
| `theta_series` | `numeric[]` | a vector, counting the number of representations of n (odd) or 2n (even) | list of arbitrary-precision integers |

---
