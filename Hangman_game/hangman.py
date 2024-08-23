import random

words = ['python', 'java', 'kotlin', 'javascript', 'ruby','swift']

# Randomly choose a word from the list
chosen_word = random.choice(words)
# print(chosen_word)
# Create a list of underscores
word_display = ['_' for _ in chosen_word]
attempts = 8 

print("Welcome to Hangman!")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display) + "\n")
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess # Reveal letter
    else:
        print("WRONG! The letter doesn't appear in the word.")
        attempts -= 1
        
# Game conclusion
if '_' not in word_display:
    print("You guessed the word!")
    print(' '.join(word_display))
    print("You survived!")
else:
    print("You ran out of attempts. The word was: " + chosen_word)
    print("You lost!!")