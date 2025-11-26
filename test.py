numbers = list(range(1, 5000))
total = 0

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            total += numbers[j]

print(total)
