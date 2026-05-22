import math

def chiffres(n):
    res = 0.0
    while (res+1)**2 < n:
        res += 1
    incr = 10
    resultatComplet = ""
    for dec in range(1, 20): # pourquoi on s'arreterait
        for i in range(0, 10):
            truc = i / incr
            if (res+truc)**2 > n: # c'est là que ça pète?
                res = res+ (i-1) /incr
                break
            resultatComplet += str(truc) + " "
            # print(truc)
        incr = incr * 10
        resultatComplet = resultatComplet + "\n"
    #print(resultatComplet)
    return res


print(chiffres(2), math.sqrt(2))