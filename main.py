from flask import Flask
from flask import render_template, request
from sql import sql_arg
SQLARG = sql_arg()

# host = "database"  # docker-composeで定義したMySQLのサービス名
# database_name = "tasks_db"
# conn = mysql.connect(
#     host="database",
#     user="izawa",
#     passwd="izawa",
#     port=3306,
#     database="tasks_db",
#     buffered = True
# )

app = Flask(__name__)

class User:
    id: int
    name: str
    password: str

@app.route('/')
def main():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('index.html',user_name=User.name)

@app.route('/login', methods=['POST'])
def login():
    user_name=request.form['name']
    user_password=request.form['password']



    password=SQLARG.get_user(user_name, user_password)
    
    for p in password[0]:
        new_pass=p

    props={'title': new_pass, 'msg': user_password}
    if new_pass==user_password:
        User.name=user_name
        User.password=user_password
        return render_template('index.html', user_name=user_name)
    else:
        return render_template('hello.html', props=props)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    user_name=request.form['name']
    user_password=request.form['password']

    SQLARG.insert_user(user_name, user_password)

    return render_template('login.html')

@app.route('/add_price', methods=['POST'])
def add_price():
    price_name=request.form['price_name']
    user_price=request.form['price']

    SQLARG.insert_price(User.name, price_name, user_price)

    return render_template('index.html', user_name=User.name)

@app.route('/sum')
def sum():
    pricelist_tmp=SQLARG.get_info(User.name)
    price_list=[]
    sum_price=0
    for i in pricelist_tmp:
        price_name=i[0]
        price=i[1]
        sum_price+=price
        price_info={
            'name': price_name,
            'price': price
        }
        price_list.append(price_info)
        
    return render_template('sum.html', price=price_list, sum_price=sum_price)

if __name__ == '__main__':
    app.run(debug=True)