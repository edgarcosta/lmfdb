# bmf — Database Schema

**3 tables, 54 columns total**

### Tables

- [bmf_dims](#bmf_dims) (456,188 rows)
- [bmf_forms](#bmf_forms) (233,333 rows)
- [bmf_test](#bmf_test) (185,800 rows)

---

## bmf_dims

Bianchi modular forms

**Rows:** 456,188

**API:** https://www.lmfdb.org/api/bmf_dims/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `field_absdisc` | `integer` | absolute value of field discriminant | integer |
| `field_label` | `text` | LMFDB label of base field | string label (cross-reference) |
| `gl2_cusp_totaldim` | `integer` | dimension of GL2 cuspforms | integer |
| `gl2_dims` | `jsonb` | Dictionary keyed by weight with values dictionaries holding the cuspidal and new dimensions for the GL(2) level | Dictionary keyed by weight with values dictionaries holding the cuspidal and new (JSON object) |
| `gl2_new_totaldim` | `integer` | dimension of GL2 newforms | integer |
| `label` | `text` | Full label of level (including base field) | string label |
| `level_label` | `text` | Level label (excluding base field) | string label (cross-reference) |
| `level_norm` | `bigint` | Level norm | integer |
| `sl2_cusp_totaldim` | `integer` | dimension of SL2 cuspforms | integer |
| `sl2_dims` | `jsonb` | Dictionary keyed by weight with values dictionaries holding the cuspidal and new dimensions for the SL(2) level | Dictionary keyed by weight with values dictionaries holding the cuspidal and new |
| `sl2_new_totaldim` | `integer` | dimension of SL2 newforms | integer |

---

## bmf_forms

Bianchi modular forms

**Rows:** 233,333

**API:** https://www.lmfdb.org/api/bmf_forms/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `AL_eigs` | `jsonb` | Atkin-Lehner eigenvalues | JSON list of Atkin-Lehner eigenvalues (+1 or -1, or string '?' if unknown), one per prime dividing the level |
| `CM` | `smallint` | Complex Multiplication flag:  a negative discriminant, or 0 if not CM | CM discriminant, 0 if no CM, or '?' if unknown |
| `Lratio` | `text` | L(F,1) divided by the real period | text |
| `bc` | `smallint` | Base change flag: d>0 if form is base change from Q with eigs in Q(sqrt(d)), 0 if not base-change | base change status: 0=no, +/-1=yes from Q, +/-n=twist of base change |
| `curve_status` | `smallint` | Elliptic curve existence status in {1,0,-1} | integer |
| `dimension` | `smallint` | dimension of the Galois orbit, i.e. degree of the Hecke eigenvalue field | dimension of eigenspace (1 for rational newforms) |
| `field_bad_primes` | `integer[]` | list of primes ramified in the base field | list of integers |
| `field_deg` | `smallint` | degree of base field | integer |
| `field_disc` | `smallint` | discriminant of base field | integer |
| `field_label` | `text` | LMFDB label of base field | imaginary quadratic field label (2.0.D.1) |
| `hecke_eigs` | `jsonb` | Hecke eigenvalues as integers or strings if not rational | JSON list of Hecke eigenvalues a_P for primes P ordered by norm. Integers for rational forms; polynomial strings in Hecke field generator for higher-dimensional forms. '?' if unknown |
| `hecke_poly` | `text` | Polynomial defining the Hecke field (x if rational) | text |
| `label` | `text` | Full label: field, level, suffix | BMF label: field_label-level_label-suffix |
| `label_nsuffix` | `smallint` | numerical version of label_suffix (1 for a, 2 for b etc) for sorting | integer |
| `label_suffix` | `text` | letter code label suffix | text |
| `level_bad_primes` | `integer[]` | list of primes dividing the level norm | list of integers |
| `level_gen` | `text` | generator of the level ideal | text |
| `level_ideal` | `text` | defining data of the level ideal | text |
| `level_label` | `text` | label of the level ideal | level ideal label |
| `level_norm` | `bigint` | level norm | norm of level ideal |
| `sfe` | `smallint` | Sign of functional equation | sign of functional equation: +1, -1, or '?' (unknown) |
| `short_label` | `text` | Short form of label (omitting field) | string label (cross-reference) |
| `weight` | `smallint` | weight | integer weight (parallel weight 2 for all currently stored) |

---

## bmf_test

**Rows:** 185,800

**API:** https://www.lmfdb.org/api/bmf_test/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `AL_eigs` | `jsonb` | (description not yet updated on this server) | JSON list of Atkin-Lehner eigenvalues (same as bmf_forms) |
| `CM` | `smallint` | (description not yet updated on this server) | integer |
| `Lratio` | `text` | (description not yet updated on this server) | text |
| `bc` | `smallint` | (description not yet updated on this server) | integer |
| `dimension` | `smallint` | (description not yet updated on this server) | non-negative integer |
| `field_deg` | `smallint` | (description not yet updated on this server) | integer |
| `field_disc` | `smallint` | (description not yet updated on this server) | integer |
| `field_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `hecke_eigs` | `jsonb` | (description not yet updated on this server) | JSON list of Hecke eigenvalues a_P (same as bmf_forms) |
| `hecke_poly` | `text` | (description not yet updated on this server) | text |
| `label` | `text` | (description not yet updated on this server) | string label |
| `label_nsuffix` | `smallint` | (description not yet updated on this server) | integer |
| `label_suffix` | `text` | (description not yet updated on this server) | text |
| `level_gen` | `text` | (description not yet updated on this server) | text |
| `level_ideal` | `text` | (description not yet updated on this server) | text |
| `level_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `level_norm` | `bigint` | (description not yet updated on this server) | integer |
| `sfe` | `smallint` | (description not yet updated on this server) | integer |
| `short_label` | `text` | (description not yet updated on this server) | string label (cross-reference) |
| `weight` | `smallint` | (description not yet updated on this server) | positive integer (weight) |

---
