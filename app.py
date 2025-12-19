import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from PIL import Image
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db = SQLAlchemy(app)

# Models
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(100), nullable=False)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    designation = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(100), nullable=False)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    mobile = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(100), nullable=False)

class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Helper function for image cropping
def save_and_crop_image(form_picture, target_size=None):
    random_hex = os.urandom(8).hex()
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.config['UPLOAD_FOLDER'], picture_fn)

    i = Image.open(form_picture)
    
    if target_size:
        i = i.resize(target_size) 
    
    i.save(picture_path)
    return picture_fn

# Login Decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_logged_in' not in session:
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

# Routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/projects')
def get_projects():
    projects = Project.query.all()
    project_list = []
    for p in projects:
        project_list.append({
            'name': p.name,
            'description': p.description,
            'image': url_for('static', filename='uploads/' + p.image_file)
        })
    return jsonify(project_list)

@app.route('/api/clients')
def get_clients():
    clients = Client.query.all()
    client_list = []
    for c in clients:
        client_list.append({
            'name': c.name,
            'designation': c.designation,
            'description': c.description,
            'image': url_for('static', filename='uploads/' + c.image_file)
        })
    return jsonify(client_list)

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    data = request.form
    new_contact = Contact(
        full_name=data['full_name'],
        email=data['email'],
        mobile=data['mobile'],
        city=data['city']
    )
    db.session.add(new_contact)
    db.session.commit()
    return jsonify({'message': 'Contact submitted successfully!'})

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    if email:
        existing = Subscriber.query.filter_by(email=email).first()
        if not existing:
            new_sub = Subscriber(email=email)
            db.session.add(new_sub)
            db.session.commit()
            return jsonify({'message': 'Subscribed successfully!'})
        return jsonify({'message': 'Already subscribed!'})
    return jsonify({'message': 'Invalid email'})

# Admin Routes

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin123':
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid Credentials', 'danger')
    return render_template('login.html')

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

@app.route('/admin')
@login_required
def admin_dashboard():
    projects = Project.query.all()
    clients = Client.query.all()
    contacts = Contact.query.all()
    subscribers = Subscriber.query.all()
    return render_template('admin.html', projects=projects, clients=clients, contacts=contacts, subscribers=subscribers)

@app.route('/admin/add_project', methods=['POST'])
@login_required
def add_project():
    name = request.form['name']
    description = request.form['description']
    image = request.files['image']
    
    if image:
        image_fn = save_and_crop_image(image, target_size=(450, 350))
        new_project = Project(name=name, description=description, image_file=image_fn)
        db.session.add(new_project)
        db.session.commit()
        
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/add_client', methods=['POST'])
@login_required
def add_client():
    name = request.form['name']
    designation = request.form['designation']
    description = request.form['description']
    image = request.files['image']
    
    if image:
        image_fn = save_and_crop_image(image, target_size=(200, 200))
        new_client = Client(name=name, designation=designation, description=description, image_file=image_fn)
        db.session.add(new_client)
        db.session.commit()
        
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/delete_project/<int:id>')
@login_required
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/delete_client/<int:id>')
@login_required
def delete_client(id):
    client = Client.query.get_or_404(id)
    db.session.delete(client)
    db.session.commit()
    return redirect(url_for('admin_dashboard'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
