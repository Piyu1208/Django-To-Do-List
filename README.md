
```markdown
# 📝 Django To-Do List App

A simple web-based To-Do List built with Django that allows users to register, log in, and manage their personal tasks. Each user can create, update, and delete their own tasks after logging in.

## 🚀 Features

- User authentication (register, login, logout)
- Create tasks
- Mark tasks as completed
- Update task details
- Delete tasks
- Only logged-in users can manage their own tasks

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, Django Templates
- **Database**: SQLite (default with Django)


## 📂 Project Structure

todo/ # Root project folder │ ├── manage.py # Django's command-line utility ├── requirements.txt # Python dependencies ├── render.yaml # Configuration file for deploying on Render ├── db.sqlite3 # SQLite database (local development only) │ ├── todo/ # Main Django project directory │ ├── init.py │ ├── settings.py # Project settings (debug, apps, middleware, etc.) │ ├── urls.py # Root URL configurations │ ├── wsgi.py # WSGI entry point for deployment │ ├── todoapp/ # Core application directory │ ├── init.py │ ├── models.py # Task model (with user, name, status) │ ├── views.py # Views for login, registration, task CRUD │ ├── forms.py # Custom forms for Task and User │ ├── admin.py # (Optional) Admin panel setup │ ├── templates/ # Templates directory │ └── todoapp/ # All app-related HTML files │ ├── home.html # Main task page │ ├── login.html # Login form │ ├── register.html # User signup form │ ├── update_task.html # Update existing task │ └── delete.html # Confirm task deletion │ └── static/ #

## ✅ How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/django-todo-app.git
   cd django-todo-app
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Open in browser**
   ```
   http://127.0.0.1:8000/
   ```

## 👤 Author

- **Piyuhs Sharma**
- GitHub: [@Piyu1208](https://github.com/Piyu1208)

## 📄 License

This project is open-source and free to use.

---

```

---
