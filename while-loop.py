num = int(input("enter the num between 0 - 10:"))

while num < 1 or num > 10:
    print("your no is valid")
    num = int(input("enter the num between 1 to 10:"))

print(f"you number is {num}")