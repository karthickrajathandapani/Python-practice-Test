text = input("Enter a string: ")

vowels = 0
consonants = 0

for char in text:
    if char.isalpha():   # Check if character is a letter
        if char.lower() in "aeiou": #Convert the "text" in lower case format
            vowels += 1
        else:
            consonants += 1 #Except vowels or consonants

print("Vowels:", vowels)
print("Consonants:", consonants)

