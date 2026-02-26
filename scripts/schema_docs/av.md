# av — Database Schema

**6 tables, 158 columns total**

### Tables

- [av_fq_endalg_data](#av_fq_endalg_data) (2,659,523 rows)
- [av_fq_endalg_factors](#av_fq_endalg_factors) (4,084,993 rows)
- [av_fq_isog](#av_fq_isog) (2,945,722 rows)
- [av_fq_pol](#av_fq_pol) (49,886,088 rows)
- [av_fq_teximages](#av_fq_teximages) (460,190 rows)
- [av_fq_weak_equivalences](#av_fq_weak_equivalences) (3,778,316 rows)

---

## av_fq_endalg_data

**Rows:** 2,659,523

**API:** https://www.lmfdb.org/api/av_fq_endalg_data/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `brauer_invariants` | `text[]` | A list of rational numbers stored as strings, giving the Brauer invariants for $\operatorname{End}^0_{q^r}(A)$ as a d... | list of strings |
| `center` | `text` | The number field label for the center of the endomorphism algebra $\operatorname{End}^0_{q^r}(A)$, where $A$ is a KNO... | text |
| `center_dim` | `smallint` | The degree of the {{KNOWL('columns.av_fq_endalg_data.center')}} over $\mathbb{Q}$ | integer |
| `divalg_dim` | `smallint` | The dimension of the endomorphism algebra $\operatorname{End}^0_{q^r}(A)$ over its {{KNOWL('columns.av_fq_endalg_data... | integer |
| `extension_label` | `text` | The label for the base changed {{KNOWL('columns.av_fq_endalg_factors.extension_label', 'simple isogeny class')}} (whi... | string label (cross-reference) |
| `galois_group` | `text` | The {{KNOWL('nf.galois_group.name', 'transitive label')}} for the Galois group of the {{KNOWL('columns.av_fq_endalg_d... | text |
| `places` | `text[]` | A list of lists of rational numbers stored as strings, giving the prime ideals above $p$.  The terms in the outer lis... | list of strings |

---

## av_fq_endalg_factors

**Rows:** 4,084,993

**API:** https://www.lmfdb.org/api/av_fq_endalg_factors/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `base_label` | `text` | The {{KNOWL('columns.av_fq_isog.label', 'label')}} of an isogeny class | string label (cross-reference) |
| `extension_degree` | `smallint` | A positive integer dividing the {{KNOWL('columns.av_fq_isog.geometric_extension_degree', 'geometric_extension_degree'... | integer |
| `extension_label` | `text` | The label of a simple factor of the base change of the {{KNOWL('columns.av_fq_endalg_factors.base_label', 'base varie... | string label (cross-reference) |
| `multiplicity` | `smallint` | The multiplicity of the {{KNOWL('columns.av_fq_endalg_factors.extension_label', 'simple factor')}} in the {{KNOWL('av... | integer |

---

## av_fq_isog

**Rows:** 2,945,722

**API:** https://www.lmfdb.org/api/av_fq_isog/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `abvar_count` | `numeric` | {{KNOWL('ag.fq.point_counts', 'Number of points')}} on this abelian variety over the base field | arbitrary-precision integer |
| `abvar_counts` | `numeric[]` | {{KNOWL('ag.fq.point_counts', 'Number of points')}} on this abelian variety over $\mathbb{F}_{q^k}$ for $1 \le k \le ... | list of arbitrary-precision integers |
| `abvar_counts_str` | `text` | Version of {{KNOWL('columns.av_fq_isog.abvar_counts', 'abvar_counts')}}, as a space separated string | text |
| `all_polarized_product` | `boolean` | Whether all polarized isomorphism classes can be expressed as a nontrivial product of abelian varietes of smaller dim... | boolean |
| `all_unpolarized_product` | `boolean` | Whether all unpolarized isomorphism classes can be expressed as a nontrivial product of abelian varietes of smaller d... | boolean |
| `angle_corank` | `smallint` | g - angle_rank | integer |
| `angle_rank` | `smallint` | {{KNOWL('av.fq.angle_rank', 'Angle rank')}} of the Weil polynomial: the dimension of the $\mathbb{Q}$-span of the {{K... | number of non-real roots of Weil polynomial divided by 2 |
| `angles` | `double precision[]` | {{KNOWL('av.fq.frobenius_angles', 'Angles')}} of the roofs of the Weil polynomial, as real numbers between 0 and 1 | list of floats |
| `center_dim` | `smallint` | Dimension over $\mathbb{Q}$ of the center of the {{KNOWL('ag.endomorphism_algebra', 'endomorphism algebra')}} | integer |
| `cohen_macaulay_max` | `smallint` | The maximum Cohen-Macaulay type among endomorphism rings of unpolarized abelian varieties in this isogeny class | integer |
| `curve_count` | `integer` | {{KNOWL('av.fq.curve_point_counts', 'Number of points')}} on a (virtual) curve whose Jacobian lies in this isogeny class | non-negative integer (count) |
| `curve_counts` | `numeric[]` | {{KNOWL('av.fq.curve_point_counts', 'Number of points')}} on a (virtual) curve whose Jacobian lies in this isogeny cl... | list of arbitrary-precision integers |
| `curve_counts_str` | `text` | Version of {{KNOWL('columns.av_fq_isog.curve_counts', 'curve_counts')}}, as a space separated string | text |
| `curves` | `text[]` | A list of curves in this isogeny class, given as strings providing an equation (with an implicit equality with zero a... | list of strings |
| `dim1_distinct` | `smallint` | Number of distinct dimension 1 factors in the {{KNOWL('av.decomposition', 'decomposition')}} into simple factors | integer |
| `dim1_factors` | `smallint` | Number of dimension 1 factors in the {{KNOWL('av.decomposition', 'decomposition')}} into simple factors, with multipl... | integer |
| `dim2_distinct` | `smallint` | Number of distinct dimension 2 factors in the {{KNOWL('av.decomposition', 'decomposition')}} into simple factors | integer |
| `dim2_factors` | `smallint` | Number of dimension 2 factors in the {{KNOWL('av.decomposition', 'decomposition')}} into simple factors, with multipl... | integer |
| `dim3_distinct` | `smallint` | Number of distinct dimension 3 factors in the {{KNOWL('av.decomposition', 'decomposition')}} into simple factors | integer |
| `dim3_factors` | `smallint` | Number of dimension 3 factors in the {{KNOWL('av.decomposition', 'decomposition')}} into simple factors, with multipl... | integer |
| `dim4_distinct` | `smallint` | Number of distinct dimension 4 factors in the {{KNOWL('av.decomposition', 'decomposition')}} into simple factors | integer |
| `dim4_factors` | `smallint` | Number of dimension 4 factors in the {{KNOWL('av.decomposition', 'decomposition')}} into simple factors | integer |
| `dim5_distinct` | `smallint` | Number of distinct dimension 5 factors in the {{KNOWL('av.decomposition', 'decomposition')}} into simple factors | integer |
| `dim5_factors` | `smallint` | Number of dimension 5 factors in the {{KNOWL('av.decomposition', 'decomposition')}} into simple factors | integer |
| `endomorphism_ring_count` | `smallint` | The number of distinct endomorphism rings among unpolarized isomorphism classes in this isogeny class; these are stor... | non-negative integer (count) |
| `g` | `smallint` | {{KNOWL('ag.dimension', 'dimension')}} of the abelian variety | dimension (genus) of the abelian variety |
| `galois_groups` | `text[]` | list of {{KNOWL('av.fq.galois_group', 'Galois groups')}} of the simple factors, each a string such as '8T44' | list of strings |
| `geom_dim1_distinct` | `smallint` | Number of distinct dimension 1 factors in the {{KNOWL('av.decomposition', 'decomposition')}} into simple factors of t... | integer |
| `geom_dim1_factors` | `smallint` | Number of dimension 1 factors in the {{KNOWL('av.decomposition', 'decomposition')}} into simple factors of the base c... | integer |
| `geom_dim2_distinct` | `smallint` | Number of distinct dimension 2 factors in the {{KNOWL('av.decomposition', 'decomposition')}} into simple factors of t... | integer |
| `geom_dim2_factors` | `smallint` | Number of dimension 2 factors in the {{KNOWL('av.decomposition', 'decomposition')}} into simple factors of the base c... | integer |
| `geom_dim3_distinct` | `smallint` | Number of distinct dimension 3 factors in the {{KNOWL('av.decomposition', 'decomposition')}} into simple factors of t... | integer |
| `geom_dim3_factors` | `smallint` | Number of dimension 3 factors in the {{KNOWL('av.decomposition', 'decomposition')}} into simple factors of the base c... | integer |
| `geom_dim4_distinct` | `smallint` | Number of distinct dimension 4 factors in the {{KNOWL('av.decomposition', 'decomposition')}} into simple factors of t... | integer |
| `geom_dim4_factors` | `smallint` | Number of dimension 4 factors in the {{KNOWL('av.decomposition', 'decomposition')}} into simple factors of the base c... | integer |
| `geom_dim5_distinct` | `smallint` | Number of distinct dimension 5 factors in the {{KNOWL('av.decomposition', 'decomposition')}} into simple factors of t... | integer |
| `geom_dim5_factors` | `smallint` | Number of dimension 5 factors in the {{KNOWL('av.decomposition', 'decomposition')}} into simple factors of the base c... | integer |
| `geometric_center_dim` | `smallint` | Dimension over $\mathbb{Q}$ of the center of the {{KNOWL('ag.endomorphism_algebra', 'endomorphism algebra')}} after b... | integer |
| `geometric_extension_degree` | `smallint` | Minimal degree after which the {{KNOWL('ag.endomorphism_algebra', 'endomorphism algebra')}} stabilizes under base change | integer |
| `geometric_galois_groups` | `text[]` | Version of {{KNOWL('columns.av_fq_isog.galois_groups', 'galois_groups')}} after base change to the algebraic closure | list of strings |
| `geometric_number_fields` | `text[]` | Version of {{KNOWL('columns.av_fq_isog.number_fields', 'number_fields')}} after base change to the algebraic closure | list of strings |
| `geometric_splitting_field` | `text` | Version of {{KNOWL('columns.av_fq_isog.splitting_field', 'splitting_field')}} after base change to the algebraic closure | text |
| `geometric_splitting_polynomials` | `numeric[]` | Version of {{KNOWL('columns.av_fq_isog.splitting_polynomials', 'splitting_polynomials')}} after base change to the al... | list of arbitrary-precision integers |
| `group_structure_count` | `smallint` | The number of distinct possible group structures for A(F_q) among unpolarized isomorphism classes in this isogeny cla... | non-negative integer (count) |
| `has_geom_ss_factor` | `boolean` | Whether at least one of the simple factors is supersingular | boolean |
| `has_jacobian` | `smallint` | Whether this isogeny class contains a {{KNOWL('av.fq.jacobian', 'Jacobian')}} | integer |
| `has_principal_polarization` | `smallint` | Whether this isogeny class contains a {{KNOWL('av.princ_polarizable', 'principally polarizable')}} abelian variety | integer |
| `hyp_count` | `integer` | The number of {{KNOWL('av.fq.jacobian', 'Jacobians')}} of {{KNOWL('ag.hyperelliptic_curve', 'hyperelliptic curves')}}... | non-negative integer (count) |
| `is_cyclic` | `boolean` | whether all abelian varieties in this isogeny class have cyclic group of points | boolean |
| `is_geometrically_simple` | `boolean` | Whether this isogeny class is {{KNOWL('ag.geom_simple', 'geometrically simple')}} | boolean, simple over algebraic closure |
| `is_geometrically_squarefree` | `boolean` | Whether this isogeny class is {{KNOWL('av.geometrically_squarefree', 'geometrically squarefree')}} | boolean |
| `is_primitive` | `boolean` | Whether this isogeny class is {{KNOWL('ag.ag.primitive', 'primitive')}} | boolean, not isogenous to base change from smaller field |
| `is_simple` | `boolean` | Whether this isogeny class is {{KNOWL('av.simple', 'simple')}} | boolean, simple over F_q |
| `is_squarefree` | `boolean` | False iff the {{KNOWL('av.decomposition', 'decomposition')}} has a repeated simple factor | boolean |
| `is_supersingular` | `boolean` | Whether this isogeny class is supersingular: all slopes 1/2 | boolean |
| `jacobian_count` | `integer` | The number of {{KNOWL('av.fq.jacobian', 'Jacobians')}} in this isogeny class | non-negative integer (count) |
| `label` | `text` | The {{KNOWL('av.fq.lmfdb_label', 'label')}} of this isogeny class | isogeny class label, e.g. '2.16.am_cn' |
| `max_divalg_dim` | `smallint` | Among the {{KNOWL('ag.endomorphism_algebra', 'endomorphism algebras')}} of the {{KNOWL('av.simple', 'simple')}} facto... | integer |
| `max_geom_divalg_dim` | `smallint` | Version of {{KNOWL('columns.av_fq_isog.max_divalg_dim', 'max_divalg_dim')}} after base change to the algebraic closure | integer |
| `max_twist_degree` | `integer` | (description not yet updated on this server) | integer |
| `newton_coelevation` | `smallint` | the length of any chain to the supersingular Newton polygon in the lattice of admissible Newton polygons (which is ca... | integer |
| `newton_elevation` | `smallint` | the length of any chain to the ordinary Newton polygon in the lattice of admissible Newton polygons (which is catenar... | integer |
| `noncyclic_primes` | `integer[]` | the primes l so that some abelian variety in this isogeny class has noncyclic l-Sylow subgroup in its group of points | list of integers |
| `number_fields` | `text[]` | The number fields associated to the irreducible factors of the Weil polynomial, as a list of LMFDB labels | list of strings |
| `p` | `smallint` | Characteristic of the {{KNOWL('ag.base_field', 'base field')}} | characteristic p |
| `p_rank` | `smallint` | The {{KNOWL('av.fq.p_rank', '$p$-rank')}} of this isogeny class | p-rank (0 to g) |
| `p_rank_deficit` | `smallint` | The {{KNOWL('av.fq.p_rank', '$p$-rank deficit')}} of this isogeny class | integer |
| `pic_prime_gens` | `integer[]` | A sequence of quadruples (i, p, pcnt, m) representing prime ideals of Z[F,V] that generate Pic(Z[F,V]).  Each such pr... | list of integers |
| `poly` | `integer[]` | The coefficients of the {{KNOWL('av.fq.l-polynomial', 'L-polynomial')}} of this isogeny class | list of integers |
| `poly_str` | `text` | Space separated string version of {{KNOWL('columns.av_fq_isog.poly', 'poly')}}, for searching | text |
| `primitive_models` | `text[]` | List of labels of {{KNOWL('ag.primitive', 'primitive')}} isogeny classes yielding this upon base change | list of strings |
| `principal_polarization_count` | `integer` | The number of principally polarized abelian varieties in this isogeny class | non-negative integer (count) |
| `q` | `integer` | Cardinality of the {{KNOWL('ag.base_field', 'base field')}} | finite field cardinality q = p^a |
| `real_poly` | `integer[]` | A polynomial of degree {{KNOWL('ag.dimension', '$g$')}} defining the real subfield, with constant coefficient 1 and i... | list of integers |
| `simple_distinct` | `text[]` | The labels of distinct {{KNOWL('av.simple', 'simple')}} {{KNOWL('av.decomposition', 'factors')}} of this isogeny class | list of strings |
| `simple_factors` | `text[]` | A list of strings, each a concatentation of the label of a {{KNOWL('av.simple', 'simple')}} {{KNOWL('av.decomposition... | list of strings |
| `simple_multiplicities` | `smallint[]` | The multiplicites of the {{KNOWL('av.simple', 'simple')}} {{KNOWL('av.decomposition', 'factors')}}, as integers in an... | list of small integers |
| `singular_primes` | `text[]` | The primes dividing the conductor of Z[F,V] | list of strings |
| `size` | `integer` | number of isomorphism classes within the isogeny class (isomorphisms of unpolarized abelian varieties) | integer |
| `slopes` | `text[]` | A list of strings, each a concatentation of a rational number (a {{KNOWL('lf.newton_polygon', 'slope')}}) and an incr... | list of strings |
| `splitting_field` | `text` | The minimal LMFDB label of a number field whose Galois closure contains all roots of the Weil polynomial | text |
| `splitting_polynomials` | `numeric[]` | A list of polynomials (as lists of coefficients), each of whose Galois closure contains all roots of the Weil polynom... | list of arbitrary-precision integers |
| `twist_count` | `integer` | The number of isogeny classes with the same {{KNOWL('ag.dimension', 'dimension')}} and {{KNOWL('ag.base_field', 'base... | non-negative integer (count) |
| `twists` | `jsonb` | A list of all minimal triples (label, bc, deg), where label is the label of a {{KNOWL('av.twist', 'twist')}} and bc i... | JSON list of [twist_label, base_change_label, min_extension_degree] triples: each identifies a twist, its common base change, and the minimal degree extension where the two become isogenous |
| `weak_equivalence_count` | `smallint` | The number of weak equivalence classes for this isogeny class, as stored in the av_fq_weak_equivalences table | non-negative integer (count) |
| `zfv_index` | `numeric` | The index of the order generated by Frobenius and Vershebung inside the maximal order of the etale algebra | arbitrary-precision integer |
| `zfv_index_factorization` | `numeric[]` | The factorization of {{KNOWL('columns.av_fq_isog.zfv_index', 'zfv_index')}} | list of arbitrary-precision integers |
| `zfv_is_bass` | `boolean` | Whether $\mathbb{Z}[F, V]$ is Bass | boolean |
| `zfv_is_maximal` | `boolean` | Whether $\mathbb{Z}[F, V]$ is the maximal order | boolean |
| `zfv_pic_size` | `integer` | (description not yet updated on this server) | integer |
| `zfv_plus_index` | `numeric` | The index of $\mathbb{Z}[F+V]$ inside the maximal order of the real subalgebra | arbitrary-precision integer |
| `zfv_plus_index_factorization` | `numeric[]` | The factorization of {{KNOWL('columns.av_fq_isog.zfv_plus_index', 'zfv_plus_index')}} | list of arbitrary-precision integers |
| `zfv_plus_norm` | `numeric` | The absolute value of the norm of $F-V$ to $\mathbb{Z}$ | arbitrary-precision integer |
| `zfv_singular_count` | `smallint` | (description not yet updated on this server) | non-negative integer (count) |
| `zfv_singular_primes` | `text[]` | (description not yet updated on this server) | list of strings |

---

## av_fq_pol

This table represents polarized abelian varieties, up to isomorphism.

**Rows:** 49,886,088

**API:** https://www.lmfdb.org/api/av_fq_pol/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `aut_group` | `text` | finite group label | text |
| `degree` | `smallint` | degree of the polarization | positive integer |
| `degree_ll` | `smallint` | order of the ll part of the kernel | integer |
| `degree_lr` | `smallint` | order of the lr part of the kernel | integer |
| `degree_rl` | `smallint` | order of the rl part of the kernel | integer |
| `degree_rr` | `smallint` | order of the rr part of the kernel | integer |
| `endomorphism_ring` | `text` | The label for the endomorphism ring, N.i | text |
| `geom_aut_group` | `text` | finite group label | text |
| `is_jacobian` | `boolean` | (description not yet updated on this server) | boolean |
| `isog_label` | `text` | The label for the isogeny class, g.q.isocls | string label (cross-reference) |
| `isom_label` | `text` | The label for the unpolarized isomorphism class, j.z, where the j gives the the weak equivalence class within the end... | string label (cross-reference) |
| `kernel` | `smallint[]` | invariant factors for the kernel of the isogeny (cokernel of the map of lattices) | list of small integers |
| `kernel_ll` | `smallint[]` | abelian invariants of the ll part of the kernel | list of small integers |
| `kernel_lr` | `smallint[]` | abelian invariants of the lr part of the kernel | list of small integers |
| `kernel_rl` | `smallint[]` | abelian invariants of the rl part of the kernel | list of small integers |
| `kernel_rr` | `smallint[]` | abelian invariants of the rr part of the kernel | list of small integers |
| `label` | `text` | The full label g.q.isocls.N.i.j.z.d.l, where l enumerates distinct polarizations of degree d within the same isomorph... | string label |
| `pol_ctr` | `integer` | The last component of the label, enumerating polarizations with the same degree of the same unpolarized isomorphism c... | integer |
| `representative` | `jsonb` | (description not yet updated on this server) | JSON [denominator, [c0,c1,...]]: representative ideal for weak equivalence class of polarization. Ideal = (c0*w0 + c1*w1 + ...)/denominator in endomorphism ring Z-basis |

---

## av_fq_teximages

Precomputed latex for displaying endomorphism rings

**Rows:** 460,190

**API:** https://www.lmfdb.org/api/av_fq_teximages/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `image` | `text` | base64 encoded image of the resulting output | text |
| `label` | `text` | latex for displaying an endomorphism ring in the poset of endomorphism rings for an isogeny class | string label |

---

## av_fq_weak_equivalences

Representatives for the weak equivalence classes

**Rows:** 3,778,316

**API:** https://www.lmfdb.org/api/av_fq_weak_equivalences/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `cohen_macaulay_type` | `smallint` | This is the Cohen-Macaulay type of the order $S$, that is, the minimal number of generators (as an $S$-module) of a c... | integer |
| `conductor` | `jsonb` | `[M, d, alpha]`, where M and d are integers and alpha is a list of integers, and the conductor is the ideal of the ma... | positive integer |
| `conductor_Oindex` | `numeric` | Index of the conductor inside the maximal order.  Only stored for endormorphism rings. | arbitrary-precision integer |
| `conductor_Sindex` | `numeric` | Index of the conductor inside this order.  Only stored for endormorphism rings. | arbitrary-precision integer |
| `conductor_class` | `text` | The label `N.i` of the first order with this conductor (allows for easier searching for orders with the same conducto... | text |
| `conductor_is_Oprime` | `boolean` | Whether the conductor is prime as an ideal of the maximal order.  Only stored for endormorphism rings. | boolean |
| `conductor_is_Sprime` | `boolean` | Whether the conductor is prime as an ideal of this order.  Only stored for endormorphism rings. | boolean |
| `diagramx` | `smallint` | x-coordinate for layout in endomorphism ring diagram | integer |
| `dimensions` | `smallint[]` | Sequence of dimensions of I/PI over S/PS as P ranges singular primes sorted according to our sorting scheme | list of small integers |
| `generator_over_ZFV` | `jsonb` | a pair [d, f] where d is an integer and f is a sequence of integers representing an element of Z[F,V], expressing thi... | a pair [d, f] where d is an integer and f is a sequence of integers representing |
| `higher_invariants` | `jsonb` | Invariant factors of `A(F_{q^d})` for d=2..10 | Invariant factors of `A(F_{q^d})` for d=2..10 (JSON array) |
| `ideal_basis_denominator` | `numeric` | denominator for coefficients in the Z-basis (will be a divisor of the index of the Frobenius order in the maximal order) | arbitrary-precision integer |
| `ideal_basis_numerators` | `numeric[]` | Z-basis for the chosen representative of weak equivalence class, after scaling by the denominator | list of arbitrary-precision integers |
| `index` | `bigint` | The index of the order inside the maximal order.  Null for non-invertible weak equivalence classes | integer |
| `is_ZFVconductor_sum` | `boolean` | Whether this ring is the sum of Z[F,V] and its conductor.  Only stored for endomorphism rings. | boolean |
| `is_Zconductor_sum` | `boolean` | Whether this ring is the sum of Z and its conductor.  Only stored for endomorphism rings. | boolean |
| `is_conjugate_stable` | `boolean` | Whether this ring is stable under complex conjugation.  Only stored for endomorphism rings. | boolean |
| `is_invertible` | `boolean` | Invertible in its multiplicator ring (only S itself is invertible) | boolean |
| `is_product` | `boolean` | Whether ideals with this multiplicator ring split nontrivially as a direct product (in some set of components of the ... | boolean |
| `isog_label` | `text` | label for the isogeny class | string label (cross-reference) |
| `label` | `text` | g.q.isocls.N.i.j where g.q.isocls is the label of the isogeny class, N is the index of the multiplicator ring in the ... | string label |
| `minimal_overorders` | `text[]` | list of labels `N.i` for minimal overorders (null except for endomorphism rings themselves) | list of strings |
| `multiplicator_ring` | `text` | label for the multiplicator ring S (N.i above) | text |
| `number_of_we` | `integer` | number of weak equivalence classes with the same multiplicator_ring and isog_label | integer |
| `pic_basis` | `integer[]` | A sequence of coefficient sequences, giving elements of Pic(S) forming an abelian basis, expressed in terms of the ex... | list of integers |
| `pic_invs` | `integer[]` | Abelian invariants for the Picard group.  Only stored for endomorphism rings.  These are Smith-style invariants, so e... | list of integers |
| `pic_size` | `integer` | The size of the Picard Group $\mathrm{Pic}(S)$ of the order $S$. Recall that $\mathrm{Pic}(S)$ is the group of inver... | integer |
| `product_partition` | `jsonb` | How ideals with this multiplicator ring split as a direct product, as a list of lists of integers, giving which compo... | How ideals with this multiplicator ring split as a direct product, as a list of  |
| `rational_invariants` | `numeric[]` | Invariant factors of `A(F_q)` | list of arbitrary-precision integers |
| `singular_support` | `integer` | An integer encoding the singular primes that divide the conductor of this order (null for non-invertible weak equival... | integer |
| `we_number` | `smallint` | number of weak equivalence classes with multiplicator ring S = Two fractional $S$-ideals $I$ and $J$ are in the same ... | integer |

---
