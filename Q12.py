a = 100
count = 0

for i in range(1, a + 1):
    if i % 2 == 0:
        print(i)
        count += 1

print("Total even numbers =", count)