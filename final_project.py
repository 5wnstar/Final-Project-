#This is a Simple Calculator Program with Python
while True:
    num1 = float(input("Enter your first number:"))
    num2 = float(input("Enter the Second number:"))
    #User Chooses Opertaions
    print("Choose an operation")
    print("1. Addition")
    print("2. Subraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo")
    print("6. Floor Division")
    print("7. Exit")
    choice = int(input("Enter your choice:"))
    #Perform Operations
    if choice == 1:
        print(f"The Addition of your input is {num1 + num2}")
    elif choice == 2:
        print(f"The Subraction of your input is {num1 - num2}")
    elif choice == 3:
        print(f"The Multiplication of your input is {num1 * num2}")
    elif choice == 4:
        if num2 !=0:
            print(f"The Division of your input is {num1 / num2}")
        else:
            print("Error! Division by zero")
    elif choice == 5:
        print(f"The Modulo of your input is {num1 % num2}")
    elif choice == 6:
        if num2 !=0:
            print(f"The Division of your input is {num1 // num2}")
        else:
            print("Error! Division by zero")
    elif choice == 7:
        print("Exiting the Program. Goodbye!")
        break
    else:
        print("Invalid Choice, Please Try Again...")
        



    




        
    
