import mysql.connector as mysql
import sqlalchemy as db
import datetime

# *****************
# 初期設定
# *****************
dt_now = datetime.datetime.now()
user_name = "izawa"
password = "izawa"
host = "database"  # docker-composeで定義したMySQLのサービス名
database_name = "tasks_db"
conn = mysql.connect(
    host="localhost",
    user="izawa",
    passwd="izawa",
    port=3306,
    database="tasks_db",
    buffered = True
)

class sql_arg:
    def get_user(self, name, password):
        conn.ping(reconnect = True)
        cur = conn.cursor()
        sql = "select password from User where name='"+str(name)+"'"
        cur.execute(sql)
        result_pass = cur.fetchall()
        print('--1--')
        print('--2--')
        return result_pass

    def insert_user(self, name, password):
        conn.ping(reconnect=True)
        cur = conn.cursor() 
        # print(values[1])
        sql = "insert into User (name, password) VALUE ( '"+str(name)+ "' , '" + str(password) + "'" + ")"
        # print(sql)
        cur.execute(sql)
        conn.commit()