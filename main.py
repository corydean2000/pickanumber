import random
#homework is to count how many guesses it takes.
#how to optimize the guesses.
print('Welcome to the guessing game.  You pick the boundaries and then try to guess a random number.\n')
low = int(input('What is the lowest number? '))
high = int(input('What is the highest number? '))
number = random.randint(low,high)
print(number)
count = 0

play = input('Would you like the computer to play for you Yes/No? ')
if play == 'yes':
  guess = round(.5*(high-low))
  count = count + 1
  print(f'The computers first guess is {guess}')
if play == 'yes':
  
  if guess == number or new_guess== number:
    print(f'The computer got it, it was {number}.')
    break

  if guess > number:
    
      print('Guess was too high, computer will guess again.')
      guess = new_guess
        while new_guess > number
          new_guess = round(.5*(guess-low))
        if new
      
    print(f'next guess is: {guess}')
    count = count + 1
    
  elif guess < number:
    print('Guess was too low, computer will guess again.')
    guess = round(guess + .5*(high -guess))
    print(guess)
    count = count + 1
  if count == 10:
    break


while play == "no":
 
  guess = input(f'What is your guess from {low} and {high} ')
  guess = int(guess)
  count += 1
  if guess > high or guess < low:
    print(f'{guess} is not between {low} and {high}.\n')

  
  if guess == number:
    print(f'You nailed it, it was {number}')
    break
  
  elif guess > number:
    print("You are too high.")
  elif guess < number:
    print('you are too low.')
  guess = str(guess)
  

print(f'\nThanks for playing, the number was: {number}')
print(f'It took you {count} guesses.')
