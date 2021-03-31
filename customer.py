import user_class
import mysql.connector

mydb = mysql.connector.connect(
    host="remotemysql.com",
    port="3306",
    user="1WsKFaZQ0B",
    passwd="V2QSOib3dp",
    database="1WsKFaZQ0B"
)

class customer(user_class.users):
        pass

cust_obj=user_class.users()

def register():
    name = input("\nEnter name : ")
    uname = input("Enter username : ")
    pword = input("Enter password : ")
    ph_num = int(input("Enter phone : "))
    email = input("Enter email: ")
    s_citi = input("honor citizen \nplease enter yes or no")
    s_vet = input("veteran \nplease enter yes or no ")

    cust_obj.set_name(name)
    cust_obj.set_uname(uname)
    cust_obj.set_pass(pword)
    cust_obj.set_ph_num(ph_num)
    cust_obj.set_email(email)
    cust_obj.set_s_citi(s_citi)
    cust_obj.set_s_vet(s_vet)

    mycursor = mydb.cursor()
    query = "INSERT INTO 1WsKFaZQ0B.customer (name,user_name,password,ph_num,email,s_citi,s_vet) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (cust_obj.get_name(), cust_obj.get_uname(), cust_obj.get_pass(), cust_obj.get_ph_num(), cust_obj.get_email(),cust_obj.get_s_citi,cust_obj.get_s_vet)
    mycursor.execute(query, val)
    mydb.commit()

def login():
    uname=input("\nEnter username : ")
    pword=input("Enter your password : ")
    query="SELECT * FROM 1WsKFaZQ0B.customer where user_name = %s and password = %s"
    val=(uname,pword)
    mycursor = mydb.cursor()
    mycursor.execute(query, val)
    myresult = mycursor.fetchone()
    if myresult != None:
        return myresult

    else:
        return -1
