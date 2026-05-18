import os

from racine import *
from math import sqrt

# Fourni par le prof, donne une idée des cas qu'on souhaite tester

def test(texte, resultat, attendu, delta=0):
    ok = abs(resultat - attendu) < delta if delta else resultat == attendu
    couleur = "\033[92m Passe\033[0m" if ok else "\033[91m Casse\033[0m"
    print(couleur, texte, "- résultat", resultat, "attendu", attendu)


def test_exception(texte, appel):
    try:
        appel()
        print("\033[91m Casse\033[0m", texte, "- aucune exception levée")
    except Exception as e:
        print("\033[92m Passe\033[0m", texte, "- Error levee comme attendu ", e)


# --- racine_arrondi_dicho ---

test("Dichotomie - carré parfait 9",               racine_arrondi_dicho(9),            3.0)
test("Dichotomie - carré parfait 9 (8 déc.)",      racine_arrondi_dicho(9, 8),         3.0)
test("Dichotomie - carré parfait 9.0",             racine_arrondi_dicho(9.0),          3.0)
test("Dichotomie - grand parfait 1000000",         racine_arrondi_dicho(1000000),      1000.0)
test("Dichotomie - grand non parfait 2000000",     racine_arrondi_dicho(2000000),      1414.21356)
test("Dichotomie - grand non parfait 2000000 (8)", racine_arrondi_dicho(2000000, 8),   1414.21356237)
test("Dichotomie - petit 0.0001",                  racine_arrondi_dicho(0.0001),       0.01)
test("Dichotomie - non entier 10.5",               racine_arrondi_dicho(10.5),         3.24037)
test("Dichotomie - non entier 10.5 (8 déc.)",      racine_arrondi_dicho(10.5, 8),      3.24037035)
test("Dichotomie - irrationnel 2 (2 déc.)",        racine_arrondi_dicho(2, 2),         1.41)
test("Dichotomie - irrationnel 2 (5 déc.)",        racine_arrondi_dicho(2),            1.41421)
test("Dichotomie - irrationnel 2 (8 déc.)",        racine_arrondi_dicho(2, 8),         1.41421356)
test("Dichotomie - précise (delta)",               racine_arrondi_dicho(2, 10),        sqrt(2),  delta=1e-9)
print("\nSi tous les tests au dessus fonctionne, tu peux faire un commit sur ton repo\n")
# --- racine_arrondi_chiffres ---

test("Chiffres - carré parfait 9",                 racine_arrondi_chiffres(9),         3.0)
test("Chiffres - carré parfait 9 (8 ch.)",         racine_arrondi_chiffres(9, 8),      3.0)
test("Chiffres - carré parfait 9.0",               racine_arrondi_chiffres(9.0),       3.0)
test("Chiffres - grand parfait 1000000",           racine_arrondi_chiffres(1000000),   1000.0)
test("Chiffres - grand non parfait 2000000",       racine_arrondi_chiffres(2000000),   1414.2135)
test("Chiffres - grand non parfait 2000000 (8)",   racine_arrondi_chiffres(2000000, 8),1414.2135623)
test("Chiffres - petit 0.0001",                    racine_arrondi_chiffres(0.0001),    0.01)
test("Chiffres - non entier 10.5",                 racine_arrondi_chiffres(10.5),      3.2403)
test("Chiffres - non entier 10.5 (8 ch.)",         racine_arrondi_chiffres(10.5, 8),   3.2403703)
test("Chiffres - irrationnel 2 (2 ch.)",           racine_arrondi_chiffres(2, 2),      1.4)
test("Chiffres - irrationnel 2 (5 ch.)",           racine_arrondi_chiffres(2),         1.4142)
test("Chiffres - irrationnel 2 (8 ch.)",           racine_arrondi_chiffres(2, 8),      1.4142135)
test("Chiffres - précise (delta)",                 racine_arrondi_chiffres(2, 10),     sqrt(2),  delta=1e-9)
print("\nSi tous les tests au dessus fonctionne, tu peux faire un commit sur ton repo\n")
# --- racine_arrondi_n ---

