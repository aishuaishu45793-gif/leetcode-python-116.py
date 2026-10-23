# Count Character Occurrences

def count_characters(text):
    frequency = {}

    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


text = input("Enter a string: ")
result = count_characters(text)

print("Character frequencies:")

for char, count in result.items():
    print(char, ":", count)