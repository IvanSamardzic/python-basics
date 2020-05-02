is_hot = True
is_cold = False

if is_hot:
    print("Its a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("Its a cold day")
    print("Wear warm clothes")
else:
    print("Its a lovely day")
print("Enjoy your day")

####

has_high_income = True
has_good_credit = True
has_criminial_record = False

if has_criminial_record:
    print("The person is at the black list for 3 years")
    print("Not eligible for loan")
elif has_high_income and has_good_credit and not(has_criminial_record):
    print("Eligible for loan")
elif has_high_income or has_good_credit and not(has_criminial_record):
    print("Put the person in the waiting list")
else:
    print("Not eligible for loan")
    
###
temperature_value = float(input("What is the temperature: "))

if temperature_value > 30:
    print("Its a hot day")
else:
    print("it is not a hot day")
    
print(temperature_value)