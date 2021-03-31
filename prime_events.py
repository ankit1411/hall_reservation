from os import system
from getpass import getpass

def show_title():
    print("\n\n")
    print("*"*20 + " WELCOME TO PRIME EVENTS "+ "*"*20)
    print("\n\n")

def user_auth_view(user):
    system('clear')
    show_title()
    print ("\n "+ user +"\n")
    username = input("Enter username : ")
    password = getpass("Enter password : ")
    print ("Validating "+"."*20)
    if username == "user" and password == "user":
        print ("Login Sucessfull")
        return True
    else:
        print ("Invalid username or password. Please try again...")
        user_auth_view(user)

def user_login_view():
    system('clear')
    show_title()
    print ("1 : CUSTOMER LOGIN")
    print ("2 : OWNER LOGIN")
    print ("3 : ADMIN LOGIN")
    option = int(input("Select your option : "))
    if option in [1,2,3]:
        return option
    else:
        print("Option is invalid. Please select the correct option")
        user_login_view()
    return option

def customer_menu():
    system('clear')
    show_title()
    print ("\n CUSTOMER MENU \n")
    print ("1 : VIEW HALLS")
    print ("2 : BOOK HALL")
    print ("3 : REQUEST QUOTATION")
    print ("4 : MANAGE BOOKINGS")
    print ("5 : WRITE REVIEW")
    print ("6 : LOGOUT")
    option = int(input("Select your option : "))
    if option == 1:
        customer_view_hall()
    elif option == 2:
        customer_book_hall()
    elif option == 3:
        customer_request_quotation()
    elif option == 4:
        customer_manage_bookings()
    elif option == 5:
        customer_write_review()
    elif option == 6:
        register_login_selector()
    else:
        print("Option is invalid. Please select the correct option")
        customer_menu()

def owner_menu():
    system('clear')
    show_title()
    print("\n OWNER MENU \n")
    print ("1 : CREATE HALL")
    print ("2 : MANAGE BOOKINGS")
    print ("3 : MANAGE HALL")
    print ("4 : MANAGE PAYMENTS")
    print ("5 : MANAGE DISCOUNTS")
    print ("6 : REPLY TO QUOTATION")
    print ("7 : LOGOUT")
    option = int(input("Select your option : "))
    if option == 1:
        owner_create_hall()
    elif option == 2:
        owner_manage_bookings()
    elif option == 3:
        owner_manage_hall()
    elif option == 4:
        owner_manage_payments()
    elif option == 5:
        owner_manage_discounts()
    elif option == 6:
        owner_reply_quotation()
    elif option == 7:
        register_login_selector()
    else:
        print("Option is invalid. Please select the correct option")
        owner_menu()

def admin_menu():
    system('clear')
    show_title()
    print("\n ADMIN MENU \n")
    print ("1 : MANAGE DISCOUNTS")
    print ("2 : MANAGE USERS")
    print ("3 : LOGOUT")
    option = int(input("Select your option : "))
    if option == 1:
        admin_manage_discounts()
    elif option == 2:
        admin_manage_users()
    elif option == 3:
        register_login_selector()
    else:
        print("Option is invalid. Please select the correct option")
        admin_menu()
    
def customer_view_hall():
    system('clear')
    show_title()
    print ("1: SEARCH HALL")
    print ("2: DISPLAY HALL")
    print ("3: BACK")
    option = int(input("Select your option : "))
    if option == 1:
        print ("SEARCHING HALL")
        # write function search halls
        customer_view_hall()
    elif option == 2:
        print("DISPLAY HALLS")
        # write function to display halls
        customer_view_hall()
    elif option == 3:
        customer_menu()
    else:
        print("Option is invalid. Please select the correct option")
        customer_view_hall()

def customer_book_hall():
    system('clear')
    show_title()
    print("1 : PAY DEPOSIT")
    print("2 : BACK")
    option = int(input("Select your option : "))
    if option in [1]:
        # write function to deposit
        customer_book_hall()
    elif option == 2:
        customer_menu()
    else:
        print("Option is invalid. Please select the correct option")
        customer_book_hall()

