dict = {"Harry": "Human Being", 6: "Ayush"}
print(dict["Harry"])
print(dict[6])

info = {"name": "Karan", "age": 24, "eligiblity": True}
print(info["name"]) #Throws an error
print(info.get("age")) #Does not Throw any error
print(info.keys())
for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")