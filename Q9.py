a = int(input("Enter the table:"))
b = int(input("Enter the table count:"))
for i in range(1, b+1):
    c = i * a
    print(i, "x", a, "=", c)
    i += 1