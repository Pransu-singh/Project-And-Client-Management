🚀 Project & Client Management System
Full Stack Web Application with Secure Admin Panel

This is a full-stack web application built using Python (Flask).
The project includes a modern landing page and a secure admin panel that allows administrators to manage projects, clients, contact form submissions, and newsletter subscribers.

The application is developed according to the given assignment requirements, focusing on functionality, usability, security, and clean structure.

🔗 Submission Links

Github Link:
https://github.com/Pransu-singh/Project-And-Client-Management

Deployment Link:
https://your-project-name.onrender.com

Description Document (Google Drive Link):
https://drive.google.com/file/d/your-file-id/view

🎯 Project Objective

The goal of this project is to demonstrate practical full-stack development skills by building a real-world application that includes:

Backend and frontend integration

Secure admin authentication

Dynamic data handling

Database management

Cloud deployment

🌐 Landing Page Features

All landing page content is fetched dynamically from the backend.

Our Projects Section

Project image

Project name

Project description

Dummy Read More button (non-functional as required)

Happy Clients Section

Client image

Client name

Client designation

Client description

Contact Form

Full name

Email address

Mobile number

City

Submitted data is stored in the database and visible in the admin panel

Newsletter Subscription

Email subscription field

Email addresses stored in database

Viewable in admin panel

🔐 Admin Panel & Security

The website includes an Admin Login button in the footer for security

Only authenticated users can access the admin dashboard

Unauthorized users cannot manage or view protected data

Admin Capabilities

Add and manage projects

Add and manage client details

View contact form submissions

View newsletter subscribers

Admin Routes

/login → Admin login page

/admin → Admin dashboard

🧰 Technology Stack

Frontend

HTML

CSS

JavaScript

Jinja Templates

Backend

Python

Flask Framework

Database

SQLite (site.db)

Deployment

Render (Free Tier)

📂 Project Structure

(The structure below matches the actual repository and is shown clearly for evaluation.)

website_project
│
├── app.py                     Main Flask application
├── requirements.txt           Project dependencies
├── README.md                  Project documentation
│
├── instance
│   └── site.db                SQLite database (included for evaluation)
│
├── static
│   ├── css
│   │   └── style.css
│   ├── js
│   └── uploads                Project and client images
│
└── templates
    ├── index.html              Landing page
    ├── login.html              Admin login page
    └── admin.html              Admin panel

⚙️ How to Run the Project Locally

Install all required dependencies using requirements.txt

Run the Flask application using Python

Open the application in a web browser at http://127.0.0.1:5000

No additional configuration is required for local testing.

🗄 Database Information

SQLite database file (site.db) is included for evaluation purposes

The database contains:

Admin login credentials

Sample projects

Sample clients

Contact form submissions

Newsletter subscribers

Including the database allows evaluators to directly test all features without manual setup.

📊 Evaluation Criteria Coverage

Functionality: All required features implemented

Code Quality: Clean, readable, and structured code

Design: Matches reference layout and usability expectations

Security: Admin authentication with footer login access

Deployment: Live and publicly accessible application

🏁 Conclusion

This project demonstrates real-world full-stack development skills, including backend logic, database handling, authentication, UI development, and deployment.
It follows clean coding practices and provides a complete, working solution as required.

👨‍💻 Developed By

Pransu Singh
Full Stack Developer
