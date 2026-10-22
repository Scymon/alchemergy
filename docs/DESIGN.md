# Alchemergy: Game Design Doc

Game design doc for Dave's Android merge game in Godot 4: merge elements from hydrogen up to black holes. Draft v0.2, 21 Oct 2026: full 359-item merge graph.

Exported from the design doc Page: https://cursor.com/canvas/store-a647317d-418e-4617-a88f-63f6bca1e90c/2959b21d-b165-4fb1-9769-ff3baa375e2f

## Contents
Pitch · Reference: Necromerger · Core loop · Content summary · Item list · Tier map · Merge chain (v0.1 fusion ladder) · Generators and energy · Meta progression and codex · Visual style and game feel · Monetization · Godot 4 technical plan · MVP scope and milestones · Open questions

## Pitch

> Merge the universe: start with a single proton, fuse your way through the periodic table, build planets and stars, and collapse them into black holes.

| | |
|---|---|
| Genre | Merge-2 board puzzle, casual / mid-core |
| Platform | Android first (portrait), Godot 4.x |
| Hook | Real cosmic nucleosynthesis as a progression ladder; learn science by playing |
| Session | 3 to 10 minute sessions, energy-gated, with longer optional play |

## Reference: Necromerger

Necromerger (Glowmade, mobile + PC) is a merge-2 game with a dark-fantasy tone. The mechanics we borrow (written from memory, not yet verified):

- **Board**: Grid where two identical items merge into the next tier; space is the core tension.
- **Generators**: Tappable sources (gravestones, crypts) spawn base items; generators themselves merge into stronger versions.
- **Energy**: Each generator tap costs energy that regenerates over time; refills via play rewards or purchase.
- **Orders / quests**: Characters request specific items; delivering them pays currency, XP and unlocks new areas.
- **Chains**: Multiple parallel item chains that cross-feed, plus a collection book of every discovered item.

## Core loop

Spend Energy → Tap Generator (spawns H, He…) → Merge on board → Fill Orders (Observatory requests) → Rewards (Stardust, XP, energy) → Unlock (new chains, sectors, generators) → loop back to Spend Energy.

Discovery (first-time merges) fires a codex card with a real fact, the emotional payoff alongside order rewards.

## Content summary

| Category | Items |
|---|---|
| Elements | 120 |
| Materials | 60 |
| Bestiary | 57 |
| Inventions | 54 |
| Space | 24 |
| Cosmic | 44 |

359 items in one validated merge graph. Every recipe is two inputs, every input exists, no pair is reused, and everything is reachable from three base generators: Hydrogen, Photon and Neutron. Elements include all 118 plus the Photon and Neutron particles. Source of truth: `data/*.json`, built by `tools/build_data.py` and checked by `tools/validate.py`.

## Item list

(The Page has a searchable item browser; this is the full list.)

### Elements

