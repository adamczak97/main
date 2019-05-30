fruits = ['apple','orange','pear','banana','apple']

print("START")
for i,fruit in enumerate(fruits):
    print("Sprawdzam ->".format())
    print(i)
    if i==3:
        break
    print(i,":",fruit)

print("KONIEC")
print(i)
