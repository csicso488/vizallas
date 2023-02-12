file=open("viz.txt","r",encoding='UTF-8',)
file2=open("vizkeres.txt","w",encoding='UTF-8',)

lista=[]

for i in file:
    if i[-1] == "\n":
        lista.append(i[:-1].split("\t"))
    else:
        lista.append(i[:-1].split("\t"))

del lista[0]


#1feladat
városok = []
for i in range(len(lista)):
    városok.append(lista[i][2])

print(len(lista))

#4

osszeg = 0
Tisza = []
for i in range(len(lista)):
    if lista[i][3] == "Tisza":
        osszeg += int(lista[i][1])
        Tisza.append(lista[i][3])

darabszám = len(Tisza)
print("A Tisza átlag mélysége: ", round(osszeg / darabszám,2))

#5 

print("Kérem a dátumot két számjeggyel adja meg. Például ha elsejét szeretne irni akkor igy tegye meg: 01")

január = input("adja meg a januári napot: ")
év_hónap = "2000.01."
mindenegyben = év_hónap + január

for i in range(len(lista)):
    if mindenegyben == (lista[i][0]):
        file2.write("" + lista[i][1] + ":" + " " + lista[i][2] + " ")