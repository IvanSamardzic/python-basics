weight = float(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ");
if unit.upper() == "L":
    kilos = weight * 0.45
    print("You are " + kilos + "kg"
elif unit.upper() == "K"
    lbs = weight / 0.45
    print("You are " + lbs + "lbs")