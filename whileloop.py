num = int(input("Enter number: "))
fact = 1
if (num == 1 or num <= 0):
    fact = 1
else:
    while (num > 1):
        fact = fact * num
        num -= 1


print("factorial is", fact)
