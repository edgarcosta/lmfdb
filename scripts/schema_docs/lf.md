# lf — Database Schema

**4 tables, 121 columns total**

### Tables

- [lf_families](#lf_families) (605,478 rows)
- [lf_fields](#lf_fields) (1,393,286 rows)
- [lf_galois](#lf_galois) (3,547 rows)
- [lf_tori](#lf_tori) (32,612 rows)

---

## lf_families

Krasner-Monge families of local fields

**Rows:** 605,478

**API:** https://www.lmfdb.org/api/lf_families/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `all_stored` | `boolean` | Whether all fields in this family are contained in the LMFDB | boolean |
| `ambiguity` | `smallint` | The ratio of the number of polynomials to the mass (adjusted by multiplying by the size of the automorphism group of ... | integer |
| `base` | `text` | The label of the base for the family (or just the string p if the base is Qp), which can be any tame extension of Qp | text |
| `base_aut` | `smallint` | Size of the automorphism group of the base over Qp | integer |
| `c` | `smallint` | conductor exponent for fields in this family | integer |
| `c0` | `smallint` | discriminant exponent for the base | integer |
| `c_absolute` | `smallint` | the absolute discriminant exponent: the discriminant exponent for fields in this family considered as extensions of Qp | integer |
| `ctr` | `smallint` | the index of this family among those with the same base, f, n and c | integer |
| `ctr0` | `integer` | ctr for the base field | integer |
| `ctr0_family` | `integer` | ctr_family for the base field | integer |
| `ctr0_subfamily` | `integer` | ctr_subfamily for the base field | integer |
| `e` | `smallint` | ramification degree of fields in this family | integer |
| `e0` | `smallint` | ramification degree of the base | integer |
| `e_absolute` | `smallint` | e*e0, the ramification index over Qp | integer |
| `f` | `smallint` | residue field degree (both for the base and fields in this family | integer |
| `f0` | `smallint` | residue field degree for the base | integer |
| `f_absolute` | `smallint` | f*f0, the absolute residue field degree for fields in this family | integer |
| `field_count` | `integer` | The number of fields within this family currently in the database | non-negative integer (count) |
| `heights` | `text` | Heights in the ramification polygon, equivalent to visible slopes | text |
| `label` | `text` | Has the form base-den.nums, where base is either p (indicating Qp) or the label for a tame extension of Qp, den is a ... | string label |
| `label_absolute` | `text` | the label of the absolute family containing this one (so that this fields in this family are a subset of the fields i... | text |
| `mass_absolute` | `double precision` | The sum of 1/#Aut(L/Qp) for fields in this family | floating-point approximation |
| `mass_absolute_display` | `text` | The sum of 1/#Aut(L/Qp) for fields in this family, as a rational number | text |
| `mass_found` | `double precision` | The mass present in fields of this family that are stored in lf_fields divided by the total mass of the family, as a ... | floating-point approximation |
| `mass_relative` | `double precision` | The sum of 1/#Aut(L/K) for fields in this family | floating-point approximation |
| `mass_relative_display` | `text` | The sum of 1/#Aut(L/K) for fields in this family, as a rational number | text |
| `mass_stored` | `text` | the sum of 1/aut for fields in this family that are in the database | text |
| `means` | `text` | Heights in the ramification polygon, scaled by 1/(e0*p^k).  Equivalent to visible slopes | text |
| `n` | `smallint` | degree of fields in this family | integer |
| `n0` | `smallint` | The degree of the base field over Qp | integer |
| `n_absolute` | `smallint` | n*n0, the degree over Qp | integer |
| `p` | `integer` | residue characteristic | integer |
| `packet_count` | `integer` | The number of packets within this family (a packet is a set of fields within the family that share the same slopes an... | non-negative integer (count) |
| `poly` | `text` | The defining polynomial for this family, which can be specialized to defining polynomials for fields in this family | text |
| `rams` | `text` | Extra height above the minimum in the ramification polygon, same as the breaks in the upper numbering filtration | text |
| `rams_absolute` | `text` | the rams of the absolute family containing this one | text |
| `rf0` | `smallint[]` | root field for the base | list of small integers |
| `slope_multiplicities` | `smallint[]` | Multiplicity vector for slopes | list of small integers |
| `slopes` | `text` | Swan slopes | text |
| `small_rams` | `text` | The rams, scaled by (p-1)/(e0*p^k) | text |
| `tiny_rams` | `text` | The rams, scaled by 1/(e0*p^k) | text |
| `top_slope` | `double precision` | the last Swan slope, 0 for tame, -1 for unramified | floating-point approximation |
| `visible` | `text` | Visible slopes in the Artin convention, which define the family (together with p) | text |
| `w` | `smallint` | fields in this family have degree p^w over the base | integer |
| `wild_segments` | `smallint` | The number of segments in the ramification polygon, which is the same as the number of distinct slopes | integer |

---

## lf_fields

Local number fields

**Rows:** 1,393,286

**API:** https://www.lmfdb.org/api/lf_fields/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `associated_inertia` | `integer[]` | for each segment of the ramification polygon, the LCM of the degrees of the irreducible factors of the residual polyn... | list of integers |
| `aut` | `smallint` | number of automorphisms of the field | integer |
| `c` | `smallint` | valuation of the discriminant | discriminant exponent v_p(disc(K/Q_p)) |
| `canonical_filtration` | `text[]` | The visible slope filtration, giving labels of subfields.  The first is the maximal unramified subfield, the second t... | list of strings |
| `coeffs` | `jsonb` | coefficients of a defining polynomial, starting with the constant term | polynomial coefficients |
| `ctr` | `integer` | counter for fields within the same subfamily | integer |
| `ctr_family` | `integer` | counter for families within the same p,f,e,c | integer |
| `ctr_subfamily` | `integer` | counter for subfamilies within the same family | integer |
| `distinguished_residual_polynomials` | `text[]` | List of distinguished residual polynomials | list of strings |
| `e` | `smallint` | ramification degree | ramification index e(K/Q_p) |
| `eisen` | `text` | Eisenstein polynomial defining relative extension of this field over the maxmial unramified subfield | text |
| `f` | `smallint` | residue field degree | residue degree f(K/Q_p), so n = e*f |
| `family` | `text` | Monge-Krasner family label | text |
| `gal` | `integer` | the Galois group [n, t] for nTt | Galois group label of Galois closure |
| `galois_degree` | `bigint` | the degree of the Galois closure | integer |
| `galois_label` | `text` | label of the Galois group | string label (cross-reference) |
| `gms` | `text` | Galois mean slope | text |
| `gsm` | `jsonb` | Global splitting model | Global splitting model (JSON array) |
| `hidden` | `text` | hidden slopes | text |
| `hw` | `text` | Hasse-Witt invariant as a string | text |
| `ind_of_insep` | `integer[]` | indices of inseparability | list of integers |
| `ind_of_insep_tmp` | `text[]` | Indices of inseparability | list of strings |
| `inertia` | `jsonb` | inertia subgroup | JSON ['t', [n, t]] for transitive inertia group nTt, or ['i', [order, gap_id]] for intransitive. E.g. ['t', [6, 6]] means inertia subgroup is 6T6 |
| `inertia_gap` | `integer[]` | small group GAP id of the inertia subgroup | list of integers |
| `is_completion` | `boolean` | Is this the completion of a global field | boolean |
| `jump_set` | `integer[]` | Jump set of this field, classifying the principle units viewed as a filtered module | list of integers |
| `label` | `text` | label | p-adic field label, e.g. '2.4.6.7' |
| `n` | `smallint` | degree | degree [K:Q_p] |
| `new_label` | `text` | New-style label that includes family information | string label (cross-reference) |
| `num` | `integer` | (description not yet updated on this server) | integer |
| `old_label` | `text` | p.n.c.tiebreaker | string label (cross-reference) |
| `p` | `integer` | prime p for the base \Q_p | prime p (residue characteristic) |
| `packet` | `text` | Label for subset of a family with the same hidden slopes and Galois group | text |
| `packet_size` | `integer` | Number of fields in the same packet as this field | integer |
| `ppow_roots_of_unity` | `smallint` | the maximum integer d so that the p^d roots of unity are contained in this field | integer |
| `ram_poly_vert` | `integer[]` | verticies of the ramification polygon for the totally ramified part of the extension | list of integers |
| `residual_polynomials` | `text[]` | list of residual polynomials in z for the totally ramified part of the extension | list of strings |
| `rf` | `jsonb` | root field | root field (JSON array) |
| `slopes` | `text` | wild ramification slopes | all ramification filtration slopes (as list of rational strings) |
| `slopes_tmp` | `text[]` | wild ramification slopes | list of strings |
| `subfamily` | `text` | a label for the set of fields sharing p, e, f, slopes and residual polynomials | text |
| `subfield` | `text[]` | list of labels of subfields | list of strings |
| `subfield_mult` | `integer[]` | multiplicities of corresponding entrieds in the column subfield | list of integers |
| `t` | `smallint` | tame degree for the Galois closure | integer |
| `top_slope` | `text` | largest slope | highest slope in ramification polygon (as rational string) |
| `u` | `smallint` | degree of maximal unramified subfield of the Galois closure | integer |
| `unram` | `text` | polynomial defining maximal unramified subfield | text |
| `visible` | `text` | Visible slopes | text |
| `visible_tmp` | `text[]` | visible slopes | list of strings |
| `wild_gap` | `integer[]` | the small group GAP id of the wild inertia group | list of integers |

---

## lf_galois

**Rows:** 3,547

**API:** https://www.lmfdb.org/api/lf_galois/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `core_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `degree` | `numeric` | (description not yet updated on this server) | positive integer |
| `galT` | `integer` | (description not yet updated on this server) | integer |
| `galn` | `smallint` | (description not yet updated on this server) | integer |
| `gapid` | `text` | (description not yet updated on this server) | text |
| `gms` | `text` | (description not yet updated on this server) | text |
| `inertia` | `jsonb` | (description not yet updated on this server) | JSON ['t', [n, t]] for transitive inertia group nTt, or ['i', [order, gap_id]] for intransitive |
| `label` | `text` | (description not yet updated on this server) | string label |
| `p` | `integer` | (description not yet updated on this server) | integer |
| `resolvents` | `text[]` | (description not yet updated on this server) | list of strings |
| `slopes` | `text[]` | (description not yet updated on this server) | list of strings |
| `t` | `smallint` | (description not yet updated on this server) | integer |
| `u` | `smallint` | (description not yet updated on this server) | integer |

---

## lf_tori

**Rows:** 32,612

**API:** https://www.lmfdb.org/api/lf_tori/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `abstract_gp` | `text` | (description not yet updated on this server) | text |
| `ambiguity` | `numeric` | (description not yet updated on this server) | arbitrary-precision integer |
| `dim` | `smallint` | (description not yet updated on this server) | non-negative integer |
| `galT` | `integer` | (description not yet updated on this server) | integer |
| `galn` | `smallint` | (description not yet updated on this server) | integer |
| `galois_gp` | `text` | (description not yet updated on this server) | text |
| `inertia` | `jsonb` | (description not yet updated on this server) | JSON ['t', [n, t]] for transitive inertia group nTt, or ['i', [order, gap_id]] for intransitive |
| `label` | `text` | (description not yet updated on this server) | string label |
| `matgp` | `text` | (description not yet updated on this server) | text |
| `p` | `smallint` | (description not yet updated on this server) | integer |
| `splitting_core` | `text` | (description not yet updated on this server) | text |
| `splitting_degree` | `numeric` | (description not yet updated on this server) | arbitrary-precision integer |
| `splitting_field` | `text` | (description not yet updated on this server) | text |

---
