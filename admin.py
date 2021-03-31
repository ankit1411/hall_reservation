import user_class
import mysql.connector

mydb = mysql.connector.connect(
    host="remotemysql.com",
    port="3306",
    user="1WsKFaZQ0B",
    passwd="V2QSOib3dp",
    database="1WsKFaZQ0B"
)

def login():
    uname=input("\nEnter username : ")
    pword=input("\nEnter your password : ")
    query="SELECT * FROM 1WsKFaZQ0B.admin where user_name = %s and password = %s"
    val=(uname,pword)
    mycursor = mydb.cursor()
    mycursor.execute(query, val)
    myresult = mycursor.fetchone()
    if myresult != None:
        return myresult

    else:
        return -1