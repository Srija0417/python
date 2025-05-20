d={
    "name":"srija",
    "age":21,
    "marks":{ #nested dictionary
        "chem":36,
        "math":43,
        "eng":45
        },
    "Gender":"F",
    12:24,
    round((22/7),3):3.14

}

d["age"]=22
d["surname"]="kallem"
d["marks"]["chem"]=45
print(d)
print(d.keys())
print(d.values())
print(d.items())
print(d.get("marks"))
print(len(d))
d.update({"city":"hyd"})
print(d)