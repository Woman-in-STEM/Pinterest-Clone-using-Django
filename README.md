# Pinterest Clone using Django


## 📌 Overview
This project is a **Pinterest Clone** built using **Django**. It allows users to upload, save, and organize images into collections, similar to Pinterest. The application features authentication, image uploading, and board creation.

## ✨ Features
- User authentication (Sign up, Login)
- Upload and manage images
- Create boards/collections
- Responsive UI

## 🛠️ Tech Stack
- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite / PostgreSQL
- **Authentication**: Django Authentication System

## 🚀 Installation

### Prerequisites
Make sure you have the following installed:
- Python (>= 3.8)
- Django (>= 4.0)
- pip & virtualenv
- PostgreSQL (optional for production)

### Steps to Run the Project
1. **Clone the repository**
   ```bash
   git clone https://github.com/Woman-in-STEM/Pinterest-Clone-using-Django.git
   cd pinterest-clone
   ```
2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Run database migrations**
   ```bash
   python manage.py migrate
   ```
4. **Create a superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```
5. **Start the development server**
   ```bash
   python manage.py runserver
   ```
6. **Access the app** in your browser at:
   ```
   http://127.0.0.1:8000/
   ```

## 📸 Screenshots
![image](https://github.com/user-attachments/assets/c4d912ab-c4dc-440d-a31d-e841e2a99189)

![image](https://github.com/user-attachments/assets/d85160df-3976-455d-8f02-8e4478f18469)

![image](https://github.com/user-attachments/assets/35d9ae18-b300-4447-bcbe-d1d27a917fbc)

![image](https://github.com/user-attachments/assets/e2822327-d31d-479a-a63f-1d8b4b9dd9ed)

![image](https://github.com/user-attachments/assets/b24f3ae7-32ad-4a02-b3d8-5953dda2deaa)

![image](https://github.com/user-attachments/assets/5280319f-80c6-4ff3-8ff6-f806d3ab2c4a)


## 🛡️ Security & Best Practices
- Use `.env` file to store secrets
- Enable Django’s security settings for production
- Use a cloud storage provider (AWS S3) for media files

## 📄 License
This project is open-source and available under the **MIT License**.

## 💡 Contribution
Contributions are welcome! Feel free to open issues and submit pull requests.

## 📬 Contact
For any inquiries, reach out via **GitHub**: [Woman in STEM](https://github.com/Woman-in-STEM)

---
⭐ If you like this project, give it a star on GitHub! 🚀
