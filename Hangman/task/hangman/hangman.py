import random

print("H A N G M A N")
word_list = ['python', 'java', 'kotlin', 'javascript']
while True:
    action = input('Type "play" to play the game, "exit" to quit:')
    if action == 'exit':
        break
    word = random.choice(word_list)
    attempt = 0

    hint = ["-"] * len(word)
    guesses = set()

    while attempt < 8:
        print()
        print(''.join(hint))
        guess = input("Input a letter: ")
        if len(guess) > 1:
            print('You should input a single letter')
            continue

        if not guess.islower() or not guess.isalpha():
            print('Please enter a lowercase English letter')
            continue

        if guess in guesses:
            print("You've already guessed this letter")
            continue

        if word.find(guess) > -1:
            hint[word.find(guess)] = guess
            if ''.join(hint) == word:
                break
            attempt -= 1
        else:
            print("That letter doesn't appear in the word")

        guesses.add(guess)
        attempt += 1

    if ''.join(hint) == word:
        print(word)
        print('You guessed the word!')
        print('You survived!')
    else:
        print("You lost!")
