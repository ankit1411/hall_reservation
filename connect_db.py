import mysql.connector

def connect_db():
    db_service = mysql.connector.connect(
        host="remotemysql.com",
        port="3306",
        user="1WsKFaZQ0B",
        passwd="V2QSOib3dp",
        database="1WsKFaZQ0B"
    )
    return db_service