#!/usr/bin/env python
# -*- coding: utf-8 -*-

items = list()

with open("numbered-names-intl.txt") as f:
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

        if cat != "en":
            continue

        items.append( (num, txt) )


lines = []
for item in sorted(items, key=lambda x: x[0]):
    num, txt = item
    code = '/* %3d */\t"%s",' % (num, txt)
    if num in [172, 299, 550]:
        code += "\t// abandoned name"
    lines.append(code)

print("static std::vector<std::string> _names = {")
print("\n".join(lines).rstrip(","))
print("};")