def customer_request_quotation():
    system('clear')
    show_title()
    print("1 : DISPLAY QUOTATION")
    print("2 : SUBMIT QUOTATION")
    print ("3 : BACK")
    option = int(input("Select your option : "))
    if option == 1:
        # write function to display quotations
        customer_request_quotation()
    elif option == 2:
        # write function to submit quotations
        customer_request_quotation()
    elif option == 3:
        customer_menu()
    else:
        print("Option is invalid. Please select the correct option")
        customer_request_quotation()

def customer_manage_bookings():
    system('clear')
    show_title()
    print ("1 : CANCEL BOOKING")
    print ("2 : CHANGE BOOKING")
    print ("3 : BACK")
    option = int(input("Select your option : "))
    if option == 1:
        # write function to cancel booking
        customer_manage_bookings()
    elif option == 2:
        # write function to change booking
        customer_manage_bookings()
    elif option == 3:
        customer_menu()
    else:
        print("Option is invalid. Please select the correct option")
        customer_manage_bookings()

def customer_write_review():
    system('clear')
    show_title()
    bk_id = input("TYPE BOOKING ID : ")
    review = input("WRITE COMMENTS : ")
    print ("1 : SUBMIT")
    print ("2 : CANCEL")
    print ("3 : BACK")
    option = int(input("Select your option : "))
    if option in [1]:
        print ("REVIEW IS SUBMITTED")
        customer_menu()
    elif option == 2:
        customer_write_review()
    elif option == 3:
        customer_menu()
    else:
        print("Option is invalid. Please select the correct option")
        customer_write_review()

def owner_create_hall():
    system("clear")
    show_title()
    hall_name = input ("ENTER HALL NAME : ")
    hall_type = input ("ENTER TYPE OF HALL : ")
    hall_capacity = input("ENTER HALL CAPACITY : ")
    hall_location = input("ENTER LOCATION : ")
    print ("1: SUBMIT")
    print ("2: CANCEL")
    print ("3: BACK")
    option = int(input("Select your option : "))
    if option == 1:
        print ("HALL HAS CREATED")
        owner_menu()
    elif option == 2:
        owner_menu()
    elif option == 3:
        owner_menu()
    else:
        print("Option is invalid. Please select the correct option")
        owner_create_hall()

def owner_manage_bookings():
    system("clear")
    show_title()
    print("1 : ADD BOOKING")
    print("2 : CHANGE BOOKING")
    print("3 : CANCEL BOOKING")
    print("4 : BACK")
    option = int(input("Select your option : "))
    if option == 1:
        # Write function to add booking
        print ("BOOKING ADDED")
        owner_menu()
    elif option == 2:
        # Write function to change booking
        print ("BOOKING CHANGED")
        owner_menu()
    elif option == 3:
        # Write function to cancel booking
        print ("BOOKING CANCELLED")
        owner_menu()
    elif option == 4:
        owner_menu()
    else:
        print("Option is invalid. Please select the correct option")
        owner_manage_bookings()

def owner_manage_hall():
    system("clear")
    show_title()
    print("1 : UPDATE INFO")
    print("2 : DELETE HALL")
    print("3 : BACK")
    option = int(input("Select your option : "))
    if option == 1:
        print ("HALL INFO UPDATED")
        owner_menu()
    elif option == 2:
        print ("HALL DELETED")
        owner_menu()
    elif option == 3:
        owner_menu()
    else:
        print("Option is invalid. Please select the correct option")
        owner_manage_hall()

def owner_manage_payments():
    system("clear")
    show_title()
    print("1 : ADD PAYMENT")
    print("2 : UPDATE PAYEMNT")
    print("3 : DELETE PAYMENT")
    print("4 : BACK")
    option = int(input("Select your option : "))
    if option == 1:
        print ("PAYMENT ADDED")
        owner_menu()
    elif option == 2:
        print ("PAYMENT UPDATED")
        owner_menu()
    elif option == 3:
        print ("PAYMENT DELETED")
        owner_menu()
    elif option == 4:
        owner_menu()
    else:
        print("Option is invalid. Please select the correct option")
        owner_manage_payments()

