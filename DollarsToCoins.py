import time
import random

# Define coin names and value associations
divisions = dict(
Penny = .01,
Nickel = .05,
Dime = .1,
Quarter = .25
)

# Get coin names and values for later use
coins = list(divisions.keys())
values = list(divisions.values())

# Convert singularWord to plural if num implies plurality
def pluralCheck(num, singularWord):
    singularValues = [-1, -.1, .1, 1]
    if (float(num) not in singularValues):
        # Catch spelling differences for penny vs pennies
        if 'penny' in singularWord.lower():
            return 'pennies'
        else:
            return singularWord + 's'
    else:
        return singularWord

# Prints given list of lines with a short pause between each
def narrate(*script):
    for i in range(len(script)):
        print(script[i])
        time.sleep(1)

# Greet and prompt user
def play(salutation):
    narrate(
    salutation,
    'I can help you convert your dollars into coins.',
    )
    ask()

# Prompt user for dollar input
def ask():
    narrate('How many dollars do you have?')
    # Store user-input
    dollars = input()

    # Print 'dollars' equivalent in each coin subdivision
    if (float(dollars) >= 0): # FIXME: Needs an error handler
        narrate('With ' + str(dollars) + ' ' + pluralCheck(dollars, 'dollar')
        + ', you have: ')
        for i in range(len(coins)):
            narrate(str(float(dollars) / values[i]) + ' '
            + pluralCheck(float(dollars) / values[i], coins[i].lower())
            )
        # FIXME: Erroneous dollars value persists after successful input
        replay()
    else:
        tryAgain()
        ask()

def replay():
    narrate(
    'Would you like to convert another dollar amount?',
    '1. Yes',
    '2. No'
    )
    prompt = input()
    if (prompt == '1'):
        play('Wonderful')
    elif (prompt == '2'):
        narrate('Very well, thank you for playing')
        exit()
    else:
        tryAgain()
        replay()

def tryAgain():
    narrate('Sorry, I don\'t understand.',
    'Please enter a valid number')

play('Hello')
replay()
