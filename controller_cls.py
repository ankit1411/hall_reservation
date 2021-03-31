import customer,owner,halls,admin,discount
def display_halls():
    print("\n")
    print("*" * 25 + " ALL AVAILABLE HALLS " + "*" * 25)
    halls.show_all_halls()

def search_halls():
    print("\n")
    print("*" * 15 + " SEARCH PARAMETERS " + "*" * 15)
    print("\n")
    print("1: HALL ID")
    print("2: HALL NAME")
    print("3: OCCASION")
    print("4: CAPACITY")
    print("5: CATERING AVAILABILITY")
    option = int(input("Select your option : "))
    if option == 1:
        halls.hall_id_search()
        search_halls()

    elif option == 2:
        halls.hall_name_search()
        search_halls()

    elif option == 3:
        halls.hall_occasion_search()
        search_halls()

    elif option == 4:
        halls.hall_capacity_search()
        search_halls()

    elif option == 5:
        halls.hall_catering_search()
        search_halls()

    else:
        print("Option is invalid. Please select the correct option")
        search_halls()

def book_hall(uid,uname):
    print("*" * 15 + "BOOKING HALL" + "*" * 15)
    halls.booking_hall(uid,uname)
   # book_hall(uid, uname)

def login_function(user_type):
    print("\n")
    print("*" * 15 + " LOGIN PAGE " + "*" * 15)
    if (user_type == 1):
        print("\n")
        print("- " * 5 + "Customer Login" + " -" * 5)
        log_res=customer.login()        #call login function from customer class
        if(log_res==-1):    #check for valid credentials
            return -1,-1

        else:
            print("\nLOGIN SUCCESSFUL!")
            return log_res[0],log_res[1]


    elif (user_type == 2):
        print("\n")
        print("- " * 5 + "Owner Login" + " -" * 5)
        log_res = owner.login()  # call login function from owner class
        if (log_res == -1):  # check for valid credentials
            return -1, -1

        else:
            print("\nLOGIN SUCCESSFUL!")
            return log_res[0], log_res[1]

    elif (user_type==3):
        print("\n")
        print("- " * 5 + "ADMIN LOGIN" + " -" * 5)
        log_res = admin.login()  # call login function from customer class
        if (log_res == -1):  # check for valid credentials
            return -1, -1
        else:
            print("\nLOGIN SUCCESSFUL!")
            return log_res[0], log_res[1]


def register_function(user_type):
    print("\n")
    print("* " * 15 + " REGISTRATION PAGE " + " *" * 15)
    if(user_type==1):
        print("\n")
        print("- "*5 + "Registering as CUSTOMER" + " -"*5)
        customer.register()   #register function from customer class
        return 1

    if (user_type == 2):
        print("\n")
        print("- "*5 + "Registering as OWNER" + " -"*5)
        owner.register()        #register function from owner class
        return 1

    else:
        print("REGISTRATION FAILED!!")

def manage_discount():
    print("\n 1.add discount \n 2.update discount \n 3.delete discount")
    option = int(input("\nSelect your option : "))
    if option == 1:
        pass
    if option == 2:
        discount.edit_discount()
    if option == 3:
        pass