# Racine carrée (exposant=2) — mêmes cas que dicho/chiffres
test("Racine n - carré parfait 9 (exp=2)",         racine_arrondi_n(9, 2),             3.0)
test("Racine n - carré parfait 9 (exp=2, 8 déc.)", racine_arrondi_n(9, 2, 8),          3.0)
test("Racine n - carré parfait 9.0 (exp=2)",       racine_arrondi_n(9.0, 2),           3.0)
test("Racine n - grand parfait 1000000 (exp=2)",   racine_arrondi_n(1000000, 2),       1000.0)
test("Racine n - grand non parfait 2000000 (exp=2)",       racine_arrondi_n(2000000, 2),       1414.21356)
test("Racine n - grand non parfait 2000000 (exp=2, 8 déc.)",racine_arrondi_n(2000000, 2, 8),    1414.21356237)
test("Racine n - petit 0.0001 (exp=2)",            racine_arrondi_n(0.0001, 2),        0.01)
test("Racine n - non entier 10.5 (exp=2)",         racine_arrondi_n(10.5, 2),          3.24037)
test("Racine n - non entier 10.5 (exp=2, 8 déc.)", racine_arrondi_n(10.5, 2, 8),       3.24037035)
test("Racine n - irrationnel 2 (exp=2, 5 déc.)",   racine_arrondi_n(2, 2),             1.41421)
test("Racine n - irrationnel 2 (exp=2, 8 déc.)",   racine_arrondi_n(2, 2, 8),          1.41421356)
test("Racine n - précise carré (delta)",           racine_arrondi_n(2, 2, 10),         sqrt(2),     delta=1e-9)
print("\nSi tous les tests au dessus fonctionne, tu peux faire un commit sur ton repo\n")
# Racine cubique (exposant=3)
test("Racine n - cube parfait 27 (exp=3)",               racine_arrondi_n(27, 3),            3.0)
test("Racine n - grand cube parfait 1000000000 (exp=3)",  racine_arrondi_n(1000000000, 3),    1000.0)
test("Racine n - grand non parfait 2000000000 (exp=3)",   racine_arrondi_n(2000000000, 3),    1259.92105)
test("Racine n - non entier 10.5 (exp=3)",               racine_arrondi_n(10.5, 3),          2.18976)
test("Racine n - irrationnel 2 (exp=3, 5 déc.)",         racine_arrondi_n(2, 3),             1.25992)
test("Racine n - irrationnel 2 (exp=3, 8 déc.)",         racine_arrondi_n(2, 3, 8),          1.25992105)
test("Racine n - négatif -8 (exp=3)",                    racine_arrondi_n(-8, 3),            -2.0)
test("Racine n - précise cube (delta)",                  racine_arrondi_n(2, 3, 10),         2 ** (1/3), delta=1e-8)
test("Racine n - 4e parfait 16 (exp=4)",           racine_arrondi_n(16, 4),            2.0)
print("\nSi tous les tests au dessus fonctionne, tu peux faire un commit sur ton repo\n")


# --- racine (précise, comparée à sqrt avec delta) ---

test("Précise - carré parfait 9",                  racine(9),          3,         delta=1e-8)
test("Précise - carré parfait 9.0",                racine(9.0),        3,       delta=1e-8)
test("Précise - grand parfait 1000000",            racine(1000000),    1000,   delta=1e-8)
test("Précise - grand non parfait 2000000",        racine(2000000),    1414.21356237,   delta=1e-8)
test("Précise - petit 0.0001",                     racine(0.0001),     0.01,    delta=1e-8)
test("Précise - non entier 10.5",                  racine(10.5),       3.24037034920393,      delta=1e-8)
test("Précise - irrationnel 2",                    racine(2),          1.414213562373095,         delta=1e-8)



# =============================================================================
# --- corrAncien : racine_arrondi_dicho ---
# =============================================================================

