num = int(input("Enter max number: "))
odd = []

for i in range(1, num):
    if i % 2 == 1:
        odd.append(i)
print(odd)