| Item | Tier | Recipe | Fact |
|---|---|---|---|
| Photon | 1 | Base generator | Light quanta; the energy currency of Alchemergy. |
| Neutron | 1 | Base generator | Free neutrons decay in about 15 minutes. |
| Hydrogen (H 1) | 1 | Base generator | Makes up about 74% of the normal matter in the universe. |
| Helium (He 2) | 1 | Hydrogen (H 1) + Hydrogen (H 1) | Discovered in the Sun's spectrum before it was found on Earth. |
| Lithium (Li 3) | 1 | Helium (He 2) + Helium (He 2) | The lightest metal; it floats on water (and reacts with it). |
| Beryllium (Be 4) | 1 | Lithium (Li 3) + Helium (He 2) | Forged by nuclear fusion inside stars. |
| Boron (B 5) | 1 | Beryllium (Be 4) + Helium (He 2) | Forged by nuclear fusion inside stars. |
| Carbon (C 6) | 1 | Boron (B 5) + Helium (He 2) | Forms more compounds than any other element: the backbone of life. |
| Nitrogen (N 7) | 1 | Carbon (C 6) + Helium (He 2) | About 78% of Earth's air is nitrogen. |
| Oxygen (O 8) | 1 | Nitrogen (N 7) + Helium (He 2) | The third most abundant element in the universe. |
| Fluorine (F 9) | 1 | Oxygen (O 8) + Helium (He 2) | Forged by nuclear fusion inside stars. |
| Neon (Ne 10) | 1 | Fluorine (F 9) + Helium (He 2) | Glows red-orange in a discharge tube: the original neon sign. |
| Sodium (Na 11) | 2 | Neon (Ne 10) + Helium (He 2) | Soft enough to cut with a butter knife. |
| Magnesium (Mg 12) | 2 | Sodium (Na 11) + Helium (He 2) | Forged by nuclear fusion inside stars. |
| Aluminium (Al 13) | 2 | Magnesium (Mg 12) + Helium (He 2) | Forged by nuclear fusion inside stars. |
| Silicon (Si 14) | 2 | Aluminium (Al 13) + Helium (He 2) | The second most abundant element in Earth's crust. |
| Phosphorus (P 15) | 2 | Silicon (Si 14) + Helium (He 2) | Forged by nuclear fusion inside stars. |
| Sulfur (S 16) | 2 | Phosphorus (P 15) + Helium (He 2) | Forged by nuclear fusion inside stars. |
| Chlorine (Cl 17) | 2 | Sulfur (S 16) + Helium (He 2) | Forged by nuclear fusion inside stars. |
| Argon (Ar 18) | 2 | Chlorine (Cl 17) + Helium (He 2) | Forged by nuclear fusion inside stars. |
| Potassium (K 19) | 2 | Argon (Ar 18) + Helium (He 2) | Forged by nuclear fusion inside stars. |
| Calcium (Ca 20) | 2 | Potassium (K 19) + Helium (He 2) | Forged by nuclear fusion inside stars. |
| Scandium (Sc 21) | 2 | Calcium (Ca 20) + Helium (He 2) | Forged by nuclear fusion inside stars. |
| Titanium (Ti 22) | 2 | Scandium (Sc 21) + Helium (He 2) | Forged by nuclear fusion inside stars. |
| Vanadium (V 23) | 2 | Titanium (Ti 22) + Helium (He 2) | Forged by nuclear fusion inside stars. |
| Chromium (Cr 24) | 2 | Vanadium (V 23) + Helium (He 2) | Forged by nuclear fusion inside stars. |
| Manganese (Mn 25) | 2 | Chromium (Cr 24) + Helium (He 2) | Forged by nuclear fusion inside stars. |
| Iron (Fe 26) | 2 | Manganese (Mn 25) + Helium (He 2) | Fusion stops at iron: making heavier nuclei costs a star energy. |
| Cobalt (Co 27) | 4 | Iron (Fe 26) + Neutron | Built by slow neutron capture in aging giant stars. |
| Nickel (Ni 28) | 4 | Cobalt (Co 27) + Neutron | Built by slow neutron capture in aging giant stars. |
| Copper (Cu 29) | 4 | Nickel (Ni 28) + Neutron | One of the first metals humans worked, over 10,000 years ago. |
| Zinc (Zn 30) | 4 | Copper (Cu 29) + Neutron | Built by slow neutron capture in aging giant stars. |
| Gallium (Ga 31) | 4 | Zinc (Zn 30) + Neutron | Built by slow neutron capture in aging giant stars. |
| Germanium (Ge 32) | 4 | Gallium (Ga 31) + Neutron | Built by slow neutron capture in aging giant stars. |
| Arsenic (As 33) | 4 | Germanium (Ge 32) + Neutron | Built by slow neutron capture in aging giant stars. |
| Selenium (Se 34) | 4 | Arsenic (As 33) + Neutron | Built by slow neutron capture in aging giant stars. |
| Bromine (Br 35) | 4 | Selenium (Se 34) + Neutron | Built by slow neutron capture in aging giant stars. |
| Krypton (Kr 36) | 4 | Bromine (Br 35) + Neutron | Built by slow neutron capture in aging giant stars. |
| Rubidium (Rb 37) | 4 | Krypton (Kr 36) + Neutron | Built by slow neutron capture in aging giant stars. |
| Strontium (Sr 38) | 4 | Rubidium (Rb 37) + Neutron | Built by slow neutron capture in aging giant stars. |
| Yttrium (Y 39) | 4 | Strontium (Sr 38) + Neutron | Built by slow neutron capture in aging giant stars. |
| Zirconium (Zr 40) | 4 | Yttrium (Y 39) + Neutron | Built by slow neutron capture in aging giant stars. |
| Niobium (Nb 41) | 4 | Zirconium (Zr 40) + Neutron | Built by slow neutron capture in aging giant stars. |
| Molybdenum (Mo 42) | 4 | Niobium (Nb 41) + Neutron | Built by slow neutron capture in aging giant stars. |
| Technetium (Tc 43) | 9 | Molybdenum (Mo 42) + Neutron | The lightest element with no stable isotopes; first made artificially in 1937. |
| Ruthenium (Ru 44) | 4 | Technetium (Tc 43) + Neutron | Built by slow neutron capture in aging giant stars. |
| Rhodium (Rh 45) | 4 | Ruthenium (Ru 44) + Neutron | Built by slow neutron capture in aging giant stars. |
| Palladium (Pd 46) | 4 | Rhodium (Rh 45) + Neutron | Built by slow neutron capture in aging giant stars. |
| Silver (Ag 47) | 4 | Palladium (Pd 46) + Neutron | The best electrical conductor of all metals. |
| Cadmium (Cd 48) | 4 | Silver (Ag 47) + Neutron | Built by slow neutron capture in aging giant stars. |
| Indium (In 49) | 4 | Cadmium (Cd 48) + Neutron | Built by slow neutron capture in aging giant stars. |
| Tin (Sn 50) | 4 | Indium (In 49) + Neutron | Built by slow neutron capture in aging giant stars. |
| Antimony (Sb 51) | 4 | Tin (Sn 50) + Neutron | Built by slow neutron capture in aging giant stars. |
| Tellurium (Te 52) | 4 | Antimony (Sb 51) + Neutron | Built by slow neutron capture in aging giant stars. |
| Iodine (I 53) | 4 | Tellurium (Te 52) + Neutron | Built by slow neutron capture in aging giant stars. |
| Xenon (Xe 54) | 4 | Iodine (I 53) + Neutron | Used to power ion engines on spacecraft like Dawn. |
| Caesium (Cs 55) | 4 | Xenon (Xe 54) + Neutron | Built by slow neutron capture in aging giant stars. |
| Barium (Ba 56) | 4 | Caesium (Cs 55) + Neutron | Built by slow neutron capture in aging giant stars. |
| Lanthanum (La 57) | 4 | Barium (Ba 56) + Neutron | Built by slow neutron capture in aging giant stars. |
| Cerium (Ce 58) | 4 | Lanthanum (La 57) + Neutron | Built by slow neutron capture in aging giant stars. |
| Praseodymium (Pr 59) | 4 | Cerium (Ce 58) + Neutron | Built by slow neutron capture in aging giant stars. |
| Neodymium (Nd 60) | 4 | Praseodymium (Pr 59) + Neutron | Neodymium magnets are the strongest permanent magnets made. |
| Promethium (Pm 61) | 9 | Neodymium (Nd 60) + Neutron | Essentially absent from Earth's crust; all of it is radioactive. |
| Samarium (Sm 62) | 4 | Promethium (Pm 61) + Neutron | Built by slow neutron capture in aging giant stars. |
| Europium (Eu 63) | 6 | Samarium (Sm 62) + Supernova | Glows red in euro banknotes under UV light, a real anti-forgery feature. |
| Gadolinium (Gd 64) | 4 | Europium (Eu 63) + Neutron | Built by slow neutron capture in aging giant stars. |
| Terbium (Tb 65) | 4 | Gadolinium (Gd 64) + Neutron | Built by slow neutron capture in aging giant stars. |
| Dysprosium (Dy 66) | 4 | Terbium (Tb 65) + Neutron | Built by slow neutron capture in aging giant stars. |
| Holmium (Ho 67) | 4 | Dysprosium (Dy 66) + Neutron | Built by slow neutron capture in aging giant stars. |
| Erbium (Er 68) | 4 | Holmium (Ho 67) + Neutron | Built by slow neutron capture in aging giant stars. |
| Thulium (Tm 69) | 4 | Erbium (Er 68) + Neutron | Built by slow neutron capture in aging giant stars. |
| Ytterbium (Yb 70) | 4 | Thulium (Tm 69) + Neutron | Built by slow neutron capture in aging giant stars. |
| Lutetium (Lu 71) | 4 | Ytterbium (Yb 70) + Neutron | Built by slow neutron capture in aging giant stars. |
| Hafnium (Hf 72) | 4 | Lutetium (Lu 71) + Neutron | Built by slow neutron capture in aging giant stars. |
| Tantalum (Ta 73) | 4 | Hafnium (Hf 72) + Neutron | Built by slow neutron capture in aging giant stars. |
| Tungsten (W 74) | 4 | Tantalum (Ta 73) + Neutron | Highest melting point of any metal: 3,422 °C. |
| Rhenium (Re 75) | 4 | Tungsten (W 74) + Neutron | Built by slow neutron capture in aging giant stars. |
| Osmium (Os 76) | 6 | Rhenium (Re 75) + Supernova | The densest naturally occurring element. |
| Iridium (Ir 77) | 6 | Osmium (Os 76) + Supernova | Forged in supernovae and neutron-star mergers (r-process). |
| Platinum (Pt 78) | 6 | Iridium (Ir 77) + Supernova | So unreactive it was used for the international kilogram standard alloy. |
| Gold (Au 79) | 6 | Platinum (Pt 78) + Supernova | Much of Earth's gold was forged in neutron-star collisions. |
| Mercury (Hg 80) | 4 | Gold (Au 79) + Neutron | The only metal that is liquid at room temperature. |
| Thallium (Tl 81) | 4 | Mercury (Hg 80) + Neutron | Built by slow neutron capture in aging giant stars. |
| Lead (Pb 82) | 4 | Thallium (Tl 81) + Neutron | Romans used it for water pipes; 'plumbing' comes from 'plumbum'. |
| Bismuth (Bi 83) | 4 | Lead (Pb 82) + Neutron | Technically radioactive, with a half-life a billion times the universe's age. |
| Polonium (Po 84) | 6 | Bismuth (Bi 83) + Supernova | Discovered by Marie and Pierre Curie, named after Poland. |
| Astatine (At 85) | 6 | Polonium (Po 84) + Supernova | Forged in supernovae and neutron-star mergers (r-process). |
| Radon (Rn 86) | 6 | Astatine (At 85) + Supernova | Forged in supernovae and neutron-star mergers (r-process). |
| Francium (Fr 87) | 6 | Radon (Rn 86) + Supernova | Forged in supernovae and neutron-star mergers (r-process). |
| Radium (Ra 88) | 6 | Francium (Fr 87) + Supernova | Forged in supernovae and neutron-star mergers (r-process). |
| Actinium (Ac 89) | 6 | Radium (Ra 88) + Supernova | Forged in supernovae and neutron-star mergers (r-process). |
| Thorium (Th 90) | 6 | Actinium (Ac 89) + Supernova | Forged in supernovae and neutron-star mergers (r-process). |
| Protactinium (Pa 91) | 6 | Thorium (Th 90) + Supernova | Forged in supernovae and neutron-star mergers (r-process). |
| Uranium (U 92) | 6 | Protactinium (Pa 91) + Supernova | The heaviest element found in significant amounts in nature. |
| Neptunium (Np 93) | 6 | Uranium (U 92) + Supernova | Forged in supernovae and neutron-star mergers (r-process). |
| Plutonium (Pu 94) | 6 | Neptunium (Np 93) + Supernova | Powers RTGs on deep-space probes like Voyager and Curiosity. |
| Americium (Am 95) | 9 | Plutonium (Pu 94) + Particle Accelerator | Only made artificially in reactors or particle accelerators. |
| Curium (Cm 96) | 9 | Americium (Am 95) + Particle Accelerator | Only made artificially in reactors or particle accelerators. |
| Berkelium (Bk 97) | 9 | Curium (Cm 96) + Particle Accelerator | Only made artificially in reactors or particle accelerators. |
| Californium (Cf 98) | 9 | Berkelium (Bk 97) + Particle Accelerator | Only made artificially in reactors or particle accelerators. |
| Einsteinium (Es 99) | 9 | Californium (Cf 98) + Particle Accelerator | First found in the debris of the first hydrogen bomb test. |
| Fermium (Fm 100) | 9 | Einsteinium (Es 99) + Particle Accelerator | Only made artificially in reactors or particle accelerators. |
| Mendelevium (Md 101) | 9 | Fermium (Fm 100) + Particle Accelerator | Only made artificially in reactors or particle accelerators. |
| Nobelium (No 102) | 9 | Mendelevium (Md 101) + Particle Accelerator | Only made artificially in reactors or particle accelerators. |
| Lawrencium (Lr 103) | 9 | Nobelium (No 102) + Particle Accelerator | Only made artificially in reactors or particle accelerators. |
| Rutherfordium (Rf 104) | 9 | Lawrencium (Lr 103) + Particle Accelerator | Only made artificially in reactors or particle accelerators. |
| Dubnium (Db 105) | 9 | Rutherfordium (Rf 104) + Particle Accelerator | Only made artificially in reactors or particle accelerators. |
| Seaborgium (Sg 106) | 9 | Dubnium (Db 105) + Particle Accelerator | Only made artificially in reactors or particle accelerators. |
| Bohrium (Bh 107) | 9 | Seaborgium (Sg 106) + Particle Accelerator | Only made artificially in reactors or particle accelerators. |
| Hassium (Hs 108) | 9 | Bohrium (Bh 107) + Particle Accelerator | Only made artificially in reactors or particle accelerators. |
| Meitnerium (Mt 109) | 9 | Hassium (Hs 108) + Particle Accelerator | Only made artificially in reactors or particle accelerators. |
| Darmstadtium (Ds 110) | 9 | Meitnerium (Mt 109) + Particle Accelerator | Only made artificially in reactors or particle accelerators. |
| Roentgenium (Rg 111) | 9 | Darmstadtium (Ds 110) + Particle Accelerator | Only made artificially in reactors or particle accelerators. |
| Copernicium (Cn 112) | 9 | Roentgenium (Rg 111) + Particle Accelerator | Only made artificially in reactors or particle accelerators. |
| Nihonium (Nh 113) | 9 | Copernicium (Cn 112) + Particle Accelerator | Only made artificially in reactors or particle accelerators. |
| Flerovium (Fl 114) | 9 | Nihonium (Nh 113) + Particle Accelerator | Only made artificially in reactors or particle accelerators. |
| Moscovium (Mc 115) | 9 | Flerovium (Fl 114) + Particle Accelerator | Only made artificially in reactors or particle accelerators. |
| Livermorium (Lv 116) | 9 | Moscovium (Mc 115) + Particle Accelerator | Only made artificially in reactors or particle accelerators. |
| Tennessine (Ts 117) | 9 | Livermorium (Lv 116) + Particle Accelerator | Only made artificially in reactors or particle accelerators. |
| Oganesson (Og 118) | 9 | Tennessine (Ts 117) + Particle Accelerator | The heaviest element known; only a handful of atoms ever made. |