# decimales = 4
test("dicho(0, 4)", racine_arrondi_dicho(0, 4), 0.0)
test("dicho(0.1, 4)", racine_arrondi_dicho(0.1, 4), 0.3162)
test("dicho(0.2, 4)", racine_arrondi_dicho(0.2, 4), 0.4472)
test("dicho(0.9, 4)", racine_arrondi_dicho(0.9, 4), 0.9487)
test("dicho(8, 4)", racine_arrondi_dicho(8, 4), 2.8284)
test("dicho(9, 4)", racine_arrondi_dicho(9, 4), 3.0)
test("dicho(81, 4)", racine_arrondi_dicho(81, 4), 9.0)
test("dicho(123, 4)", racine_arrondi_dicho(123, 4), 11.0905)
test("dicho(999, 4)", racine_arrondi_dicho(999, 4), 31.607)

# decimales = 5
test("dicho(0, 5)", racine_arrondi_dicho(0, 5), 0.0)
test("dicho(0.1, 5)", racine_arrondi_dicho(0.1, 5), 0.31623)
test("dicho(0.2, 5)", racine_arrondi_dicho(0.2, 5), 0.44721)
test("dicho(0.9, 5)", racine_arrondi_dicho(0.9, 5), 0.94868)
test("dicho(8, 5)", racine_arrondi_dicho(8, 5), 2.82843)
test("dicho(9, 5)", racine_arrondi_dicho(9, 5), 3.0)
test("dicho(81, 5)", racine_arrondi_dicho(81, 5), 9.0)
test("dicho(123, 5)", racine_arrondi_dicho(123, 5), 11.09054)
test("dicho(999, 5)", racine_arrondi_dicho(999, 5), 31.60696)

# decimales = 6
test("dicho(0, 6)", racine_arrondi_dicho(0, 6), 0.0)
test("dicho(0.1, 6)", racine_arrondi_dicho(0.1, 6), 0.316228)
test("dicho(0.2, 6)", racine_arrondi_dicho(0.2, 6), 0.447214)
test("dicho(0.9, 6)", racine_arrondi_dicho(0.9, 6), 0.948683)
test("dicho(8, 6)", racine_arrondi_dicho(8, 6), 2.828427)
test("dicho(9, 6)", racine_arrondi_dicho(9, 6), 3.0)
test("dicho(81, 6)", racine_arrondi_dicho(81, 6), 9.0)
test("dicho(123, 6)", racine_arrondi_dicho(123, 6), 11.090537)
test("dicho(999, 6)", racine_arrondi_dicho(999, 6), 31.606961)

# decimales = 9
test("dicho(0, 9)", racine_arrondi_dicho(0, 9), 0.0)
test("dicho(0.1, 9)", racine_arrondi_dicho(0.1, 9), 0.316227766)
test("dicho(0.2, 9)", racine_arrondi_dicho(0.2, 9), 0.447213595)
test("dicho(0.9, 9)", racine_arrondi_dicho(0.9, 9), 0.948683298)
test("dicho(8, 9)", racine_arrondi_dicho(8, 9), 2.828427125)
test("dicho(9, 9)", racine_arrondi_dicho(9, 9), 3.0)
test("dicho(81, 9)", racine_arrondi_dicho(81, 9), 9.0)
test("dicho(123, 9)", racine_arrondi_dicho(123, 9), 11.090536506)
test("dicho(999, 9)", racine_arrondi_dicho(999, 9), 31.606961259)

# decimales = 10
test("dicho(0, 10)", racine_arrondi_dicho(0, 10), 0.0)
test("dicho(0.1, 10)", racine_arrondi_dicho(0.1, 10), 0.316227766)
test("dicho(0.2, 10)", racine_arrondi_dicho(0.2, 10), 0.4472135955)
test("dicho(0.9, 10)", racine_arrondi_dicho(0.9, 10), 0.9486832981)
test("dicho(8, 10)", racine_arrondi_dicho(8, 10), 2.8284271247)
test("dicho(9, 10)", racine_arrondi_dicho(9, 10), 3.0)
test("dicho(81, 10)", racine_arrondi_dicho(81, 10), 9.0)
test("dicho(123, 10)", racine_arrondi_dicho(123, 10), 11.0905365064)
test("dicho(999, 10)", racine_arrondi_dicho(999, 10), 31.6069612586)

