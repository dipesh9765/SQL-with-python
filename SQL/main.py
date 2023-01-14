import mysql.connector as connector
from mysql.connector import Error
import pandas as pd



# class created
class Helper:
    # constructor created
    def __init__(self):
        self.con = connector.connect(host="localhost", port="3306", user="root", password="Royal@9765",
                                     database="pythontest")

        query = "create table if not exists user(userId int primary key ,username varchar(20), phone varchar(12) )"
        cur = self.con.cursor()
        print(cur)
        cur.execute(query)
        print("Created")


# main code
print("SQL doing")