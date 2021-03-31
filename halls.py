import datetime

import mysql.connector

mydb = mysql.connector.connect(
    host="remotemysql.com",
    port="3306",
    user="1WsKFaZQ0B",
    passwd="V2QSOib3dp",
    database="1WsKFaZQ0B"
)
mycursor = mydb.cursor()

def show_all_halls():
    mycursor.execute("Select * from 1WsKFaZQ0B.halls where availability='Y'")
    myresult = mycursor.fetchall()

    print("-" * 75)
    for x in myresult:
        print("\nHall ID : ", x[0])
        print("Hall Name : ", x[1])
        print("Hall ID : ", x[2])
        print("Occasion type : ", x[3])
        print("Capacity : ", x[4])
        print("Catering availability : ", x[5], "\n")
        print("-" * 75)

def hall_id_search():
    sid=int(input("\nEnter hall ID to search : "))
    query = "SELECT * FROM 1WsKFaZQ0B.halls where hall_id = %s and availability='Y'"
    val = (sid,)
    mycursor.execute(query, val)
    myresult = mycursor.fetchone()
    if myresult != None:
        hall_info_display(myresult)
    else:
        print("\nEnter valid hall ID!!")

def hall_name_search():
    sname=input("\nEnter hall name to search : ")
    query = "SELECT * FROM 1WsKFaZQ0B.halls where hall_name = %s and availability='Y'"
    val=(sname,)
    mycursor.execute(query, val)
    myresult = mycursor.fetchone()
    if myresult != None:
        hall_info_display(myresult)
    else:
        print("\nEnter valid hall name!")

def hall_occasion_search():
    socca=input("\nEnter occasion type to search halls : ")
    query = "SELECT * FROM 1WsKFaZQ0B.halls where occasion = %s and availability='Y'"
    val=(socca,)
    mycursor.execute(query,val)
    myresult = mycursor.fetchall()
    if myresult != None:
        for x in myresult:
            hall_info_display(x)
    else:
        print("\nNo halls found for that occasion!")
        hall_occasion_search()

def hall_capacity_search():
    scapa=input("\nEnter capacity to search halls for : ")
    query = "SELECT * FROM 1WsKFaZQ0B.halls where capacity>= %s and availability='Y'"
    val=(scapa,)
    mycursor.execute(query,val)
    myresult = mycursor.fetchall()
    if myresult != None:
        for x in myresult:
            hall_info_display(x)
    else:
        print("\nNo halls found for that capacity requirement!")

def hall_catering_search():
    print("\n")
    print("*" * 15 + " CATERING AVAILABLE FOR THE FOLLLOWING HALLS " + "*" * 15)
    print("\n")
    query = "SELECT * FROM 1WsKFaZQ0B.halls where catering='Y' and availability='Y'"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    if myresult != None:
        for x in myresult:
            hall_info_display(x)
    else:
        print("\nNo halls found for that capacity requirement!")

def booking_hall(user_id,user_name):
    quot_check=int(input("Enter your quotation ID, enter 0 to request quotation = "))
    if(quot_check!=0):
        quot = "SELECT * FROM 1WsKFaZQ0B.quotation where quot_id = %s"
        val = (quot_check,)
        mycursor.execute(quot, val)
        quot_status = mycursor.fetchone()

        if(quot_status[9] == 'Y' or quot_status[9]=='y') and (quot_status[10]!=None):
            print("\nYour quotation has been accepted!")
            print("\nYour details are: ")
            print("Hall ID: ",quot_status[1])
            print("Owner ID: ",quot_status[3])
            print("Occasion: ",quot_status[4])
            print("Capacity: ",quot_status[5])
            print("Duration (hours): ", quot_status[6])
            print("Date: ", quot_status[7])
            print("Catering: ", quot_status[8])
            print("\nDeposit amount is = ",quot_status[10])

            print("\nProceeding to book the hall...")

            book_hall(quot_status)

        else:
            print("Quotation rejected")

    else:
        request_quotation(user_id,user_name)

def book_hall(quot_status):
    pay=input("\nPay the amount due? (Y/N)")
    if(pay=='Y' or pay=='y'):
        print("\nGenerating your booking id...")
        cursor = mydb.cursor()
        query = "INSERT INTO 1WsKFaZQ0B.booking (quot_id, user_id, owner_id, hall_id, date, deposit_amount) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (quot_status[0],quot_status[2],quot_status[3],quot_status[1],quot_status[7],quot_status[10])
        cursor.execute(query, val)
        mydb.commit()

        query = "Select booking_id from 1WsKFaZQ0B.booking where quot_id=%s and user_id=%s and hall_id = %s"
        val = (quot_status[0], quot_status[2], quot_status[1])
        mycursor.execute(query, val)
        myresult = mycursor.fetchone()
        print("\nYour booking number is = ", myresult[0], ". Please note this for further reference.")


def request_quotation(user_id,user_name):
    print("*" * 15 + "REQUEST A QUOTATION" + "*" * 15)
    hid = int(input("Enter the hall ID you want to book = "))
    query = "SELECT * FROM 1WsKFaZQ0B.halls where hall_id = %s and availability='Y'"
    value = (hid,)
    mycursor.execute(query, value)
    result = mycursor.fetchone()
    if result != None:
        hall_info_display(result)

        print("-" * 75)
        confirm = input("Enter Y to confirm the hall details  \nEnter N if details are incorrect : \n")
        print("-" * 75)
        if confirm == "Y" or confirm == "y":
            print("\nPlease enter the following details in order to request a quotation from the owner.\n")
            occasion = input("Enter the occasion: ")
            capacity = input("Enter the Gathering size: ")
            duration = input("Enter the number of hours you want the hall: ")
            while True:
                try:
                    date = input("Please enter the event start date in the format YYYY-MM-DD")
                    datetime.datetime.strptime(date,'%Y-%m-%d')
                    break
                except ValueError:
                    print("Incorrect date format")

            query = "Select owner_id from 1WsKFaZQ0B.halls where hall_id = %s"
            val = (hid,)
            mycursor.execute(query, val)
            myresult = mycursor.fetchone()
            hall_id=myresult[0]
            catering = input("Do you want catering service from the hall owner: ")
            print("-" * 75)

            query = "INSERT INTO 1WsKFaZQ0B.quotation (hall_id, u_id, owner_id, occasion, quantity, duration, start_date, catering) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (hid, user_id, hall_id,occasion,capacity,duration, date, catering)
            mycursor.execute(query, val)
            mydb.commit()
            print("Thank you for the input.\n\nThe owner will soon reply to your quotation.")

            query = "Select quot_id from 1WsKFaZQ0B.quotation where hall_id = %s and u_id = %s and occasion=%s and start_date=%s"
            val = (hid,user_id,occasion,date)
            mycursor.execute(query, val)
            myresult = mycursor.fetchone()
            print("\nYour quotation number is = ",myresult[0],". Please note this for further reference.")
            pass

        else:
            print("\nPlease enter the correct hall id you wish to book.")
            booking_hall(user_id, user_name)
    else:
        print("\nYou have entered an invalid hall id")

def hall_info_display(myresult):
    print("\nHall ID : ", myresult[0])
    print("Hall Name : ", myresult[1])
    print("Hall ID : ", myresult[2])
    print("Occasion type : ", myresult[3])
    print("Capacity : ", myresult[4])
    print("Catering availability : ", myresult[5], "\n")
    print("-" * 75)
