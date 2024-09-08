#!/usr/bin/env python
# -*- coding: utf-8 -*-

obsolete_regions = [172, 299, 550]

from contextlib import redirect_stdout

items = dict()

with open("data/numbered-names-intl.txt") as f:
    while True:
        line = f.readline().strip()
        if not(line):
            break
        if line[0] == "#":
            continue
        line = line.split(maxsplit=2)
        number = int(line[0])
        category = line[1]
        name = line[2]

        if category not in items:
            items[category] = dict()

        items[category][number] = (number, name)

assert "en" in items

with open("src/fe-names.cpp", 'w') as out:
    with redirect_stdout(out):

        print("std::map<std::string, std::map<size_t, std::string>> _names = {")

        categories = [category for category in items.keys()]
        for category in items:
            lines = []
            print('\t{ "' + category + '", {')
            keys = sorted(items[category].keys())
            for key in keys:
                number, name = items[category][key]
                code = '\t/* %s */\t{%4d, "%s" },' % (category, number, name)
                if number in obsolete_regions:
                    code += "\t// obsolete name"
                lines.append(code)
            print("\n".join(lines).rstrip(","))
            print('\t} }' + ("" if category==categories[-1] else ","))

        print("};")
