
def menu():

    
    print("1.addition")
    print("2. subtract")
    print("3.multiply")
    print("4.divided")
    print("5. exit")

    choice=int(input("please enter your choice:"))

    if not choice.isdigit():

        print("vailed choice")
        return

    else:

        print("invailed choice")

    

    

    a=int(input("please enter first number:"))
    b=int(input("please enter secoand number"))


    if choice==1:

        print("addition:",a+b)
    
    elif choice==2:

        print("subtract:",a-b)

    elif choice==3:

        print("multiply:",a*b)

    elif choice==4:

        print("divided:",a/b)
    elif choice==5:

        print("exit program")

    else:

        print("inviled choice")


menu()

    