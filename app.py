from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/do_register', methods=['POST'])
def do_register():
    user_id = request.form.get('user_id')
    password = request.form.get('password')

    if user_id in users:
        return "User already exists!", 400
    
    users[user_id] = password
    return redirect(url_for('index'))

@app.route('/do_login', methods=['POST'])
def do_login():
    user_id = request.form.get('user_id')
    password = request.form.get('password')

    if user_id in users and users[user_id] == password:
        return "Login successful!", 200
    return "Invalid credentials!", 401

if __name__ == '__main__':
    app.run(debug=True)
