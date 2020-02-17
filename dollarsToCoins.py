import time
import random
import itertools


# Define coin names and value associations
divisions = {
    "Penny"=.01,
    "Nickel"=.05,
    "Dime"=.1,
    "Quarter"=.25
}

# Update divisions to contain individual coin values
divisions = {x: (list(round((y*divisions[x]),2) for y in
range(1, int(1/divisions[x])+1))) for x, y in divisions.items()}


# Get coin names and values for later use
coins = divisions.keys()
values = [i[0] for i in divsions.values()]


# List of possible permutations
allPerms = [i for i in it.permutations(divisions.items())]


# Function to calculate permutations == 1.0

masterHolder = [] # Holds string statements of all permutations to be printed

for thisPerm in allPerms: # there needs to be a while != len(allPerms) loop here
    for allSets in thisPerm:
        holder = []
        for thisSet in allSets:
            coinName = thisSet[0]
            coinVal = thisSet[1][0]
            currentSum = 0
            for x in thisSet[1]:
                coinQuant = x/coinVal
                while currentSum != 1:
                    currentSum += x # somewhere around here
                    if coinQuant == len(thisSet[0])
                        x += 1
                        holder.append(str(coinQuant) + " " + pluralCheck(coinName))
                        masterHolder += holder # this line might need to come later?



for i in allCoins.keys():
    holder = [] # Holds coin name + quantities (sum/value) to append to masterHolder
    for j in
    while divisions != 1:

    holder = []
    for j in allCoins[i]:
            print(i, j) # Replace these lines with something involving permutations


# Convert singularWord to plural if num implies plurality
def pluralCheck(num, singularWord):
    singularValues = [-1, -.1, .1, 1]
    if (float(num) not in singularValues):
        # Catch spelling differences for penny vs pennies
        if "penny" in singularWord.lower():
            return "pennies"
        else:
            return singularWord + "s"
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
        "I can help you convert your dollars into coins.",
    )
    ask()


# Prompt user for dollar input
def ask():
    narrate("How many dollars do you have?")
    # Store user-input
    dollars = input()

    # Check for int(dollars). Catch errors.
    try:
        float(dollars)
    except Exception as e:
        tryAgain()
        ask()
    else:
        narrate(
            "With " + str(dollars) + " " + pluralCheck(dollars, "dollar")
            + ", you have: "
        )
        # Print "dollars" equivalent in each coin subdivision
        # FIXME: Remove unnecessary decimal 0" and include commas where
        # applicable.
        for i in range(len(coins)):
            narrate(
                str(float(dollars) / values[i]) + " "
                + pluralCheck(float(dollars) / values[i], coins[i].lower())
            )
        replay()


# Prompt for replay or quit
def replay():
    narrate(
        "Would you like to convert another dollar amount?",
        "1. Yes",
        "2. No"
    )
    prompt = input()
    if (prompt == "1"):
        play("Wonderful")
    elif (prompt == "2"):
        narrate("Very well, thank you for playing")
        exit()
    else:
        tryAgain()
        replay()


# Catch for invalid answers
def tryAgain():
    narrate(
        "Sorry, I don't understand.",
        "Please enter a valid number"
        )


# Run game
play("Hello")
replay()
