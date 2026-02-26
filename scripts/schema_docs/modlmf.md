# modlmf — Database Schema

**1 tables, 16 columns total**

### Tables

- [modlmf_forms](#modlmf_forms) (264 rows)

---

## modlmf_forms

Mod-ell modular forms

**Rows:** 264

**API:** https://www.lmfdb.org/api/modlmf_forms/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `atkinlehner` | `jsonb` | [[int(p^e), int(W_{p^e})] for p^e exactly dividing N] | [[int(p^e), int(W_{p^e})] for p^e exactly dividing N] |
| `base_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `characteristic` | `smallint` | the characteristic of the base ring of the form | integer |
| `coeffs` | `jsonb` | coefficients of the q-expansion. The finite field where the coefficients belongs is represented using Conway polynomi... | polynomial coefficients |
| `cuspidal_lift` | `jsonb` | description of the characteristic zero cuspidal lift of smallest weight and smallest Galois orbit (alphabetical order... | description of the characteristic zero cuspidal lift of smallest weight and smal (JSON array) |
| `deg` | `smallint` | degree of base field over prime field | positive integer |
| `dirchar` | `text` | label of the mod ell Dirichlet character | text |
| `index` | `smallint` | (description not yet updated on this server) | integer |
| `label` | `text` | (description not yet updated on this server) | string label |
| `level` | `smallint` | minimal level of the form, that is the smallest level in which the eigenvalue system does occurr. If the associated r... | positive integer |
| `min_theta_weight` | `smallint` | minimum weight in a theta cycle | integer |
| `n_coeffs` | `integer` | the number of Fourier coefficients | integer |
| `ordinary` | `smallint` | 1 means ordinary | integer |
| `reducible` | `jsonb` | this means that the associated representation is reducible of the form    chi_1 cycl^a + chi_2 cycl^b, with a < b    ... | this means that the associated representation is reducible of the form    chi_1  |
| `theta_cycle` | `jsonb` | theta cycle, formattes as list of [weight, label of the Galois orbit] | theta cycle, formattes as list of [weight, label of the Galois orbit] (JSON array) |
| `weight_grading` | `smallint` | @@weight of the form modulo ell-1 | integer |

---
