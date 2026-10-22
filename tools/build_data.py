#!/usr/bin/env python3
"""Rebuild data/*.json from the design doc's item definitions (tools/raw_items.txt + element rules)."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYMS = "H Hydrogen,He Helium,Li Lithium,Be Beryllium,B Boron,C Carbon,N Nitrogen,O Oxygen,F Fluorine,Ne Neon,Na Sodium,Mg Magnesium,Al Aluminium,Si Silicon,P Phosphorus,S Sulfur,Cl Chlorine,Ar Argon,K Potassium,Ca Calcium,Sc Scandium,Ti Titanium,V Vanadium,Cr Chromium,Mn Manganese,Fe Iron,Co Cobalt,Ni Nickel,Cu Copper,Zn Zinc,Ga Gallium,Ge Germanium,As Arsenic,Se Selenium,Br Bromine,Kr Krypton,Rb Rubidium,Sr Strontium,Y Yttrium,Zr Zirconium,Nb Niobium,Mo Molybdenum,Tc Technetium,Ru Ruthenium,Rh Rhodium,Pd Palladium,Ag Silver,Cd Cadmium,In Indium,Sn Tin,Sb Antimony,Te Tellurium,I Iodine,Xe Xenon,Cs Caesium,Ba Barium,La Lanthanum,Ce Cerium,Pr Praseodymium,Nd Neodymium,Pm Promethium,Sm Samarium,Eu Europium,Gd Gadolinium,Tb Terbium,Dy Dysprosium,Ho Holmium,Er Erbium,Tm Thulium,Yb Ytterbium,Lu Lutetium,Hf Hafnium,Ta Tantalum,W Tungsten,Re Rhenium,Os Osmium,Ir Iridium,Pt Platinum,Au Gold,Hg Mercury,Tl Thallium,Pb Lead,Bi Bismuth,Po Polonium,At Astatine,Rn Radon,Fr Francium,Ra Radium,Ac Actinium,Th Thorium,Pa Protactinium,U Uranium,Np Neptunium,Pu Plutonium,Am Americium,Cm Curium,Bk Berkelium,Cf Californium,Es Einsteinium,Fm Fermium,Md Mendelevium,No Nobelium,Lr Lawrencium,Rf Rutherfordium,Db Dubnium,Sg Seaborgium,Bh Bohrium,Hs Hassium,Mt Meitnerium,Ds Darmstadtium,Rg Roentgenium,Cn Copernicium,Nh Nihonium,Fl Flerovium,Mc Moscovium,Lv Livermorium,Ts Tennessine,Og Oganesson"
EFACTS = {
 "H":"Makes up about 74% of the normal matter in the universe.","He":"Discovered in the Sun's spectrum before it was found on Earth.",
 "Li":"The lightest metal; it floats on water (and reacts with it).","C":"Forms more compounds than any other element: the backbone of life.",
 "N":"About 78% of Earth's air is nitrogen.","O":"The third most abundant element in the universe.","Ne":"Glows red-orange in a discharge tube: the original neon sign.",
 "Na":"Soft enough to cut with a butter knife.","Si":"The second most abundant element in Earth's crust.","Fe":"Fusion stops at iron: making heavier nuclei costs a star energy.",
 "Cu":"One of the first metals humans worked, over 10,000 years ago.","Tc":"The lightest element with no stable isotopes; first made artificially in 1937.",
 "Ag":"The best electrical conductor of all metals.","Xe":"Used to power ion engines on spacecraft like Dawn.","Nd":"Neodymium magnets are the strongest permanent magnets made.",
 "Pm":"Essentially absent from Earth's crust; all of it is radioactive.","Eu":"Glows red in euro banknotes under UV light, a real anti-forgery feature.",
 "W":"Highest melting point of any metal: 3,422 °C.","Os":"The densest naturally occurring element.","Pt":"So unreactive it was used for the international kilogram standard alloy.",
 "Au":"Much of Earth's gold was forged in neutron-star collisions.","Hg":"The only metal that is liquid at room temperature.",
 "Pb":"Romans used it for water pipes; 'plumbing' comes from 'plumbum'.","Bi":"Technically radioactive, with a half-life a billion times the universe's age.",
 "Po":"Discovered by Marie and Pierre Curie, named after Poland.","U":"The heaviest element found in significant amounts in nature.",
 "Pu":"Powers RTGs on deep-space probes like Voyager and Curiosity.","Es":"First found in the debris of the first hydrogen bomb test.","Og":"The heaviest element known; only a handful of atoms ever made.",
}
ORIGIN = {"fusion":"Forged by nuclear fusion inside stars.","neutron capture":"Built by slow neutron capture in aging giant stars.",
 "supernova":"Forged in supernovae and neutron-star mergers (r-process).","lab synthesis":"Only made artificially in reactors or particle accelerators."}
VIA = {"fusion":"helium","neutron capture":"neutron","supernova":"supernova","lab synthesis":"particle_accelerator"}
ETIER = {"fusion":1,"neutron capture":4,"supernova":6,"lab synthesis":9}
CATS = ["elements","materials","bestiary","inventions","space","cosmic"]
def method(z):
    if z <= 26: return "fusion"
    if z in (43, 61) or z >= 95: return "lab synthesis"
    if z >= 84 or z in (63, 76, 77, 78, 79): return "supernova"
    return "neutron capture"
def elements():
    els = [s.split(" ") for s in SYMS.split(",")]
    ids = [e[1].lower() for e in els]
    out = [dict(id="photon",name="Photon",category="elements",subcategory="particle",tier=1,recipe=None,fact="Light quanta; the energy currency of Alchemergy."),
           dict(id="neutron",name="Neutron",category="elements",subcategory="particle",tier=1,recipe=None,fact="Free neutrons decay in about 15 minutes.")]
    for i,(sym,name) in enumerate(els):
        z=i+1; m=method(z)
        rec = None if z==1 else ["hydrogen","hydrogen"] if z==2 else [ids[i-1],"neutron"] if z in (43,61) else [ids[i-1],VIA[m]]
        tier = (1 if z<=10 else 2) if m=="fusion" else ETIER[m]
        out.append(dict(id=ids[i],name=f"{name} ({sym} {z})",category="elements",subcategory=m,tier=tier,recipe=rec,
                        fact=EFACTS.get(sym,ORIGIN[m]),symbol=sym,atomic_number=z))
    return out
def main():
    items = elements(); cat=None
    for line in open(os.path.join(ROOT,"tools","raw_items.txt"),encoding="utf-8"):
        line=line.rstrip("\n")
        if not line: continue
        if line.startswith("["): cat=line[1:-1]; continue
        id_,name,sub,tier,rec,fact=line.split("|")
        items.append(dict(id=id_,name=name,category=cat,subcategory=sub,tier=int(tier),recipe=rec.split("+"),fact=fact))
    by={i["id"]:i for i in items}; depth={}
    def d(x):
        if x not in depth:
            r=by[x]["recipe"]; depth[x]=0 if not r else 1+max(d(a) for a in r)
        return depth[x]
    for i in items: i["depth"]=d(i["id"])
    keys=["id","name","category","subcategory","tier","depth","recipe","fact","symbol","atomic_number"]
    for c in CATS:
        rows=[{k:i[k] for k in keys if k in i} for i in items if i["category"]==c]
        with open(os.path.join(ROOT,"data",f"{c}.json"),"w",encoding="utf-8") as f: json.dump(rows,f,indent=1,ensure_ascii=False)
    summ=dict(version="0.2",total=len(items),bases=["hydrogen","photon","neutron"],
              by_category={c:sum(i["category"]==c for i in items) for c in CATS},
              by_tier={str(t):sum(i["tier"]==t for i in items) for t in sorted({i["tier"] for i in items})},
              mvp_tiers=[1,2,3,4,5,6],max_depth=max(i["depth"] for i in items))
    with open(os.path.join(ROOT,"data","summary.json"),"w") as f: json.dump(summ,f,indent=1)
    print(json.dumps(summ))
if __name__=="__main__": main()
