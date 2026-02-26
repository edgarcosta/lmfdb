# halfmf — Database Schema

**1 tables, 8 columns total**

### Tables

- [halfmf_forms](#halfmf_forms) (3 rows)

---

## halfmf_forms

Half integral weight cuspforms spaces and Shimura decomposition

**Rows:** 3

**API:** https://www.lmfdb.org/api/halfmf_forms/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `character` | `text` | character label in the LMFDB notation | text |
| `dim` | `smallint` | dimension of the space | non-negative integer |
| `dimtheta` | `smallint` | dimension of the S0 subspace (see the shimura decomposition knowl http://beta.lmfdb.org/knowledge/show/mf.half_integr... | integer |
| `label` | `text` | LMFDB label | string label |
| `level` | `smallint` | Level | positive integer |
| `newpart` | `jsonb` | description of the subspace corresponding to the image of the shimura map. The entries of the dictionary contain the ... | description of the subspace corresponding to the image of the shimura map. The e (JSON array) |
| `thetas` | `jsonb` | label of the characters appearing in the S0 subspace | label of the characters appearing in the S0 subspace (JSON array) |
| `weight` | `smallint` | double of the weight of the forms | positive integer (weight) |

---
