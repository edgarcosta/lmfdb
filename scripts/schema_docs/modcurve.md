# modcurve — Database Schema

**10 tables, 83 columns total**

### Tables

- [modcurve_decomposition](#modcurve_decomposition) (525,349 rows)
- [modcurve_images](#modcurve_images) (3,079 rows)
- [modcurve_modelmaps](#modcurve_modelmaps) (109,042 rows)
- [modcurve_modelmaps_old](#modcurve_modelmaps_old) (8,025 rows)
- [modcurve_models](#modcurve_models) (110,173 rows)
- [modcurve_models_old](#modcurve_models_old) (3,160 rows)
- [modcurve_pictures](#modcurve_pictures) (19,648 rows)
- [modcurve_points](#modcurve_points) (1,848,861 rows)
- [modcurve_points_old](#modcurve_points_old) (1,747,697 rows)
- [modcurve_teximages](#modcurve_teximages) (5,891 rows)

---

## modcurve_decomposition

Data on decompositions of Jacobians of modular curves into simple modular abelian varieites

**Rows:** 525,349

**API:** https://www.lmfdb.org/api/modcurve_decomposition/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `analytic_ranks` | `smallint[]` | A list of positive integers giving the analytic ranks of the simple isogeny factors that appear in the {{KNOWL('modcu... | list of small integers |
| `dims` | `integer[]` | A list of positive integers giving the dimensions of the simple isogeny factors that appear in the {{KNOWL('modcurve.... | list of integers |
| `gassman_class` | `text` | The label of the Gassman class of the modular curve (the first four parts of the label).  Decomposition data is const... | text |
| `mults` | `integer[]` | The multiplicities of each modular abelian variety $A_f$ appearing in the {{KNOWL('modcurve.decomposition', 'isogeny ... | list of integers |
| `newforms` | `text[]` | The list of distinct labels of newforms $f$ for which the modular abelian variety $A_f$ is an isogeny factor of the J... | list of strings |

---

## modcurve_images

Images for modular curves, as unions of triangles in the hyperbolic disc

**Rows:** 3,079

**API:** https://www.lmfdb.org/api/modcurve_images/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `CPlabel` | `text` | The Cummins&Pauli label | text |
| `image` | `text` | The image, as a base64 encoded png string | text |

---

## modcurve_modelmaps

Maps between modular curves, mostly induced by inclusions of the corresponding subgroups of GL(2, Zhat)

**Rows:** 109,042

**API:** https://www.lmfdb.org/api/modcurve_modelmaps/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `codomain_label` | `text` | The {{KNOWL("modcurve.label", "label")}} of the codomain. | string label (cross-reference) |
| `codomain_model_type` | `smallint` | The {{KNOWL('columns.modcurve_models.model_type', 'type of model')}} used in specifying coordinates on the domain. | integer |
| `coordinates` | `text[]` | (description not yet updated on this server) | list of strings |
| `degree` | `integer` | The degree of this map, which should equal the ratio of the index of the domain by the index of the codomain. | positive integer |
| `domain_label` | `text` | The {{KNOWL("modcurve.label", "label")}} of the domain. | string label (cross-reference) |
| `domain_model_type` | `smallint` | The {{KNOWL('columns.modcurve_models.model_type', 'type of model')}} used in specifying coordinates on the domain. | integer |
| `dont_display` | `boolean` | (description not yet updated on this server) | boolean |
| `factored` | `boolean` | (description not yet updated on this server) | boolean |
| `leading_coefficients` | `text[]` | (description not yet updated on this server) | list of strings |
| `upload_id` | `bigint` | id for the row in data_uploads that added this map | integer |

---

## modcurve_modelmaps_old

**Rows:** 8,025

**API:** https://www.lmfdb.org/api/modcurve_modelmaps_old/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `codomain_label` | `text` | Label for the codomain as a modular curve or other kind of curve | string label (cross-reference) |
| `codomain_model_type` | `smallint` | Specify which model to use for the domain (0=canonical, 1=P^1 (t or j coord), 2=plane, 3=P^1 (j-1728 coord), 4=weight... | integer |
| `coordinates` | `text[]` | A list of lists of polynomial in the coordinates on the domain. They will be homogeneous except in the case that the ... | list of strings |
| `degree` | `integer` | Degree of the map | positive integer |
| `domain_label` | `text` | Label for the domain as a modular curve | string label (cross-reference) |
| `domain_model_type` | `smallint` | Specify which model to use for the domain (0=canonical, 1=P^1, 2=plane) | integer |
| `dont_display` | `boolean` | if true, will never be displayed on a homepage, but will still be available for download | boolean |
| `factored` | `boolean` | whether the numerators and denominators are factored into irreducibles | boolean |
| `leading_coefficients` | `text[]` | a list of lists of leading coefficients (parallel to the coordinates above). If null, interpreted as all 1s, but avai... | list of strings |

---

## modcurve_models

Models for modular curves

**Rows:** 110,173

**API:** https://www.lmfdb.org/api/modcurve_models/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `dont_display` | `boolean` | (description not yet updated on this server) | boolean |
| `equation` | `text[]` | The standard order of variables in the equation is XYZWTUVRSABCDEFGHIKLMNOPQJ. If there are more than 26 variables, ... | list of strings |
| `modcurve` | `text` | (description not yet updated on this server) | text |
| `model_type` | `smallint` | An integer encoding the type of the model as follows:  * 0: canonical (including plane models for nonhyperelliptic ... | integer |
| `number_variables` | `smallint` | (description not yet updated on this server) | integer |
| `smooth` | `boolean` | (description not yet updated on this server) | boolean |
| `upload_id` | `bigint` | id for the row in data_uploads that added this point | integer |

---

## modcurve_models_old

**Rows:** 3,160

**API:** https://www.lmfdb.org/api/modcurve_models_old/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `dont_display` | `boolean` | If true, will never be displayed on a homepage, but will still be available for download | boolean |
| `equation` | `text` | Equation(s) for this model | text |
| `gonality_bounds` | `integer[]` | A lower and an upper bound on the gonality | list of integers |
| `modcurve` | `text` | Label of the modular curve | text |
| `model_type` | `smallint` | A code for the type of model: 0=canonical, 1=P^1 (such rows are skipped, but the code is used for the modcurve_modelm... | integer |
| `number_variables` | `smallint` | The number of variables in the equation | integer |
| `smooth` | `boolean` | Whether this model is smooth over Q | boolean |

---

## modcurve_pictures

Profile pictures for modular curves

**Rows:** 19,648

**API:** https://www.lmfdb.org/api/modcurve_pictures/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `image` | `text` | The image, as a base 64 encoded string | text |
| `psl2label` | `text` | The label for the action of the group on the upper half plane, which factors through PSL(2,Z). | text |

---

## modcurve_points

Rational points on modular curves

**Rows:** 1,848,861

**API:** https://www.lmfdb.org/api/modcurve_points/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `Elabel` | `text` | (description not yet updated on this server) | text |
| `ainvs` | `text` | (description not yet updated on this server) | list of 5 integers [a1, a2, a3, a4, a6] |
| `cardinality` | `integer` | (description not yet updated on this server) | integer |
| `cm` | `smallint` | (description not yet updated on this server) | integer |
| `conductor_norm` | `numeric` | The norm of the conductor of the minimal twist of an elliptic curve corrsponding to this point | arbitrary-precision integer |
| `coordinates` | `jsonb` | A dictionary with keys the different model types and values a list of coordinates as strings with coordinates in term... | JSON dict: keys are model type ints (as strings, 0=canonical, 2=plane, 5=Weierstrass), values are lists of coordinate strings in the residue field basis |
| `curve_genus` | `integer` | The genus of the modular curve on which this point lies | integer |
| `curve_index` | `integer` | The index in GL(2,Z/N) of the modular curve on which this point lies | integer |
| `curve_label` | `text` | The label of the modular curve | string label (cross-reference) |
| `curve_level` | `integer` | The level of the modular curve on which this point lies | integer |
| `curve_name` | `text` | If applicable, the name of the modular curve such as X_0(N) | text |
| `cusp` | `boolean` | Whether this point lies above j=infinity | boolean |
| `degree` | `smallint` | (description not yet updated on this server) | positive integer |
| `isolated` | `smallint` | Whether the point is isolated (not in a family parameterized by a P1 or abelian variety) | integer |
| `j_field` | `text` | (description not yet updated on this server) | text |
| `j_height` | `double precision` | The height of the j-invariant | floating-point approximation |
| `jinv` | `text` | (description not yet updated on this server) | text |
| `jorig` | `text` | A comma separated list of rationals giving coordinates of the j-invariant in the residue field, when not rational and... | text |
| `quo_info` | `smallint[]` | (description not yet updated on this server) | list of small integers |
| `residue_field` | `text` | (description not yet updated on this server) | text |
| `upload_id` | `bigint` | id for the row in data_uploads that added this point | integer |

---

## modcurve_points_old

**Rows:** 1,747,697

**API:** https://www.lmfdb.org/api/modcurve_points_old/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `Elabel` | `text` | If the GL2 subgroup does not contain -1, the label of the corresponding elliptic curve | text |
| `cm` | `smallint` | The CM discriminant of the point, or 0 if not CM | integer |
| `conductor_norm` | `bigint` | (description not yet updated on this server) | integer |
| `coordinates` | `jsonb` | (description not yet updated on this server) | JSON dict: keys are model type ints (as strings), values are lists of coordinate strings in the residue field basis |
| `curve_genus` | `integer` | (description not yet updated on this server) | integer |
| `curve_index` | `integer` | (description not yet updated on this server) | integer |
| `curve_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `curve_level` | `integer` | (description not yet updated on this server) | integer |
| `curve_name` | `text` | (description not yet updated on this server) | text |
| `cusp` | `boolean` | (description not yet updated on this server) | boolean |
| `degree` | `smallint` | The degree of the point | positive integer |
| `isolated` | `smallint` | Whether the point is isolated | integer |
| `j_field` | `text` | The minimal field containing the j-invariant | text |
| `j_height` | `double precision` | (description not yet updated on this server) | floating-point approximation |
| `jinv` | `text` | The j-invariant as as tring, comma separated coefficients of the power basis of the j_field | text |
| `jorig` | `text` | (description not yet updated on this server) | text |
| `quo_info` | `smallint[]` | A list of primes giving an Atkin-Lehner quotient | list of small integers |
| `residue_field` | `text` | The field of definition of the point | text |

---

## modcurve_teximages

**Rows:** 5,891

**API:** https://www.lmfdb.org/api/modcurve_teximages/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `image` | `text` | A `data:image/png;base64` encoded image of the rendered latex | text |
| `label` | `text` | The {{KNOWL('columns.gps_groups.tex_name', 'latex form')}} of the group | string label |

---
