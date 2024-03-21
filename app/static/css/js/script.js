// Custom JavaScript for TaskMate application

// Add your custom JavaScript functions here
document.addEventListener('DOMContentLoaded', function() {
    // Example: Alert when a button with ID 'myButton' is clicked
    var myButton = document.getElementById('myButton');
    if (myButton) {
        myButton.addEventListener('click', function() {
            alert('Button clicked!');
        });
    }
});

// static/js/script.js - register html element
document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission
    
    // Get form data
    const formData = {
        username: document.getElementById('username').value,
        email: document.getElementById('email').value,
        password: document.getElementById('password').value
    };
    
    // Send registration data to server as JSON
    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Registration failed');
        }
        return response.json();
    })
    .then(data => {
        console.log(data.message); // Log server response
        // Optionally, redirect user or display success message
    })
    .catch(error => {
        console.error('Error:', error.message);
        // Handle registration error (e.g., display error message to user)
    });
});


// static/js/script.js

document.addEventListener('DOMContentLoaded', function() {
    // Function to fetch user tasks from the backend
    function fetchUserTasks() {
        fetch('/tasks', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch tasks');
            }
            return response.json();
        })
        .then(tasks => {
            // Render tasks on the UI
            renderTasks(tasks);
        })
        .catch(error => {
            console.error('Error fetching tasks:', error.message);
        });
    }

    // Function to render tasks on the UI
    function renderTasks(tasks) {
        const tasksList = document.getElementById('tasks-list');

        // Clear previous tasks
        tasksList.innerHTML = '';

        // Append each task to the tasks list
        tasks.forEach(task => {
            const taskItem = document.createElement('li');
            taskItem.textContent = task.title;
            tasksList.appendChild(taskItem);
        });
    }

    // Fetch and render user tasks when the page loads
    fetchUserTasks();
});

