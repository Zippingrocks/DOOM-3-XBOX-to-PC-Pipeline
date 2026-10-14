# Format findings and unknowns


## Checkpoint 009 CM.X collision findings

Xbox CM.X is a compact little-endian serialization of runtime collision data.
The file begins with a model count. Each model carries its name, bounds,
contents, convex flag, vertices, 16-byte edges, a shared plane table, brushes,
polygons and a preorder BSP. Brush sides and polygons reference the shared
plane table. BSP nodes carry their original polygon/brush reference lists.
Internal edge normals, primitive numbers, aggregate allocation counters and
node references are runtime metadata; standard PC CM 1.00 text does not encode
all of them and reconstructs its caches from collision geometry plus BSP planes.

As with AAS.X, each packed plane stores internal `idPlane.d`. PC CM text stores
`idPlane::Dist() == -d`, so both polygon and brush plane distances must be
negated on export. Edge records accept two observed flag states (ordinary and
internal) and two observed reserved-field states (world/static and convex trace
models). The decoder rejects unknown flags, bad indices, unsafe names, malformed
node preorder, duplicate model names, non-finite values, truncation and trailing
bytes. Empty brush materials are legitimate in 258 extracted records because PC
CM brushes export numeric contents; no polygon material is empty.

A deterministic corpus audit parsed all 1,200 extracted CM.X members, representing
391 unique SHA-256 payloads and 66,076,100 stored bytes. Across all members it
validated 4,813 models, 428,453 vertices, 792,130 edges, 294,185 planes, 50,693
brushes, 356,793 polygons and 381,933 BSP nodes. Every collision primitive is
reachable from at least one Xbox BSP node, no node repeats a primitive reference,
and no bytes remain unconsumed. The corpus receipt SHA-256 is
`838535f1924ffa89f15bfbfb8397b705fe1178cc74ac01e88a46e6bbc974762f`;
its path-and-payload manifest digest is
`a4e1fd30551a26de22310c7c13085b527d9cd5e7fdbdeb35ef11a1791c3779ca`.

A separate export audit computes each paired converted MAP's geometry CRC using
the GPL `idMapFile::SetGeometryCRC` contract, expands the matching map CM.X
in memory and records the resulting PC CM hash without retaining licensed
outputs. All 20 co-op map CMs export: 43,791,272 CM.X bytes become 71,372,306
PC CM bytes across 3,633 models, 329,260 vertices, 562,201 edges, 50,435
brushes, 224,733 polygons and 182,879 nodes. The MAP/CM.X/output manifest digest
is `3a27835c398b2d5c9bd280a29c397efe47868ea965ae4d9f9900fa2755cf0603`;
the JSON receipt SHA-256 is
`af213e9f7825973f5e02920c00d65a2df2bc97a876dcfdf7d088295546340609`.

The first co-op segment's 2,003,187-byte CM.X has SHA-256
`bbfe12d231e229279757fe6b48fe13490cd0cc4dc6f7db44bd30f82c19b034a5`.
With the converted MAP geometry CRC `2410032894`, it expands to a
3,320,995-byte standard CM with SHA-256
`35a8ebff563a9d449995c02a90f1e822aa9dfeb42ec289b0128b8b1132cd8931`.
The PC engine loaded that file directly in 29 ms as 243 models, 15,146 vertices,
25,468 edges, 10,005 polygons, 2,784 brushes and 7,167 nodes, then spawned all
940 map entities and exited normally. The log SHA-256 is
`c56451c2e4bff8cbfc6185504baa9a98a08d71c8a16ea4bdeafe2eed09dd6d08`.

The PC loader reconstructed all 9,237 Xbox brush-node references. It constructed
21,999 polygon-node references versus 22,341 references stored in the packed
Xbox BSP. Reference-list placement is an acceleration structure rather than
collision geometry, but the difference prevents a claim of proven trace
equivalence. Matched trace sampling, movers/triggers, actor contacts and native
loading for the remaining maps are required before collision fidelity can be
accepted.

## Checkpoint 008 AAS plane serialization findings

