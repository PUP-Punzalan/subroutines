print("Apple = 20 pesos, Orange = 25 pesos")

def getQuantity():
    appleF = int(input("Number of apple: "))
    orangeF = int(input("Number of orange: "))
    totalF = (appleF*20) + (orangeF*25)
    return totalF

def display(totalF):
    print(f"The total amount is {totalF}.")

total = getQuantity()
display(total)