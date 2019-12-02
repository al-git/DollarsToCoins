# Define coin types and values
# Consolidate into pending dictionary
penny = .01
nickel = .05
dime = .1
quarter = .25

# Store coin value and names
# Convert to dictionary of coin name : value
coins = [penny, nickel, dime, quarter, 'Pennies', 'Nickels',
        'Dimes', 'Quarters']

# Store user prompt
# Add line-break after prompt
dollars = float(input('How many dollars do you have?'))

# Print 'dollars' equivalent in each coin subdivision
# Update to reference dictionary key : values
for i in range(4):
    print(coins[i+4] + ': ' +  str(dollars / coins[i]))
