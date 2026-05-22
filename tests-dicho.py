

def dicho(nombre):
    if nombre < 0: raise ValueError
    if nombre == 0: return 0
    if nombre == 1: return 1
    min = 0
    max = nombre if nombre > 1 else 1
    while min < max:
        mil = (min + max) / 2
        if mil * mil > nombre:
            max = mil
        else:
            min = mil
        print(min, max)
    # print(min, min*min, nombre)
    return min

def dichoFini(nombre):
    if nombre < 0: raise ValueError
    if nombre == 0: return 0
    if nombre == 1: return 1
    min = 0
    max = nombre if nombre > 1 else 1
    while min != (min + max) / 2 and  max != (min + max) / 2:
        mil = (min + max) / 2
        if mil * mil > nombre:
            max = mil
        else:
            min = mil
        #print(min, max)
    print(min, min*min,  max, max*max,  (min + max) / 2, ((min + max) / 2)* ((min + max) / 2), nombre)
    return (min + max) / 2 # pourrait retourner 2 valeurs min ou max > accepte delta

dichoFini(2)

#dicho(2)