a = float(input("Podaj długosć boku A: "))
b = float(input("Podaj długość boku B: "))
c = float(input("Podaj dułgość boku C: "))

lista = [a,b,c]
lista.sort()
for liczba in lista:
    print(liczba)
print(end='')

a1 = lista[0]
b1 = lista[1]
c1 = lista[2]

if a1+b1 <= c1:
    print ("Trójkąt ma nieodpowiednie wymiary",end='')
else:
    print("Trójkat ma odpowiednie wymiary")

if (a1*a1) + (b1*b1) == c1*c1:
    print("Ten trójkąt jest trójkątem pitagorejskim")
else:
    print("Ten trójkąt nie jest trójkątem pitagorejskim")
