t = input("the value of the character is:")

for i in t:
    print(i)

for i in range(len(t)):
    print(t[i])


# complex on for loop side

a = input("define the character for loop program:")


for i in range(len(a)):
    if i % 2 != 0:
        print(a[i])

    else:
        print(f"odd index: {a[i]}")

t = 5

for i in a:
    if i % 2 == 0:
        print("it's event no")

