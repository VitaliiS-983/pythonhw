import random
guessesTaken = 0
number = random.randint(1, 10)
print('I am thinking of a number between 1 and 10.')
while guessesTaken < 4:
    print('Take a guess...')
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess < number:
        print('Is too low...')
    if guess > number:
        print('Is too high...')
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print('You guessed my number in ' + guessesTaken + ' guesses')
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
