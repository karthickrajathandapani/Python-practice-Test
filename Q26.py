text = input("Enter the string:")
frequency = {}
for ch in text:
    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1
print("Character frequency:")
for key in frequency:
    print(key, ":", frequency[key])