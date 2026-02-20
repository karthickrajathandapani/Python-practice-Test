def count_words(sentence):
    words = sentence.split()
    count_dict = {}

    for word in words:
        if word in count_dict:
            count_dict[word] = count_dict[word] + 1
        else:
            count_dict[word] = 1
            
    return count_dict

text = input("Enter a sentence: ")

result = count_words(text)

print("Word occurrences:")
for key in result:
    print(key, ":", result[key])
