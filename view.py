from owner_model import Owner
from payment import Payment
class View:

    def show_title(self):       #to display PRIME EVENTS TITLE
        print("\n")
        print("*"*20 + " WELCOME TO PRIME EVENTS "+ "*"*20)
        print("\n")


    def display(self,output):
        print(output)
        
    def login_view(self):       #to display login choices
        self.show_title()
        print("1 : CUSTOMER LOGIN")
        print("2 : OWNER LOGIN")
        print("3 : ADMIN LOGIN")
        print("\n4: BACK TO PREVIOUS MENU")
        option = int(input("\nSelect your option : "))
        if option in [1,2,3]:
            return option
        elif(option==4):
            self.main_menu()
        else:
            print("Option is invalid. Please select the correct option")
            self.login_view()
        return option

    def register_view(self):
        self.show_title()
        print ("1 : REGISTER AS CUSTOMER")
        print ("2 : REGISTER AS OWNER")
        print("\n3: BACK TO PREVIOUS MENU")
        option = int(input("\nSelect your option : "))
        if option in [1,2]:
            return option
        elif (option == 3):
            self.main_menu()
        else:
            print("Option is invalid. Please select the correct option")
            self.login_view()
        return option

    def display_user_info(self,uid,uname):
        print("\n")
        print("- "*10+"PRIME EVENTS"+" -"*10)
        print("\nUser ID : ",uid,"\t\t\t\tUser name : ",uname,"\n")


    def login(self):
        username=input("\nEnter username : ")
        password=input("\nEnter password : ")
        return (username,password)

    def register(self):
        name = input("\nEnter name : ")
        username = input("Enter username : ")
        password = input("Enter password : ")
        phone_number = int(input("Enter phone Number: "))
        email_id = input("Enter email Id: ")
        return (name,username,password,phone_number,email_id)

    def owner_menu(self, owner_obj):
        print ("Hi "+ owner_obj.name)
        print ("\n\t\t\t OWNER MENU \n")
        print ("1 : CREATE HALL")
        print ("2 : MANAGE BOOKINGS")
        print ("3 : MANAGE HALL")
        print ("4 : MANAGE PAYMENTS")
        print ("5 : MANAGE DISCOUNTS")
        print ("6 : REPLY TO QUOTATION")
        print ("7 : LOGOUT")
        option = int(input("Select your option : "))
        if option in [1,2,3,4,5,6]:
            return option
        elif option == 7:
            print("\nLOGGED OUT SUCCESSFULLY...")
            self.main_menu()
        else:
            print("Option is invalid. Please select the correct option")
            self.owner_menu()

    def owner_payment_menu(self):    
        self.show_title()
        print("1 : ADD PAYMENT")
        print("2 : UPDATE PAYMENT")
        print("3 : DELETE PAYMENT")
        print("4 : LOGOUT")
        option = int(input("Select your option : "))
        return option

    def owner_add_payment_view(self):
        self.show_title()
        payment_id = int(input("Enter Payment ID : "))
        booking_id = int(input("Enter Booking ID : "))
        deposit_amount = int(input("Enter Deposit Amount : "))
        payment_obj = Payment(payment_id,booking_id,deposit_amount)
        return payment_obj

    def owner_update_payment_view(self):

        payment_id = int(input("Enter Payment ID  to be updated ? : "))
        booking_id =None
        deposit_amount = int(input("Enter new Deposit Amount : "))
        payment_obj = Payment(payment_id,booking_id,deposit_amount)
        return payment_obj



    def main_menu(self):    #displaying the main menu for prime events
        self.show_title()
        print("1 : LOGIN")
        print("2 : REGISTER")
        print("3 : EXIT")
        option = int(input("Select your option : "))
        return option



        