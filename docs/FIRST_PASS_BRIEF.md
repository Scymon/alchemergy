# First Pass Build Brief (for the coding agent)

You are building the **first playable pass** of Alchemergy, a merge-2 game. Read `docs/DESIGN.md` for the full vision; this brief is the exact scope. When done, open a PR into `main` and set the README status to `first-pass`. Claude reviews next, then AndroidBro continues.

## Hard constraints

- **Godot 4.x** (4.3 or newer), GDScript only, project at the **repo root** (`project.godot` at `/`).
- **Portrait mobile**: base viewport 720×1280, stretch mode `canvas_items`, aspect `expand`, orientation locked to portrait. Use the **Mobile** renderer (fallback-safe for Compatibility).
- **Data-driven**: never hard-code items. Load every `data/*.json` (except `summary.json`) at startup. Do not edit `data/` by hand; if data must change, change `tools/raw_items.txt` / `tools/build_data.py` and rerun `tools/validate.py`.
- **Scope: MVP tiers 1 to 6 only.** Items with `tier > 6` must never spawn or be produced; a merge whose result is tier > 6 is treated as "no recipe" (pieces spring back). Keep the code tier-agnostic so raising the cap later is a one-line change (`const MAX_TIER := 6` in `Db`).
- Placeholder art is fine: draw pieces procedurally (colored circle or rounded square per category, item short name or element symbol, tier badge). No external asset packs.
- No ads, IAP, analytics, or network calls in this pass.

## Suggested structure

```
project.godot
export_presets.cfg          # Android preset (see below)
scenes/Main.tscn            # scene switcher: Board <-> Codex
scenes/Board.tscn  scripts/board.gd
scenes/Piece.tscn  scripts/piece.gd
scenes/Generator.tscn scripts/generator.gd
scenes/Codex.tscn  scripts/codex.gd
scenes/fx/MergeBurst.tscn   # pooled one-shot particles
autoload/Db.gd              # item defs + pair lookup
autoload/GameState.gd       # board contents, discovered set, energy
autoload/SaveManager.gd
autoload/Fx.gd              # pooled particles, haptics, audio, shake
```

## Features

### 1. Item database (`Db`)
- Parse all JSON files into a Dictionary `id -> def`.
- Build the merge lookup: key = the two recipe ids sorted and joined with `|` (e.g. `"hydrogen|hydrogen"`), value = result id. Both identical (H + H) and cross merges (hydrogen + oxygen → water) go through this one lookup.
- `get_result(a, b) -> String` returns `""` when there is no recipe or the result exceeds `MAX_TIER`.

### 2. Merge board
- 7 columns × 9 rows grid of cells, sized to fit the portrait width with margins; top bar (energy, Codex button), bottom bar (generators).
- **Drag and drop** with touch and mouse: press a piece to pick it up, drag, release on a cell.
  - Empty cell: move there.
  - Occupied cell, valid recipe: merge. Both inputs are removed, the result appears in the target cell.
  - Occupied cell, no recipe: swap the two pieces.
  - Outside the board: spring back to the original cell.
- While dragging, highlight cells whose piece forms a valid merge with the held piece.

### 3. Three generators
- **Quantum Vent** spawns `hydrogen`, **Photon Lamp** spawns `photon`, **Neutron Source** spawns `neutron`.
- Tap: costs 1 energy, spawns the item into the nearest empty cell with a pop animation; if the board is full, shake the generator and refund.
- Energy: cap 100, regen 1 per 120 s, computed from Unix time so it also regenerates offline. Show energy and the time to the next point.
- Debug toggle (`OS.is_debug_build()` only): infinite energy, for testing deep chains.

