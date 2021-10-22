#Number Guessing Game Objectives:
from art import logo
from replit import clear
import random
print(logo)



def turns_left(turns, guess, didWin, didGameEnd):
  #global didGameEnd
  if didWin == False:
    turns -= 1
  if turns <= 0: didGameEnd = True
  return turns, didGameEnd

def make_a_guess(turns, answer):
  if turns == 1: print("last guess")
  didWin = False
  guess = int(input("Submit a guess between 1 and 100:  "))
  if guess == answer:
    didWin = True
    result = "spot on"
  elif guess < answer:
    result = "too low"
  elif guess > answer:
    result = "too high"
  return guess, result, didWin

def difficulty():
  didWin = False
  didGameEnd = False
  guess_list = []
  guess_list_x = ["X"]
  difficulty = (input("Would you like to play hard or easy? [easy] ") or "easy").lower()
  clear()
  if difficulty == "easy": turns = 10
  elif difficulty == "hard": turns = 5
  else: turns = 10
  answer = random.choice(list(range(1,101))) #change to choice for range , list = range then choice
  return turns, answer, didWin, didGameEnd, guess_list, guess_list_x

def guess_list_maker(guess, guess_list, answer):
  guess_list.append(guess)
  guess_list.sort()
  guess_list_x = guess_list[:]
  #global answer
  guess_list_x.append(answer)
  guess_list_x.sort()
  index = guess_list_x.index(answer)
  guess_list_x[index] = "X"
  return guess_list, guess_list_x

def guess_again():
  turns, answer, didWin, didGameEnd, guess_list, guess_list_x = difficulty()
  while didWin == False and didGameEnd == False:
    clear()
    #print(f"answer is {answer}")
    print(f"Find X  {guess_list_x}")
    print(f"You have {turns} turns remaining")
    guess, result, didWin = make_a_guess(turns, answer)  #access answer via a global
    guess_list, guess_list_x = guess_list_maker(guess, guess_list, answer)
    print(f"You guessed {guess} and it was {result}!\n")
    turns, didGameEnd = turns_left(turns, guess, didWin, didGameEnd)

play = "y"
while play == "y":
  guess_again()
  #play = (input("Would you like to play hard or easy?  ") or "easy").lower()
  play = (input("Would you like to guess again? [y] ") or "y").lower()
  #play.lower()


