def anagram(text1, text2):
    text1 = text1.lower()
    text2 = text2.lower()

    if sorted(text1) == sorted(text2):
        print("Anagram")
    else:
        print("Not Anagram")

text1 = input("Enter the 1st text: ")
text2 = input("Enter the 2nd text: ")

anagram(text1, text2)