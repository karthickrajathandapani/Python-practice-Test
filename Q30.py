a = [10, 60, 15, 20, 35, 5]
min = a[0]
max = a[0]
for b in a:
    if max > b:
        max = b
    elif min < b:
        min = b
print(max)
print(min)
        