def owner_manage_discounts():
    system("clear")
    show_title()
    print("1 : ADD DISCOUNT")
    print("2 : UPDATE DISCOUNT")
    print("3 : DELETE DISCOUNT")
    print("4 : BACK")
    option = int(input("Select your option : "))
    if option == 1:
        print ("DISCOUNT ADDED")
        owner_menu()
    elif option == 2:
        print ("DISCOUNT UPDATED")
        owner_menu()
    elif option == 3:
        print ("DISCOUNT DELETED")
        owner_menu()
    elif option == 4:
        owner_menu()
    else:
        print("Option is invalid. Please select the correct option")
        owner_manage_discounts()

def owner_reply_quotation():
    system("clear")
    show_title()
    print ("QUOTATION ")
    answer = input("TYPE Y TO ACCEPT THE QUOTATION : ")
    if answer == 'y' or answer == 'Y':
        print ("QUOTATION IS ACCEPTED")
        owner_menu()
    else:
        owner_reply_quotation()

def admin_manage_discounts():
    system("clear")
    show_title()
    print("1 : ADD DISCOUNT")
    print("2 : UPDATE DISCOUNT")
    print("3 : DELETE DISCOUNT")
    print("4 : BACK")
    option = int(input("Select your option : "))
    if option == 1:
        print ("DISCOUNT ADDED")
        admin_menu()
    elif option == 2:
        print ("DISCOUNT UPDATED")
        admin_menu()
    elif option == 3:
        print ("DISCOUNT DELETED")
        admin_menu()
    elif option == 4:
        admin_menu()
    else:
        print("Option is invalid. Please select the correct option")
        admin_manage_discounts()

def admin_manage_users():
    system("clear")
    show_title()
    print("1 : ADD USER")
    print("2 : UPDATE USER")
    print("3 : DELETE USER")
    print("4 : BACK")
    option = int(input("Select your option : "))
    if option == 1:
        print ("USER ADDED")
        admin_menu()
    elif option == 2:
        print ("USER UPDATED")
        admin_menu()
    elif option == 3:
        print ("USER DELETED")
        admin_menu()
    elif option == 4:
        admin_menu()
    else:
        print("Option is invalid. Please select the correct option")
        admin_manage_users()

def register_user():
    system("clear")
    show_title()
    username = input("ENTER USERNAME : ")
    password = input("ENTER PASSWORD : ")
    c_password = input("CONFIRM PASSWORD : ")
    address = input("ENTER ADDRESS : ")
    phone_no = input("ENTER PHONE NO : ")
    print ("1 : SUBMIT")
    print ("2 : CANCEL")
    option = int(input("Select your option : "))
    if option == 1:
        if password == c_password:
            print ("ACCOUNT HAS CREATED")
            register_login_selector()
        else:
            print ("PASSWORD MISMATCH")
            register_user()
    elif option == 2:
        register_user()
    else:
        print("Option is invalid. Please select the correct option")
        register_user()
    
def login_control_view(option):
    if option == 1:
        success = user_auth_view("CUSTOMER LOGIN")
        if success:
            customer_menu() 
    elif option == 2:
        success = user_auth_view("OWNER LOGIN")
        if success:
            owner_menu() 
    elif option == 3:
        success = user_auth_view("ADMIN LOGIN")
        if success:
            admin_menu() 

def login_view():
    option = user_login_view()
    login_control_view(option)

def register_login_selector():
    system("clear")
    show_title()
    print("1 : LOGIN")
    print("2 : REGISTER")
    print("3 : EXIT")
    option = int(input("Select your option : "))
    if option == 1:
        login_view()
    elif option == 2:
        register_user()
    else:
        return


if __name__ ==  "__main__":
    register_login_selector()
