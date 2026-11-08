"""Cute cat"""
import json
def main():
    """main func"""
    n = int(input())
    catfox_dic = {}
    cat_list = {}
    fox_list = {}
    cat, fox = 0, 0
    for _ in range(n):
        catfox_dic.update(json.loads(input()))
    if ("Cat01" not in catfox_dic.values()) and ("Garfield" not in catfox_dic):
        cat += 1
        cat_list.update({"Garfield":"Cat01"})
    if ("Fox01" not in catfox_dic.values()) and ("Fubuki" not in catfox_dic):
        fox += 1
        fox_list.update({"Fubuki" : "Fox01"})
    for name, types in catfox_dic.items():
        if "Cat" in types:
            cat_list.update({name : types})
            cat += 1
        elif "Fox" in types:
            fox_list.update({name : types})
            fox += 1
    cat_list = dict(sorted(cat_list.items(), key=lambda item: item[1]))
    fox_list = dict(sorted(fox_list.items(), key=lambda item: item[1]))
    print(f"Cat : {cat}\n"+f"Fox : {fox}")
    for name, cat in cat_list.items():
        print(f"{name} : {cat}")
    for name, fox in fox_list.items():
        print(f"{name} : {fox}")
main()
