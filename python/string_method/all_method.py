name = "anthony"
phrase = "Bonjour tout le monde"

# Break method
print(name.upper()) 
print(name.lower())
print(name.capitalize())
print(phrase.title())

print("---------------------")
# Replace method

print(phrase.replace("jour", "soir")) # "Bonsoir tout le monde"
print(phrase.replace("jour", "soir").title()) # "Bonsoir Tout Le Monde"
print(phrase.replace(" ", "").title()) # BonsoirToutLeMonde

print("---------------------")
# Strip method

country = " France "

print(country.strip())
print(country.strip(" rce")) #lstrip / rstrip

print("---------------------")
# join & split method

nombre = "1, 2, 3, 4, 5"

print(nombre.split(", ")) # Retourne une liste
print(",".join("1, 2, 3, 4, 5".split(", ")))

print("---------------------")
# zfill method

print("4".zfill(4)) # remplir avec des zero

print("---------------------")
# is method

print("Bonjour".islower())
print(" 50".isdigit())

print("---------------------")
# count method

print("Bonjour le jour".count(" jour")) # compte les occurances d'un mot

print("---------------------")
# find and index method

print("Bonsoir le soir".index("soir"))
print("Bonsoir le soir".find("soir"))

print("---------------------")
# endswith method

print("image.png".endswith(".png"))
print("image.png".startswith("image"))
print("camera".endswith("video"))

