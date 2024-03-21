import requests

# Define the base URL of your Flask application
BASE_URL = 'http://127.0.0.1:5000/#hire'

# Function to register a new user
def register_user(username, email, password):
    url = f'{BASE_URL}/register'
    data = {
        'username': username,
        'email': email,
        'password': password
    }
    response = requests.post(url, json=data)
    return response

# Function to login with user credentials
def login_user(username, password):
    url = f'{BASE_URL}/login'
    data = {
        'username': username,
        'password': password
    }
    response = requests.post(url, json=data)
    return response

# Test user registration
def test_registration():
    # Replace with your test user details
    username = 'test_user'
    email = 'test@example.com'
    password = 'test_password'

    response = register_user(username, email, password)
    print(f'Registration Response: {response.json()}')
    assert response.status_code == 201, 'User registration failed'

# Test user login
def test_login():
    # Replace with your test user credentials
    username = 'test_user'
    password = 'test_password'

    response = login_user(username, password)
    print(f'Login Response: {response.json()}')
    assert response.status_code == 200, 'User login failed'

if __name__ == '__main__':
    # Run the test functions
    test_registration()
    test_login()