### Materials

| Item | Tier | Recipe | Fact |
|---|---|---|---|
| Water | 2 | Hydrogen (H 1) + Oxygen (O 8) | Expands about 9% when it freezes. |
| Salt | 2 | Sodium (Na 11) + Chlorine (Cl 17) | Two dangerous elements, one tasty crystal. |
| Carbon Dioxide | 2 | Carbon (C 6) + Oxygen (O 8) | Plants breathe it in to build sugar. |
| Methane | 2 | Carbon (C 6) + Hydrogen (H 1) | Main ingredient of natural gas; also found on Titan. |
| Ammonia | 2 | Nitrogen (N 7) + Water | The Haber process to make it feeds half of humanity. |
| Ozone | 2 | Oxygen (O 8) + Oxygen (O 8) | A thin layer of it shields Earth from UV. |
| Hydrogen Peroxide | 2 | Water + Oxygen (O 8) | Used as rocket propellant in the 1940s. |
| Silica | 2 | Silicon (Si 14) + Oxygen (O 8) | The most common mineral family in Earth's crust. |
| Quartz | 2 | Silica + Silica | Quartz crystals keep time in most watches. |
| Sand | 2 | Quartz + Water | Desert sand is too round for good concrete. |
| Clay | 2 | Sand + Water | Humans fired clay figurines 26,000 years ago. |
| Feldspar | 2 | Silica + Aluminium (Al 13) | About half of Earth's crust is feldspar. |
| Mica | 2 | Silica + Potassium (K 19) | Splits into sheets thin enough to see through. |
| Granite | 2 | Quartz + Feldspar | Continents are largely built on granite. |
| Corundum | 2 | Aluminium (Al 13) + Oxygen (O 8) | Second only to diamond in hardness among natural minerals. |
| Ruby | 2 | Corundum + Chromium (Cr 24) | The first laser, in 1960, used a ruby crystal. |
| Sapphire | 2 | Corundum + Titanium (Ti 22) | Sapphire comes in every color except red. |
| Emerald | 2 | Beryllium (Be 4) + Silica | Its green comes from traces of chromium. |
| Graphite | 2 | Carbon (C 6) + Carbon (C 6) | Pencil 'lead' is actually graphite. |
| Diamond | 2 | Graphite + Graphite | Forms 150 km deep under enormous pressure. |
| Graphene | 7 | Graphite + Electricity | One atom thick and about 200x stronger than steel. |
| Rust (Iron Oxide) | 2 | Iron (Fe 26) + Oxygen (O 8) | Makes Mars red. |
| Magnetite | 2 | Rust (Iron Oxide) + Iron (Fe 26) | Natural lodestones are magnetized magnetite. |
| Limestone | 2 | Calcium (Ca 20) + Carbon Dioxide | Often made of ancient seashells. |
| Quicklime | 5 | Limestone + Fire | Gets hot enough to boil water when wetted. |
| Cement | 5 | Quicklime + Clay | Roman concrete still stands after 2,000 years. |
| Concrete | 5 | Cement + Sand | The most used material on Earth after water. |
| Glass | 5 | Sand + Fire | Natural glass forms when lightning strikes sand. |
| Steel | 3 | Iron (Fe 26) + Carbon (C 6) | Just ~1% carbon makes iron far stronger. |
| Stainless Steel | 3 | Steel + Chromium (Cr 24) | Chromium forms a self-healing oxide skin. |
| Bronze | 4 | Copper (Cu 29) + Tin (Sn 50) | Gave its name to an entire age. |
| Brass | 4 | Copper (Cu 29) + Zinc (Zn 30) | Used for doorknobs partly because it kills microbes. |
| Pewter | 4 | Tin (Sn 50) + Lead (Pb 82) | Modern pewter is lead-free. |
| Solder | 4 | Tin (Sn 50) + Silver (Ag 47) | Holds every circuit board together. |
| Electrum | 6 | Gold (Au 79) + Silver (Ag 47) | The first coins, from Lydia, were electrum. |
| Titanium Alloy | 3 | Titanium (Ti 22) + Aluminium (Al 13) | Jet engines and rockets rely on it. |
| Neodymium Magnet | 4 | Iron (Fe 26) + Neodymium (Nd 60) | Can lift over 1,000 times its own weight. |
| YBCO Superconductor | 4 | Yttrium (Y 39) + Barium (Ba 56) | Carries current with zero resistance when cold. |
| Sulfuric Acid | 2 | Sulfur (S 16) + Water | The most produced industrial chemical. |
| Nitric Acid | 2 | Ammonia + Oxygen (O 8) | Key to fertilizers and explosives. |
| Hydrochloric Acid | 2 | Chlorine (Cl 17) + Hydrogen (H 1) | Your stomach makes it. |
| Saltpeter | 2 | Potassium (K 19) + Nitric Acid | Once scraped from cave walls for gunpowder. |
| Charcoal | 5 | Wood + Fire | Nearly pure carbon. |
| Gunpowder | 5 | Saltpeter + Charcoal | Invented by Chinese alchemists seeking immortality. |
| Sugar | 2 | Carbon (C 6) + Water | Glucose is the fuel of nearly all cells. |
| Ethylene | 2 | Methane + Methane | Plants use it as a ripening hormone. |
| Benzene | 2 | Ethylene + Methane | Kekulé said he dreamed of its ring shape. |
| Polyethylene | 4 | Ethylene + Ethylene | The world's most common plastic. |
| Nylon | 4 | Ammonia + Ethylene | First sold as toothbrush bristles in 1938. |
| Kevlar | 4 | Nylon + Benzene | Five times stronger than steel by weight. |
| Silicone | 4 | Silicon (Si 14) + Methane | Stays flexible from -50 to 200 °C. |
| Latex | 5 | Rubber Tree + Rubber Tree | Milky sap that drips from rubber trees. |
| Vulcanized Rubber | 5 | Latex + Sulfur (S 16) | Goodyear discovered vulcanization by accident. |
| Paper | 5 | Wood + Water | Invented in China around 100 CE. |
| Crude Oil | 5 | Plankton + Sand | Mostly ancient marine plankton, not dinosaurs. |
| Petrol | 5 | Crude Oil + Fire | Refined by heating and distilling crude oil. |
| Doped Silicon | 3 | Silicon (Si 14) + Phosphorus (P 15) | A few impurity atoms per million transform silicon. |
| Enriched Uranium | 8 | Uranium (U 92) + Centrifuge | Reactor fuel is only ~4% U-235. |
| Optical Fiber | 8 | Glass + Laser | Carries most of the internet as light. |
| Carbon Nanotube | 7 | Graphene + Graphene | Rolled graphene: the dream cable for a space elevator. |

