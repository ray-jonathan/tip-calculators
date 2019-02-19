# Prompt or Question
## Prompt the user for two things:

# The total bill amount
# The level of service, which can be one of the following: good, fair, or bad
# Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based on the level of service is based on:

# good -> 20%
# fair -> 15%
# bad -> 10%

#######
# Setup
#######
sub_total = float(input('How much is the bill? $'))
service = input("""How was your service?
Was it \"Good,\" \"Fair,\" or \"Bad?\" """).lower()

#######
# Do work
#######
if service == "good":
    tip = .20
    tip_amount = sub_total*tip
    total = sub_total*(1+tip)
elif service == "fair":
    tip = .15
    tip_amount = sub_total*tip
    total = sub_total*(1+tip)
elif service == "bad":
    tip = .10
    tip_amount = sub_total*tip
    total = sub_total*(1+tip)
else:
    return ("Please type either \"good,\" \"fair,\" or \"bad.\"")

#######
# Payoff
#######
return ("Tip amount: $%.2f" %tip_amount)
return ("Total amount: $%.2f" %total)
