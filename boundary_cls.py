import controller_cls,halls

def show_title():       #to display PRIME EVENTS TITLE
    print("\n")
    print("*"*20 + " WELCOME TO PRIME EVENTS "+ "*"*20)
    print("\n")

def login_view():       #to display login choices
    show_title()
    print("1 : CUSTOMER LOGIN")
    print("2 : OWNER LOGIN")
    print("3 : ADMIN LOGIN")
    print("\n4: BACK TO PREVIOUS MENU")
    option = int(input("\nSelect your option : "))
    if option in [1,2,3]:
        return option
    elif(option==4):
        main_menu()
    else:
        print("Option is invalid. Please select the correct option")
        login_view()
    return option

def register_view():
    show_title()
    print ("1 : REGISTER AS CUSTOMER")
    print ("2 : REGISTER AS OWNER")
    print("\n3: BACK TO PREVIOUS MENU")
    option = int(input("\nSelect your option : "))
    if option in [1,2]:
        return option
    elif (option == 3):
        main_menu()
    else:
        print("Option is invalid. Please select the correct option")
        login_view()
    return option

def display_user_info(uid,uname):
    print("\n")
    print("- "*10+"PRIME EVENTS"+" -"*10)
    print("\nUser ID : ",uid,"\t\t\t\tUser name : ",uname,"\n")


def customer_view_hall(user_id,user_name):
    display_user_info(user_id,user_name)
    print ("1: SEARCH HALL")
    print ("2: DISPLAY ALL AVAILABLE HALLS")
    print("3: BOOK HALL")
    print ("4: BACK")
    option = int(input("Select your option : "))
    if option == 1:
        controller_cls.search_halls()

    elif option == 2:
        controller_cls.display_halls()

    elif option == 3:
        controller_cls.book_hall(user_id,user_name)

    elif option == 4:
        display_user_info(user_id,user_name)
        customer_menu(user_id,user_name)
    else:
        print("Option is invalid. Please select the correct option")
        display_user_info(user_id,user_name)
        customer_view_hall(user_id,user_name)

def customer_menu(user_id,user_name):
    print ("\t\t\t CUSTOMER MENU \n")
    print ("1 : VIEW HALLS")
    print ("6 : LOGOUT")
    option = int(input("Select your option : "))
    if option == 1:
        customer_view_hall(user_id,user_name)

    elif option == 6:
        print("\nLOGGED OUT SUCCESSFULLY...")
        main_menu()

    else:
        print("Option is invalid. Please select the correct option")
        customer_menu(user_id,user_name)

def owner_menu():
    print ("\n\t\t\t OWNER MENU \n")
    print ("1 : CREATE HALL")
    print ("2 : MANAGE BOOKINGS")
    print ("3 : MANAGE HALL")
    print ("4 : MANAGE PAYMENTS")
    print ("5 : MANAGE DISCOUNTS")
    print ("6 : REPLY TO QUOTATION")
    print ("7 : LOGOUT")
    option = int(input("Select your option : "))
    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 5:
        controller_cls.manage_discount()
    elif option == 6:
        pass

    elif option == 7:
        print("\nLOGGED OUT SUCCESSFULLY...")
        main_menu()

    else:
        print("Option is invalid. Please select the correct option")
        owner_menu()

def admin_menu():
    print ("\n\t\t\t ADMIN MENU \n")
    print ("1 : MANAGE DISCOUNTS")
    print ("2 : MANAGE USERS")
    print ("3 : LOGOUT")
    option = int(input("Select your option : "))
    if option == 1:
        controller_cls.manage_discount()
    elif option == 2:
        pass
    elif option == 3:
        print("\nLOGGED OUT SUCCESSFULLY...")
        main_menu()

    else:
        print("Option is invalid. Please select the correct option")
        admin_menu()

def main_menu():    #displaying the main menu for prime events
    show_title()
    print("1 : LOGIN")
    print("2 : REGISTER")
    print("3 : EXIT")
    option = int(input("Select your option : "))
    if option == 1:     #selected login option
        response = login_view()
        user_id,user_name=controller_cls.login_function(response)     #show login page
        if user_id!=-1:     #check if login was successful
            display_user_info(user_id,user_name)       #display user info
            if response==1:
                customer_menu(user_id,user_name)     #display customer menu if user type is customer

            if response==2:
                owner_menu()        #display owner menu if user type is owner


            if response==3:
                admin_menu()        #display admin menu if user type is admin

        else:   #invalid login credentials
            print("\n\tLOGIN FAILED!\nENTER VALID CREDENTIALS!")
            main_menu()

    elif option == 2:   #selected login option
        response = register_view()      #show register page
        reg_success=controller_cls.register_function(response)      #pass login type
        if(reg_success==1):
            print("\nREGISTRATION SUCCESSFUL!\n\n You can now log in!")
            main_menu()
    else:
        exit(0)

if __name__ ==  "__main__":
    main_menu()
