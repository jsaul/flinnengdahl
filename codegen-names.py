#!/usr/bin/env python
# -*- coding: utf-8 -*-

items = dict()

with open("data/numbered-names-intl.txt") as f:
    while True:
        line = f.readline().strip()
        if not(line):
            break
        if line[0] == "#":
            continue
        line = line.split(maxsplit=2)
        num  = int(line[0])
        cat = line[1]
        txt = line[2]

        if cat not in items:
            items[cat] = dict()

        items[cat][num] = (num, txt)

assert "en" in items

with open("src/fe-names.cpp", "w") as out:

    print("std::map<std::string, std::map<size_t, std::string>> _names = {", file=out)

    categories = [key for key in items.keys()]
    for cat in items:
        lines = []
        print('\t{ "'+cat+'", {', file=out)
        keys = sorted(items[cat].keys())
        for key in keys:
            num, txt = items[cat][key]
            code = '\t/* %s */\t{%4d, "%s" },' % (cat, num, txt)
            if num in [172, 299, 550]:
                code += "\t// abandoned name"
            lines.append(code)
        print("\n".join(lines).rstrip(","), file=out)
        print('\t} }' + ("" if cat==categories[-1] else ","), file=out)

    print("};", file=out)
