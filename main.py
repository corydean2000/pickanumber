import random
#homework is to count how many guesses it takes.
#how to optimize the guesses.
print('Welcome to the guessing game.  You pick the boundaries and then try to guess a random number.\n')
low = int(input('What is the lowest number? '))
high = int(input('What is the highest number? '))
number = random.randint(low,high)
print(number)
count = 0
guesses = []
play = input('Would you like the computer to play for you Yes/No? ')
if play == 'yes':
    guess = round(.5*(1+high-low))
    count +=1
    print(f'\nThe computers first guess is {guess}')

    if guess == number:
        print(f'Nice work got it on the first try, it was {guess}')

    if guess > number:
        guess = guess - round(.5*(guess-low))
        count +=1
        print(f'New guess is {guess}')
        while guess != number:
            if count == 15:
                break
            elif guess > number:
                guess = guess - round(.5*(guess-low))
                print(f'New guess is {guess}, this is guess # {count}')
                count +=1
            elif guess < number:
                guess = guess + 1
                print(f'New guess is {guess}, this is guess # {count}')
                count +=1
            
    if guess < number:
        guess = guess + round(.5*(high - guess))
        count +=1
        print(f'New guess is {guess}, this is guess # {count}')
        while guess != number:
            if count == 15:
                break
            elif guess < number:
                guess = guess + round(.5*(high - guess))
                print(f'New guess is {guess}, this is guess # {count}')
                count +=1
            elif guess > number:
                guess = guess - 1
                print(f'New guess is {guess}, this is guess # {count}')
                count +=1
            

while play == "no":
 
  guess = input(f'What is your guess from {low} and {high} ')
  guesses.append(guess)
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
print(guesses)
