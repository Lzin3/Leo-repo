weight = float(input("weight: "))
unit = input ( "K (kgs) or L for (lbs)")
if unit.upper() == "K":
    converted = weight / 0.45
    print("weight in Lbs: ", converted)
    