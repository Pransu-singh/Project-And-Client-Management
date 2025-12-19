# 🚀 Project & Client Management System  
### Full Stack Web Application with Secure Admin Panel

A complete **full-stack web application** built using **Python (Flask)** that includes a dynamic landing page and a **secure admin panel**.  
The application allows administrators to manage projects, clients, contact form submissions, and newsletter subscribers, while users can interact with a clean and responsive landing page.

---

## 🔗 Submission Links

**Github Link :**  
https://github.com/Pransu-singh/Project-And-Client-Management

**Deployment Link :**  
https://your-project-name.onrender.com

**Description Document (Google Drive Link) :**  
https://drive.google.com/file/d/your-file-id/view

---

## 🎯 Objective

The objective of this project is to demonstrate full-stack development skills by building a real-world application that includes:

- Backend data handling
- Secure admin authentication
- Dynamic content rendering
- Database integration
- Cloud deployment

---

## 🌐 Landing Page Features

The landing page fetches all data dynamically from the backend and includes:

### 📌 Our Projects Section
- Project Image
- Project Name
- Project Description
- Dummy **Read More** button (as required)

### 📌 Happy Clients Section
- Client Image
- Client Name
- Client Designation
- Client Description

### 📌 Contact Form
- Full Name
- Email Address
- Mobile Number
- City  
- Submitted data is stored in the database and visible in the admin panel

### 📌 Newsletter Subscription
- Email subscription form
- Subscribed emails stored in database
- Viewable by admin

---

## 🔐 Admin Panel & Security

- The website includes an **Admin Login button in the footer** for security
- Only authenticated users can access the admin dashboard
- Unauthorized access is restricted

### Admin Capabilities
- Add and manage projects
- Add and manage client details
- View contact form submissions
- View newsletter subscribers

### Admin Routes
- `/login` → Admin Login Page  
- `/admin` → Admin Dashboard  

---

## 🧰 Technology Stack

### Frontend
- HTML  
- CSS  
- JavaScript  
- Jinja Templates  

### Backend
- Python  
- Flask Framework  

### Database
- SQLite (`site.db`)

### Deployment
- Render (Free Tier)

---

## 📂 Project Structure

website_project/
│
├── app.py # Main Flask application
├── requirements.txt # Project dependencies
├── README.md # Documentation
│
├── instance/
│ └── site.db # SQLite database (included for demo & evaluation)
│
├── static/
│ ├── css/
│ │ └── style.css
│ ├── js/
│ └── uploads/ # Project & client images
│
└── templates/
├── index.html # Landing page
├── login.html # Admin login page
└── admin.html # Admin panel

yaml
Copy code

---

## ⚙️ How to Run the Project Locally

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
Step 2: Run the Application
bash
Copy code
python app.py
Step 3: Open in Browser
cpp
Copy code
http://127.0.0.1:5000
🗄 Database Information
SQLite database (site.db) is included for evaluation purposes

The database contains:

Admin login credentials

Sample projects

Sample clients

Contact form submissions

Newsletter subscribers

📌 Including the database ensures that the evaluator can directly test all features without additional setup.

📊 Evaluation Criteria Coverage
✔ Functionality – All required features implemented
✔ Code Quality – Clean, readable, and structured code
✔ Design – Matches reference layout and usability expectations
✔ Security – Admin authentication with footer login access
✔ Deployment – Live, publicly accessible application

🏁 Conclusion
This project showcases practical full-stack development skills, including backend logic, database integration, authentication, UI design, and cloud deployment.
It is built with scalability and usability in mind while following clean coding practices.

👨‍💻 Developed By
Pransu Singh
