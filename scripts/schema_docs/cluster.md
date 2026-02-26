# cluster — Database Schema

**1 tables, 9 columns total**

### Tables

- [cluster_pictures](#cluster_pictures) (279 rows)

---

## cluster_pictures

**Rows:** 279

**API:** https://www.lmfdb.org/api/cluster_pictures/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `depth` | `text` | Depth of the cluster picture | text |
| `genus` | `smallint` | Genus of any curve having this cluster picture | non-negative integer (genus) |
| `image` | `text` | Encoding of a hi-res picture of the cluster picture | text |
| `label` | `text` | Label of the cluster picture | string label |
| `potential_good_jacobian_reduction` | `boolean` | Describes whether the Jacobian of any curve having this cluster picture has potentially good reduction | boolean |
| `potential_good_reduction` | `boolean` | Described whether a curve having this cluster picture has potentially good reduction | boolean |
| `potential_toric_rank` | `smallint` | Potential toric rank of the Jacobian of any curve having this cluster picture | integer |
| `size` | `smallint` | Number of points in the cluster picture | integer |
| `thumbnail` | `text` | Encoding of a lo-res thumbnail of the cluster picture | text |

---
