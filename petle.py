fruits = ['apple','orange','pear','banana','apple']

print("START")
for i,fruit in enumerate(fruits):
    print("Sprawdzam ->",i)
    if i==3:
        print("TUTAJ")
        break
    print(i,":",fruit)

print("KONIEC")
