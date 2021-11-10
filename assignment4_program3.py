def getFunction():
    moneyTotalF = float(input("Money: "))
    applePriceF = float(input("Apple Price: "))
    appleTotalF = (moneyTotalF//applePriceF)
    pricetotalF = appleTotalF * applePriceF
    changeF = moneyTotalF - pricetotalF
    return appleTotalF, changeF

def display(appleTotalF, changeF):
    print(f"You can buy {appleTotalF:.0f} apples and your change is {changeF:.2f} pesos.")

appleTotal, change = getFunction()
display(appleTotal, change)