minuman = ["air zamzam", "fresh tea", "cocacola", "pepsi", "teh kotak", "marimas"] 
print(minuman[2])

minuman.append("marimas")

minuman.pop(2)
print(minuman)


makanan = ("nasi untug oncm", "sate", "baso", "seblak", "indomie")
update = list(makanan)
update[0] = "nasi timbel"
tuple = tuple(update)
print(tuple)