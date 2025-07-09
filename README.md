# 🛠️ Freelance Marketplace API

A backend API for a freelance marketplace platform built using Django and Django REST Framework. This system supports user registration (clients & freelancers), service listings, reviews, and a public freelancer directory. Authentication is handled via JWT tokens.

## 🚀 Features
- 🔐 JWT-based Authentication (Login/Register)
- 👤 Role-based User Model (Freelancer / Client)
- 📦 Freelancers can post services
- 💬 Clients can post reviews on services
- 📂 Public Freelancer Directory
- ✅ Protected API endpoints
- 📬 Ready for Postman testing

## 🧱 Tech Stack
- Backend: Django, Django REST Framework
- Auth: Simple JWT
- Database: SQLite (default, easily swappable)
- Testing: Postman
- Version Control: Git

## 🔑 API Endpoints

### 🔐 Authentication
- `POST /api/users/register/` — Register a new user
- `POST /api/users/login/` — Get JWT access/refresh tokens
- `POST /api/users/token/refresh/` — Refresh token

### 🧑‍💻 Freelancer Directory
- `GET /api/freelancers/` — List all freelancers
- `GET /api/freelancers/{id}/` — Get specific freelancer profile

### 📦 Services
- `GET /api/services/` — List all services
- `POST /api/services/` — Create new service (freelancer only)
- `GET /api/services/{id}/` — Service details

### 💬 Reviews
- `POST /api/reviews/` — Post a review (client only)
- `GET /api/reviews/` — View all reviews

## 🛠️ Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/your-username/freelance-marketplace-api.git
cd freelance-marketplace-api
