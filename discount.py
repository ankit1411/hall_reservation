import mysql.connector

mydb = mysql.connector.connect(
    host="remotemysql.com",
    port="3306",
    user="1WsKFaZQ0B",
    passwd="V2QSOib3dp",
    database="1WsKFaZQ0B"
)
mycursor = mydb.cursor()



class Discount():
    def __init__(self,discount_type, discount_rate):
        self._discount_type = discount_type
        self._discount_rate = discount_rate

    def discount_type(self):
        return self._discount_type

    def set_discount_type(self, discount_type):
        self._discount_type = discount_type

    def discount_rate(self):
        return self._discount_rate

    def set_discount_rate(self, discount_rate):
        self._discount_rate = discount_rate


def display_discount():
    sql='Select * from 1WsKFaZQ0B.discount ;'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print("hall id  admin id owner id discount type discount rate")
    for i in myresult:
        print(i)





def edit_discount():
    display_discount()
    hall_id = int(input("\nplease enter hall id: "))
    print("\nPlease enter discount type:\n1.veteran discount\n2.honor citizen discount")
    discount_type_sel = int(input("\nplease enter your choice:"))
    if discount_type_sel == 1:
        discount_type = "veteran discount"
    else:
        discount_type = "honor citizen discount"
    discount_rate = int(input("Enter new discount rate : "))
    discount = Discount(discount_type, discount_rate)
    # Discount.set_discount_rate(discount_rate)
    query = 'UPDATE 1WsKFaZQ0B.discount set discount_type="%s", discount_rate=%d where hall_id=%d'\
            % (discount.discount_type(), discount.discount_rate(), hall_id)
    mycursor.execute(query)
    mydb.commit()
    print("new discount data")
    #display_discount()
    sql = 'select * from 1WsKFaZQ0B.discount where hall_id="%d"' % hall_id
    mycursor.execute(sql)
    new_data=mycursor.fetchall()
    print(new_data)




