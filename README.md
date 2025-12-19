Project and Client Management System
===================================

This repository contains a full stack web application developed using Python and Flask. 
The application provides a public-facing landing page along with a secure admin panel 
to manage projects, clients, contact form submissions, and newsletter subscriptions.

The project is implemented according to the given assignment requirements and focuses on 
clean structure, functionality, security, and deployment readiness.


Submission Links
----------------

Github Link:
https://github.com/Pransu-singh/Project-And-Client-Management

Deployment Link:
https://your-project-name.onrender.com

Description Document (Google Drive Link):
https://drive.google.com/file/d/your-file-id/view


Project Objective
-----------------

The objective of this project is to design and develop a complete full stack application 
that demonstrates:

- Backend and frontend integration
- Secure admin authentication
- Dynamic data handling
- Database management
- Cloud deployment on a free platform


Landing Page Features
---------------------

All content on the landing page is dynamically fetched from the backend.

Our Projects Section:
- Project image
- Project name
- Project description
- Read More button (non-functional as per requirement)

Happy Clients Section:
- Client image
- Client name
- Client designation
- Client description

Contact Form:
- Full name
- Email address
- Mobile number
- City
- Submitted data is stored in the database and displayed in the admin panel

Newsletter Subscription:
- Email subscription input
- Email addresses stored in database
- Accessible in admin panel


Admin Panel and Security
------------------------

The application includes a secure admin panel with authentication.

- An Admin Login button is provided in the footer section of the website
- Only authenticated users can access the admin dashboard
- Unauthorized access is restricted

Admin functionalities include:
- Adding and managing projects
- Adding and managing client information
- Viewing contact form submissions
- Viewing newsletter subscribers

Admin routes:
/login   - Admin login page
/admin   - Admin dashboard


Technology Stack
----------------

Frontend:
- HTML
- CSS
- JavaScript
- Jinja Templates

Backend:
- Python
- Flask Framework

Database:
- SQLite (site.db)

Deployment:
- Render (Free Tier)


Project Structure
-----------------

website_project/
|
|-- app.py                     Main Flask application
|-- requirements.txt           Project dependencies
|-- README.md                  Project documentation
|
|-- instance/
|   |-- site.db                SQLite database (included for evaluation)
|
|-- static/
|   |-- css/
|   |   |-- style.css
|   |-- js/
|   |-- uploads/               Project and client images
|
|-- templates/
    |-- index.html              Landing page
    |-- login.html              Admin login page
    |-- admin.html              Admin panel


Running the Project Locally
---------------------------

1. Install project dependencies using the requirements.txt file.
2. Run the Flask application using Python.
3. Open a web browser and navigate to http://127.0.0.1:5000


Database Information
--------------------

The SQLite database file (site.db) is included in the repository for evaluation purposes.

The database contains:
- Admin login credentials
- Sample projects
- Sample clients
- Contact form submissions
- Newsletter subscriber records

Including the database allows evaluators to test all features immediately without 
additional setup.


Evaluation Criteria Coverage
----------------------------

- Functionality: All required features are implemented and working correctly.
- Code Quality: Code is clean, structured, and readable.
- Design: Layout and user flow align with the reference design.
- Security: Admin authentication is implemented with restricted access.
- Deployment: Application is deployed and publicly accessible.


Conclusion
----------

This project demonstrates practical full stack development skills including backend logic, 
database handling, authentication, user interface design, and deployment. 
The application is structured, secure, and ready for evaluation.


Author
------

Pransu Singh
Full Stack Developer
