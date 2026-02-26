# weil — Database Schema

**1 tables, 6 columns total**

### Tables

- [weil_basechange](#weil_basechange) (0 rows)

---

## weil_basechange

**Rows:** 0

**API:** https://www.lmfdb.org/api/weil_basechange/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `geometric_center_dim` | `smallint` | (description not yet updated on this server) | integer |
| `geometric_extension_degree` | `smallint` | (description not yet updated on this server) | integer |
| `is_primitive` | `boolean` | (description not yet updated on this server) | boolean |
| `label` | `text` | (description not yet updated on this server) | string label |
| `primitive_models` | `text[]` | (description not yet updated on this server) | list of strings |
| `twists` | `jsonb` | (description not yet updated on this server) | JSON list of [twist_label, base_change_label, extension_degree] triples (same format as av_fq_isog.twists) |

---