### Bestiary

| Item | Tier | Recipe | Fact |
|---|---|---|---|
| Amino Acid | 3 | Ammonia + Methane | Found in meteorites and made in the Miller-Urey experiment. |
| Nucleotide | 3 | Phosphorus (P 15) + Sugar | The letters of the genetic code. |
| Lipid | 3 | Methane + Water | Self-assembles into bubbles: the first cell walls. |
| Protein | 3 | Amino Acid + Amino Acid | Your body has tens of thousands of kinds. |
| RNA | 3 | Nucleotide + Nucleotide | Can store information and catalyze reactions. |
| DNA | 3 | RNA + Protein | About 2 meters of it in every human cell. |
| Primordial Soup | 3 | Amino Acid + Water | Darwin imagined life starting in a 'warm little pond'. |
| Protocell | 4 | Lipid + RNA | A membrane bubble holding self-copying molecules. |
| Bacterium | 4 | Protocell + DNA | You carry about as many bacterial cells as human cells. |
| Archaea | 4 | Bacterium + Methane | Some thrive in boiling acid springs. |
| Cyanobacteria | 4 | Bacterium + Photon | Filled Earth's air with oxygen. |
| Eukaryote | 4 | Bacterium + Archaea | Born when one microbe engulfed another. |
| Algae | 5 | Eukaryote + Photon | Produce about half of Earth's oxygen. |
| Plankton | 5 | Algae + Water | Name means 'drifter' in Greek. |
| Fungus | 4 | Eukaryote + Sugar | Closer relatives of animals than of plants. |
| Lichen | 5 | Fungus + Algae | A partnership that can survive in space. |
| Moss | 5 | Algae + Clay | Among the first plants on land. |
| Soil | 5 | Sand + Fungus | A handful holds more microbes than people on Earth. |
| Fern | 5 | Moss + Water | Ferns predate dinosaurs. |
| Tree | 5 | Fern + Soil | There are about 3 trillion trees on Earth. |
| Wood | 5 | Tree + Tree | Made largely of cellulose and lignin. |
| Rubber Tree | 5 | Tree + Water | Native to the Amazon basin. |
| Grass | 5 | Moss + Soil | Grasses evolved alongside dinosaurs. |
| Flower | 5 | Fern + Sugar | Flowers appeared about 130 million years ago. |
| Fruit | 5 | Flower + Water | Evolved to get animals to spread seeds. |
| Wheat | 5 | Grass + Photon | Domesticated about 10,000 years ago. |
| Sponge | 6 | Eukaryote + Silica | Possibly the oldest animal lineage. |
| Jellyfish | 6 | Plankton + Protein | One species is biologically immortal. |
| Worm | 6 | Eukaryote + Soil | Darwin wrote a whole book on earthworms. |
| Fish | 6 | Worm + Water | More species than all other vertebrates combined. |
| Shark | 6 | Fish + Fish | Older than trees. |
| Insect | 6 | Worm + Grass | About 10 quintillion alive at any time. |
| Bee | 6 | Insect + Flower | Bees dance to share directions. |
| Butterfly | 6 | Insect + Fruit | Tastes with its feet. |
| Spider | 6 | Insect + Insect | Spider silk rivals steel in strength. |
| Frog | 6 | Fish + Moss | Some frogs freeze solid and thaw in spring. |
| Lizard | 6 | Frog + Sand | Some lizards can run on water. |
| Dinosaur | 6 | Lizard + Lizard | Ruled the Earth for about 165 million years. |
| Bird | 6 | Dinosaur + Insect | Birds are living dinosaurs. |
| Early Mammal | 6 | Lizard + Fruit | Early mammals were small and nocturnal. |
| Horse | 6 | Early Mammal + Grass | Can sleep standing up. |
| Whale | 6 | Early Mammal + Fish | Blue whales are the largest animals ever. |
| Wolf | 6 | Early Mammal + Early Mammal | Every dog descends from wolves. |
| Primate | 6 | Early Mammal + Tree | Forward-facing eyes for judging jumps between branches. |
| Human | 6 | Primate + Fire | Cooking may have helped grow our big brains. |
| Alchemical Slime | 7 | Protocell + Mercury (Hg 80) | The alchemists' prima materia, given life. |
| Homunculus | 7 | Human + Mercury (Hg 80) | Paracelsus claimed a recipe for a tiny artificial man. |
| Golem | 7 | Clay + Human | A clay guardian from Jewish folklore. |
| Fire Salamander | 7 | Lizard + Fire | Alchemists' elemental spirit of fire. |
| Phoenix | 7 | Bird + Fire | Reborn from its own ashes. |
| Dragon | 7 | Dinosaur + Fire | Dinosaur fossils may have inspired dragon myths. |
| Unicorn | 7 | Horse + Diamond | Narwhal tusks were once sold as unicorn horns. |
| Hippogriff | 7 | Bird + Horse | Half eagle, half horse. |
| Kraken | 7 | Jellyfish + Whale | Possibly inspired by giant squid. |
| Philosopher's Stone | 7 | Gold (Au 79) + Homunculus | The alchemists' ultimate goal: turning lead to gold. |
| Star Whale | 7 | Whale + Nebula | A leviathan that swims between stars. |
| Void Wyrm | 7 | Dragon + Black Hole | Devours light itself. |

