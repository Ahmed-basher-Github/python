weight = input("Weight: ")
Kg_or_Lbs = input("(K)g or (L)bs: ")
if Kg_or_Lbs.lower() == "l":
    conweight = float(weight) * 0.45
    print("Weight in kg:" + str(conweight))
elif Kg_or_Lbs.lower() == "k":
    conweight = float(weight) / 0.45
    print("Weight in lbs:" + str(conweight))
