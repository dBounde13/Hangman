import random

print('H A N G M A N\n')
user_type = input(f'Type "play" to play the game, "exit" to quit: ')
print()
while user_type == 'exit':
    break

words_list = ['python', 'java', 'kotlin', 'javascript']
word = list(random.choice(words_list))
guesses = list('-' * len(word))
print(''.join(guesses))

count = 8
tried_letter = []
while count > 0:
    print()
    print(''.join(guesses))
    user_letter = input('Input a letter: ')
    if len(user_letter) != 1:
        print("You should input a single letter")
        tried_letter.append(user_letter)
        continue
    elif not user_letter.islower() or not user_letter.isalpha():
        print("Please enter a lowercase English letter")
        tried_letter.append(user_letter)
        continue
    elif user_letter in guesses or user_letter in tried_letter:
        print("You've already guessed this letter")
        continue
    elif user_letter in word and user_letter not in guesses:
        for i in range(len(word)):
            if user_letter == word[i]:
                guesses[i] = user_letter
                if "-" not in guesses:
                    print("You guessed the word!")
                    print("You survived!")
                    exit()
    else:
        print("That letter doesn't appear in the word")
        tried_letter.append(user_letter)
        count -= 1
        if count == 0:
            print("You lost!")
