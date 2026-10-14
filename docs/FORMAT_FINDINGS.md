# Format findings and unknowns

Checkpoint 001, requested October 13, 2026 (America/Denver).
Every claim below is either a source-code observation, a tool implementation
contract, or an explicitly open recovery task. No retail campaign payload was
available for a new field-level investigation in this pass.

## 1. Archive container: existing extraction contract

The reconstruction repository already contains `tools/extract_vv_gob.py`, blob
`c1d1d5701f5a3f7cbedf2dcfa52bc9eae50918d5`, at source baseline
`833379c9920403fdfcc9f460042ca1b7ff205808`.
Its format description attributes the GFC/GOB layout to Luigi Auriemma's
`over_the_hedge.bms`. This pass read the existing implementation. Attempts to
fetch the original BMS were unsuccessful; neither an independent BMS comparison
nor a new retail-archive validation is claimed.

The implemented GFC index contract uses big-endian unsigned 32-bit words.
Let B be block_count and F be file_count:

| Offset | Length | Interpretation used by the tool |
| --- | --- | --- |
| 0 | 4 | Magic `0x00008008` |
| 4 | 4 | Declared GOB length |
| 8 | 4 | B |
| 12 | 4 | F |
| 16 | 12*B | Block records: stored length, GOB offset, flags |
| 16+12*B | 4*B | Auxiliary words; preserved, not interpreted |
| 16+16*B | 12*F | File records: name hash, expanded length, first block |
| 16+16*B+12*F | 264*F | Name records: 256-byte name area plus 8 opaque bytes |

The minimum index size is `16 + 16*B + 276*F` bytes. Additional bytes are retained
as opaque tail data. Original name records are retained in hex; the decoded name
is the Latin-1 byte sequence before the first NUL. Empty names are not invented
or renamed automatically. Flags, auxiliary words, name-hash semantics, trailer
semantics and unconsumed tail bytes remain uninterpreted.

Each supported block begins with ASCII `STBL`, followed by a codec byte:
`z` consumes one complete zlib stream; `0` copies the stored body. Unknown codec
or envelope, incomplete streams, and trailing compressed-stream data are
rejected. The earlier extractor has a non-STBL heuristic branch; this new strict
tool deliberately does not implement it without separately established evidence.

Files begin at their first expanded block and consume the declared byte count
across successive blocks, matching the existing extractor's contract. The
manifest records every block contribution and unused final-block suffix. It
does not assert that such suffixes are padding, that block flags are irrelevant
to every title, or that corrupted record overlaps are semantically valid.

**Do not transfer the index's endianness to the map payload.** Container parsing,
block decompression and inner-map decoding are three different obligations.

## 2. PC destination: official reader contracts

Primary source: id Software's official DOOM-3 repository, commit
[`a9c49da5afb18201d31e3f0a429a037e56ce2b9a`](https://github.com/id-Software/DOOM-3/tree/a9c49da5afb18201d31e3f0a429a037e56ce2b9a).

[RenderWorld.h](https://github.com/id-Software/DOOM-3/blob/a9c49da5afb18201d31e3f0a429a037e56ce2b9a/neo/renderer/RenderWorld.h)
defines the PC render-world identifier `mapProcFile003`.
[RenderWorld_load.cpp](https://github.com/id-Software/DOOM-3/blob/a9c49da5afb18201d31e3f0a429a037e56ce2b9a/neo/renderer/RenderWorld_load.cpp)
contains separate readers for `model`, `shadowModel`, `interAreaPortals` and
`nodes`. A model surface identifies its material, vertex count and index count;
its vertex records have eight float components: XYZ, ST and normal XYZ.
Shadow records have their own cap-index counts and position layout. These are
**PC format facts**, not evidence of the Xbox stored layout.

[RenderWorld_local.h](https://github.com/id-Software/DOOM-3/blob/a9c49da5afb18201d31e3f0a429a037e56ce2b9a/neo/renderer/RenderWorld_local.h)
defines positive BSP children as node indices, zero as solid, and negative
children as `-1-areaNumber`. The loader's area entities look up `_areaN` render
models. The new parser checks references, required area models and cycles,
including unreachable cycles, before reporting a structurally decoded PROC.

[MapFile.cpp](https://github.com/id-Software/DOOM-3/blob/a9c49da5afb18201d31e3f0a429a037e56ce2b9a/neo/idlib/MapFile.cpp)
uses a separate MAP entity/brush/patch parser. It disables string-escape
interpretation for map strings. The new structural inspector retains raw
ordered epairs and exact primitive byte spans/hashes; it deliberately does not
emulate geometry construction, origin transforms, idDict duplicate handling,
entity inheritance or script execution. `decoded` remains false for this
partial MAP representation.

The new PROC parser is stricter than the complete engine lexer and should not
be advertised as accepting every file the engine accepts. Float values are
normalized to float32; structural comparisons retain signed-zero differences.
Order is retained, not canonicalized by geometric similarity.

## 3. Using converted multiplayer maps correctly

First establish provenance: the original Xbox MP file and the PC conversion
must represent the same map and revision. Record all known manual edits,
regeneration steps and replacement assets. Do not use a remake or a merely
similar map as a bit-exact reference.

The reference probe searches Xbox-candidate bytes for exact PC material strings
and float32 XYZ/eight-float vertex sequences, separately in both endians. It
records offsets, source vertex identity, pattern bytes and capped hit lists.
All-zero XYZ is excluded as weak evidence. A hit proves only that the bytes
occur. A miss does not prove absence: compression, quantization, swizzling,
packing, transforms or editing can defeat exact matching.

Promotion from a candidate to an established layout requires independent
constraints: a bounded record region, sensible counts and offsets, consistent
stride, valid index ranges, multiple distinct vertices/materials, known
transform rules, consumption accounting and confirmation from additional maps
or the actual Xbox reader. The official PC reader can suggest counterparts in
the retail executable; it is not a retail PDB or proof that structure layouts
match. This pass did not have the retail executable and resolved no such reader.

Keep MP evidence scoped to shared format elements. It does not establish co-op
triggers, second-player spawns, encounters, checkpoint logic or campaign transitions.

## 4. Open Xbox-map work

The inner file identifiers, versions, compression layers, field endianness,
vertex/index encoding, brush/patch representation, compiled collision, portal
ordering, navigation representation, entity serialization, script linkage and
campaign registry relationships are **unestablished by this checkpoint**.
No candidate offsets were obtained from actual Xbox maps. Do not fill these
unknowns from memory, guessed C structures, PC defaults or file extensions.

For each established field, record source hash, byte range, type, endian,
reader evidence, meaning, transformation, output location and counterexamples.
Retain unexplained spans. Separately label recovered editable source geometry,
recovered compiled geometry and newly reconstructed geometry; they are not
interchangeable forms of evidence.