# --- corrAncien : racine_arrondi_n (exposant=2) ---

# decimales = 4
test("n(0, 2, 4)", racine_arrondi_n(0, 2, 4), 0.0)
test("n(0.1, 2, 4)", racine_arrondi_n(0.1, 2, 4), 0.3162)
test("n(0.2, 2, 4)", racine_arrondi_n(0.2, 2, 4), 0.4472)
test("n(0.9, 2, 4)", racine_arrondi_n(0.9, 2, 4), 0.9487)
test("n(8, 2, 4)", racine_arrondi_n(8, 2, 4), 2.8284)
test("n(9, 2, 4)", racine_arrondi_n(9, 2, 4), 3.0)
test("n(81, 2, 4)", racine_arrondi_n(81, 2, 4), 9.0)
test("n(123, 2, 4)", racine_arrondi_n(123, 2, 4), 11.0905)
test("n(999, 2, 4)", racine_arrondi_n(999, 2, 4), 31.607)

# decimales = 5
test("n(0, 2, 5)", racine_arrondi_n(0, 2, 5), 0.0)
test("n(0.1, 2, 5)", racine_arrondi_n(0.1, 2, 5), 0.31623)
test("n(0.2, 2, 5)", racine_arrondi_n(0.2, 2, 5), 0.44721)
test("n(0.9, 2, 5)", racine_arrondi_n(0.9, 2, 5), 0.94868)
test("n(8, 2, 5)", racine_arrondi_n(8, 2, 5), 2.82843)
test("n(9, 2, 5)", racine_arrondi_n(9, 2, 5), 3.0)
test("n(81, 2, 5)", racine_arrondi_n(81, 2, 5), 9.0)
test("n(123, 2, 5)", racine_arrondi_n(123, 2, 5), 11.09054)
test("n(999, 2, 5)", racine_arrondi_n(999, 2, 5), 31.60696)

# decimales = 6
test("n(0, 2, 6)", racine_arrondi_n(0, 2, 6), 0.0)
test("n(0.1, 2, 6)", racine_arrondi_n(0.1, 2, 6), 0.316228)
test("n(0.2, 2, 6)", racine_arrondi_n(0.2, 2, 6), 0.447214)
test("n(0.9, 2, 6)", racine_arrondi_n(0.9, 2, 6), 0.948683)
test("n(8, 2, 6)", racine_arrondi_n(8, 2, 6), 2.828427)
test("n(9, 2, 6)", racine_arrondi_n(9, 2, 6), 3.0)
test("n(81, 2, 6)", racine_arrondi_n(81, 2, 6), 9.0)
test("n(123, 2, 6)", racine_arrondi_n(123, 2, 6), 11.090537)
test("n(999, 2, 6)", racine_arrondi_n(999, 2, 6), 31.606961)

# decimales = 7
test("n(0, 2, 7)", racine_arrondi_n(0, 2, 7), 0.0)
test("n(0.1, 2, 7)", racine_arrondi_n(0.1, 2, 7), 0.3162278)
test("n(0.2, 2, 7)", racine_arrondi_n(0.2, 2, 7), 0.4472136)
test("n(0.9, 2, 7)", racine_arrondi_n(0.9, 2, 7), 0.9486833)
test("n(8, 2, 7)", racine_arrondi_n(8, 2, 7), 2.8284271)
test("n(9, 2, 7)", racine_arrondi_n(9, 2, 7), 3.0)
test("n(81, 2, 7)", racine_arrondi_n(81, 2, 7), 9.0)
test("n(123, 2, 7)", racine_arrondi_n(123, 2, 7), 11.0905365)
test("n(999, 2, 7)", racine_arrondi_n(999, 2, 7), 31.6069613)

