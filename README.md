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


