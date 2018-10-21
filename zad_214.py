line = "Lorem ipsum dolor sit amet consectetur adipiscing elit"

longest_word =""

for word in line.split():
    if len(longest_word) < len(word):
        longest_word = word

print(longest_word)
print(len(longest_word))