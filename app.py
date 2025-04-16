from flask import Flask, render_template, request, redirect, url_for, session, flash
import firebase_admin
from firebase_admin import credentials, auth
import json
import pyrebase
import dropbox
from dropbox.exceptions import AuthError
from threading import Timer
import qrcode
import io
import base64


app = Flask(__name__)
app.secret_key = 'c3b579c35369ea25ab99c3e64b438e3f7b826cd087a79e50c439c48d388dbc0e'


########### drop box functions  ##################

db_client = None

# Store files and delete timers
active_files = {}

def delete_file(path):
    try:
        if db_client:
            db_client.files_delete_v2(path)
            print(f"Deleted: {path}")
    except Exception as e:
        print(f"Error deleting file: {e}")

def handle_file_upload(file):
    try:
        file_path = f"/{file.filename}"
        db_client.files_upload(file.read(), file_path, mode=dropbox.files.WriteMode.overwrite)
        shared_link_metadata = db_client.sharing_create_shared_link_with_settings(file_path)
        url = shared_link_metadata.url.replace('?dl=0', '?dl=1')

        # Schedule file deletion
        t = Timer(1800, delete_file, args=[file_path])  # 30 minutes = 1800 seconds
        t.start()
        active_files[file_path] = t

        return url
    except Exception as e:
        return f"error: {e}"


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
            user = login_auth.create_user_with_email_and_password(email=email, password=password)
            return redirect(url_for('login'))
        except Exception as e:
            return render_template('register.html',email_error="Email already exists")
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = login_auth.sign_in_with_email_and_password(email=email,password=password)
            session['user'] = email  # Store user session
            return redirect(url_for('app_page'))
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
            print(reset_link)
            return render_template('forgot_password.html',reset_link=reset_link)
        except Exception as e:
            return render_template('forgot_password.html',error="Invalid Email")

    return render_template('forgot_password.html')



@app.route('/app')
def app_page():
    if 'user'  in session:
        return redirect(url_for("token_input"))
    return redirect(url_for('login'))


@app.route('/token_input', methods=['GET', 'POST'])
def token_input():
    if "user" in session:
        global db_client
        if request.method == 'POST':
            token = request.form['access_token']
            try:
                db_client = dropbox.Dropbox(token)
                db_client.users_get_current_account()
                session['access_token'] = token
                return redirect(url_for('upload_file'))
            except AuthError:
                flash('Invalid Access Token!')
        return render_template('token_input.html')
    return redirect(url_for('login'))
    

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if 'user' in session:
        global db_client
        if 'access_token' not in session:
            flash('Access token not found. Please enter it first.')
            return redirect(url_for('login'))

        if not db_client:
            db_client = dropbox.Dropbox(session['access_token'])
        
        download_url = ""
        error_message = ""
        qr_code = None

        if request.method == 'POST':
            file = request.files['file']
            if file:
                result = handle_file_upload(file)
                if result.startswith("error:"):
                    error_message = result
                else:
                    download_url = result

                    # Generate QR code for the download URL
                    qr = qrcode.make(download_url)
                    buffer = io.BytesIO()
                    qr.save(buffer, format="PNG")
                    buffer.seek(0)
                    qr_code = base64.b64encode(buffer.getvalue()).decode('ascii')

        user_name = session['user']
        user_name = user_name.split("@")[0]
        return render_template(
            'file_upload.html',
            download_url=download_url,
            qr_code=qr_code,
            error_message=f"{error_message}".split("(")[0],
            user_name=str(user_name)
        )
    
    return redirect(url_for('login'))

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/use")
def How_to_use():
    return render_template("how_to_use.html")

@app.route('/logout',)
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True,port=5003)
