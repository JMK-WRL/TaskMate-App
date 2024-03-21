from flask import jsonify, request, session, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from app.models.user import User
from app.models.tasks import Task



# Home page
@app.route('/')
def home():
    return render_template('home.html')

# User registration endpoint
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.json
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Check if username or email already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'message': 'Username or email already exists'}), 400

        # Hash the password before storing
        hashed_password = generate_password_hash(password)

        # Insert the new user into the database
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 201
    else:
        return render_template('register.html')

# User login endpoint
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Find the user in the database
        user = User.query.filter_by(username=username).first()

        # Check if user exists and verify password
        if user and check_password_hash(user.password, password):
            # Store user session
            session['username'] = username
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'message': 'Invalid username or password'}), 401
    else:
        return render_template('login.html')

# User logout endpoint
@app.route('/logout')
def logout():
    # Clear user session
    session.pop('username', None)
    return jsonify({'message': 'Logout successful'}), 200

# Task creation endpoint
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    title = data.get('title')
    description = data.get('description')

    # Insert the new task into the database
    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()

    return jsonify({'message': 'Task created successfully'}), 201

# Task retrieval endpoint
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.serialize() for task in tasks]), 200

# Task deletion endpoint
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    # Find and delete the task by its ID
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted successfully'}), 200
    else:
        return jsonify({'message': 'Task not found'}), 404

# API endpoint to fetch tasks for the logged-in user
@app.route('/user/tasks', methods=['GET'])
def get_user_tasks():
    # Get the current user ID (assuming it's stored in the session)
    user_id = session.get('user_id')
    
    if user_id:
        # Query SQLAlchemy for tasks associated with the user
        tasks = Task.query.filter_by(user_id=user_id).all()
        
        # Convert tasks to JSON format
        task_list = [{'id': task.id, 'title': task.title, 'description': task.description} for task in tasks]
        
        return jsonify(task_list)
    else:
        return jsonify({'message': 'User not logged in'}), 401
