# data — Database Schema

**1 tables, 11 columns total**

### Tables

- [data_uploads](#data_uploads) (1 rows)

---

## data_uploads

Data uploads to certain tables, tracked through a verification and review process

**Rows:** 1

**API:** https://www.lmfdb.org/api/data_uploads/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `comment` | `text` | comment provided by reviewer or if upload is withdrawn | text |
| `data` | `jsonb` | dictionary holding the input data, as well as auxiliary columns computed during verification and processing that are ... | dictionary holding the input data, as well as auxiliary columns computed during  |
| `processed` | `timestamp without time zone` | timestamp when processing finished | timestamp (datetime) when processing finished |
| `reviewed` | `timestamp without time zone` | timestamp when reviewed | timestamp (datetime) when reviewed |
| `section` | `text` | a code for what kind of upload this is, determining which tables and columns are included | text |
| `status` | `smallint` | review status: -5=Withdrawn -4=Unexpected error -3=Processing failed -2=Negatively reviewed -1=Verification failed 0=... | integer |
| `submitted` | `timestamp without time zone` | timestamp initially submitted | timestamp (datetime) initially submitted |
| `submitter` | `text` | LMFDB username for the person who initially submitted the data | text |
| `updated` | `timestamp without time zone` | timestamp of most recent change | timestamp (datetime) of most recent change |
| `verified` | `timestamp without time zone` | timestamp when verification finished | timestamp (datetime) when verification finished |
| `version` | `smallint` | version number in case data format needs to change | integer |

---
