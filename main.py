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

@app.route('/')
def main():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    user_name=request.form['name']
    user_password=request.form['password']

    password=SQLARG.get_user(user_name, user_password)
    print(password)
    print(user_password)
    if password==user_password:
        return render_template('login.html')
    else:
        return render_template('register.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    user_name=request.form['name']
    user_password=request.form['password']

    SQLARG.insert_user(user_name, user_password)

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)