### Inventions

| Item | Tier | Recipe | Fact |
|---|---|---|---|
| Fire | 5 | Wood + Oxygen (O 8) | Humans controlled fire at least 400,000 years ago. |
| Stone Tool | 5 | Granite + Wood | Stone tools are over 3.3 million years old. |
| Spear | 5 | Stone Tool + Rope | One of the oldest hunting tools. |
| Rope | 5 | Grass + Grass | Neanderthals twisted fibers into cord. |
| Wheel | 5 | Wood + Stone Tool | Used for pottery before carts. |
| Pottery | 5 | Clay + Fire | Older than farming in East Asia. |
| Kiln | 5 | Pottery + Fire | Reached temperatures that enabled metal smelting. |
| Agriculture | 5 | Wheat + Soil | Changed humans from foragers to farmers. |
| Bread | 5 | Wheat + Fire | Older than agriculture itself. |
| Boat | 5 | Wood + Rope | Humans reached Australia by boat 50,000+ years ago. |
| Writing | 5 | Clay + Stone Tool | Cuneiform began as tallies on clay. |
| Book | 6 | Paper + Writing | The codex replaced scrolls in late antiquity. |
| Forge | 5 | Kiln + Charcoal | Blacksmiths shaped the Iron Age. |
| Bronze Sword | 5 | Bronze + Stone Tool | A Bronze Age high-tech weapon. |
| Iron Tools | 5 | Iron (Fe 26) + Forge | Iron was cheaper and more plentiful than bronze. |
| Compass | 6 | Magnetite + Wood | First used in China for divination. |
| Printing Press | 6 | Paper + Iron Tools | Gutenberg's press sped up the spread of knowledge. |
| Cannon | 6 | Gunpowder + Bronze | Bronze cannon were common for centuries. |
| Lens | 6 | Glass + Glass | Eyeglasses appeared in Italy around 1290. |
| Telescope | 6 | Lens + Brass | Galileo saw Jupiter's moons in 1610. |
| Microscope | 6 | Lens + Bacterium | Van Leeuwenhoek first saw bacteria in 1676. |
| Gear | 6 | Brass + Wheel | The Antikythera mechanism had dozens of gears. |
| Clock | 6 | Gear + Gear | Marine clocks solved the longitude problem. |
| Steam Engine | 7 | Steel + Water | Powered the Industrial Revolution. |
| Locomotive | 7 | Steam Engine + Wheel | Standardized time zones were invented for railways. |
| Factory | 7 | Steam Engine + Gear | Mass production reshaped society. |
| Electricity | 7 | Copper (Cu 29) + Magnetite | Faraday made the first generator in 1831. |
| Battery | 7 | Electricity + Sulfuric Acid | Volta stacked metal discs into the first battery. |
| Lithium Battery | 8 | Battery + Lithium (Li 3) | Earned a 2019 Nobel Prize. |
| Electric Motor | 7 | Electricity + Neodymium Magnet | About half of the world's electricity runs motors. |
| Light Bulb | 7 | Electricity + Glass | Tungsten filaments glow at over 2,500 °C. |
| Telegraph | 7 | Electricity + Writing | The first transatlantic cable was laid in 1858. |
| Telephone | 7 | Telegraph + Copper (Cu 29) | Bell's first words: 'Come here, I want to see you.' |
| Radio | 8 | Telephone + Quartz | Quartz crystals tune radio frequencies. |
| Vacuum Tube | 8 | Light Bulb + Radio | Early computers used thousands of them. |
| Television | 8 | Radio + Vacuum Tube | Moving pictures carried by radio waves. |
| Combustion Engine | 7 | Steel + Petrol | Burns fuel inside the cylinder. |
| Car | 8 | Combustion Engine + Wheel | Over a billion are on the road today. |
| Airplane | 8 | Combustion Engine + Bird | The Wright brothers flew 12 seconds in 1903. |
| Transistor | 8 | Doped Silicon + Electricity | The most manufactured device in history. |
| Integrated Circuit | 8 | Transistor + Transistor | Modern chips hold tens of billions of transistors. |
| Computer | 8 | Integrated Circuit + Clock | Every chip runs to the beat of a clock. |
| Laser | 8 | Light Bulb + Ruby | The first laser used a ruby crystal. |
| Solar Panel | 8 | Doped Silicon + Photon | Photons knock electrons free to make current. |
| Centrifuge | 8 | Electric Motor + Steel | Spins up to separate uranium isotopes. |
| Nuclear Reactor | 8 | Enriched Uranium + Steel | A natural reactor ran in Gabon 2 billion years ago. |
| Particle Accelerator | 8 | YBCO Superconductor + Electricity | The LHC is 27 km around. |
| Fusion Reactor | 9 | Nuclear Reactor + YBCO Superconductor | Aims to bottle a star on Earth. |
| Internet | 8 | Computer + Telephone | Began as ARPANET in 1969. |
| Smartphone | 8 | Computer + Lithium Battery | More computing power than the Apollo guidance computer. |
| Robot | 8 | Computer + Electric Motor | 'Robot' comes from a Czech word for forced labor. |
| 3D Printer | 8 | Computer + Polyethylene | Can print rocket engine parts. |
| Artificial Intelligence | 8 | Internet + Book | Learned from humanity's written words. |
| Quantum Computer | 9 | Computer + YBCO Superconductor | Qubits are chilled near absolute zero. |

