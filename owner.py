import user_class
import mysql.connector

mydb = mysql.connector.connect(
    host="remotemysql.com",
    port="3306",
    user="1WsKFaZQ0B",
    passwd="V2QSOib3dp",
    database="1WsKFaZQ0B"
)

class owner(user_class.users):
        pass

own_obj=user_class.users()

def register():
    name = input("\nEnter name : ")
    uname = input("Enter username : ")
    pword = input("Enter password : ")
    ph_num = int(input("Enter phone : "))
    email = input("Enter email: ")
    own_obj.set_name(name)
    own_obj.set_uname(uname)
    own_obj.set_pass(pword)
    own_obj.set_ph_num(ph_num)
    own_obj.set_email(email)

    mycursor = mydb.cursor()
    query = "INSERT INTO 1WsKFaZQ0B.owner (name,user_name,password,ph_num,email) VALUES (%s,%s,%s,%s,%s)"
    val = (own_obj.get_name(), own_obj.get_uname(), own_obj.get_pass(), own_obj.get_ph_num(), own_obj.get_email())
    mycursor.execute(query, val)
    mydb.commit()

def login():
    uname=input("\nEnter username : ")
    pword=input("\nEnter your password : ")
    query="SELECT * FROM 1WsKFaZQ0B.owner where user_name = %s and password = %s"
    val=(uname,pword)
    mycursor = mydb.cursor()
    mycursor.execute(query, val)
    myresult = mycursor.fetchone()
    if myresult != None:
        return myresult

    else:
        return -1