### 4. Merge juice (the part that matters most)
Keep every merge animation under 0.35 s total.
- **Pickup**: tween scale to 1.1, slight tilt toward drag direction, raise `z_index`, grow a drop shadow.
- **Snap / spring back**: `Tween` with `TRANS_BACK`, `EASE_OUT`, about 0.12 s.
- **Squash and stretch**: inputs squash toward each other (scale x 1.2, y 0.8), result pops in from 0.6 to 1.15 and settles to 1.0 with `TRANS_ELASTIC`.
- **Flash and particles**: white flash on the result (shader uniform or `modulate`), plus a pooled `GPUParticles2D` one-shot burst whose `amount` and color scale with result tier (for example 12 + tier × 6, tinted by category). Pool at least 8 emitters; never instance during a merge. Fall back to `CPUParticles2D` on the Compatibility renderer.
- **Haptics**: `Input.vibrate_handheld(10)` on pickup, `(25)` on merge, `(60)` on a new discovery. A settings toggle disables them. Android export needs the VIBRATE permission.
- **Audio**: one pooled merge blip whose `pitch_scale` steps up a pentatonic scale for quick successive merges (combo resets after 1.5 s). A generated or CC0 placeholder sound is fine.
- **Screen shake**: small `Camera2D` trauma shake on tier 5+ results and stronger on `supernova` and `black_hole`.
- **Discovery**: the first time an item is made, show a toast or card with its name and `fact`, and add it to the codex.
- **Reduce motion** setting disables shake and flash.

### 5. Codex screen
- Scrollable grid of every item with `tier <= 6`, grouped by category tabs (Elements, Materials, Bestiary, Inventions, Space, Cosmic).
- Discovered items show name, tier, recipe (as names) and fact; undiscovered show a silhouette and "???".
- Header shows discovered / total counts. Elements may use a simple periodic-table layout (by atomic number) if time allows; a grid is acceptable.

### 6. Save / load
- JSON at `user://save.json`: `version`, board cells (id per cell or null), discovered ids, energy, last energy timestamp, settings.
- Autosave after every merge, spawn and move, and on `NOTIFICATION_APPLICATION_PAUSED` / `NOTIFICATION_WM_CLOSE_REQUEST`. Write to `save.tmp` then rename.
- On load, ignore unknown ids (data may change) and recompute offline energy.
- New game: the starting board holds 2 hydrogen and 1 photon.

### 7. Android export preset
- Commit `export_presets.cfg` with an **Android** preset: package `com.scymon.alchemergy`, name "Alchemergy", portrait, min SDK 24, target SDK per current Play requirements, VIBRATE permission, arm64-v8a (+ armeabi-v7a), Gradle build off for now. Export path `build/alchemergy.apk` (git-ignored).
- **No keystores or passwords in the repo.** Leave signing fields blank and document in the README how to set the debug keystore in Editor Settings.

## Out of scope
Orders, Stardust, Observatory, sectors, ads and IAP, final art, tiers 7 to 12, chain-reaction auto-merges, tier-up slow-mo, shaders beyond a simple flash and outline.

## Acceptance criteria
1. `godot --headless --path . --quit` opens the project with no script errors, on Godot 4.3+.
2. All items load from `data/*.json`; a startup log prints the item count (359) and the number of MVP items (`tier <= 6`).
3. `python3 tools/validate.py` still prints `PASS`.
4. In the editor at 720×1280 portrait: tapping each generator spawns its item and spends 1 energy; with 0 energy, a tap does nothing visible except a "no energy" shake.
5. Dragging hydrogen onto hydrogen makes helium; hydrogen + oxygen makes water; water + water (no recipe) swaps; a drop off-board springs back.
6. A merge whose result is tier > 6 (e.g. electricity + glass → light bulb) does not happen.
7. Every merge visibly squashes, pops, flashes and bursts particles, with bigger bursts for higher tiers; on an Android device it also vibrates.
8. The first creation of an item shows its fact and the item appears in the Codex; Codex counts update.
9. Kill and relaunch the app: board, discovered items and energy are restored, with offline regen applied.
10. Stays at 60 fps with a full board and repeated merges on desktop; no node instancing during merges (pooled FX).
11. The Android preset exists and exports a debug APK once export templates and the SDK are installed (documented in the README; CI not required).
12. Code is organized as above, with short comments on non-obvious logic, and the README has run and export instructions.