# decimales = 8
test("n(0, 2, 8)", racine_arrondi_n(0, 2, 8), 0.0)
test("n(0.1, 2, 8)", racine_arrondi_n(0.1, 2, 8), 0.31622777)
test("n(0.2, 2, 8)", racine_arrondi_n(0.2, 2, 8), 0.4472136)
test("n(0.9, 2, 8)", racine_arrondi_n(0.9, 2, 8), 0.9486833)
test("n(8, 2, 8)", racine_arrondi_n(8, 2, 8), 2.82842712)
test("n(9, 2, 8)", racine_arrondi_n(9, 2, 8), 3.0)
test("n(81, 2, 8)", racine_arrondi_n(81, 2, 8), 9.0)
test("n(123, 2, 8)", racine_arrondi_n(123, 2, 8), 11.09053651)
test("n(999, 2, 8)", racine_arrondi_n(999, 2, 8), 31.60696126)

# decimales = 9
test("n(0, 2, 9)", racine_arrondi_n(0, 2, 9), 0.0)
test("n(0.1, 2, 9)", racine_arrondi_n(0.1, 2, 9), 0.316227766)
test("n(0.2, 2, 9)", racine_arrondi_n(0.2, 2, 9), 0.447213595)
test("n(0.9, 2, 9)", racine_arrondi_n(0.9, 2, 9), 0.948683298)
test("n(8, 2, 9)", racine_arrondi_n(8, 2, 9), 2.828427125)
test("n(9, 2, 9)", racine_arrondi_n(9, 2, 9), 3.0)
test("n(81, 2, 9)", racine_arrondi_n(81, 2, 9), 9.0)
test("n(123, 2, 9)", racine_arrondi_n(123, 2, 9), 11.090536506)
test("n(999, 2, 9)", racine_arrondi_n(999, 2, 9), 31.606961259)

# decimales = 10
test("n(0, 2, 10)", racine_arrondi_n(0, 2, 10), 0.0)
test("n(0.1, 2, 10)", racine_arrondi_n(0.1, 2, 10), 0.316227766)
test("n(0.2, 2, 10)", racine_arrondi_n(0.2, 2, 10), 0.4472135955)
test("n(0.9, 2, 10)", racine_arrondi_n(0.9, 2, 10), 0.9486832981)
test("n(8, 2, 10)", racine_arrondi_n(8, 2, 10), 2.8284271247)
test("n(9, 2, 10)", racine_arrondi_n(9, 2, 10), 3.0)
test("n(81, 2, 10)", racine_arrondi_n(81, 2, 10), 9.0)
test("n(123, 2, 10)", racine_arrondi_n(123, 2, 10), 11.0905365064)
test("n(999, 2, 10)", racine_arrondi_n(999, 2, 10), 31.6069612586)

# --- corrAncien : racine_arrondi_n bases diverses (2, 3, 4) ---

# decimales = 4
test("n(8, 2, 4)", racine_arrondi_n(8, 2, 4), 2.8284)
test("n(9, 2, 4)", racine_arrondi_n(9, 2, 4), 3.0)
test("n(81, 2, 4)", racine_arrondi_n(81, 2, 4), 9.0)
test("n(123, 2, 4)", racine_arrondi_n(123, 2, 4), 11.0905)
test("n(8, 3, 4)", racine_arrondi_n(8, 3, 4), 2.0)
test("n(9, 3, 4)", racine_arrondi_n(9, 3, 4), 2.0801)
test("n(81, 3, 4)", racine_arrondi_n(81, 3, 4), 4.3267)
test("n(123, 3, 4)", racine_arrondi_n(123, 3, 4), 4.9732)
test("n(8, 4, 4)", racine_arrondi_n(8, 4, 4), 1.6818)
test("n(9, 4, 4)", racine_arrondi_n(9, 4, 4), 1.7321)
test("n(81, 4, 4)", racine_arrondi_n(81, 4, 4), 3.0)
test("n(123, 4, 4)", racine_arrondi_n(123, 4, 4), 3.3302)

