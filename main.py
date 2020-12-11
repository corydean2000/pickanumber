import random
#homework is to count how many guesses it takes.
#how to optimize the guesses.
print('Welcome to the guessing game.  You pick the boundaries and then try to guess a random number.\n')
low = int(input('What is the lowest number? '))
high = int(input('What is the highest number? '))
number = random.randint(low,high)
guess = 0
print(number)
while guess != 'q':
 
  guess = int(input(f'What is your guess from {low} and {high} '))
  if guess > high or guess < low:
    print(f'{guess} is not between {low} and {high}.\n')

  
  if guess == number:
    print(f'You nailed it, it was {number}')
    break
  elif str(guess) == 'quit':
      break
  elif guess > number:
    print("You are too high.")
  elif guess < number:
    print('you are too low.')
  
print('Thanks for playing, the number was: ' + str(number))
