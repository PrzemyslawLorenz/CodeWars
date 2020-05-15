def tickets(people):
    bills = {
        25: 0,
        50: 0,
        100: 0
    }

    for bill in people:
        if bill == 25:
            bills[25] += 1
        if bill == 50:
            if bills[25] == 0:
                return "NO"
            else:
                bills[25] -= 1
                bills[50] += 1
        if bill == 100:
            if bills[50] == 0 and bills[25] < 3 or bills[25] == 0:
                return "NO"
            if bills[50] >= 1 and bills[25] >= 1:
                bills[50] -= 1
                bills[25] -= 1
                bills[100] += 1
            elif bills[50] == 0 and bills[25] >= 3:
                bills[25] -= 3
                bills[100] += 1

    return "YES"


print(tickets([25, 25, 50]))  # => YES
# => NO. Vasya will not have enough money to give change to 100 dollars
print(tickets([25, 100]))
# => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
print(tickets([25, 25, 50, 50, 100]))