### Space

| Item | Tier | Recipe | Fact |
|---|---|---|---|
| Rocket Fuel | 9 | Petrol + Oxygen (O 8) | Kerosene and liquid oxygen powered Saturn V's first stage. |
| Rocket | 9 | Rocket Fuel + Titanium Alloy | Must reach about 7.8 km/s to stay in orbit. |
| Satellite | 9 | Rocket + Radio | Sputnik beeped from orbit in 1957. |
| GPS | 9 | Satellite + Clock | Must correct for relativity to stay accurate. |
| Space Telescope | 9 | Satellite + Telescope | JWST sees galaxies from 13+ billion years ago. |
| Astronaut | 9 | Human + Rocket | Over 600 people have flown to space. |
| Moon Landing | 9 | Astronaut + Moon | Apollo 11 landed in 1969. |
| Space Station | 9 | Satellite + Astronaut | The ISS circles Earth every 90 minutes. |
| Nuclear Battery (RTG) | 9 | Plutonium (Pu 94) + Battery | Has powered Voyager for nearly 50 years. |
| Space Probe | 9 | Satellite + Nuclear Battery (RTG) | Voyager 1 is in interstellar space. |
| Mars Rover | 9 | Robot + Mars | Curiosity has driven over 30 km on Mars. |
| Reusable Rocket | 9 | Rocket + Artificial Intelligence | Boosters now land themselves. |
| Ion Drive | 9 | Xenon (Xe 54) + Electricity | Gentle thrust but extremely efficient. |
| Mars Colony | 9 | Space Station + Mars | Mars has a day just 37 minutes longer than Earth's. |
| Space Elevator | 10 | Carbon Nanotube + Satellite | A cable to orbit would replace rockets. |
| Solar Sail | 9 | Space Probe + Laser | Sails on the pressure of light. |
| Fusion Drive | 9 | Fusion Reactor + Rocket | Could reach the outer planets in weeks. |
| Starship | 10 | Fusion Drive + Space Station | A city that can cross the void. |
| Generation Ship | 10 | Starship + Mars Colony | Crews born en route to the stars. |
| Dyson Swarm | 10 | Solar Panel + Star | Countless collectors orbiting a star. |
| Dyson Sphere | 10 | Dyson Swarm + Dyson Swarm | Captures nearly all of a star's energy. |
| Warp Drive | 10 | Starship + Exotic Matter | The Alcubierre metric bends space itself. |
| Matrioshka Brain | 10 | Dyson Sphere + Artificial Intelligence | A star-powered computer of nested shells. |
| Galactic Civilization | 10 | Matrioshka Brain + Galaxy | Kardashev Type III: harnessing a whole galaxy. |

### Cosmic

| Item | Tier | Recipe | Fact |
|---|---|---|---|
| Gas Cloud | 1 | Hydrogen (H 1) + Photon | Interstellar gas averages about one atom per cubic cm. |
| Nebula | 1 | Gas Cloud + Gas Cloud | Stellar nurseries light-years across. |
| Cosmic Dust | 1 | Carbon (C 6) + Nebula | Tons of it fall on Earth every day. |
| Protostar | 2 | Nebula + Hydrogen (H 1) | A collapsing cloud heating toward ignition. |
| Star | 2 | Protostar + Helium (He 2) | The Sun fuses 600 million tons of hydrogen per second. |
| Brown Dwarf | 2 | Protostar + Methane | Too small to fuse hydrogen: a failed star. |
| Red Dwarf | 2 | Protostar + Cosmic Dust | The most common stars; they live trillions of years. |
| Red Giant | 2 | Star + Carbon (C 6) | The Sun will swell into one in about 5 billion years. |
| White Dwarf | 5 | Red Giant + Oxygen (O 8) | A teaspoon weighs about 5 tons. |
| Planetary Nebula | 2 | Red Giant + Photon | Nothing to do with planets: a dying star's shell. |
| Blue Supergiant | 2 | Star + Star | Burns out in only a few million years. |
| Supernova | 5 | Blue Supergiant + Iron (Fe 26) | An iron core collapses in under a second. |
| Neutron Star | 5 | Supernova + Neutron | A city-sized ball denser than an atomic nucleus. |
| Pulsar | 5 | Neutron Star + Photon | Some spin over 700 times a second. |
| Magnetar | 5 | Pulsar + Neodymium Magnet | The strongest magnets in the universe. |
| Kilonova | 5 | Neutron Star + Neutron Star | Neutron-star collisions forge gold and platinum. |
| Black Hole | 6 | Neutron Star + Blue Supergiant | Not even light escapes past its event horizon. |
| Planetesimal | 3 | Cosmic Dust + Cosmic Dust | Building blocks of planets. |
| Asteroid | 3 | Planetesimal + Iron (Fe 26) | Some are almost pure metal. |
| Comet | 3 | Planetesimal + Water | A dirty snowball with a tail pointing away from the Sun. |
| Rocky Planet | 3 | Asteroid + Asteroid | Built up by countless collisions. |
| Earth | 3 | Rocky Planet + Water | The only known world with life (so far). |
| Mars | 3 | Rocky Planet + Rust (Iron Oxide) | Its red color is literally rust. |
| Moon | 3 | Rocky Planet + Rocky Planet | Likely formed when a Mars-sized body hit Earth. |
| Gas Giant | 3 | Rocky Planet + Gas Cloud | Jupiter could hold over 1,300 Earths. |
| Ice Giant | 3 | Gas Giant + Ammonia | It may rain diamonds inside Neptune. |
| Ring System | 3 | Gas Giant + Comet | Saturn's rings are mostly water ice. |
| Solar System | 4 | Star + Earth | Formed 4.6 billion years ago. |
| Star Cluster | 4 | Solar System + Solar System | Globular clusters hold up to millions of stars. |
| Supermassive Black Hole | 6 | Black Hole + Black Hole | Sagittarius A* weighs 4 million Suns. |
| Galaxy | 8 | Star Cluster + Supermassive Black Hole | The Milky Way has 100-400 billion stars. |
| Quasar | 8 | Supermassive Black Hole + Gas Cloud | Can outshine its entire host galaxy. |
| Ultramassive Black Hole | 8 | Supermassive Black Hole + Quasar | Over 10 billion solar masses. |
| Galaxy Cluster | 9 | Galaxy + Galaxy | The largest gravitationally bound objects. |
| Supercluster | 9 | Galaxy Cluster + Galaxy Cluster | We live in the Laniakea Supercluster. |
| Cosmic Web | 9 | Supercluster + Supercluster | Filaments of galaxies around vast voids. |
| Dark Matter | 10 | Galaxy + Photon | About 5x more of it than normal matter. |
| Dark Energy | 10 | Cosmic Web + Dark Matter | Is accelerating the expansion of the universe. |
| Exotic Matter | 10 | Dark Energy + Particle Accelerator | Hypothetical matter with negative energy density. |
| Wormhole | 10 | Black Hole + Exotic Matter | A shortcut through spacetime, if it exists. |
| White Hole | 10 | Wormhole + Photon | A black hole's time-reversed twin. |
| Universe | 12 | Cosmic Web + Dark Energy | About 93 billion light-years across (observable). |
| Big Bang | 12 | Ultramassive Black Hole + White Hole | Everything began 13.8 billion years ago. |
| Multiverse | 12 | Universe + Universe | The final merge: infinite universes. |

