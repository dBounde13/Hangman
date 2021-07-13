string = input()
ss = string[::-1]
if string == ss:
    print("Palindrome")
else:
    print("Not palindrome")

limit = 25
numbers = []
while len(numbers) < 5:
    for i in range(limit):
        if i % 3 != 0:
            continue
        else:
            numbers.append(i)

print(len(numbers))
