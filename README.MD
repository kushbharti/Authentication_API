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

authapi/
│
├── account/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── renderers.py
│ ├── utils/
│ │ ├── email.py
│ │ └── tokens.py
│ └── urls.py
│
├── authapi/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
└── manage.py

</pre>

<h2>API Endpoints</h2>
<table>
        <thead>
            <tr>
                <th>Method</th>
                <th>Endpoint</th>
                <th>Description</th>
                <th>Authentication Required</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>POST</td>
                <td>/api/register/</td>
                <td>User Registration</td>
                <td>No</td>
            </tr>
            <tr>
                <td>POST</td>
                <td>/api/login/</td>
                <td>User Login</td>
                <td>No</td>
            </tr>
            <tr>
                <td>GET</td>
                <td>/api/profile/</td>
                <td>Get User Profile</td>
                <td>Yes</td>
            </tr>
            <tr>
                <td>POST</td>
                <td>/api/change-password/</td>
                <td>Change Password</td>
                <td>Yes</td>
            </tr>
            <tr>
                <td>POST</td>
                <td>/api/send-reset-password-email/</td>
                <td>Request Password Reset Email</td>
                <td>No</td>
            </tr>
            <tr>
                <td>POST</td>
                <td>/api/reset-password/&lt;uid&gt;/&lt;token&gt;/</td>
                <td>Reset Password using token</td>
                <td>No</td>
            </tr>
        </tbody>
    </table>

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
        <li>Other standard Python libraries (email, utils)</li>
    </ul>
