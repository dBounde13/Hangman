string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = "a", "e", "i", "o", "u"

count = 0
for i in string:
    if i in vowels:
        count += 1
print(count)
