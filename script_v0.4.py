# I can't write regular, so I write violent matching

from replace_post_tex import replace_dollar_tex
from rules import repl
import re
import pyperclip

# l = "$sinx+cosx$+$$tanx$$\n+$tanx$"
l = pyperclip.paste()
l = "".join(l)  # 得到一串

l = replace_dollar_tex(l)
# print(l)
imath_start = [i for i in range(len(l)) if l.startswith(r"+imath+", i)]
imath_end = [i for i in range(len(l)) if l.startswith(r"+/imath+", i)]
dmath_start = [i for i in range(len(l)) if l.startswith(r"+dmath+", i)]
dmath_end = [i for i in range(len(l)) if l.startswith(r"+/dmath+", i)]

for i in range(len(imath_start)):
    imath_start[i] += 7

for i in range(len(dmath_start)):
    dmath_start[i] += 7

imath_pos = list(zip(imath_start, imath_end))
dmath_pos = list(zip(dmath_start, dmath_end))

pos = imath_pos+dmath_pos  # Finding formula positions

pos.sort()
pos.reverse()  # Reverse order, so changing the back will not affect the previous
# print(pos)

for i in pos:
    temp = l[i[0]: i[1]]
    for j in repl:
        for k in j:
            temp = temp.replace(k, j[k])
    l = l.replace(l[i[0]: i[1]], temp)

l = l.replace(
    r"+imath+", r"$")
l = l.replace(
    r"+/imath+", r"$")
l = l.replace(
    r"+dmath+", r"$$")
l = l.replace(
    r"+/dmath+", r"$$")

while "  " in l:
    l = l.replace("  ", " ")

print(l)

pyperclip.copy(l)