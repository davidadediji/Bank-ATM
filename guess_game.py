#set attempts for difficulty
import random
import math



EASY_ATTEMPT = 10
HARD_ATTEMPT = 5
answer = random.randint(1, 100)


print('Welcome to the guessing game')
print("I'm thinking of a number between 1 and 100")

def check_answer(guess, answer):
  if guess < answer:
    print("Too low")
  elif guess > answer:
    print("Too high")
  else:
    print(f"You got it the answer was {answer}")
    
def set_difficulty():
  level = input("choose difficulty: ")
  if level == 'easy':
    return EASY_ATTEMPT
  else:
    return HARD_ATTEMPT





#make functionality to set difficulty


#let the user guess a number
guess = int(input("Make a guess: "))

turns = set_difficulty()



  