## Tier map

| Tier | Era | What unlocks | Items |
|---|---|---|---|
| 1 | Primordial | Particles, H to Ne, gas clouds, nebulae | 15 |
| 2 | Stellar fusion | Na to Fe, first compounds and minerals, stars | 53 |
| 3 | Planets and alloys | Steel, doped silicon, rocky and gas planets, organic molecules | 21 |
| 4 | Heavy forge | Neutron-capture elements, bronze, polymers, cells, solar systems | 68 |
| 5 | Life and fire | Plants, microbes, fire, stone age tools, supernovae, neutron stars | 44 |
| 6 | Creatures and r-process | Animals, medieval tech, gold and uranium, black holes | 47 |
| 7 | Industry and myth | Steam, electricity, mythic creatures | 24 |
| 8 | Modern age | Computers, AI, reactors, galaxies, quasars | 24 |
| 9 | Space age | Rockets, stations, fusion, lab-made superheavy elements | 47 |
| 10 | Interstellar | Starships, Dyson spheres, dark matter, wormholes | 13 |
| 12 | Beyond | Universe, Big Bang, Multiverse | 3 |

Elements past iron chain one step at a time (previous element + Neutron, Supernova or Particle Accelerator), so heavy elements gate on reaching stellar remnants and the modern lab. In play these become codex unlocks and rare drops rather than 90 consecutive board merges.

## Merge chain (v0.1 fusion ladder)

Merge-2 of identical items unless marked cross-merge. Fusion steps are simplified for fun but follow real stellar nucleosynthesis order. (Superseded in data by the v0.2 graph above; kept as the original design sketch.)

| Arc | Tier | Item | Made from | Merges into |
|---|---|---|---|---|
| Fusion | 1 | Proton / H | Generator: Quantum Vent | H + H → Deuterium |
| Fusion | 2 | Deuterium | H + H | D + D → Helium |
| Fusion | 3 | Helium | D + D (fusion) | He + He → Beryllium |
| Fusion | 4 | Beryllium | He + He | Be + Be → Carbon (triple-alpha flavor) |
| Fusion | 5 | Carbon | Be + Be | C + C → Oxygen |
| Fusion | 6 | Oxygen | C + C | O + O → Silicon |
| Fusion | 7 | Silicon | O + O | Si + Si → Iron |
| Fusion | 8 | Iron | Si + Si | Fusion ceiling; heavier elements need Supernova drops |
| Chemistry | C1 | Water H₂O | H + O (cross-merge) | Water + Water → Ice Crystal |
| Chemistry | C2 | Methane / CO₂ | C + H or C + O | → Organic Soup |
| Chemistry | C3 | Quartz SiO₂ | Si + O | Quartz + Quartz → Rock |
| Chemistry | C4 | Steel Ingot | Fe + C | Steel + Steel → Planetary Core |
| Chemistry | C5 | Rock → Boulder → Asteroid | Quartz chain | Asteroid + Asteroid → Planetesimal |
| Cosmic | 9 | Planetesimal | Asteroids | + → Rocky Planet |
| Cosmic | 10 | Rocky / Ocean / Gas Planet | Planetesimal + Core / Water / He | Gas Giant + Gas Giant → Brown Dwarf |
| Cosmic | 11 | Protostar | Brown Dwarf + H cloud | + → Red Dwarf |
| Cosmic | 12 | Red Dwarf → Yellow Star → Blue Giant | Stars | Blue Giant + Blue Giant → Red Supergiant |
| Cosmic | 13 | Supernova | Red Supergiant + Iron | Drops gold, uranium, platinum shards; → Neutron Star |
| Cosmic | 14 | Neutron Star → Pulsar → Magnetar | Supernova remnant | Magnetar + Magnetar → Kilonova |
| Cosmic | 15 | Stellar Black Hole | Kilonova or Supernova of a hypergiant | BH + BH → Supermassive Black Hole (endgame) |

Heavy elements (gold, uranium, platinum) are not fused directly: they drop only from Supernovas and Kilonovas, mirroring real r-process nucleosynthesis, and they feed rare orders and codex sets.

## Generators and energy

| Generator | Spawns | Upgrade path |
|---|---|---|
| Quantum Vent | H (mostly), occasional D | Merge two Vents → Nebula Vent (spawns He, higher tiers) |
| Stellar Forge | C, O, Si (unlocks at Sector 2) | → Fusion Core |
| Lab Bench | Catalysts that enable cross-merges | → Particle Collider |
| Cosmic Ray Chest | Random burst of 5 to 10 items, no energy cost | Reward-only, not merged |

| | |
|---|---|
| Energy name | Photons |
| Cap / regen | 100 cap, 1 per 2 min (tune in playtest) |
| Cost | 1 Photon per tap; higher-tier generators cost 2 but spawn better items |
| Overflow | Level-ups and order bonuses can exceed cap |
| Board | 7×9 grid; storage 'Dark Matter Pocket' with paid / earned slots |

## Meta progression and codex

- **Sectors: Map of the universe.** Lab → Solar System → Galaxy Arm → Galactic Core; each a themed board and order set.
- **Observatory: Base building.** Spend Stardust to build telescopes and labs that boost energy, spawn rates and storage.
- **Codex: Periodic table collection.** Interactive table fills as elements are discovered; each card has symbol, atomic number, origin and one real fact.
- **Sets: Collection rewards.** Complete noble gases, alkali metals, star types etc. for permanent bonuses.
- **Events: Limited boards.** e.g. 'Comet Week', 'Great Oxidation Event' with unique chains.

| Codex example | Fact |
|---|---|
| Hydrogen (1) | About 74% of the visible universe's ordinary mass; made in the first minutes after the Big Bang. |
| Helium (2) | Discovered in the Sun's spectrum in 1868, before it was found on Earth. |
| Carbon (6) | Made in stars by the triple-alpha process: three helium nuclei fuse. |
| Iron (26) | Fusing iron consumes energy, which is why a massive star's core collapses. |
| Gold (79) | Much of it is thought to come from neutron star mergers (kilonovas). |

## Visual style and game feel

> Target: Candy Crush clarity and payoff with Necromerger's tactile board. Every merge should look, sound and feel like a tiny reward, and bigger tiers should feel bigger.

| Category | Shape language | Color and finish |
|---|---|---|
| Elements | Round glossy orbs with symbol and number; noble gases get a halo ring | Color by element family (alkali red, halogen green, noble violet); radioactive pieces pulse |
| Materials | Faceted gems, ingots, crystals, poured blocks | Gemstone saturation, specular highlights, metal sheen sweep |
| Life | Soft blobs and rounded silhouettes, cute faces from cells upward | Greens and warm pastels; mythic creatures in gold-trimmed variants |
| Inventions | Chunky toy-like objects on a rounded-square tile | Warm wood to brass to chrome to neon as eras advance |
| Space | Sleek hard-surface icons on hexagon tiles | White, orange, teal; engine glow accents |
| Cosmic | Borderless, luminous, slowly rotating | Deep blues and magentas with glow and bloom; black holes use a lensing shader |

Readability rules: one bold silhouette per item, a tier badge in a fixed corner, a dark outline for contrast on any board, and no detail smaller than 4 dp at 64 dp piece size.

