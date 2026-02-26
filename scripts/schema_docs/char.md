# char — Database Schema

**2 tables, 26 columns total**

### Tables

- [char_dirichlet](#char_dirichlet) (562,396,733 rows)
- [char_orbits](#char_orbits) (21,045,332 rows)

---

## char_dirichlet

Dirichlet character orbits

**Rows:** 562,396,733

**API:** https://www.lmfdb.org/api/char_dirichlet/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `conductor` | `integer` | The {{KNOWL('character.dirichlet.conductor', 'conductor')}} of the {{KNOWL('character.dirichlet', 'Dirichlet characte... | positive integer |
| `degree` | `integer` | The {{KNOWL('character.dirichlet.degree', 'degree')}} of the {{KNOWL('character.dirichlet', 'Dirichlet characters')}}... | positive integer |
| `first` | `integer` | The {{KNOWL('character.dirichlet.conrey.index','Conrey index')}} $n$ of the first {{KNOWL('character.dirichlet', 'Dir... | integer |
| `is_even` | `boolean` | True if the {{KNOWL('character.dirichlet.parity', 'parity')}} of the {{KNOWL('character.dirichlet', 'Dirichlet charac... | boolean |
| `is_minimal` | `boolean` | True if the {{KNOWL('character.dirichlet', 'Dirichlet characters')}} in this {{KNOWL('character.dirichlet.galois_orbi... | boolean |
| `is_primitive` | `boolean` | True if the {{KNOWL('character.dirichlet', 'Dirichlet characters')}} in this {{KNOWL('character.dirichlet.galois_orbi... | boolean |
| `is_real` | `boolean` | True if the {{KNOWL('character.dirichlet', 'Dirichlet characters')}} in this {{KNOWL('character.dirichlet.galois_orbi... | boolean |
| `label` | `text` | The {{KNOWL('character.dirichlet.galois_orbit_label', 'label')}} of this {{KNOWL('character.dirichlet.galois_orbit', ... | string label |
| `last` | `integer` | The {{KNOWL('character.dirichlet.conrey.index','Conrey index')}} $n$ of the last {{KNOWL('character.dirichlet', 'Diri... | integer |
| `modulus` | `integer` | The {{KNOWL('character.dirichlet', 'modulus')}} of the {{KNOWL('character.dirichlet.modulus', 'Dirichlet characters')... | integer |
| `orbit` | `integer` | The ordinal $i\ge 1$ such this {{KNOWL('character.dirichlet.galois_orbit', 'orbit')}}  is the $i$th orbit of its modu... | integer |
| `order` | `integer` | The {{KNOWL('character.dirichlet.order', 'order')}} of the {{KNOWL('character.dirichlet', 'Dirichlet characters')}} i... | integer |
| `primitive_orbit` | `integer` | The ordinal $i\ge 1$ such that the {{KNOWL('character.dirichlet.galois_orbit', 'orbit')}} of the {{KNOWL('character.d... | integer |

---

## char_orbits

**Rows:** 21,045,332

**API:** https://www.lmfdb.org/api/char_orbits/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `conductor` | `integer` | The {{KNOWL('character.dirichlet.conductor', 'conductor')}} of the Dirichlet characters in this orbit. | positive integer |
| `degree` | `integer` | The {{KNOWL('character.dirichlet.degree', 'degree')}} of the {{KNOWL('character.dirichlet.value_field', 'field of val... | positive integer |
| `first_label` | `text` | The {{KNOWL('character.dirichlet.conrey','Conrey label')}} of the first {{KNOWL('character.dirichlet', 'Dirichlet cha... | string label (cross-reference) |
| `is_minimal` | `boolean` | True if the Dirichlet characters in this orbit are {{KNOWL('character.dirichlet.minimal', 'minimal')}}. | boolean |
| `is_primitive` | `boolean` | True if the {{KNOWL('character.dirichlets', 'Dirichlet character')}} in this orbit are {{KNOWL('character.dirichlet.p... | boolean |
| `is_real` | `boolean` | True if the {{KNOWL('character.dirichlet', 'Dirichlet characters')}} in this orbit are {{KNOWL('character.dirichlet.r... | boolean |
| `label` | `text` | The {{KNOWL('character.dirichlet.galois_orbit_label', 'label')}} of this {{KNOWL('character.dirichlet.galois_orbit', ... | string label |
| `last_label` | `text` | The {{KNOWL('character.dirichlet.conrey','Conrey label')}} of the last {{KNOWL('character.dirichlet', 'Dirichlet char... | string label (cross-reference) |
| `modulus` | `integer` | The {{KNOWL('character.dirichlet', 'modulus')}} of the {{KNOWL('character.dirichlet.modulus', 'Dirichlet characters')... | integer |
| `orbit_index` | `integer` | The index of this {{KNOWL('character.dirichlet.galois_orbit', 'orbit')}} among orbits of the same {{KNOWL('character.... | integer |
| `order` | `integer` | The {{KNOWL('character.dirichlet.order', 'order')}} of the {{KNOWL('character.dirichlet', 'Dirichlet characters')}} i... | integer |
| `parity` | `smallint` | The {{KNOWL('character.dirichlet.parity', 'parity')}} of the {{KNOWL('character.dirichlet', 'Dirichlet characters')}}... | integer |
| `primitive_label` | `text` | The {{KNOWL('character.dirichlet.galois_orbit_label', 'label')}} of the {{KNOWL('character.dirichlet.galois_orbit', '... | string label (cross-reference) |

---