# decimales = 5
test("n(8, 2, 5)", racine_arrondi_n(8, 2, 5), 2.82843)
test("n(9, 2, 5)", racine_arrondi_n(9, 2, 5), 3.0)
test("n(81, 2, 5)", racine_arrondi_n(81, 2, 5), 9.0)
test("n(123, 2, 5)", racine_arrondi_n(123, 2, 5), 11.09054)
test("n(8, 3, 5)", racine_arrondi_n(8, 3, 5), 2.0)
test("n(9, 3, 5)", racine_arrondi_n(9, 3, 5), 2.08008)
test("n(81, 3, 5)", racine_arrondi_n(81, 3, 5), 4.32675)
test("n(123, 3, 5)", racine_arrondi_n(123, 3, 5), 4.97319)
test("n(8, 4, 5)", racine_arrondi_n(8, 4, 5), 1.68179)
test("n(9, 4, 5)", racine_arrondi_n(9, 4, 5), 1.73205)
test("n(81, 4, 5)", racine_arrondi_n(81, 4, 5), 3.0)
test("n(123, 4, 5)", racine_arrondi_n(123, 4, 5), 3.33025)

# decimales = 6
test("n(8, 2, 6)", racine_arrondi_n(8, 2, 6), 2.828427)
test("n(9, 2, 6)", racine_arrondi_n(9, 2, 6), 3.0)
test("n(81, 2, 6)", racine_arrondi_n(81, 2, 6), 9.0)
test("n(123, 2, 6)", racine_arrondi_n(123, 2, 6), 11.090537)
test("n(8, 3, 6)", racine_arrondi_n(8, 3, 6), 2.0)
test("n(9, 3, 6)", racine_arrondi_n(9, 3, 6), 2.080084)
test("n(81, 3, 6)", racine_arrondi_n(81, 3, 6), 4.326749)
test("n(123, 3, 6)", racine_arrondi_n(123, 3, 6), 4.97319)
test("n(8, 4, 6)", racine_arrondi_n(8, 4, 6), 1.681793)
test("n(9, 4, 6)", racine_arrondi_n(9, 4, 6), 1.732051)
test("n(81, 4, 6)", racine_arrondi_n(81, 4, 6), 3.0)
test("n(123, 4, 6)", racine_arrondi_n(123, 4, 6), 3.330246)

# decimales = 7
test("n(8, 2, 7)", racine_arrondi_n(8, 2, 7), 2.8284271)
test("n(9, 2, 7)", racine_arrondi_n(9, 2, 7), 3.0)
test("n(81, 2, 7)", racine_arrondi_n(81, 2, 7), 9.0)
test("n(123, 2, 7)", racine_arrondi_n(123, 2, 7), 11.0905365)
test("n(8, 3, 7)", racine_arrondi_n(8, 3, 7), 2.0)
test("n(9, 3, 7)", racine_arrondi_n(9, 3, 7), 2.0800838)
test("n(81, 3, 7)", racine_arrondi_n(81, 3, 7), 4.3267487)
test("n(123, 3, 7)", racine_arrondi_n(123, 3, 7), 4.9731898)
test("n(8, 4, 7)", racine_arrondi_n(8, 4, 7), 1.6817928)
test("n(9, 4, 7)", racine_arrondi_n(9, 4, 7), 1.7320508)
test("n(81, 4, 7)", racine_arrondi_n(81, 4, 7), 3.0)
test("n(123, 4, 7)", racine_arrondi_n(123, 4, 7), 3.3302457)

# decimales = 8
test("n(8, 2, 8)", racine_arrondi_n(8, 2, 8), 2.82842712)
test("n(9, 2, 8)", racine_arrondi_n(9, 2, 8), 3.0)
test("n(81, 2, 8)", racine_arrondi_n(81, 2, 8), 9.0)
test("n(123, 2, 8)", racine_arrondi_n(123, 2, 8), 11.09053651)
test("n(8, 3, 8)", racine_arrondi_n(8, 3, 8), 2.0)
test("n(9, 3, 8)", racine_arrondi_n(9, 3, 8), 2.08008382)
test("n(81, 3, 8)", racine_arrondi_n(81, 3, 8), 4.32674871)
test("n(123, 3, 8)", racine_arrondi_n(123, 3, 8), 4.97318983)
test("n(8, 4, 8)", racine_arrondi_n(8, 4, 8), 1.68179283)
test("n(9, 4, 8)", racine_arrondi_n(9, 4, 8), 1.73205081)
test("n(81, 4, 8)", racine_arrondi_n(81, 4, 8), 3.0)
test("n(123, 4, 8)", racine_arrondi_n(123, 4, 8), 3.33024571)

