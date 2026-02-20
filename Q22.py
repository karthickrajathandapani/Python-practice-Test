a = "madam"
rev = ""

for char in a:
    rev = char + rev

if rev == a:
    print("Palindrome")
else:
    print("Not Palindrome")
  