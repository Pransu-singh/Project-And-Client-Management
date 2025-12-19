# Full Stack Web Application with Secure Admin Panel

This is a full-stack web application developed using **Python Flask**.  
The project consists of a dynamic landing page and a **secure admin panel** that allows administrators to manage projects, clients, contact form responses, and newsletter subscriptions.

The application is designed according to the given assignment requirements and focuses on functionality, usability, security, and clean code structure.

---

## 🔗 Submission Links

Github Link :
https://github.com/your-username/your-repository-name

Deployment Link :
https://your-project-name.onrender.com

Description Document (Google Drive Link) :
https://drive.google.com/file/d/your-file-id/view

---

## 🎯 Project Objective

The objective of this project is to build a complete full-stack web application that includes:
- A user-facing landing page
- Backend integration for dynamic data
- A secure admin panel for managing all content
- Proper deployment on a cloud platform

---

## 🌐 Landing Page Features

The landing page fetches all data dynamically from the backend and includes:

### 🔹 Our Projects Section
- Project Image
- Project Name
- Project Description
- Dummy "Read More" button (non-functional as required)

### 🔹 Happy Clients Section
- Client Image
- Client Name
- Client Designation
- Client Description

### 🔹 Contact Form
- Full Name
- Email Address
- Mobile Number
- City  
- Form data is stored in the database and visible in the admin panel

### 🔹 Newsletter Subscription
- User can enter email address
- Subscribed emails are stored in the database
- Admin can view all subscribers

---

## 🔐 Admin Panel & Security

- The website includes an **Admin Login button in the footer** for security purposes
- Only authenticated users can access the admin panel
- Admin Panel allows:
  - Adding and managing projects
  - Adding and managing client details
  - Viewing contact form submissions
  - Viewing newsletter subscribers

Admin Routes:
/login → Admin Login Page
/admin → Admin Dashboard

yaml
Copy code

---

## 🧰 Technology Stack

### Frontend
- HTML
- CSS
- JavaScript
- Jinja Templates (Flask)

### Backend
- Python
- Flask Framework

### Database
- SQLite (site.db)

### Deployment
- Render (Free Tier)

---

## 📂 Project Structure

website_project/
├── app.py # Main Flask application
├── requirements.txt # Project dependencies
├── README.md # Project documentation
├── instance/
│ └── site.db # SQLite database (included for demo)
│
├── static/
│ ├── css/
│ │ └── style.css
│ ├── js/
│ └── uploads/ # Project & client images
│
├── templates/
│ ├── index.html # Landing page
│ ├── login.html # Admin login page
│ └── admin.html # Admin panel

yaml
Copy code

---

## ⚙️ How to Run the Project Locally

### Step 1: Install dependencies
```bash
pip install -r requirements.txt
Step 2: Run the application
bash
Copy code
python app.py
Step 3: Open in browser
cpp
Copy code
http://127.0.0.1:5000
🗄 Database Information
SQLite database (site.db) is included for evaluation purposes

Database contains:

Admin credentials

Sample projects

Sample clients

Contact form entries

Newsletter subscribers

📌 Including the database ensures:

Admin login works immediately

Evaluators can see complete functionality without extra setup

⭐ Additional Notes
Clean and readable code structure

Secure admin authentication

Dynamic backend integration

Responsive UI

Project follows best practices for a full-stack Flask application

📊 Evaluation Criteria Coverage
✔ Functionality – All required features implemented
✔ Code Quality – Clean and structured code
✔ Design – Matches reference layout and usability
✔ Security – Admin login for protected access
✔ Deployment – Live and publicly accessible

