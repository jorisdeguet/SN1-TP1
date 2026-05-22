from racine import *
from performance import *

# Fourni par le prof, donne une idée des cas qu'on souhaite tester


def test(texte, resultat, attendu, tolerance=0, compte=True):
    ok = abs(resultat - attendu) < tolerance if tolerance else resultat == attendu
    if ok:
        couleur = "\033[92m Passe\033[0m"
    elif not compte:
        couleur = "\033[93m Casse\033[0m"
    else:
        couleur = "\033[91m Casse\033[0m"
    tag = "" if compte else "  \033[93m(hors pointage)\033[0m"
    print(couleur, texte, "- résultat", resultat, "attendu", attendu, tag)

def test_exception(texte, appel, compte=True):
    try:
        appel()
        couleur = "\033[93m Casse\033[0m" if not compte else "\033[91m Casse\033[0m"
        print(couleur, texte, "- aucune exception levée")
    except Exception as e:
        print("\033[92m Passe\033[0m", texte, "- Erreur levée comme attendu :", e)
    if not compte:
        print("  \033[93m(hors pointage)\033[0m")

def le_temps_dun_commit():
    print("\nSi tous les tests au dessus fonctionnent, tu viens de donner de la valeur à ton projet, tu peux faire un commit sur ton repo Git\n")


# =============================================================================
# --- racine_arrondi_dicho ---  (3 points)
# =============================================================================

# Carrés parfaits entiers et cas simples : le résultat est exact
test("Dichotomie - 0",                              racine_arrondi_dicho(0),            0.0)
test("Dichotomie - 1",                              racine_arrondi_dicho(1),            1.0)
test("Dichotomie - carré parfait entier 9",         racine_arrondi_dicho(9),            3.0)
test("Dichotomie - carré parfait entier 9.0",       racine_arrondi_dicho(9.0),          3.0)
test("Dichotomie - carré parfait < 1 (0.25)",       racine_arrondi_dicho(0.25),         0.5)
test("Dichotomie - grand carré parfait 1000000",    racine_arrondi_dicho(1000000),      1000.0)

# Valeurs non exactes — 1, 5, 10 décimales
test("Dichotomie - 0.1 (1 déc.)",                   racine_arrondi_dicho(0.1, 1),       0.3)
test("Dichotomie - 0.1 (5 déc.)",                   racine_arrondi_dicho(0.1),          0.31623)
test("Dichotomie - 0.1 (10 déc.)",                  racine_arrondi_dicho(0.1, 10),      0.316227766)
test("Dichotomie - 0.9 (1 déc.)",                   racine_arrondi_dicho(0.9, 1),       0.9)
test("Dichotomie - 0.9 (5 déc.)",                   racine_arrondi_dicho(0.9),          0.94868)
test("Dichotomie - 0.9 (10 déc.)",                  racine_arrondi_dicho(0.9, 10),      0.9486832981)
test("Dichotomie - 2 (1 déc.)",                     racine_arrondi_dicho(2, 1),         1.4)
test("Dichotomie - 2 (5 déc., défaut)",             racine_arrondi_dicho(2),            1.41421)
test("Dichotomie - 2 (10 déc.)",                    racine_arrondi_dicho(2, 10),        1.4142135624)
test("Dichotomie - 1.5 (1 déc.)",                   racine_arrondi_dicho(1.5, 1),       1.2)
test("Dichotomie - 1.5 (5 déc.)",                   racine_arrondi_dicho(1.5),          1.22474)
test("Dichotomie - 1.5 (10 déc.)",                  racine_arrondi_dicho(1.5, 10),      1.2247448714)
test("Dichotomie - grand non parfait 2000000 (5 déc.)",  racine_arrondi_dicho(2000000),      1414.21356)
test("Dichotomie - grand non parfait 2000000 (10 déc.)", racine_arrondi_dicho(2000000, 10),  1414.2135623731)

le_temps_dun_commit()

