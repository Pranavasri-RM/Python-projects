import random 
from art import logo

EASY_LEVEL_TRIES = 10
HARD_LEVEL_TRIES = 5

#function to set difficulty
def set_difficulty():
  diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if diff == 'easy':
    return EASY_LEVEL_TRIES
  elif diff == 'hard':
    return HARD_LEVEL_TRIES
  else:
    print("Invalid choice.")
    
#function to check answer
def check_answer(guess, answer, tries):
  if guess < answer:
    print("Too Low.")
    return tries-1
  elif guess > answer:
    print("Too High.")
    return tries-1
  else:
    print(f"You got it! The answer was {answer}.")


def game():
  
  print(logo)
  
  #Randomly selecting answer
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  
  answer = random.randint(1, 100)
  
  tries = set_difficulty()

  guess = 0
  
  while guess != answer:
    print(f"You have {tries} attempts remaining to guess the number.")
    
    #user's guess
    guess = int(input("Make a guess: "))
    
    tries = check_answer(guess, answer, tries)

    if tries == 0:
      print("You have run out of guesses. You lose!")
      return
    else:
      if guess != answer:
        print("Guess again.")

game()