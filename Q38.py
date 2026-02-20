data = {
    "a": 10,
    "b": 25,
    "c": 15,
    "d": 30
}

max_key = None
max_value = 0

for key in data:
    if data[key] > max_value:
        max_value = data[key] 
        max_key = key

print("Key with maximum value:", max_key)
print("Maximum value:", max_value)
