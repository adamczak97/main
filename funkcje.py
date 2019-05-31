def c_mniejsze(x,y):
    wynik = (x*x) + y
    print("Wynik to: ", wynik)

def c_wieksze(x,y):
    wynik = x - (y*y)
    print("Wynik to: ", wynik)

def c_rowne(x,y):
    wynik = 1/(x-y)
    print("Wynik to: ", wynik)

def dzielenie_przez_0(x,y):
        print("Próba dzielenia przez zero")

a = float(input("Podaj A: "))
b = float(input("Podaj B: "))
c = int(input("Podaj C: "))

if c > 0:
    c_mniejsze(a,b)
elif c < 0:
    c_wieksze(a,b)
elif c==0 and b-a !=0 or a-b!=0:
    c_rowne(a,b)
elif b-a == 0 or a-b == 0:
    dzielenie_przez_0(a,b)
