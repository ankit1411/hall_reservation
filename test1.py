import mysql.connector

mydb = mysql.connector.connect(
    host="remotemysql.com",
    port="3306",
    user="1WsKFaZQ0B",
    passwd="V2QSOib3dp",
    database="1WsKFaZQ0B"
)

mycursor = mydb.cursor()

#query="insert into 1WsKFaZQ0B.customer values(null,'John snow','json','GoT',9888,'js@gmail.com')"
#mycursor.execute(query)      #name,username,password,phone_num,email ****ORDER IMPORTANT
#mydb.commit()
'''
mycursor.execute("Select * from 1WsKFaZQ0B.customer")
myresult = mycursor.fetchall()

print(myresult)

mycursor.execute("Select * from 1WsKFaZQ0B.owner")
myresult = mycursor.fetchall()

print(myresult)

mycursor.execute("Select * from 1WsKFaZQ0B.admin")
myresult = mycursor.fetchall()

print(myresult)

query="SELECT * FROM 1WsKFaZQ0B.owner where name = %s and password = %s"
val=("owner","own123")
mycursor.execute(query,val)
myresult = mycursor.fetchone()
if myresult!=None:
    print(myresult[0],myresult[1])
else:
    print("Enter valid username and password")
    
mycursor.execute("Select * from 1WsKFaZQ0B.halls where availability='Y'")
myresult = mycursor.fetchall()

print("-"*75)
for x in myresult:
    print("\nHall ID : ",x[0])
    print("Hall Name : ", x[1])
    print("Hall ID : ", x[2])
    print("Occasion type : ", x[3])
    print("Capacity : ", x[4])
    print("Catering availability : ", x[5],"\n")
    print("-"*75)


uname=input("\nEnter hall ID : ")
query="SELECT * FROM 1WsKFaZQ0B.halls where capacity>%s and availability='Y'"
val=(uname,)
#mycursor = mydb.cursor()
mycursor.execute(query,val)
myresult = mycursor.fetchall()
if myresult != None:
    print( myresult)
'''
#query="insert into 1WsKFaZQ0B.customer values(null,'John snow','json','GoT',9888,'js@gmail.com')"
#mycursor.execute(query)      #name,username,password,phone_num,email ****ORDER IMPORTANT
#mydb.commit()

cursor=mydb.cursor()
query = "INSERT INTO 1WsKFaZQ0B.quotation (Hall_ID, u_id, owner_id, occasion, quantity, duration, start_date, catering,  u_name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val = ( 3, 10, 6, "Birthday", 20 , 10 , "2019-10-12", "Y", "Null",)
cursor.execute(query, val)
mydb.commit()