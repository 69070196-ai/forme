"""Vowel"""
array = input().lower()
spl = []
spl.extend(array)
if "a" in spl:
    print((f"a : {spl.count("a")}"))
if "e" in spl:
    print((f"e : {spl.count("e")}"))
if "i" in spl:
    print((f"i : {spl.count("i")}"))
if "o" in spl:
    print((f"o : {spl.count("o")}"))
if "u" in spl:
    print((f"u : {spl.count("u")}"))
