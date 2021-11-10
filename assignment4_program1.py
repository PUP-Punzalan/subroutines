def Informations():
    # get name, age, and address
    getName = input("Name: ")
    getAge = int(input("Age: "))
    getAdd = input("Address: ")
    return getName, getAge, getAdd

def display(getName, getAge, getAdd):
    print(f"Hi my name is {getName}. I am {getAge} and I live in {getAdd}.")

name, age, address = Informations()
display(name, age, address)