Xbox AAS.X `xboxData` stores each plane as the engine's in-memory
`idPlane` vector `(a, b, c, d)`, whose signed side test is
`normal dot point + d`. Standard PC AAS text stores `idPlane::Dist()`,
which is `-d`; the PC loader reads that value through `SetDist` and restores
the internal fourth component as its negation. The original exporter copied the
packed fourth float directly into PC text, thereby reversing every nonzero BSP
plane distance when the PC engine loaded it.

The old offline route auditor had the complementary error: it treated the PC
text value as internal `d`. That made its point-to-area results appear correct
for the incorrectly exported files while the native engine returned area zero
for every diagnosed start and goal. The exporter now writes the negated packed
component, and the auditor evaluates textual planes as
`normal dot point - distance`. Nonzero-distance regression fixtures cover
both directions of the contract.

All 26 recovered AAS.X products were regenerated with the corrected
serialization. The campaign-port suite passes 116 tests. On
`xc_mars_city1_1`, the corrected AAS48 has SHA-256
`aa4448e1abca303022f6e4efa6c61ced42a0445781a522ec5385488b78821168`;
a true-COOP native run then loaded all 940 entities and produced zero AI path
warnings, zero failed point-to-area diagnostics and zero missing runtime
resources.

Three Xbox DEF files refer to inventory-icon images that are absent from both
the selected-map GFC and the shared `assets.gfc` inventory:
`guis/assets/hud/items/chaingun_ammo.tga`,
`guis/assets/hud/items/rocket_ammo.tga`, and
`guis/assets/hud/items/pda.tga`. Their Xbox gameplay definitions are retained.
The overlay generator comments only the matching `inv_icon` line in the exact
chaingun, rocket-launcher and PDA DEF paths, records each transform and leaves
unrelated definitions unchanged. The corrected native run has zero
missing-image warnings.

## Checkpoint 007 PC-host and HUD-format findings

The Xbox co-op HUD cannot call the stock PC executable's UI manager as though
the Xbox `idUserInterfaceManager` vtable were present. An exact-symbol
first-chance crash dump placed the invalid call in `idPlayer::DrawHUD`; the
target value was `0x3d3d3d3d`. The Xbox branch's `DrawText` virtual slot does
not exist at the same PC ABI position. The source-port solution sets
`xboxCoopStatusText` and `xboxCoopStatusVisible` on the existing player HUD
and lets the normal PC `Redraw` path render an injected status window. This is
a host-compatibility shim, not recovered map content.

The retail HUD uses four Xbox-only GUI script commands. For the PC host the
overlay generator applies these path-scoped translations:

| Xbox command | PC HUD state change |
| --- | --- |
| `HidePDAIcon` | hide `NewPDAVis`, `NEWPDAIcon` and `NEWPDA` |
| `ShowPDAIcon` | show `NEWPDAIcon` |
| `HideVidIcon` | hide `NewVidVis`, `NEWVidIcon` and `NEWVid` |
| `ShowVidIcon` | show `NEWVidIcon` |

The authenticated disc's `global.d3tfull` extent starts at byte
`2825555968`, is `178959016` bytes long, has magic `0xd574dcd2` and table
tag `0x83ac5c28`. Six selected missing HUD images establish three record-type
cases. `0x83f0` is DXT1, while `0x83f2` and `0x83f3` are DXT5. The
`0x83f3` conclusion is supported by valid decoded alpha/color output for
`TipBorder` and all three Xbox-Live icons, plus their retail material usage;
it is not a filename-only guess.

