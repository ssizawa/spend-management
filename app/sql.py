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
    host="database",
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
        return result_pass

    def insert_user(self, name, password):
        conn.ping(reconnect=True)
        cur = conn.cursor() 
        # print(values[1])
        sql = "insert into User (name, password) VALUE ( '"+str(name)+ "' , '" + str(password) + "'" + ")"
        # print(sql)
        cur.execute(sql)
        conn.commit()

    def insert_price(self, user_name, price_name, price, date):
        conn.ping(reconnect=True)
        cur = conn.cursor()
        sql = "insert into Spend (spend_name, price, pic, date) VALUE ( '"+str(price_name)+ "' , '"+price+ "' , '"+str(user_name)+ "' , '"+str(date)+"'"+ ")"
        cur.execute(sql)
        conn.commit()
    
    def get_info(self, user_name, year, mon):
        conn.ping(reconnect=True)
        cur = conn.cursor()
        if mon<10:
            sql = "select spend_name,price,date from Spend where pic ='"+str(user_name)+"' && DATE_FORMAT(date, '%Y%m')='"+str(year)+str(0)+str(mon)+"'"
        else:
            sql = "select spend_name,price,date from Spend where pic ='"+str(user_name)+"' && DATE_FORMAT(date, '%Y%m')='"+str(year)+str(mon)+"'"
        cur.execute(sql)
        price_data=cur.fetchall()
        return price_data
    
    def delete_spend(self, user_name, spendName, price):
        conn.ping(reconnect=True)
        cur = conn.cursor()
        sql = "delete from Spend where pic = '"+str(user_name)+"' &&spend_name ='"+str(spendName)+"' &&price='"+str(price)+"'"
        print(user_name, spendName, price)
        cur.execute(sql)
        conn.commit()