userNumber = int(input("Give me your number: "))

result = 0

for number in range(0, userNumber):
    if number % 3 == 0 or number % 5 == 0:
        result += number

print(result)