| Logical image | Type | DDS SHA-256 |
| --- | --- | --- |
| `guis/assets/health/hspike1` | `0x83f2` / DXT5 | `774c9836351afa1a83ad86fe3f1739c62ad5896a1509ac5f0098c78473d1517f` |
| `guis/assets/hud/TipBorder` | `0x83f3` / DXT5 | `a043d44ee341a95c002c92c617bcab5d43582a9beb53526087970fd6c6d8aa31` |
| `guis/assets/hud/Vote` | `0x83f0` / DXT1 | `7778109ee07668cb6fb26bc8f95cffa7ffd983a7009c75521e8ccc859b00f450` |
| `guis/live/assets/FriendInviteReceived` | `0x83f3` / DXT5 | `83f993881ce1735971dd5bd2951ff92679badca54c0e042685bd10f9e9bdc17d` |
| `guis/live/assets/FriendOnline` | `0x83f3` / DXT5 | `c51c85219f9477f8fccf7c4cbb2ba1346108d96af6b29773845c01e6871cb81e` |
| `guis/live/assets/GameInviteReceived` | `0x83f3` / DXT5 | `7c3d503a292b5326e45b474a46807c655e5ff4aecd3ef06c17722a21cce61de6` |

Xbox material declarations may contain a standalone `dxt5` storage hint that
the stock PC material parser does not recognize. The generated material closure
removes only that token from the five selected declarations. The referenced DDS
files still carry a DXT5 FourCC, so texture compression is not changed.

The final true-`COOP` native run has no missing-image, unknown-GUI-command or
unknown-material-token warning. Its five remaining AI warnings all have static
directed routes in the recovered AAS48: areas 849→793 (11 areas), 793→718
(14), 575→571 (6), 571→499 (10), and 55→4 (4). The discrepancy is therefore
between static graph connectivity and runtime nearest-area/bounds/obstacle
state; it is not evidence that those five reachability chains are absent.

## Checkpoint 005 runtime-format findings

Xbox MDV (`IDMD`) stores both meshes and animations. Mesh decoding uses the
serialized joint hierarchy and inverse bind transforms to reconstruct MD5
weights; influences are normalized only after rejecting bad joint/range data.
Animation decoding restores local transforms without inventing joints. On the
first-map dependency closure, 21 meshes and 234 animations decode. Xbox
MD5ANIM.X is a separate packed-track representation; 55 first-map files decode
after validating component spans, overlap and complete payload consumption.
Where the Xbox skeleton prunes an identity-only intermediate, retargeting
composes source world transforms onto the target parent hierarchy.

D3TFULL records use a keyed table and store Xbox DXT payloads without a PC DDS
container. The extractor resolves logical names, validates record extents and
emits DDS headers for established DXT1, DXT3 and DXT5 formats. Eight images
selected by the first-map HUD dependency ledger were decoded; this is not a
claim that every D3TFULL format code is known.

Xbox campaign audio resolution is a chain, not a filename lookup: XSND shader
metadata selects an INDEXLIST entry, which selects XSB cue/sound metadata and
then an XWB bank/wave entry. The established codec for the first-map selections
is Xbox IMA ADPCM. Eight required cues were decoded to PCM WAV with channel,
rate, encoded-byte and output-frame accounting. Duplicate PCM hashes are
retained when different logical sounds deliberately point to equivalent data.

Retail XBE inspection is read-only and maps file offsets through XBE virtual
sections. It supports ASCII references, direct address references, calls,
dwords and bounded x86 disassembly. Clean-room analysis of `idTurkeyPuncher`
established two 32-bit scores, network snapshots, a server activation event and
client GUI triggers. This behavioral contract was reconstructed in GPL source;
no executable bytes or disassembly are distributed.

The standard PC script compiler exposes a host mismatch in the first co-op
segment: one relay calls `test_trigger_relay`, another calls
`map_marscity1::test_trigger_relay`, and the segmented co-op script omits the
body. The matching Xbox solo script supplies the exact namespaced callback.
The runtime overlay restores that body and qualifies the unqualified reference,
recording both edits and their hashes.

The Xbox player MDV has 50 joints versus the stock PC body's 75. It retains
`loneckcontrol` but omits identity child `neckcontrol`; the two stock bind-world
transforms are identical. Using `loneckcontrol` as the `copy_joint` source for
the PC head removes the native warning without changing the recovered mesh.

Offline AAS route auditing starts at BSP node 1. Checkpoint 005 incorrectly
treated the fourth PC text component as the engine's internal `d`; the correct
text-side test is `normal dot point - distance`. That sign bug canceled the
original exporter's complementary mistake and made all five warned pairs appear
to have directed walk-only routes. Checkpoint 008 corrects both tools and
confirms the result in the native engine.

