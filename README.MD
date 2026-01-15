<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Authentication API README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f4;
            color: #333;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        code, pre {
            background-color: #ecf0f1;
            padding: 5px;
            display: block;
            border-radius: 5px;
            overflow-x: auto;
        }
        a {
            color: #2980b9;
        }
        ul {
            margin: 10px 0 10px 20px;
        }
    </style>
</head>
<body>
    <h1>Authentication API</h1>
    <p>This project is a Django REST Framework-based <strong>Authentication API</strong> providing user registration, login, profile management, password change, and password reset functionalities.</p>

    <h2>Features</h2>
    <ul>
        <li>User Registration with email, name, password, and terms & conditions agreement.</li>
        <li>User Login and JWT Token generation.</li>
        <li>View User Profile (requires authentication).</li>
        <li>Change Password for logged-in users.</li>
        <li>Request Password Reset via Email.</li>
        <li>Reset Password using secure token link.</li>
    </ul>

    <h2>Folder Structure</h2>
    <pre>

authentication_api/
│
├── account/
│ ├── models.py # Custom User model
│ ├── serializers.py # DRF serializers for registration, login, profile, password
│ ├── views.py # API views for auth functionality
│ ├── renderers.py # Custom renderer for consistent response format
│ ├── utils/
│ │ ├── email.py # Email sending utility
│ │ └── tokens.py # Token generation & validation
│ └── urls.py # API route definitions
│
├── authentication_api/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
└── manage.py

</pre>

    <h2>API Endpoints</h2>
    <ul>
        <li><strong>POST /api/register/</strong> - User Registration</li>
        <li><strong>POST /api/login/</strong> - User Login</li>
        <li><strong>GET /api/profile/</strong> - Get User Profile (Authentication required)</li>
        <li><strong>POST /api/change-password/</strong> - Change Password (Authentication required)</li>
        <li><strong>POST /api/send-reset-password-email/</strong> - Request Password Reset Email</li>
        <li><strong>POST /api/reset-password/&lt;uid&gt;/&lt;token&gt;/</strong> - Reset Password using token</li>
    </ul>

    <h2>Installation & Setup</h2>
    <ol>
        <li>Clone the repository: <code>git clone &lt;repo_url&gt;</code></li>
        <li>Create a virtual environment: <code>python -m venv venv</code></li>
        <li>Activate the environment:
            <ul>
                <li>Windows: <code>venv\Scripts\activate</code></li>
                <li>Linux/Mac: <code>source venv/bin/activate</code></li>
            </ul>
        </li>
        <li>Install dependencies: <code>pip install -r requirements.txt</code></li>
        <li>Apply migrations: <code>python manage.py migrate</code></li>
        <li>Run server: <code>python manage.py runserver</code></li>
    </ol>

    <h2>Usage</h2>
    <p>Use tools like <a href="https://www.postman.com/" target="_blank">Postman</a> or <code>curl</code> to test API endpoints. Include the JWT token in the Authorization header for protected routes:</p>
    <pre>

Authorization: Bearer &lt;your_token&gt;

</pre>

    <h2>Dependencies</h2>
    <ul>
        <li>Django</li>
        <li>Django REST Framework</li>
        <li>PyJWT (for JWT token handling)</li>
        <li>Other standard Python libraries (email, utils)</li>
    </ul>

    <h2>Author</h2>
    <p>Kush Bharti</p>

    <h2>License</h2>
    <p>This project is open-source and free to use under the MIT License.</p>

</body>
</html>
