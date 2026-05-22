# gemini je voudrais 2 boucle en python pour énumérer les .1 .2 .3 .4 .5 .6 .7 .8 .9 puis .01 .02 .03 jusqu'à 20 chiffres après la virgule. la variable doit être un float


# Première boucle : le nombre de zéros / la position de la décimale (de 1 à 20)
for position in range(1, 21):
    print(f"--- Position {position} après la virgule ---")

    # Deuxième boucle : le chiffre significatif de 1 à 9
    for chiffre in range(1, 10):
        # On force la création d'un float pur via la division
        ma_variable_float = float(chiffre) / (10.0 ** position)

        # On vérifie le type pour s'assurer que c'est bien un float
        type_var = type(ma_variable_float).__name__

        # Affichage avec l'écriture scientifique (inévitable pour les floats si petits)
        print(f"Valeur : {ma_variable_float} | Type : {type_var}")

# .1 à .9
for i in range(1, 10):
    x = float(f"0.{i}")
    print(x)

# .01 .02 .03 ... jusqu'à 20 chiffres après la virgule
for n in range(2, 21):
    for i in range(1, 10):
        x = float("0." + "0" * (n - 1) + str(i))
        print(x)