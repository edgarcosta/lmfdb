# belyi — Database Schema

**7 tables, 168 columns total**

### Tables

- [belyi_galmap_portraits](#belyi_galmap_portraits) (915 rows)
- [belyi_galmaps](#belyi_galmaps) (1,111 rows)
- [belyi_galmaps_new](#belyi_galmaps_new) (1,111 rows)
- [belyi_galmaps_test](#belyi_galmaps_test) (1,111 rows)
- [belyi_galmaps_test_consts](#belyi_galmaps_test_consts) (1,111 rows)
- [belyi_passports](#belyi_passports) (1,007 rows)
- [belyi_specializations](#belyi_specializations) (5,106 rows)

---

## belyi_galmap_portraits

**Rows:** 915

**API:** https://www.lmfdb.org/api/belyi_galmap_portraits/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `label` | `text` | LMFDB label | string label |
| `portrait` | `text` | Portrait of the Belyi map, stored as a base 64 string | binary image data (PNG) |

---

## belyi_galmaps

label

**Rows:** 1,111

**API:** https://www.lmfdb.org/api/belyi_galmaps/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `BelyiDB_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `BelyiDB_plabel` | `text` | (description not yet updated on this server) | text |
| `a_s` | `smallint` | The first element of sorted(abc), i.e., sorted(abc) = [a_s, b_s, c_s] | smallest element of abc |
| `abc` | `smallint[]` | The orders of the elements of the corresponding {{ KNOWL('belyi.permutation_triple', title='permutation triple')}} | orders [a,b,c] of ramification above 0,1,infinity |
| `aut_group` | `jsonb` | Generators of automorphism group of the Belyi map, given as permutations in one-line notation | JSON: automorphism group generators in one-line permutation notation |
| `b_s` | `smallint` | The second element of sorted(abc), i.e., sorted(abc) = [a_s, b_s, c_s] | second smallest element of abc |
| `base_field` | `numeric[]` | The coefficients of the polredabs polynomial defining the number field over which the Belyi map is defined. Cf., the ... | polredabs polynomial coefficients of field of definition |
| `base_field_label` | `text` | The LMFDB label of the base field, if it appears in the number fields database | LMFDB number field label of field of definition |
| `c_s` | `smallint` | The third element of sorted(abc), i.e., sorted(abc) = [a_s, b_s, c_s] | largest element of abc |
| `curve` | `text` | The equation(s) for the curve on which the Belyi map is defined | text |
| `curve_label` | `text` | The LMFDB label for the curve, if it appears in the database | LMFDB label of the source curve (if it exists in LMFDB) |
| `deg` | `smallint` | The {{ KNOWL('belyi.degree', title='degree')}} of the Belyi map | degree of the Belyi map |
| `embeddings` | `jsonb` | The {{ KNOWL('nf.embedding', title='embeddings')}} of the {{ KNOWL('belyi.base_field', title='base field knowl')}} of... | JSON: complex embeddings of base_field as list of [real, imag] pairs |
| `friends` | `text[]` | URLs for objects related to the Belyi map | list of URLs to related LMFDB objects |
| `g` | `smallint` | The genus of the curve on which the Belyi map is defined | genus of the source curve |
| `geomtype` | `text` | The {{ KNOWL('belyi.geometry_type', title='geometry type')}} of the Belyi map. Either 'S' for spherical, 'E' for Eucl... | 'H' = hyperbolic, 'E' = Euclidean, 'S' = spherical |
| `group` | `text` | The {{ KNOWL('gg.conway_name', title='transitive group label')}} of the {{ KNOWL('belyi.group', title='monodromy grou... | Galois group label nTt, e.g. '4T5' |
| `group_num` | `smallint` | The second number in the {{ KNOWL('gg.conway_name', title='transitive group label')}}. E.g., if the transitive group ... | t-number in nTt notation |
| `is_primitive` | `boolean` | True if Belyi map is primitive; otherwise false | boolean |
| `label` | `text` | LMFDB label | Belyi map label: degTgroup-partitions-orbit, e.g. '6T7-4.2_3.3_4.2-a' |
| `lambdas` | `jsonb` | A triple of partitions, giving the disjoint cycle structures of the corresponding {{ KNOWL('belyi.permutation_triple'... | JSON: conjugacy type of each triple as partitions, e.g. [[4,2],[3,3],[4,2]] |
| `map` | `text` | The equation for the Belyi map | text |
| `models` | `jsonb` | Alternative models for the curve and Belyi map | JSON list of model dicts: {model_type, ..., curve, map} with equation data |
| `moduli_field` | `numeric[]` | The coefficients of the polredabs polynomial defining the field of moduli the Belyi map. | polredabs polynomial coefficients of field of moduli |
| `moduli_field_label` | `text` | The LMFDB label of the field of moduli, if it appears in the number fields database | LMFDB number field label of field of moduli |
| `orbit_size` | `smallint` | The {{ KNOWL('belyi.orbit_size', title='size of the Galois orbit')}} of the Belyi map | size of Galois orbit of this dessin |
| `pass_size` | `smallint` | The {{ KNOWL('belyi.pass_size', title='size of the passport')}} of the Belyi map | number of dessins in the passport |
| `plabel` | `text` | The LMFDB label of the passport of the Belyi map | passport label |
| `plane_constant` | `text` | The number a such that (1/a)*t is a Belyi map, i.e., ramified above 1 | text |
| `plane_map_constant_factored` | `text` | Constant of plane map, in factored and LaTeXed form. | text |
| `plane_model` | `text` | A plane model for the Belyi curve | text |
| `plane_model_latex` | `text` | Factored form of plane model for the curve, formatted for LaTeX | text |
| `primitivization` | `text` | The LMFDB label of the primitivization of the Belyi map | text |
| `specializations` | `jsonb` | no data yet; will contain specializations of Belyi map at select values | JSON: map t -> specialization data |
| `triples` | `jsonb` | The permutation triples corresponding to the Belyi map orbit, taken up to simultaneous conjugacy in S_d, with each pe... | JSON: permutation triples per embedding. Each triple = 3 permutations as lists |
| `triples_cyc` | `jsonb` | The permutation triples corresponding to the Belyi map orbit, taken up to simultaneous conjugacy in S_d, with each pe... | JSON: same triples in cycle notation, e.g. [[[1,4,3,6],[2,5,8,7]],...] |

---

## belyi_galmaps_new

label

**Rows:** 1,111

**API:** https://www.lmfdb.org/api/belyi_galmaps_new/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `BelyiDB_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `BelyiDB_plabel` | `text` | (description not yet updated on this server) | text |
| `a_s` | `smallint` | The first element of sorted(abc), i.e., sorted(abc) = [a_s, b_s, c_s] | integer |
| `abc` | `smallint[]` | The orders of the elements of the corresponding {{ KNOWL('belyi.permutation_triple', title='permutation triple')}} | list of small integers |
| `aut_group` | `jsonb` | Generators of automorphism group of the Belyi map, given as permutations in one-line notation | Generators of automorphism group of the Belyi map, given as permutations in one- (JSON array) |
| `b_s` | `smallint` | The second element of sorted(abc), i.e., sorted(abc) = [a_s, b_s, c_s] | integer |
| `base_field` | `numeric[]` | The coefficients of the polredabs polynomial defining the number field over which the Belyi map is defined. Cf., the ... | list of arbitrary-precision integers |
| `base_field_label` | `text` | The LMFDB label of the base field, if it appears in the number fields database | string label (cross-reference) |
| `c_s` | `smallint` | The third element of sorted(abc), i.e., sorted(abc) = [a_s, b_s, c_s] | integer |
| `curve` | `text` | The equation(s) for the curve on which the Belyi map is defined | text |
| `curve_label` | `text` | The LMFDB label for the curve, if it appears in the database | string label (cross-reference) |
| `deg` | `smallint` | The {{ KNOWL('belyi.degree', title='degree')}} of the Belyi map | positive integer |
| `embeddings` | `jsonb` | The {{ KNOWL('nf.embedding', title='embeddings')}} of the {{ KNOWL('belyi.base_field', title='base field knowl')}} of... | The {{ KNOWL('nf.embedding', title='embeddings')}} of the {{ KNOWL('belyi.base_f (JSON array) |
| `friends` | `text[]` | URLs for objects related to the Belyi map | list of strings |
| `g` | `smallint` | The genus of the curve on which the Belyi map is defined | non-negative integer (genus) |
| `geomtype` | `text` | The {{ KNOWL('belyi.geometry_type', title='geometry type')}} of the Belyi map. Either 'S' for spherical, 'E' for Eucl... | text |
| `group` | `text` | The {{ KNOWL('gg.conway_name', title='transitive group label')}} of the {{ KNOWL('belyi.group', title='monodromy grou... | text |
| `group_num` | `smallint` | The second number in the {{ KNOWL('gg.conway_name', title='transitive group label')}}. E.g., if the transitive group ... | integer |
| `is_primitive` | `boolean` | True if Belyi map is primitive; otherwise false | boolean |
| `label` | `text` | LMFDB label | string label |
| `lambdas` | `jsonb` | A triple of partitions, giving the disjoint cycle structures of the corresponding {{ KNOWL('belyi.permutation_triple'... | A triple of partitions, giving the disjoint cycle structures of the correspondin (JSON array) |
| `map` | `text` | The equation for the Belyi map | text |
| `models` | `jsonb` | Alternative models for the curve and Belyi map | Alternative models for the curve and Belyi map |
| `moduli_field` | `numeric[]` | The coefficients of the polredabs polynomial defining the field of moduli the Belyi map. | list of arbitrary-precision integers |
| `moduli_field_label` | `text` | The LMFDB label of the field of moduli, if it appears in the number fields database | string label (cross-reference) |
| `orbit_size` | `smallint` | The {{ KNOWL('belyi.orbit_size', title='size of the Galois orbit')}} of the Belyi map | integer |
| `pass_size` | `smallint` | The {{ KNOWL('belyi.pass_size', title='size of the passport')}} of the Belyi map | integer |
| `plabel` | `text` | The LMFDB label of the passport of the Belyi map | text |
| `plane_constant` | `text` | The number a such that (1/a)*t is a Belyi map, i.e., ramified above 1 | text |
| `plane_map_constant_factored` | `text` | Constant of plane map, in factored and LaTeXed form. | text |
| `plane_model` | `text` | A plane model for the Belyi curve | text |
| `plane_model_latex` | `text` | Factored form of plane model for the curve, formatted for LaTeX; now obsolete | text |
| `primitivization` | `text` | The LMFDB label of the primitivization of the Belyi map | text |
| `specializations` | `jsonb` | no data yet; will contain specializations of Belyi map at select values | no data yet; will contain specializations of Belyi map at select values |
| `triples` | `jsonb` | The permutation triples corresponding to the Belyi map orbit, taken up to simultaneous conjugacy in S_d, with each pe... | The permutation triples corresponding to the Belyi map orbit, taken up to simult (JSON array) |
| `triples_cyc` | `jsonb` | The permutation triples corresponding to the Belyi map orbit, taken up to simultaneous conjugacy in S_d, with each pe... | The permutation triples corresponding to the Belyi map orbit, taken up to simult (JSON array) |

---

## belyi_galmaps_test

label

**Rows:** 1,111

**API:** https://www.lmfdb.org/api/belyi_galmaps_test/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `BelyiDB_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `BelyiDB_plabel` | `text` | (description not yet updated on this server) | text |
| `a_s` | `smallint` | (description not yet updated on this server) | integer |
| `abc` | `smallint[]` | (description not yet updated on this server) | list of small integers |
| `aut_group` | `jsonb` | (description not yet updated on this server) | JSON list of permutations in one-line notation: generators of Aut(phi) (same as belyi_passports) |
| `b_s` | `smallint` | (description not yet updated on this server) | integer |
| `base_field` | `numeric[]` | (description not yet updated on this server) | list of arbitrary-precision integers |
| `base_field_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `c_s` | `smallint` | (description not yet updated on this server) | integer |
| `curve` | `text` | (description not yet updated on this server) | text |
| `curve_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `deg` | `smallint` | (description not yet updated on this server) | positive integer |
| `embeddings` | `jsonb` | (description not yet updated on this server) | JSON list of [Re, Im] pairs: complex embeddings (same as belyi_passports) |
| `friends` | `text[]` | Related objects | list of strings |
| `g` | `smallint` | (description not yet updated on this server) | non-negative integer (genus) |
| `geomtype` | `text` | (description not yet updated on this server) | text |
| `group` | `text` | (description not yet updated on this server) | text |
| `group_num` | `smallint` | (description not yet updated on this server) | integer |
| `is_primitive` | `boolean` | (description not yet updated on this server) | boolean |
| `label` | `text` | (description not yet updated on this server) | string label |
| `lambdas` | `jsonb` | (description not yet updated on this server) | JSON list of 3 partitions: ramification type (same as belyi_passports) |
| `map` | `text` | (description not yet updated on this server) | text |
| `models` | `jsonb` | (description not yet updated on this server) | JSON list of model dicts (same as belyi_passports) |
| `moduli_field` | `numeric[]` | (description not yet updated on this server) | list of arbitrary-precision integers |
| `moduli_field_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `orbit_size` | `smallint` | (description not yet updated on this server) | integer |
| `pass_size` | `smallint` | (description not yet updated on this server) | integer |
| `plabel` | `text` | (description not yet updated on this server) | text |
| `plane_constant` | `text` | (description not yet updated on this server) | text |
| `plane_map_constant_factored` | `text` | LaTeX for a factored version of the constant a in the expression phi = a*t for the planar version of the Belyi map | text |
| `plane_model` | `text` | (description not yet updated on this server) | text |
| `plane_model_latex` | `text` | Factored form of plane model for the curve, formatted for LaTeX | text |
| `primitivization` | `text` | (description not yet updated on this server) | text |
| `specializations` | `jsonb` | (description not yet updated on this server) | JSON (not yet populated, same as belyi_passports) |
| `triples` | `jsonb` | (description not yet updated on this server) | JSON list of monodromy triples in one-line notation (same as belyi_passports) |
| `triples_cyc` | `jsonb` | (description not yet updated on this server) | JSON list of monodromy triples in cycle notation (same as belyi_passports) |

---

## belyi_galmaps_test_consts

label

**Rows:** 1,111

**API:** https://www.lmfdb.org/api/belyi_galmaps_test_consts/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `BelyiDB_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `BelyiDB_plabel` | `text` | (description not yet updated on this server) | text |
| `a_s` | `smallint` | The first element of sorted(abc), i.e., sorted(abc) = [a_s, b_s, c_s] | integer |
| `abc` | `smallint[]` | The orders of the elements of the corresponding {{ KNOWL('belyi.permutation_triple', title='permutation triple')}} | list of small integers |
| `aut_group` | `jsonb` | Generators of automorphism group of the Belyi map, given as permutations in one-line notation | Generators of automorphism group of the Belyi map, given as permutations in one- (JSON array) |
| `b_s` | `smallint` | The second element of sorted(abc), i.e., sorted(abc) = [a_s, b_s, c_s] | integer |
| `base_field` | `numeric[]` | The coefficients of the polredabs polynomial defining the number field over which the Belyi map is defined. Cf., the ... | list of arbitrary-precision integers |
| `base_field_label` | `text` | The LMFDB label of the base field, if it appears in the number fields database | string label (cross-reference) |
| `c_s` | `smallint` | The third element of sorted(abc), i.e., sorted(abc) = [a_s, b_s, c_s] | integer |
| `curve` | `text` | The equation(s) for the curve on which the Belyi map is defined | text |
| `curve_label` | `text` | The LMFDB label for the curve, if it appears in the database | string label (cross-reference) |
| `deg` | `smallint` | The {{ KNOWL('belyi.degree', title='degree')}} of the Belyi map | positive integer |
| `embeddings` | `jsonb` | The {{ KNOWL('nf.embedding', title='embeddings')}} of the {{ KNOWL('belyi.base_field', title='base field knowl')}} of... | The {{ KNOWL('nf.embedding', title='embeddings')}} of the {{ KNOWL('belyi.base_f (JSON array) |
| `friends` | `text[]` | URLs for objects related to the Belyi map | list of strings |
| `g` | `smallint` | The genus of the curve on which the Belyi map is defined | non-negative integer (genus) |
| `geomtype` | `text` | The {{ KNOWL('belyi.geometry_type', title='geometry type')}} of the Belyi map. Either 'S' for spherical, 'E' for Eucl... | text |
| `group` | `text` | The {{ KNOWL('gg.conway_name', title='transitive group label')}} of the {{ KNOWL('belyi.group', title='monodromy grou... | text |
| `group_num` | `smallint` | The second number in the {{ KNOWL('gg.conway_name', title='transitive group label')}}. E.g., if the transitive group ... | integer |
| `is_primitive` | `boolean` | True if Belyi map is primitive; otherwise false | boolean |
| `label` | `text` | LMFDB label | string label |
| `lambdas` | `jsonb` | A triple of partitions, giving the disjoint cycle structures of the corresponding {{ KNOWL('belyi.permutation_triple'... | A triple of partitions, giving the disjoint cycle structures of the correspondin (JSON array) |
| `map` | `text` | The equation for the Belyi map | text |
| `models` | `jsonb` | Alternative models for the curve and Belyi map | Alternative models for the curve and Belyi map |
| `moduli_field` | `numeric[]` | The coefficients of the polredabs polynomial defining the field of moduli the Belyi map. | list of arbitrary-precision integers |
| `moduli_field_label` | `text` | The LMFDB label of the field of moduli, if it appears in the number fields database | string label (cross-reference) |
| `orbit_size` | `smallint` | The {{ KNOWL('belyi.orbit_size', title='size of the Galois orbit')}} of the Belyi map | integer |
| `pass_size` | `smallint` | The {{ KNOWL('belyi.pass_size', title='size of the passport')}} of the Belyi map | integer |
| `plabel` | `text` | The LMFDB label of the passport of the Belyi map | text |
| `plane_constant` | `text` | The number a such that (1/a)*t is a Belyi map, i.e., ramified above 1 | text |
| `plane_map_constant_factored` | `text` | Constant of plane map, in factored and LaTeXed form. | text |
| `plane_model` | `text` | A plane model for the Belyi curve | text |
| `plane_model_latex` | `text` | Factored form of plane model for the curve, formatted for LaTeX | text |
| `primitivization` | `text` | The LMFDB label of the primitivization of the Belyi map | text |
| `specializations` | `jsonb` | no data yet; will contain specializations of Belyi map at select values | no data yet; will contain specializations of Belyi map at select values |
| `triples` | `jsonb` | The permutation triples corresponding to the Belyi map orbit, taken up to simultaneous conjugacy in S_d, with each pe... | The permutation triples corresponding to the Belyi map orbit, taken up to simult (JSON array) |
| `triples_cyc` | `jsonb` | The permutation triples corresponding to the Belyi map orbit, taken up to simultaneous conjugacy in S_d, with each pe... | The permutation triples corresponding to the Belyi map orbit, taken up to simult (JSON array) |

---

## belyi_passports

**Rows:** 1,007

**API:** https://www.lmfdb.org/api/belyi_passports/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `BelyiDB_plabel` | `text` | (description not yet updated on this server) | text |
| `a_s` | `smallint` | The first element of sorted(abc), i.e., sorted(abc) = [a_s, b_s, c_s] | smallest element of abc |
| `abc` | `smallint[]` | The orders of the elements of the corresponding {{ KNOWL('belyi.permutation_triple', title='permutation triple')}} | orders [a,b,c] |
| `aut_group` | `jsonb` | Generators of automorphism group of the Belyi map, given as permutations in one-line notation | JSON list of permutations in one-line notation: generators of Aut(phi), the automorphism group of the Belyi map. E.g. [[3,4,1,2],[4,3,2,1]] |
| `b_s` | `smallint` | The second element of sorted(abc), i.e., sorted(abc) = [a_s, b_s, c_s] | second smallest element |
| `c_s` | `smallint` | The third element of sorted(abc), i.e., sorted(abc) = [a_s, b_s, c_s] | largest element |
| `deg` | `smallint` | The {{ KNOWL('belyi.degree', title='degree')}} of the Belyi map | degree |
| `g` | `smallint` | The genus of the curve on which the Belyi map is defined | genus |
| `geomtype` | `text` | The {{ KNOWL('belyi.geometry_type', title='geometry type')}} of the Belyi map. Either 'S' for spherical, 'E' for Eucl... | 'H', 'E', or 'S' |
| `group` | `text` | The {{ KNOWL('gg.conway_name', title='transitive group label')}} of the {{ KNOWL('belyi.group', title='monodromy grou... | group label nTt |
| `group_num` | `smallint` | An identifier for the monodromy group, i.e., the k in the transitive group label dTk | integer |
| `is_primitive` | `boolean` | (description not yet updated on this server) | boolean |
| `lambdas` | `jsonb` | A triple of partitions, giving the disjoint cycle structures of the corresponding {{ KNOWL('belyi.permutation_triple'... | JSON list of exactly 3 partitions: cycle structures of (sigma_0, sigma_1, sigma_inf). Each partition = descending list of positive ints summing to degree d |
| `maxdegbf` | `smallint` | The size of the largest Galois orbit contained in the passport; equivalently, the degree of the number field over whi... | maximal degree of base field among maps in passport |
| `num_orbits` | `smallint` | The number of Galois orbits contained in the passport | number of Galois orbits in passport |
| `pass_size` | `smallint` | The {{ KNOWL('belyi.pass_size', title='size of the passport')}} of the Belyi map | number of Belyi maps in passport |
| `plabel` | `text` | The LMFDB label of the passport | passport label |
| `primitivization` | `text` | (description not yet updated on this server) | text |
| `triples` | `jsonb` | The permutation triples contained in the passport, taken up to simultaneous conjugacy in S_d, with each permutation g... | JSON list of monodromy triples: each = [[perm0],[perm1],[perm_inf]] in one-line notation (lists of d ints). One triple per Galois conjugate. sigma_0*sigma_1*sigma_inf = id |

---

## belyi_specializations

specializations of Belyi maps

**Rows:** 5,106

**API:** https://www.lmfdb.org/api/belyi_specializations/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `algebra` | `jsonb` | List of number fields given by coefficients for the algebra | List of number fields given by coefficients for the algebra (JSON array) |
| `label` | `text` | Label of a Belyi map | string label |
| `point` | `text` | Specialization point | text |

---
