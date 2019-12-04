import time
import random

# Define coin names and value associations
divisions = dict(
Pennies = .01,
Nickels = .05,
Dimes = .1,
Quarters = .25
)

# Get coin names and values for later use
coins = list(divisions.keys())
values = list(divisions.values())

# Convert singularWord to plural if num > 1
def pluralCheck(num, singularWord):
    if (float(num) > 1):
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
    try:
        float(dollars)
        narrate('With ' + str(dollars) + ' ' + pluralCheck(dollars, 'dollar')
        + ', you have: ')
        for i in range(len(coins)):
            narrate(str(float(dollars) / float(values[i])) + ' '
            + coins[i].lower())
            pass
            # FIXME: Erroneous dollars value persists after successful input
    except Exception as e:
        tryAgain()
        ask()
        raise

def replay():
    narrate(
    'Would you like to convert another dollar amount?',
    '1. Yes',
    '2. No'
    )
    prompt = int(input())
    if (prompt == 1):
        play('Wonderful')
    elif (prompt == 2):
        narrate('Very well, thank you for playing')
        exit()
    else:
        tryAgain()
        replay()

def tryAgain():
    narrate('Sorry, I don\'t understand.',
    'Please enter a number')

play('Hello')
# FIXME: Replay only replays once. Wrap play() and replay() for many replay()'s
replay()