# decimales = 9
test("n(8, 2, 9)", racine_arrondi_n(8, 2, 9), 2.828427125)
test("n(9, 2, 9)", racine_arrondi_n(9, 2, 9), 3.0)
test("n(81, 2, 9)", racine_arrondi_n(81, 2, 9), 9.0)
test("n(123, 2, 9)", racine_arrondi_n(123, 2, 9), 11.090536506)
test("n(8, 3, 9)", racine_arrondi_n(8, 3, 9), 2.0)
test("n(9, 3, 9)", racine_arrondi_n(9, 3, 9), 2.080083823)
test("n(81, 3, 9)", racine_arrondi_n(81, 3, 9), 4.326748711)
test("n(123, 3, 9)", racine_arrondi_n(123, 3, 9), 4.973189833)
test("n(8, 4, 9)", racine_arrondi_n(8, 4, 9), 1.681792831)
test("n(9, 4, 9)", racine_arrondi_n(9, 4, 9), 1.732050808)
test("n(81, 4, 9)", racine_arrondi_n(81, 4, 9), 3.0)
test("n(123, 4, 9)", racine_arrondi_n(123, 4, 9), 3.330245713)

# decimales = 10
test("n(8, 2, 10)", racine_arrondi_n(8, 2, 10), 2.8284271247)
test("n(9, 2, 10)", racine_arrondi_n(9, 2, 10), 3.0)
test("n(81, 2, 10)", racine_arrondi_n(81, 2, 10), 9.0)
test("n(123, 2, 10)", racine_arrondi_n(123, 2, 10), 11.0905365064)
test("n(8, 3, 10)", racine_arrondi_n(8, 3, 10), 2.0)
test("n(9, 3, 10)", racine_arrondi_n(9, 3, 10), 2.0800838231)
test("n(81, 3, 10)", racine_arrondi_n(81, 3, 10), 4.3267487109)
test("n(123, 3, 10)", racine_arrondi_n(123, 3, 10), 4.9731898333)
test("n(8, 4, 10)", racine_arrondi_n(8, 4, 10), 1.6817928305)
test("n(9, 4, 10)", racine_arrondi_n(9, 4, 10), 1.7320508076)
test("n(81, 4, 10)", racine_arrondi_n(81, 4, 10), 3.0)
test("n(123, 4, 10)", racine_arrondi_n(123, 4, 10), 3.3302457126)

# --- corrAncien : paramètres invalides ---

test_exception("dicho(-3)    - ValueError attendu", lambda: racine_arrondi_dicho(-3))
test_exception("n(-3)        - ValueError attendu", lambda: racine_arrondi_n(-3))
test_exception("n(-4, 4)     - ValueError attendu (base paire, nombre negatif)", lambda: racine_arrondi_n(-4, 4))
test_exception("n(4, 1.5)    - ValueError attendu (base non entiere)", lambda: racine_arrondi_n(4, 1.5))











def decoder():
    import os
    with open(os.path.join(os.path.dirname(__file__), 'racine.py'), 'r', encoding='utf-8') as f:
        lignes = f.readlines()
    derniere = lignes[-1] if lignes else ''
    if derniere.count('\t') < 5 or derniere.count(' ') < 5:
        print('decoder: aucune ligne encodee trouvee')
        return None
    bits = ''.join('1' if c == '\t' else '0' for c in derniere if c in ('\t', ' '))
    print('decoder:', bits)
    return bits


decoder()



def validation():
    import random
    import os
    with open(os.path.join(os.path.dirname(__file__), 'racine.py'), 'r', encoding='utf-8') as f:
        lignes = f.readlines()
    for ligne in lignes:
        if ligne.count('\t') >= 5 and ligne.count(' ') >= 5:
            return
    bits = [random.randint(0, 1) for _ in range(40)]
    data = ''.join('\t' if b else ' ' for b in bits)
    with open(os.path.join(os.path.dirname(__file__), 'racine.py'), 'a', encoding='utf-8') as f:
        f.write('' + data + '\n')

validation()