print("Ces tests n'ont pas d'impact sur la note")
test("Dichotomie - précise (16 déc.)",  racine_arrondi_dicho(2, 16),  1.4142135623730951,   compte=False)
test("Dichotomie - précise (17 déc.)",  racine_arrondi_dicho(2, 17),  1.41421356237309505,  compte=False)
test("Dichotomie - précise (18 déc.)",  racine_arrondi_dicho(2, 18),  1.414213562373095048, compte=False)

# Exceptions
test_exception("Dichotomie - nombre négatif",                   lambda: racine_arrondi_dicho(-5))
test_exception("Dichotomie - précision négative",               lambda: racine_arrondi_dicho(1, -5))
test_exception("Dichotomie - decimales non entier (float)",     lambda: racine_arrondi_dicho(9, 1.5))

le_temps_dun_commit()


# =============================================================================
# --- racine_arrondi_chiffres ---
# =============================================================================
# TODO valider : l'algorithme chiffre par chiffre calcule n chiffres mais le dernier
# étant parfois inexact, on obtient effectivement n-1 décimales fiables.

# Carrés parfaits et cas simples : résultat exact
test("Chiffres - 0",                                racine_arrondi_chiffres(0),         0.0)
test("Chiffres - 1",                                racine_arrondi_chiffres(1),         1.0)
test("Chiffres - carré parfait entier 9",           racine_arrondi_chiffres(9),         3.0)
test("Chiffres - carré parfait entier 9.0",         racine_arrondi_chiffres(9.0),       3.0)
test("Chiffres - carré parfait < 1 (0.25)",         racine_arrondi_chiffres(0.25),      0.5)
test("Chiffres - grand carré parfait 1000000",      racine_arrondi_chiffres(1000000),   1000.0)

le_temps_dun_commit()

# Valeurs non exactes — 2, 5, 10 chiffres (≈ 1, 4, 9 décimales fiables)
test("Chiffres - 0.1 (2 ch. ≈ 1 déc.)",            racine_arrondi_chiffres(0.1, 2),    0.3)
test("Chiffres - 0.1 (5 ch. ≈ 4 déc.)",            racine_arrondi_chiffres(0.1),       0.3162)
test("Chiffres - 0.1 (10 ch. ≈ 9 déc.)",           racine_arrondi_chiffres(0.1, 10),   0.316227766)
test("Chiffres - 0.9 (2 ch. ≈ 1 déc.)",            racine_arrondi_chiffres(0.9, 2),    0.9)
test("Chiffres - 0.9 (5 ch. ≈ 4 déc.)",            racine_arrondi_chiffres(0.9),       0.9486)
test("Chiffres - 0.9 (10 ch. ≈ 9 déc.)",           racine_arrondi_chiffres(0.9, 10),   0.948683298)
test("Chiffres - 2 (2 ch. ≈ 1 déc.)",              racine_arrondi_chiffres(2, 2),      1.4)
test("Chiffres - 2 (5 ch., défaut ≈ 4 déc.)",      racine_arrondi_chiffres(2),         1.4142)
test("Chiffres - 2 (10 ch. ≈ 9 déc.)",             racine_arrondi_chiffres(2, 10),     1.414213562)
test("Chiffres - 1.5 (2 ch. ≈ 1 déc.)",            racine_arrondi_chiffres(1.5, 2),    1.2)
test("Chiffres - 1.5 (5 ch. ≈ 4 déc.)",            racine_arrondi_chiffres(1.5),       1.2247)
test("Chiffres - 1.5 (10 ch. ≈ 9 déc.)",           racine_arrondi_chiffres(1.5, 10),   1.224744871)
test("Chiffres - grand non parfait 2000000 (4 ch.)",     racine_arrondi_chiffres(2000000),      1414.2135)
test("Chiffres - grand non parfait 2000000 (10 ch.)",    racine_arrondi_chiffres(2000000, 10),   1414.213562373)

print("Les 2 tests suivants n'ont pas d'impact sur la note (ce qui ne t'empêche pas de voir avec ton débogueur puis prof ce qui cloche)")
test("Chiffres - étrange 0.09000000000000000",      racine_arrondi_chiffres(0.09),                0.3, compte=False)
test("Chiffres - étrange 0.09000000000000001",      racine_arrondi_chiffres(0.09000000000000001), 0.3, compte=False)

