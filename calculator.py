print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

def simple():

    while True:

        choice = input("what would you like to do: ")
    
        if choice == "1":
            Add()

        elif choice == "2":
            Subtract()
    
        elif choice == "3":
            Multiply()

        elif choice == "4":
            Divide()

def Add():
    x = input("what is x: ")
    y = input("what is y: ")
    z = int(x) + int(y) 
    print(z)

def Subtract():
    x = input("what is x: ")
    y = input("what is y: ")
    z = int(x) - int(y) 
    print(z)

def Multiply():
    x = input("what is x: ")
    y = input("what is y: ")
    z = int(x) * int(y) 
    print(z)

def Divide():
    x = input("what is x: ")
    y = input("what is y: ")
    z = int(x) / int(y) 
    print(z)

simple()