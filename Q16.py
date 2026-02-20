num = 153
num2 = str(num)
n = len(num2)
sum = 0

for i in num2:
    sum += int(i) ** n

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")