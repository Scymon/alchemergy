# Alchemergy

**Merge the universe.** A merge-2 mobile game for Android (portrait), built in **Godot 4**. Start with a single proton, fuse your way through all 118 elements, mix materials, evolve life, invent tools up to AI and starships, build planets and stars, and collapse them into black holes, all the way to the Big Bang and the Multiverse. Visual target: Candy Crush clarity and payoff with Necromerger's tactile board.

## Status: `pre-first-pass`

Design and content data only. No Godot project yet.

## Repo layout

| Path | What |
|---|---|
| `docs/DESIGN.md` | Full game design doc (pitch, loop, tiers, generators, codex, game feel, monetization, tech plan, milestones) |
| `docs/FIRST_PASS_BRIEF.md` | Build brief for the first-pass coding agent |
| `data/*.json` | The 359-item merge graph: elements, materials, bestiary, inventions, space, cosmic, plus `summary.json` |
| `tools/build_data.py` | Regenerates `data/` from `tools/raw_items.txt` and the element rules |
| `tools/validate.py` | Checks every recipe input exists, every input pair is unique, and every item is reachable from Hydrogen, Photon and Neutron |

```sh
python3 tools/build_data.py   # rebuild data/
python3 tools/validate.py     # must print PASS
```

Item fields: `id, name, category, subcategory, tier, depth, recipe ([a, b] or null for bases), fact` (elements also carry `symbol, atomic_number`).

## How the bots collaborate

1. **Codex** builds the first pass: a playable Godot 4 MVP following `docs/FIRST_PASS_BRIEF.md`, on a branch with a PR.
2. **Claude** reviews and refines it: code quality, bugs, game feel, and alignment with `docs/DESIGN.md`.
3. **AndroidBro** (Dave's agent) takes it from there: Android builds, device testing, content waves, and further milestones.

Rules for every agent: work on branches and open PRs into `main`; run `tools/validate.py` after any data change; treat `data/*.json` as the source of truth for content; update the status line above when a phase finishes.

Fun facts have not been fact-checked against sources yet.
