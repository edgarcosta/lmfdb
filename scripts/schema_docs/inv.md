# inv — Database Schema

**6 tables, 25 columns total**

### Tables

- [inv_dbs](#inv_dbs) (28 rows)
- [inv_fields_auto](#inv_fields_auto) (951 rows)
- [inv_fields_human](#inv_fields_human) (951 rows)
- [inv_ops](#inv_ops) (2 rows)
- [inv_rollback](#inv_rollback) (0 rows)
- [inv_tables](#inv_tables) (66 rows)

---

## inv_dbs

**Rows:** 28

**API:** https://www.lmfdb.org/api/inv_dbs/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `_id` | `integer` | (description not yet updated on this server) | integer |
| `name` | `text` | (description not yet updated on this server) | text |
| `nice_name` | `text` | (description not yet updated on this server) | text |

---

## inv_fields_auto

**Rows:** 951

**API:** https://www.lmfdb.org/api/inv_fields_auto/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `_id` | `integer` | (description not yet updated on this server) | integer |
| `cname` | `text` | (description not yet updated on this server) | text |
| `data` | `jsonb` | (description not yet updated on this server) | JSON object: auto-generated inventory data for the field (internal metadata) |
| `name` | `text` | (description not yet updated on this server) | text |
| `schema` | `text` | (description not yet updated on this server) | text |
| `table_id` | `integer` | (description not yet updated on this server) | integer |

---

## inv_fields_human

**Rows:** 951

**API:** https://www.lmfdb.org/api/inv_fields_human/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `_id` | `integer` | (description not yet updated on this server) | integer |
| `data` | `jsonb` | (description not yet updated on this server) | JSON object: human-curated inventory data for the field (internal metadata) |
| `name` | `text` | (description not yet updated on this server) | text |
| `table_id` | `integer` | (description not yet updated on this server) | integer |

---

## inv_ops

**Rows:** 2

**API:** https://www.lmfdb.org/api/inv_ops/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `content` | `jsonb` | (description not yet updated on this server) | JSON object: inventory operation content (internal metadata) |
| `isa` | `text` | (description not yet updated on this server) | text |
| `scan_date` | `timestamp without time zone` | (description not yet updated on this server) | timestamp (datetime) of last scan |

---

## inv_rollback

**Rows:** 0

**API:** https://www.lmfdb.org/api/inv_rollback/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `diff` | `jsonb` | (description not yet updated on this server) | JSON: diff for rollback operation (internal metadata) |

---

## inv_tables

**Rows:** 66

**API:** https://www.lmfdb.org/api/inv_tables/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `INFO` | `jsonb` | (description not yet updated on this server) | JSON object: aggregated inventory info (internal metadata) |
| `NOTES` | `jsonb` | (description not yet updated on this server) | JSON object: aggregated inventory notes (internal metadata) |
| `_id` | `integer` | (description not yet updated on this server) | integer |
| `db_id` | `integer` | (description not yet updated on this server) | integer |
| `name` | `text` | (description not yet updated on this server) | text |
| `nice_name` | `text` | (description not yet updated on this server) | text |
| `scan_date` | `timestamp without time zone` | (description not yet updated on this server) | timestamp (datetime) of last scan |
| `status` | `smallint` | (description not yet updated on this server) | integer |

---
