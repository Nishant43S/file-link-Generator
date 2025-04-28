# 🔗 File Link Generator


The **File Link Generator App** is a web-based tool that allows users to upload files and generate secure, shareable download links along with QR codes. Built using **Flask** and integrated with **Dropbox API**, it provides a fast and efficient way to share files online.

Live app <a href="https://file-link-generator-major-project.onrender.com" target='_blank'>Click Here to Use</a>

---

## 🚀 Features

- 🔐 **User Authentication**
  - Register and log in with your email ID
  - Secure **Forgot Password** feature using Firebase

- ☁️ **Dropbox Integration**
  - Upload files directly to Dropbox
  - Generate temporary download links
  - Requires Dropbox Access Token (entered via token input field)

- 📁 **File Upload & Link Generation**
  - Upload any type of file
  - Instantly generate a **download link** and a **QR code**
  - Copy the download link to clipboard for easy sharing

- 💻 **Responsive UI**
  - file upload interface
  - Clean, modern design using Bootstrap 5
  - Font Awesome icons for intuitive visuals

---

## 🛠️ Technologies Used

### Frontend:
- HTML
- CSS
- JavaScript
- Bootstrap 5
- Font Awesome Icons

### Backend:
- Python
- Flask

### APIs & Services:
- Dropbox API (file storage and temporary link generation)
- Firebase (authentication and password recovery)

---

## 📌 How to Use

1. Register or log in using your email address.
2. If you're a new user, verify your email and log in.
3. Enter your **Dropbox Access Token** in the token input field.
4. Upload your file using the drag-and-drop area or file picker.
5. The app will generate:
   - A **download link**
   - A **QR code** for quick access
6. Click to **copy** the download link or scan the QR to download.

---

## 🧪 Run Locally

To run this project locally, use the following commands:

```bash
  git clone https://github.com/Nishant43S/file-link-Generator.git
```

```bash
  pip install -r requirements.txt
```
to run

```bash
  python wsgi.py
```

---

## 📁 Project Directory Structure

```plaintext
📂 project-root/
├── 📂 templates/         # HTML templates
│   └── 📄 *.html
├── 🌐 static/            # Static files
│   ├── 📂 js/            # JavaScript files
│   ├── 📂 css/           # CSS files
│   └── 🖼️ assets/        # Images & other assets
├── 🐍 __pycache__/       # Compiled Python files
│   └── 📦 *.pyc
├── 🔑 firebase/          # Firebase credentials
│   └── 🔒 credentials/
├── ⚙️ __init__.py        # Flask app package initializer
├── 📄 app.py             # Flask app backend
├── 📦 requirements.txt   # Project dependencies
└── 🚀 wsgi.py            # Entry point to run the app
```


## 🛠️ Technologies Used

- 🐍 Python  
- 🔥 Flask  
- 🌐 HTML, CSS, JavaScript  
- 🎨 Bootstrap 5  
- 🔐 Firebase (for authentication)  
- ☁️ Dropbox (for cloud storage)

## 📷 project screenshots

- landing page
  
![Screenshot 2025-04-18 201414](https://github.com/user-attachments/assets/712fb02f-4363-49ef-916b-d5ef1a785ac9)


![Screenshot 2025-04-18 201438](https://github.com/user-attachments/assets/1975d542-bb3a-4576-86a5-5595d3bb2df7)


![Screenshot 2025-04-18 201454](https://github.com/user-attachments/assets/0ab70203-4b67-4e67-ac28-53fa4982eb81)


- login page

![Screenshot 2025-04-18 202228](https://github.com/user-attachments/assets/f851adec-dbc2-43d0-ab56-f245dbe93afd)

- register page
  
![Screenshot 2025-04-18 202622](https://github.com/user-attachments/assets/7ca57a5d-9596-4083-8f4a-17ed9b37df2f)

- forgot password

![Screenshot 2025-04-18 204020](https://github.com/user-attachments/assets/ee5c5f87-f83a-44bb-80c8-daf171c8e06c)


- token input page

![Screenshot 2025-04-18 202925](https://github.com/user-attachments/assets/9a897dc2-0093-4578-b3bb-ae18caa8e9bc)

- upload page

![Screenshot 2025-04-18 203602](https://github.com/user-attachments/assets/f4ca529d-3a8c-4f5d-9c94-d678e0d53c2b)

![Screenshot 2025-04-18 203628](https://github.com/user-attachments/assets/413bc245-7b09-4f44-9895-829cfa9df91f)



## admin panel

![Screenshot 2025-04-23 004309](https://github.com/user-attachments/assets/8da76c83-cea9-47a3-8e93-38bb74a76001)

![Screenshot 2025-04-23 004429](https://github.com/user-attachments/assets/04074cdd-74cf-4b94-a1e2-752dcb5c4b8d)



![Screenshot 2025-04-23 004640](https://github.com/user-attachments/assets/7eb2ad7f-2a9f-4cb5-9076-91bf6ea0a2da)

![Screenshot 2025-04-23 005402](https://github.com/user-attachments/assets/ae8bc164-33df-469d-a746-85e192856875)


![Screenshot 2025-04-23 005734](https://github.com/user-attachments/assets/6da8a462-aa41-4637-879c-73e96acab21d)





![Screenshot 2025-04-23 005900](https://github.com/user-attachments/assets/266db5de-2817-4cf0-b81b-796557396fd6)


![Screenshot 2025-04-23 005959](https://github.com/user-attachments/assets/f6114869-9b15-411e-94c0-14278157ef5b)

---

## 📁 Project Directory Structure

```plaintext
📂 project-root/
📂 project-root/
├── 📂 .streamlit/                 # Streamlit configuration
│   └── ⚙️ config.toml
├── 🐍 __pycache__/            # Compiled Python files
│   └── 📦 *.pyc
├── 🎨 css/                             # Custom CSS files
│   └── 📄 *.css
├── 📄 html/                           # HTML files
│   └── 📄 *.html
├── 🔐 firebase/                    # Firebase credentials
│   └── 🔒 credentials/
├── ⚙️ __init__.py                  # App initializer
├── 🔥 firebase.py                # Firebase authentication functions
├── 📘 about_app.py           # About the application content
├── ➕ add_user.py              # Script to add new users
├── 🛠️ admin_page.py        # Main admin features and UI
├── 📦 requirements.txt     # Project dependencies
├── 🚀 streamlit_app.py     # Main entry point to run Streamlit app
└── 🖥️ admin.bat                  # Batch file to launch the admin app
```

---

### to run admin panel

```bash
  pip install -r requirements.txt
```
to run

```bash
  python -m streamlit run streamlit_app.py
```


