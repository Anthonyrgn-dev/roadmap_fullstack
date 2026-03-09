# Dans cet exercices vous devez remplacer le mot "Bonjour" dans la variable phrase par le mot "Bonsoir"
# A l'aide d'une methode disponible sur les chaines de caracteres.
# La variable nouvelle_phrase devra donc contenir la chaine de caracteres "Bonsoir tout le monde"

phrase = "Bonjour tout le monde"
nouvelle_phrase = phrase.replace("Bonjour", "Bonsoir")

print(nouvelle_phrase)

print("-------------------------------")
# Dans cet exercice, nous cherchons a compter le nombre d'occurences d'une lettre dans une 
# chaine de caracteres

lettre_a_chercher = "o"
phrase = "Bonjour tout le monde"

resultat = phrase.lower().count(lettre_a_chercher)

print(resultat)

print("-------------------------------")
# Dans cet exercice, le but est de compter le nombre de phrases presentes dans le texte contenu dans la
# variable lorem

lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut     labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

resultat2 = lorem.count(".")

# Cet exercice est assez difficile compte tenu du fait que l'on a pas encore vu les listes en details
# Le but de cet exercice est de remettre en ordre alphabetique les prenoms present dans la chaine de 
# caracteres. 
# Vous devez creer une variable chaine_en_ordre qui, a la fin de l'exercice, doit contenir
# La chaine de caracteres suivante : Anne, Julien, Lucien, Marie, Pierre 
# Pour trier une liste on utilise la methode sort. ou sorted.

chaine = "Pierre, Julien, Anne, Marie, Lucien"

chaine_en_ordre = ", ".join(sorted(chaine.split(", ")))

print(chaine_en_ordre)

print("----------------------")
