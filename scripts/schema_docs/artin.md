# artin — Database Schema

**3 tables, 37 columns total**

### Tables

- [artin_field_data](#artin_field_data) (606,677 rows)
- [artin_old2new_labels](#artin_old2new_labels) (1,631,776 rows)
- [artin_reps](#artin_reps) (798,140 rows)

---

## artin_field_data

Artin representations

**Rows:** 606,677

**API:** https://www.lmfdb.org/api/artin_field_data/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `ArtinReps` | `jsonb` |  (list of pairs, [string, int]): the string is the baselabel of an entry from the Artin representation database, and ... | JSON: list of Artin representations arising from this field |
| `ComplexConjugation` | `smallint` | index for ConjClasses to say where complex conjugation lies | index of conjugacy class of complex conjugation |
| `ConjClasses` | `jsonb` | (list of dicts): for each conjugacy class of the group: its Order (int), Representative (list of ints giving a permut... | JSON: conjugacy class data (sizes, orders, representatives) |
| `FrobResolvents` | `jsonb` | (list of dicts): each entry gives information on how to compute the local factor for a prime via Dokchitser and Dokch... | JSON: Frobenius resolvent data |
| `Frobs` | `jsonb` | if the i-th entry is j, then the Frobenius for the i-th prime lies in the j-th conjugacy class | JSON: Frobenius conjugacy classes indexed by prime |
| `G-Gens` | `jsonb` | inner lists are permutations given as lists which generate the Galois group | Galois group generators (permutations) |
| `G-Name` | `text` | name for the Galois group, but we usually substitute a latex'ed name from the Galois group database, but this is a fa... | Galois group name string |
| `Polynomial` | `jsonb` | coefficients of a polynomial defining this field, the comma-separated list of coefficients as a string. This is the m... | defining polynomial of number field |
| `QpRts` | `jsonb` | each entry is a p-adic root, where entries in the list give the coefficients of powers of p in the p-adic approximati... | p-adic roots of defining polynomial |
| `QpRts-minpoly` | `jsonb` | coefficients for a defining polynomial over Qp used for explicitly writing roots. The first coefficient is the consta... | minimal polynomial for p-adic root computation |
| `QpRts-p` | `integer` | the prime p used for computing the roots p-adicly | prime p used for p-adic roots |
| `QpRts-prec` | `integer` | p-adic roots are computed up to (p^prec) | precision of p-adic root computation |
| `Size` | `numeric` | order of the Galois group | Galois group order |Gal(K/Q)| |
| `TransitiveDegree` | `smallint` | degree of the polynomial | degree of the number field [K:Q] |

---

## artin_old2new_labels

**Rows:** 1,631,776

**API:** https://www.lmfdb.org/api/artin_old2new_labels/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `new` | `text` | New (current) label for a representation | text |
| `old` | `text` | Old label for the same representation | text |

---

## artin_reps

Artin representations

**Rows:** 798,140

**API:** https://www.lmfdb.org/api/artin_reps/

| Column | Type | Description | Mathematical Type |
|--------|------|-------------|-------------------|
| `BadPrimes` | `jsonb` | list of bad primes, i.e., primes dividing the conductor. Stored as strings since they may get too big | ramified primes |
| `Baselabel` | `text` | label for the Galois orbit of the representation | base representation label (without GaloisConjugate suffix) |
| `CharacterField` | `smallint` | the n for writing the character | integer |
| `Conductor` | `numeric` | conductor | Artin conductor |
| `Container` | `text` | Smallest permutation representation which has this representation as a factor.  Permutation representations are order... | smallest permutation container nTt |
| `Dets` | `text[]` | A list of determinant characters in the same order as the Galois conjugates.  If the dimension is 1, it is the corres... | determinants of conjugate representations (character labels) |
| `Dim` | `smallint` | dimension | dimension of the representation |
| `GalConjSigns` | `jsonb` | A list of signs for the functional equation when we know they are 1 or -1, otherwise it gives 0.  The list is paralle... | signs for each Galois conjugate representation |
| `Galn` | `smallint` | the degree of the defining polynomial | integer |
| `GaloisConjugates` | `jsonb` | list of Galois conjugate character information.  Each entry in the GaloisConjugates list is a dictionary with the fol... | JSON: array of conjugate representations with local factors |
| `GaloisLabel` | `text` | Label for the Galois group of the defining polynomial | text |
| `Galt` | `integer` | t-number of Galois group of the defining polynomial | integer |
| `HardPrimes` | `jsonb` | primes dividing the polynomial discriminant for the defining field. These include the Bad Primes | primes where local computation is difficult |
| `Hide` | `smallint` | 0 if we should show it when searching for Artin rep'ns, 1 if not. The representations are invariants of the Galois cl... | integer |
| `Indicator` | `smallint` | Frobenius-Schur indicator, 1 for orthogonal, -1 for symplectic, and 0 for other | integer |
| `Is_Even` | `boolean` | The parity of the representation, true if even, false if odd | boolean, true if det(rho) is even (trivial on complex conjugation) |
| `NFGal` | `jsonb` | list of Galois conjugate character information | number field polynomial (defining the Galois closure) |
| `NumBadPrimes` | `smallint` | the number of ramified primes | integer |
| `Proj_GAP` | `integer[]` | GAP id of the projective quotient of the image | list of integers |
| `Proj_Polynomial` | `numeric[]` | coefficients of a minimal polredabs'ed defining polynomial for the corresponding projective representation | list of arbitrary-precision integers |
| `Proj_nTj` | `integer[]` | pair [n, t] for the Galois group of the polynomial for the projective representation | projective image in nTt notation |

---
