expense = [2200, 2350, 2600, 2130, 2190]

extra = expense[1] - expense[0]
tot = 0
for i in range(len(expense)):
    if i < 3:
        tot += expense[i]
    else:
        break


def exact(expense):
    return 2000 in expense


expense.append(1980)

print(extra)
print(tot)
print(exact(expense))
print(expense)
expense[3] = expense[3] - 200
print(expense)
