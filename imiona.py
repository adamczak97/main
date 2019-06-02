imiona = ['Jan','Daga','Michał','Adam','Julia','Marcin']
x = len(imiona)
print(x)
#podane = input("Podaj imie")

def wyswietl(num1,*args):
    print(f'Liczba 1: {num1}')

    for i in args:
        print(f'Nastepna wartosc : {i}')

#wyswietl(2,4,5,6,7,44)



#imiona = ['Anna','Jan','Paweł']
#wyswietl(*imiona)

def pracownik(**kwargs):
    for key,val in kwargs.items():
        print(f'Klucz:{key}\nWartość :{val}')

pracownik1 = {
'imie':'Janusz',
'nazwisko':'Pawlacz',
'wiek':50,
'umowaOprace':True
}

pracownik(**pracownik1)