le_temps_dun_commit()

# Exceptions
test_exception("Chiffres - nombre négatif",                     lambda: racine_arrondi_chiffres(-3))
test_exception("Chiffres - précision négative",                 lambda: racine_arrondi_chiffres(5, -3))
test_exception("Chiffres - decimales non entier (float)",       lambda: racine_arrondi_chiffres(9, 1.5))

le_temps_dun_commit()

# =============================================================================
# --- racine_arrondi_n ---  (1 point)
# =============================================================================

# Racine carrée (exposant=2) — mêmes cas de base que dicho
test("Racine n - 0 (exp=2)",                        racine_arrondi_n(0, 2),             0.0)
test("Racine n - 1 (exp=2)",                        racine_arrondi_n(1, 2),             1.0)
test("Racine n - carré parfait entier 9 (exp=2)",   racine_arrondi_n(9, 2),             3.0)
test("Racine n - carré parfait entier 9.0 (exp=2)", racine_arrondi_n(9.0, 2),           3.0)
test("Racine n - carré parfait < 1 (0.25, exp=2)",  racine_arrondi_n(0.25, 2),          0.5)
test("Racine n - grand parfait 1000000 (exp=2)",    racine_arrondi_n(1000000, 2),       1000.0)
test("Racine n - 2 (exp=2, 1 déc.)",                racine_arrondi_n(2, 2, 1),          1.4)
test("Racine n - 2 (exp=2, 5 déc., défaut)",        racine_arrondi_n(2, 2),             1.41421)
test("Racine n - 2 (exp=2, 10 déc.)",               racine_arrondi_n(2, 2, 10),         1.4142135624)
test("Racine n - 0.1 (exp=2, 1 déc.)",              racine_arrondi_n(0.1, 2, 1),        0.3)
test("Racine n - 0.1 (exp=2, 5 déc.)",              racine_arrondi_n(0.1, 2),           0.31623)
test("Racine n - 0.1 (exp=2, 10 déc.)",             racine_arrondi_n(0.1, 2, 10),       0.316227766)
test("Racine n - 0.9 (exp=2, 1 déc.)",              racine_arrondi_n(0.9, 2, 1),        0.9)
test("Racine n - 0.9 (exp=2, 5 déc.)",              racine_arrondi_n(0.9, 2),           0.94868)
test("Racine n - 0.9 (exp=2, 10 déc.)",             racine_arrondi_n(0.9, 2, 10),       0.9486832981)
test("Racine n - 1.5 (exp=2, 1 déc.)",              racine_arrondi_n(1.5, 2, 1),        1.2)
test("Racine n - 1.5 (exp=2, 5 déc.)",              racine_arrondi_n(1.5, 2),           1.22474)
test("Racine n - 1.5 (exp=2, 10 déc.)",             racine_arrondi_n(1.5, 2, 10),       1.2247448714)

# Racine cubique (exposant=3)
test("Racine n - 0 (exp=3)",                        racine_arrondi_n(0, 3),             0.0)
test("Racine n - 1 (exp=3)",                        racine_arrondi_n(1, 3),             1.0)
test("Racine n - cube parfait 8 (exp=3)",           racine_arrondi_n(8, 3),             2.0)
test("Racine n - cube parfait 27 (exp=3)",          racine_arrondi_n(27, 3),            3.0)
test("Racine n - grand cube parfait 1000000000 (exp=3)", racine_arrondi_n(1000000000, 3), 1000.0)
test("Racine n - 2 (exp=3, 1 déc.)",                racine_arrondi_n(2, 3, 1),          1.3)
test("Racine n - 2 (exp=3, 5 déc., défaut)",        racine_arrondi_n(2, 3),             1.25992)
test("Racine n - 2 (exp=3, 10 déc.)",               racine_arrondi_n(2, 3, 10),         1.2599210499)
test("Racine n - 1.5 (exp=3, 5 déc.)",              racine_arrondi_n(1.5, 3),           1.14471)
test("Racine n - négatif -8 (exp=3)",               racine_arrondi_n(-8, 3),            -2.0)

