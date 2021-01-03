liste1 = []
liste2 = []
liste3 = []
liste4 = []

for x in range(1,100):
    if x % 15 == 0:
        liste1.append(x)

for y in range(1,31):
    if y % 5 == 0:
        liste2.append(y)

for z in range(100,49,-1):
    if z % 10 == 0:
        liste3.append(z)

for k in range(2,65):
    if k % 2 == 0:
        liste4.append(k)

for n in range(6):
    print(liste1[n],liste2[n],liste3[n],liste4[n])
# print(l1[0],l2[0],l3[0],l4[0])    
# print(l1[1],l2[1],l3[1],l4[1])
# print(l1[2],l2[2],l3[2],l4[2])
# print(l1[3],l2[3],l3[3],l4[3])
# print(l1[4],l2[4],l3[4],l4[4])
# print(l1[5],l2[5],l3[5],l4[5])
