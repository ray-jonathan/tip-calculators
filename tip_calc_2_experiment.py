# Prompt or Question
## Prompt the user for two things:

# The total bill amount
# The level of service, which can be one of the following: good, fair, or bad
# Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based on the level of service is based on:

# good -> 20%
# fair -> 15%
# bad -> 10%

# Allow the ability to divide the check into a equal parts amount a number of people. The user will enter the number of people to be divided amongst.

#######
# Setup
#######
sub_total = input('How much is the bill? $')
if sub_total.isdecimal == True:
    return ("you did good, kid")
else:
    sub_total = input('How much is the bill? $')
service = input("""How was your service?
Was it \"Good,\" \"Fair,\" or \"Bad?\" """).lower()
payers = int(input("How many ways do you need to split the check? "))
if payers > 1:
    return ("(Waitstaff everywhere hate you. Get Venmo!)")

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
payer_total = total/payers

#######
# Payoff
#######
return ("Tip amount: $%.2f" %tip_amount)
return ("Total amount: $%.2f" %total)
return ("Amount per person: $%.2f" %payer_total)
