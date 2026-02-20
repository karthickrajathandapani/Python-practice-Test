n = 12345

sum = sum(map(int, str(n)))
print(sum)

total = 0

for digit in str(n):
    total += int(digit)

print(total)
