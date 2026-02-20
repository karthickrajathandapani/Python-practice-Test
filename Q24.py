text = input("Enter a string: ")

result = ""

for ch in text:
    if ch >= 'a' and ch <= 'z':   # check if lowercase
        result = result + chr(ord(ch) - 32) #
    else:
        result = result + ch      # keep other characters same

print("Uppercase string:", result)
