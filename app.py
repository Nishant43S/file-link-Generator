from flask import Flask, render_template, request, redirect, url_for, session
import firebase_admin
from firebase_admin import credentials, auth
import json
import pyrebase

app = Flask(__name__)
app.secret_key = 'c3b579c35369ea25ab99c3e64b438e3f7b826cd087a79e50c439c48d388dbc0e'

# Initialize Firebase Admin SDK
cred = credentials.Certificate("firebase/key.json")
firebase_admin.initialize_app(cred)

def read_cred(file_path):
    """Reads a JSON file config"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return None
    
firebaseConfig = read_cred("firebase/cred.json")

firebase = pyrebase.initialize_app(firebaseConfig)
login_auth = firebase.auth()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.create_user(email=email, password=password)
            return redirect(url_for('login'))
        except Exception as e:
            return render_template('register.html',email_error="Email already exists")
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_name = lambda email: email.split('@')[0]
        try:
            user = login_auth.sign_in_with_email_and_password(email=email,password=password)
            session['user'] = email  # Store user session
            return redirect(url_for('app_page',user=user_name(email=email)))
        except Exception as e:
            return render_template('login.html',error_msg="Invalid Credentials") 
    return render_template('login.html')

# Forgot Password 
@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        try:
            # Send reset password email
            reset_link = auth.generate_password_reset_link(email)
            return render_template('forgot_password.html',reset_link=reset_link)
        except Exception as e:
            return render_template('forgot_password.html',error="Invalid Email")

    return render_template('forgot_password.html')


@app.route('/app',methods=["GET","POST"],defaults={"user":None})
@app.route('/app/<user>',methods=["GET","POST"])
def app_page(user):
    if 'user'  in session:
        return render_template('app.html',user=user)
    return redirect(url_for('login'))

@app.route('/logout',)
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True,port=5003)
