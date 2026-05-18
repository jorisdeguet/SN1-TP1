import racine
import math


def print_vert(texte):
    print(f"\033[32m{texte}\033[0m")

def print_rouge(texte):
    print(f"\033[31m{texte}\033[0m")

def print_jaune(texte):
    print(f"\033[93m{texte}\033[0m")


def verifier_racine_base_diverse(methode, nombre, base, decimales):
    if base == 2:
        attendu = round(math.sqrt(nombre), decimales)
    elif base == 3:
        attendu = round(math.cbrt(nombre), decimales)
    elif base == 4:
        attendu = round(math.sqrt(math.sqrt(nombre)), decimales)

    obtenu = methode(nombre, base, decimales)

    if obtenu == attendu:
        print_vert("Succès")
    else:
        print_rouge("Échec")
        print_rouge(f"     attendu : {attendu}")
        print_rouge(f"      obtenu : {obtenu}")
        global erreur_detecte_partie_2
        erreur_detecte_partie_2 = True


def verifier_racine_carre(methode, nombre, decimales):
    attendu = round(math.sqrt(nombre), decimales)
    obtenu = methode(nombre, decimales=decimales)

    if obtenu == attendu:
        print_vert("Succès")
    else:
        print_rouge("Échec")
        print_rouge(f"     attendu : {attendu}")
        print_rouge(f"      obtenu : {obtenu}")
        global erreur_detecte_partie_1
        erreur_detecte_partie_1 = True


version = "1.0.3"
print("*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*")
print(f"  SCRIPT DE VALIDATION DES 2 FONCTIONS CALCULANT LA RACINE CARRÉE ({version})")
print()
print("    🤖 ÉTAPE 1 de 3 - Validation de la structure du module racine.py ")
print("*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*\n")

# Les fonctions testées sont connues directement, pas besoin d'introspection.
# racine_arrondi_dicho : (nombre, decimales=5)      — racine carrée uniquement
# racine_arrondi_n     : (nombre, exposant=2, decimales=5) — racine n-ième
liste_methodes              = [racine.racine_arrondi_dicho, racine.racine_arrondi_n]
liste_methode_cas_n_possibles = [racine.racine_arrondi_n.__name__]

for methode in liste_methodes:
    print(f"  - Fonction : {methode.__name__}")
    if methode.__doc__ is None:
        print_rouge(f"    ❌ La fonction {methode.__name__} ne possède pas de DOCSTRING!")
        exit()
    print(f"       Docstring : présente")
    print()


print()
print("*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*")
print("    🤖 ÉTAPE 2 de 3 - Exécution des tests avec des paramètres valides ")
print("*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*\n")

liste_precisions       = [4, 5, 6, 7, 8, 9, 10]
liste_cas_racine_carre = [0, 0.1, 0.2, 0.9, 8, 9, 81, 123, 999]
liste_cas_racine_diverses = [8, 9, 81, 123]

erreur_detecte_partie_1 = False
erreur_detecte_partie_2 = False

for methode in liste_methodes:
    for decimales in liste_precisions:

        for cas in liste_cas_racine_carre:
            instruction = f"{methode.__name__}({cas})"
            print(f"  {instruction:<50} précision {decimales:<2} base par défaut        ", end="")
            verifier_racine_carre(methode, cas, decimales)

        if methode.__name__ in liste_methode_cas_n_possibles:
            for base in [2, 3, 4]:
                for cas in liste_cas_racine_diverses:
                    instruction = f"{methode.__name__}({cas})"
                    print(f"  {instruction:<50} précision {decimales:<2} base {base}                 ", end="")
                    verifier_racine_base_diverse(methode, cas, base, decimales)

print()
print("*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*")
print("🤖 ÉTAPE 3 de 3 - Exécution des tests avec des paramètres invalides ")
print("*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*\n")

erreur_detecte_partie_3 = False

for methode in liste_methodes:
    try:
        instruction = f"{methode.__name__}(-3)"
        print(f"  {instruction:<50}", end="")
        methode(-3)
        print_rouge("Échec")
        print_rouge("La racine négative n'est pas possible (avec base 2), exception non levée.")
        erreur_detecte_partie_3 = True
    except ValueError:
        print_vert("Succès")

try:
    instruction = f"{racine.racine_arrondi_n.__name__}(-4, 4)"
    print(f"  {instruction:<50}", end="")
    racine.racine_arrondi_n(-4, 4)
    print_rouge("Échec")
    print_rouge("La racine d'un nombre négatif est possible uniquement avec une base impaire, exception non levée.")
    erreur_detecte_partie_3 = True
except ValueError:
    print_vert("Succès")

try:
    instruction = f"{racine.racine_arrondi_n.__name__}(4, 1.5)"
    print(f"  {instruction:<50}", end="")
    racine.racine_arrondi_n(4, 1.5)
    print_rouge("Échec")
    print_rouge("La base doit être un entier >= 2, exception non levée.")
    erreur_detecte_partie_3 = True
except ValueError:
    print_vert("Succès")

print()

erreur = erreur_detecte_partie_1 or erreur_detecte_partie_2 or erreur_detecte_partie_3

if erreur:
    print_rouge("🛑 DES CORRECTIONS SONT NÉCESSAIRES!")
else:
    print_vert("*** ✅ TOUS LES TESTS ONT PASSÉS AVEC SUCCÈS 🎉 BRAVO! ***")
