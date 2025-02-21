# Auth System with Google OAuth & JWT Authentication

This is a Django-based authentication system that supports:
- User registration & login using JWT
- Google OAuth authentication
- API-based authentication using Django Rest Framework

## 🚀 Features
- JWT authentication for secure API access
- Google OAuth for easy login/signup
- User profile management
- Frontend integration with Django templates

## 🛠️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/GarimaSingh16/Auth_System2.git
cd Auth_System2
```

### 2️⃣ Create a Virtual Environment & Activate It
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file in the root directory and add:
```ini
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=*
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
```

### 5️⃣ Apply Migrations & Create Superuser
```bash
python manage.py migrate
python manage.py createsuperuser  # Follow the prompts to create an admin user
```

### 6️⃣ Run the Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000` to access the application.

## 🔗 API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/api/register/` | Register a new user |
| POST | `/api/token/` | Obtain JWT token |
| POST | `/api/token/refresh/` | Refresh JWT token |
| GET | `/api/user/` | Get user profile (requires authentication) |
| GET | `/google-login/` | Redirect to Google OAuth login |
| GET | `/google-profile/` | Fetch Google user profile |

## 🎨 Frontend Views
- `/auth/login/` → User Login Page
- `/dashboard/` → User Dashboard
- `/google-login/` → Google Login Page

## 🐟 License
This project is licensed under the MIT License.