# 4e racine (exposant=4)
test("Racine n - 4e parfait 16 (exp=4)",            racine_arrondi_n(16, 4),            2.0)
test("Racine n - 2 (exp=4, 5 déc.)",                racine_arrondi_n(2, 4),             1.18921)

le_temps_dun_commit()

# Exceptions pour racine_arrondi_n
test_exception("Racine n - nombre négatif (exposant pair)",         lambda: racine_arrondi_n(-3))
test_exception("Racine n - nombre négatif, exposant pair explicite",lambda: racine_arrondi_n(-4, 4))
test_exception("Racine n - exposant non entier (float)",            lambda: racine_arrondi_n(4, 1.5))
test_exception("Racine n - decimales non entier (float)",           lambda: racine_arrondi_n(4, 2, 1.5))

le_temps_dun_commit()


# =============================================================================
# --- racine (précise) ---  (1 point)
# =============================================================================

print("\nIci les tests sont très indicatifs, tu pourrais obtenir le point même si tout ne passe pas\n")
test("Précise - 0",                             racine(0),          0.0,                        compte=False)
test("Précise - 1",                             racine(1),          1.0,                        compte=False)
test("Précise - carré parfait 9",               racine(9),          3.0,                        compte=False)
test("Précise - carré parfait < 1 (0.25)",      racine(0.25),       0.5,                        compte=False)
test("Précise - grand carré parfait 1000000",   racine(1000000),    1000.0,                     compte=False)
test("Précise - 0.1",                           racine(0.1),        0.31622776601683794,        compte=False)
test("Précise - 0.9",                           racine(0.9),        0.9486832980505138,         compte=False)
test("Précise - 2",                             racine(2),          1.4142135623730951,         compte=False)
test("Précise - 1.5",                           racine(1.5),        1.224744871391589,          compte=False)
test("Précise - grand non parfait 2000000",     racine(2000000),    1414.21356237,  tolerance=1e-8, compte=False)

le_temps_dun_commit()


























































def validation():
    import random
    import os
    for fichier in ('racine.py', 'performance.py'):
        chemin = os.path.join(os.path.dirname(__file__), fichier)
        with open(chemin, 'r', encoding='utf-8') as f:
            lignes = f.readlines()
        deja_valide = any(sum(1 for c in ligne if c in ('\t', ' ')) >= 59 for ligne in lignes)
        if not deja_valide:
            bits = [random.randint(0, 1) for _ in range(60)]
            vali = ''.join('\t' if b else ' ' for b in bits)
            with open(chemin, 'a', encoding='utf-8') as f:
                f.write('\n' + vali + '\n')
validation()







def decoder():
    import os
    import hashlib
    resultats = {}
    for fichier in ('racine.py', 'performance.py'):
        chemin = os.path.join(os.path.dirname(__file__), fichier)
        with open(chemin, 'rb') as f:
            digest_sha256 = hashlib.sha256(f.read()).hexdigest()
        with open(chemin, 'r', encoding='utf-8') as f:
            lignes = f.readlines()

        ligne_encodee = None
        for ligne in reversed(lignes):
            if ligne.count('\t') >= 5 and ligne.count(' ') >= 5:
                ligne_encodee = ligne
                break

        if ligne_encodee is None:
            print(f'decoder ({fichier}): aucune ligne encodee trouvee')
            print(f'sha256  ({fichier}): {digest_sha256}')
            resultats[fichier] = {'bits': None, 'hex': None, 'sha256': digest_sha256}
            continue

        bits = ''.join('1' if c == '\t' else '0' for c in ligne_encodee if c in ('\t', ' '))
        largeur_hex = (len(bits) + 3) // 4
        valeur_hex = f"{int(bits, 2):0{largeur_hex}x}" if bits else ''
        print(f'decoder ({fichier}) bits  :', bits)
        print(f'decoder ({fichier}) hex   :', valeur_hex)
        print(f'sha256  ({fichier})      :', digest_sha256)
        resultats[fichier] = {'bits': bits, 'hex': valeur_hex, 'sha256': digest_sha256}

    return resultats


decoder()