| Juice | What it does | Godot 4 implementation |
|---|---|---|
| Drag pickup | Piece lifts 8 to 12% scale, tilts toward drag, soft drop shadow grows | `Tween` on scale and rotation; shadow `Sprite2D` offset and alpha; `z_index` raised while dragged |
| Snap | Eases into the cell with a small overshoot; invalid drop springs back | `Tween` with `TRANS_BACK` and `EASE_OUT`, 0.12 s |
| Merge anticipation | Matching pieces glow and lean toward each other when hovered | Outline shader uniform tweened; small position nudge |
| Squash and stretch | Inputs squash together, result pops out stretched then settles | `Tween` chain on scale; elastic settle via `TRANS_ELASTIC` |
| Flash and burst | White flash plus particle burst; particle count, size and color scale with tier | Flash shader uniform; pooled `GPUParticles2D` with `one_shot`, `amount` set from tier |
| Chain reactions | A new item that matches a neighbour auto-merges in a cascade (opt-in per board) | Merge queue resolved with short delays; combo counter in `board.gd` |
| Number popups | +Stardust and XP numbers float up and fade; combos print larger | Pooled `Label` with `Tween` on position and modulate |
| Tier-up celebration | First item of a new tier: slow-mo beat, rays, banner | `AnimationPlayer` scene; `Engine.time_scale` dip to 0.5 for 0.2 s |
| Discovery reveal | Codex card flips in with the item's fact; rare items get a foil shimmer | Card flip by scaling x to 0 and back in an `AnimationPlayer`; foil shader on a gradient texture |
| Shake and hit-stop | Tiny shake on big merges, stronger on supernova and black hole | `Camera2D` offset driven by noise and decaying trauma; 40 to 80 ms hit-stop |
| Idle life | Gentle wobble, occasional sparkles, generators breathe | Vertex wobble shader with per-piece random phase; sparse `CPUParticles2D` |
| Board ambience | Parallax starfield and nebula drift; background shifts by sector | `ParallaxBackground` and a cheap scrolling noise shader |
| Audio | Merge notes rise in pitch through a scale on each combo step; tier stingers | `AudioStreamPlayer` pool; `pitch_scale` from a pentatonic table; separate SFX bus |
| Haptics | Light tick on pickup and snap, stronger pulse on merge, pattern on tier-up | `Input.vibrate_handheld(duration_ms)` at 10, 25 and 60 ms; settings toggle; needs the VIBRATE permission in export |
| Dissolve | Delivered or sold items dissolve into stardust | Dissolve shader with a noise texture and tweened threshold |

Performance rules:

1. Pool everything: particles, popups, audio players and item nodes; never instance during a merge.
2. Cap live particles around 300 to 500 on mid-range phones; scale with a quality setting and fall back to `CPUParticles2D` on Compatibility-renderer devices.
3. One texture atlas per category; keep real glow to cosmic pieces and bake bloom into sprites where possible.
4. Keep shaders short with no loops; share one material with per-instance uniforms.
5. Reduce-motion setting disables shake, flash and haptics; keep each merge animation under 0.35 s so play stays fast.
6. Profile on a real low-end Android device every milestone; target 60 fps (frame time under 16 ms).

## Monetization

**Do**
- Opt-in rewarded ads: energy refill, double order reward, open a chest
- Season pass (free + premium track) with cosmetic board themes
- One-time 'Remove forced ads + extra storage' purchase
- Starter pack at fair value, cosmetic item skins (retro, neon, sketchbook)
- Energy and Stardust bundles with clear prices

**Avoid**
- Paid loot boxes with hidden odds
- Interstitial ads mid-merge
- Fake countdown pressure or limited-time guilt pop-ups
- Paywalled codex facts (education stays free)
- Hard energy walls in the first hour

## Godot 4 technical plan

| Scene / script | Responsibility |
|---|---|
| `Main.tscn` | Root; autoload-driven scene switcher |
| `Board.tscn` + `board.gd` | Grid model, cell nodes, drag-and-drop, merge resolution |
| `Item.tscn` | Visual piece; reads an `ItemDef` resource, tween on merge |
| `Generator.tscn` | Item subclass that spawns from a weighted table, costs energy |
| `OrdersPanel.tscn` | Active orders, delivery, rewards |
| `Codex.tscn` | Periodic table UI, fact cards |
| Autoloads | `GameState`, `EnergyManager`, `SaveManager`, `Db` (item defs), `Audio` |

1. **Data-driven merge table.** `ItemDef` custom Resource (id, tier, chain, texture, merges_into, spawn_weights, codex_fact). Authored in a JSON/CSV sheet, imported by an editor tool script into `.tres` files so designers edit one spreadsheet.
2. **Merge lookup.** `Db` builds a Dictionary keyed by sorted pair `"h|h"` → result id, supporting both identical and cross merges.
3. **Save system.** JSON to `user://save.json` (board cells, inventory, energy timestamp, codex flags, version). Autosave on merge and on `NOTIFICATION_APPLICATION_PAUSED`; write to temp then rename.
4. **Offline energy.** Store Unix time on save; on load, add regen for elapsed time, clamp to cap.
5. **Android export.** Godot Android export template, Gradle build, target API per current Play requirement, AAB for Play Store, portrait lock, Mobile renderer. Plugins: Google Play Billing and AdMob Godot plugins.
6. **Performance.** Pool item nodes, use one texture atlas, avoid per-frame allocations; target 60 fps on mid-range devices.

## MVP scope and milestones

| Milestone | Scope | Est. |
|---|---|---|
| M1 Prototype | Board, drag/merge, JSON importer for data/*.json, pair lookup, H/Photon/Neutron generators, placeholder art | 2 wks |
| M2 Loop | Energy, orders, rewards, save/load, codex cards from item facts | 2 wks |
| M3 MVP slice | Tiers 1 to 6: elements to Fe plus Cu, Sn, Zn, Au, U; materials; Earth life to Human; fire to iron tools; stars to Black Hole (curated to about 150 of the 248 items in tiers 1 to 6) | 3 wks |
| M3.5 Juice | Core feel on graybox: pickup, snap, squash, tier-scaled bursts, popups, combo pitch audio, haptics, shake; performance pass on a low-end phone | 2 wks |
| M4 Polish | Art pass in the category style guide, cosmic glow shaders, codex card reveal, tier-up celebrations, ambience, tutorial, onboarding | 3 wks |
| M5 Soft launch | Ads + IAP, analytics, Play internal testing | 2 wks |
| M6 Content waves | Industrial to AI, space age, interstellar, mythic branch, full 118-element codex, cosmic endgame to Multiverse | 4 to 6 wks |

The MVP slice ends at the first Black Hole; tiers 7 to 12 ship as post-launch content waves. Events, season pass and multiple sectors follow soft-launch data.

## Open questions

1. Art direction: neon sci-fi, clean flat icons, or hand-drawn?
2. Strict merge-2 everywhere, or allow cross-merges (H + O → Water) as a signature twist?
3. Is there a narrative or characters giving orders (e.g. a quirky scientist AI)?
4. How educational should it be: optional facts only, or quizzes for rewards?
5. Monetization tolerance: ads at all, or premium/IAP only?
6. Target devices and minimum Android version?
7. Solo project or team? Who does art and audio?
8. Is the endgame a supermassive black hole, or a Big Bang prestige reset?
