import random
import sys
from termcolor import colored

def print_menu():
    print("Let's play Word Play:")
    print("Type a 5 letter word and hit enter!\n")


def read_random_word():
    with open("word.txt") as f:
         words = f.read().splitlines()
         return random.choice(words)


print_menu()
word = read_random_word()
play_again = ""
while play_again != 'q':

  for attempt in range(1,7):
    guess = input().lower()

    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

for i in range (min(len(guess), 5) ):
    if guess[i] == word[i]:
        print(colored(guess[i], 'green'), end="")
    elif guess[i] in word:
        print(colored(guess[i], 'yellow'), end="")
    else:
        print(guess[i], end="")
      
print()
if guess == word :
  print(colored(f"Whoa you got it in {attempt}",'red'))
  
  'break'
play_again = input("Want to play again? Type q to exit") 

