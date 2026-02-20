a = "12321"
b = str(a)
print(b[::-1] == str(a))

#using loop
a = "madam"
rev = ""

for char in a:
    rev = char + rev

if rev == a:
    print("Palindrome")
else:
    print("Not Palindrome")
