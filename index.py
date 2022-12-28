from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template, request

from DataStore.MySQL import MySQL
dns = {
    'user': 'mysql',
    'host': 'localhost',
    'password': 'izawa',
    'database': 'kaggle'
}
db = MySQL(**dns)

app = Flask(__name__)

@app.route('/')
def main():
    props = {'title': 'Step-by-Step Flask - index', 'msg': 'Welcome to Index Page.'}
    html = render_template('index.html', props=props)
    return html

@app.route('/hello')
def hello():
    props = {'title': 'Step-by-Step Flask - hello', 'msg': 'Hello World.'}
    html = render_template('hello.html', props=props)
    return html

# @app.route('/add', methods=['POST'])
# def useradd():
#     props = {'title': 'Step-by-Step Flask - index', 'msg': 'Welcome to Index Page.'}
#     name=request.form['name']
#     age=request.form['age']
#     gender=request.form['gender']
#     print(name, age, gender)
#     stmt='INSERT INTO users (name, age, gender) VALUE('+name+','+age+','+gender+')'
#     hello=db.query(stmt)
#     return render_template('index.html', props=props)

# @app.route('/users')
# def users():
#     props = {'title': 'Users List', 'msg': 'Users List'}
#     stmt = 'SELECT * FROM users'
#     users = db.query(stmt)
#     html = render_template('users.html', props=props, users=users)
#     return html

# @app.route('/users/<int:id>')
# def user(id):
#     props = {'title': 'User Information', 'msg': 'User Information'}
#     stmt = 'SELECT * FROM users WHERE id = ?'
#     user = db.query(stmt, id, prepared=True)
#     html = render_template('user.html', props=props,user=user[0])
#     return html

@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True)