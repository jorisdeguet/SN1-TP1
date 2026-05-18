import math
import sys

from racine import *
# A compléter par vous, changez, ajoutez des cas pour pouvoir tester souvent votre code.

b = 2
a = b = 3
c = b == 2
print(sys.float_info.max)
racine_arrondi_n(-8, 3)

# un premier test la racine de 9 devrait être 3
resultat = racine_arrondi_chiffres(9)
print(resultat)
print(" réussite ? ", resultat == 3.0)

#print(racineArrondiDicho(2, 5), " devrait être proche de ", 1.41421, " réussite ? ", racineArrondiDicho(2, 5) == 1.41421) # la racine de 2 1.41421 avec 5 décimales
#print(racineArrondiDicho(2, 4), " devrait être proche de ", 1.4142, " réussite ? ", racineArrondiDicho(2, 5) == 1.4142)  # la racine de 2 1.4142 avec 4


print(math.sqrt(2))