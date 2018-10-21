line = "Lorem ipsum dolor sit amet consectetur adipiscing elit"
first = ""
last = ""
for word in line.split():
    first += word[0]
    last += word[-1:]

print(first)
print(last)