# Secure-Password-Manager

Cyber Security University Semester Project. Fully secure password manager application that stores encrypted credentials in a database and provides an interface for users to access their password safely.

Author: Mykhailo Feniuk

The web app and components in it like register, login, logout, add/edit/delete data are made by using Flask framework.
The security of user's password is safe by hash functionality, bcrypt and cryptography frameworks.

Features:

- User Registration
- User Authentication (Login / Logout)
- Secure Password Hashing with bcrypt
- Encrypted Credential Storage
- Password Generation
- Credential Retrieval
- Edit Stored Credentials
- Delete Stored Credentials
- Password Strength Validation
- SQLite Database Integration
- Flask Web Interface
- CSRF Protection
- Protection against SQL Injection
- Basic XSS Mitigation through Jinja2 escaping

<!-- ------------------------------------------------------ -->
<!-- ------------------------------------------------------ -->
<!-- ------------------------------------------------------ -->
<!-- ------------------------------------------------------ -->

Technologies used:

- Python
- Flask
- Flask-Login
- Flask-WTF
- Flask
- Flask-SQLAlchemy
- SQLite
- bcrypt
- cryptography (Fernet)

<!-- ------------------------------------------------------ -->
<!-- ------------------------------------------------------ -->
<!-- ------------------------------------------------------ -->
<!-- ------------------------------------------------------ -->

How to start the project:
At first install all dependencies from requirements.txt file:

- pip install -r requirements.txt

Start the app:

1. run - python create_db.py
2. run - python initialize.py
3. open - http://127.0.0.1:5000

<!-- ------------------------------------------------------ -->
<!-- ------------------------------------------------------ -->
<!-- ------------------------------------------------------ -->
<!-- ------------------------------------------------------ -->

Security Mechanisms:

1. Password Hashing:
   User account passwords are hashed using bcrypt with automatic salting. Plaintext passwords are never stored in the database.

2. Credential Encryption:
   Stored website usernames and passwords are encrypted using Fernet symmetric encryption before being written to the database.

3. SQL Injection Protection:
   SQLAlchemy ORM is used instead of raw SQL queries.

4. CSRF Protection:
   All forms are protected using Flask-WTF CSRF tokens.

5. XSS Protection:
   Jinja2 automatic output escaping is used to prevent script injection attacks.
