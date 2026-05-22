
print("methode 1")
incr = 10
resultatComplet = ""
for dec in range(1,20):
    for i in range(1, 10):
        truc = i / incr
        resultatComplet += str(truc)+ " "
        #print(truc)
        if (round(truc, dec) != truc): print("Ouch    ", truc, round(truc, dec))
    incr = incr *10
    resultatComplet = resultatComplet + "\n"
print(resultatComplet)
#
# print("methode 2")
# resultatComplet = ""
# for dec in range(1,20):
#     for i in range(1, 10):
#         truc = i / 10**dec
#         resultatComplet += str(truc)+ " "
#         #print(truc)
#         if (round(truc, dec) != truc): print("Ouch    ", truc, round(truc, dec))
#     resultatComplet = resultatComplet + "\n"
# print(resultatComplet)


print("methode 2")
resultatComplet = ""
for dec in range(1,20):
    for i in range(1, 10):
        truc = i * 10**-dec
        resultatComplet += str(truc) + " "
        #print(truc)
        # if (round(truc, dec) != truc):
        #     print("Ouch    ", truc, round(truc, dec))
        #     print(f"{truc:.50f}")
    resultatComplet = resultatComplet + "\n"
print(resultatComplet)


print("methode 3")
incr = .1
resultatComplet = ""
for dec in range(1,20):
    for i in range(1, 10):
        truc = i * incr
        #print(truc)
        # if (round(truc, dec) != truc):
        #     print("Ouch    ", truc, round(truc, dec))
        #     print(f"{truc:.50f}")
        resultatComplet += str(truc) + " "
    incr = incr /10
    resultatComplet = resultatComplet + "\n"
print(resultatComplet)


print("methode 4") #methode 4 string
resultatComplet = ""
for dec in range(1, 18):
    for i in range(1, 10):
        truc = float("0." + "0" * (dec - 1) + str(i))
        resultatComplet += str(truc) + " "
    resultatComplet = resultatComplet + "\n"
print(resultatComplet)
