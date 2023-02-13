import random

def rolld100():
    
    result = 0
    bonusDice = 0
    penaltyDice = 0
    tens_die_rolls = []

    bonusDice = int(input('Any bonus dice?[0]') or "0")
    penaltyDice = int(input('Any penalty dice?[0]') or "0")
    resultDice = abs(bonusDice - penaltyDice) + 1

    # Roll the ones die
    d2 = random.randint(0,9)
    
    # Determine if bonus or penalty dice are to be rolled and roll the appropriate number of dice
    
    if bonusDice > penaltyDice:
        # Determine and print the number of Bonus dice to roll
        print('Rolling d100 with ' + str(resultDice -1) + ' bonus dice.\n')

        for i in range(resultDice):
            tens_die_roll = random.randint(0,9)
            if d2 == 0 and tens_die_roll == 0:
                tens_die_roll =100 
            print('Tens die ' + str(i+1) + ': ' + str(tens_die_roll))
            tens_die_rolls.append(tens_die_roll)
            d1 = max(tens_die_rolls)

    elif penaltyDice > bonusDice:
        # Determine and print the number of Penalty dice to roll
        print('Rolling d100 with ' + str(resultDice -1) + ' penalty dice.\n')
  
        for i in range(resultDice):
            tens_die_roll = random.randint(0,9)
            if d2 == 0 and tens_die_roll == 0:
                tens_die_roll =100 
            print('Tens die ' + str(i+1) + ': ' + str(tens_die_roll))
            tens_die_rolls.append(tens_die_roll)
            d1 = min(tens_die_rolls)

    else:
        # Determine and print the number of dice to roll
        print('Rolling d100 with no bonus or penalty dice.\n')
        d1 = random.randint(0,9)
        print('Tens die: ' + str(d1))

    print ("Ones die: " + str(d2))

    if d1 == 100 and d2 == 0:
        result = 100
    else:
        result = d1 * 10 + d2
    return result

print("Final roll: " + str(rolld100()))