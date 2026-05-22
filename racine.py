import math


def racine_arrondi_dicho(nombre, decimales = 5):
  """
     dichotomie

     Parameters:
     a (int/float): The first number to multiply.
     b (int/float): The second number to multiply.

     Returns:
     int/float: The product of a and b.
     """
  # ici on va programmer la racine du nombre arrondi à un certain nombre de décimales
  # le fonctionnement correct de cette fonction vaut pour 3 points
  if nombre == 0: return 0
  if nombre == 1: return 1
  min = 0
  max = nombre if nombre > 1 else 1
  # print(min, max)
  while min < max:
    mil = (min + max) / 2
    if (round(min, decimales) == round(max, decimales)): return round(min, decimales)
    if (mil == max or mil == min):
      # plus de précision en stock avec float
      return min
    if mil * mil > nombre:
      max = mil
    else:
      min = mil
    # print(min, max)
  # print(min, min*min, nombre)
  return min


def _partieEntiere(nombre):
  res = 0
  # partie entière
  while res**2 < nombre:
    res += 1
  if (res*res) == nombre: return res
  return res - 1

def racine_arrondi_chiffres(nombre, decimales=5):
  # Handle negative numbers immediately
  if nombre < 0:
    return -1.0
  if nombre == 0: return 0.0
  # 1. Approach the integer part (by under)
  integer_part = 0
  while (integer_part + 1) ** 2 <= nombre:
    integer_part += 1

  current_value = float(integer_part)

  # 2. Approach each decimal place by testing 0 through 9
  for position in range(1, decimales + 1):
    step = 10 ** (-position)

    # Test increments from 1 to 9 for the current decimal place
    for digit in range(1, 11):
      next_value = current_value + step

      if next_value ** 2 <= nombre:
        current_value = next_value
      else:
        # As soon as it exceeds, we stop incrementing this decimal place
        break

  # Rounding to the requested number of decimals to avoid floating-point artifacts
  return round(current_value, decimales)

# def racine_arrondi_chiffres(nombre, decimales = 5):
#   if nombre == 0: return 1
#   if nombre == 1: return 1
#   res = _partieEntiere(nombre)
#   if (res * res) == nombre: return res  # gère les racines entières
#   # partie entière
#   for position in range(2, decimales + 1):
#     if (res * res) == nombre:
#       return res
#     prochain_chiffre = _trouver_prochain_chiffre(nombre, res, position)
#     #if prochain_chiffre == 0 and res == prochain_chiffre * 10 ** -(position-1) + res:
#     #  return res  # si le chiffre est 0 ou si j'ai atteint la limite de précision float
#     res += prochain_chiffre * 10 ** -(position-1)
#
#   return round(res, decimales)

def _trouver_prochain_chiffre(nombre, base, position):
  for i in range(1, 10):
    delta = i * 10 ** -(position-1)
    # print(delta)
    candidat = base + delta
    carre = candidat * candidat
    if carre > nombre: return i - 1
  return 9

def racine_arrondi_n(nombre, exposant=2,  decimales = 5):
  """dichotomie"""
  # ici on va programmer la racine du nombre arrondi à un certain nombre de décimales
  # le fonctionnement correct de cette fonction vaut pour 1 point
  if exposant == 0: return nombre
  if exposant < 0: raise ValueError
  if nombre < 0 and exposant % 2 == 0: raise ValueError
  if nombre == 0: return 0
  if nombre == 1: return 1
  mini = min(nombre, 1) if nombre < 0 else 0
  maxi = max(nombre, 1) if nombre >= 0 else 0
  # print(min, max)
  while mini < maxi:
    mil = (mini + maxi) / 2
    if (round(mini, decimales) == round(maxi, decimales)): return round(mini, decimales)
    if (mil == maxi or mil == mini):
      # plus de précision en stock avec float
      return mini
    if abs(mil **exposant) > abs(nombre):
      maxi = mil
    else:
      mini = mil
    # print(min, max)
  # print(min, min*min, nombre)
  return mini

def racine(nombre):
  if nombre == 0: return 0
  if nombre == 1: return 1
  min = 0
  max = nombre if nombre > 1 else 1
  # print(min, max)
  while min < max:
    mil = (min + max) / 2
    if (mil == max or mil == min):
      # print(min, max, max*max, min * min, nombre)
      return min
    if mil * mil > nombre:
      max = mil
    else:
      min = mil
    # print(min, max)
  # print(min, min*min, nombre)
  return min
 	    	 		   		  						 				 	  	   	  			 	       	      	 
