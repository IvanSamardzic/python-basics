#House price is 1M$, it is printed on the screen
house_price = float(1000000)
print("House price is: " + house_price + "$")

#The user inputs the boolean value about buyer credit ability
is_good_credit = bool(input("Is credit good?\nYes -> True\nNo -> False"))

#check the boolean variable state
if is_good_credit:
    put_down = house_price * 0.1
else:
    put_down = house_price * 0.2
print("Down paymant is: " + put_down + "$")

