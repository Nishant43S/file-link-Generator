# 🔗 File Link Generator


The **File Link Generator App** is a web-based tool that allows users to upload files and generate secure, shareable download links along with QR codes. Built using **Flask** and integrated with **Dropbox API**, it provides a fast and efficient way to share files online.

Live app [Click Here to Use](https://file-link-generator-major-project.onrender.com)
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
  - Drag-and-drop file upload interface
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
python wsgi.py
```

