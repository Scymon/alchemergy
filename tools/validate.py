#!/usr/bin/env python3
"""Validate the Alchemergy merge graph in data/*.json. Exit 1 on any failure."""
import json, os, sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATS=["elements","materials","bestiary","inventions","space","cosmic"]
BASES={"hydrogen","photon","neutron"}
items=[i for c in CATS for i in json.load(open(os.path.join(ROOT,"data",f"{c}.json"),encoding="utf-8"))]
errs=[]; ids=[i["id"] for i in items]; idset=set(ids)
if len(ids)!=len(idset): errs.append("duplicate ids: "+str({x for x in ids if ids.count(x)>1}))
pairs={}
for i in items:
    for f in ("id","name","category","subcategory","tier","depth","recipe","fact"):
        if f not in i: errs.append(f"{i.get('id')}: missing field {f}")
    r=i["recipe"]
    if r is None:
        if i["id"] not in BASES: errs.append(f"{i['id']}: no recipe but not a base")
        continue
    if len(r)!=2: errs.append(f"{i['id']}: recipe must have 2 inputs"); continue
    for x in r:
        if x not in idset: errs.append(f"{i['id']}: unknown input {x}")
    k="|".join(sorted(r))
    if k in pairs: errs.append(f"pair {k} used by {pairs[k]} and {i['id']}")
    pairs[k]=i["id"]
reach=set(BASES); changed=True
while changed:
    changed=False
    for i in items:
        if i["id"] not in reach and i["recipe"] and all(x in reach for x in i["recipe"]):
            reach.add(i["id"]); changed=True
un=idset-reach
if un: errs.append(f"{len(un)} unreachable: {sorted(un)}")
s=json.load(open(os.path.join(ROOT,"data","summary.json")))
if s.get("total")!=len(items): errs.append("summary total mismatch")
print(f"items={len(items)} unique_pairs={len(pairs)} reachable={len(reach)}")
if errs:
    print("FAIL"); [print(" -",e) for e in errs]; sys.exit(1)
print("PASS")