## Checkpoint 004 AAS.X findings

AAS.X begins with standard `DewmAAS "1.07"` text. Settings, areas and every
reachability remain textual. The standard geometry/topology arrays are omitted
from their normal positions and stored in one final `xboxData` binary block,
delimited by `# ` and ` #`.

The block is a sequence of little-endian uint32 counts and tightly specified
arrays in this order: planes (`float32[4]`, with the fourth float storing
internal `idPlane::d` and therefore negated when exported as PC text
distance), vertices (`float32[3]`), edges
(`int32[2]`), edgeIndex (`int32`), faces (`uint16 plane, uint16 flags, int32
numEdges, int32 firstEdge, int16 areas[2]`), faceIndex (`int32`), nodes
(`uint16 plane, two padding bytes, int32 children[2]`), portals (five int16
fields plus one uint16 cached travel-time field), portalIndex (`int32`) and
clusters (`int32 numAreas, numReachableAreas, numPortals, firstPortal`). The PC
text exporter restores the official field order where memory order differs.

The official GPL `idAASFileLocal::Load` accepts only the standard top-level
sections, so leaving `xboxData` in place is not PC-compatible. On the first map,
all eleven recovered section counts exactly equal independent PC `dmap` output,
and native Doom 3 successfully loaded the recovered AAS48. This establishes
parser compatibility, not AI route or co-op gameplay fidelity.

## Checkpoint 003 PROC.X findings

PROC.X retains `mapProcFile003` textual structure while replacing selected
arrays with `# ... #` binary records. Model-surface vertices are 24 bytes:
five little-endian float32 values (XYZ and ST) followed by one NV2A
`D3DVSDT_NORMPACKED3` word. The normal word stores signed X/Y/Z in 11/11/10
bits, normalized by 1023/1023/511 with the unused negative extrema clamped to
-1. Surface indices are little-endian uint16.

BSP nodes are 28 bytes: plane float32[4], child int32[2], then a zero int32
padding word. Shadow blocks begin with float32 minimum/maximum bounds, followed
by 8-byte vertices (`uint16 x,y,z,w`) and uint16 indices. XYZ reconstructs as
`minimum + q * (maximum-minimum) / 65535`; observed `w` values are 0 or 1 and
the PC textual shadow representation omits them.

Native PC regeneration independently confirms model identity, visible-surface
counts, index counts, area/portal graph and BSP node counts. Xbox shadow data is
more compact than PC regeneration and must remain comparison evidence rather
than being silently substituted when evaluating shadow fidelity.

## Checkpoint 002 retail findings

The retail XDVDFS volume descriptor is at byte `0x10000`, with 2,048-byte
sectors. Its root directory sector is 264 and its root table is 4,188 bytes.
Directory child links are little-endian 16-bit offsets in four-byte units;
extent sectors and sizes are little-endian 32-bit values.

The image contains 20 co-op archives whose names begin `xc_`. Their generated
map members use `.map.x`, `.proc.x`, `.cm.x` and one or more `.aas*.x` names.
MAP.X is a hybrid format: ordinary Version-2 MAP text surrounds `# ... #` binary
records. Brush-side records contain ten little-endian float32 values: four plane
values and two three-value texture rows. PatchDef2 records contain two float32
integer dimensions followed by width*height vertices of five float32 values.
PatchDef3 adds two float32 integer subdivision values before the same vertex
matrix. Rows are width-major and each row contains `height` vertices.

PROC.X is likewise hybrid text/binary and identifies itself as
`mapProcFile003`; CM.X begins with a binary collision representation; AAS.X is
text beginning `DewmAAS "1.07"`. These facts do not yet establish PC runtime
compatibility. The conversion milestone covers MAP.X only.

Authentic GOB blocks have `STBL`, a codec byte, the stored/zlib body, then the
four-byte footer `ENBL`. The exact footer is accepted and any other bytes after
the zlib stream remain an error. This supersedes checkpoint 001's statement
that all zlib unused data is rejected.

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

