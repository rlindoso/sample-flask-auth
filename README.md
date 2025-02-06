# Sample Flask Authentication

This project is a simple authentication API built with Flask, designed to provide user registration, login, and protected routes for authenticated users. It utilizes `flask_login` to manage user sessions and `bcrypt` for password hashing.

## Features

- **User Registration**: Create new user accounts with encrypted passwords.
- **User Login**: Authenticate users and manage sessions.
- **Protected Routes**: Restrict access to certain routes for authenticated users only.
- **Role Management**: Differentiate between regular users and administrators using a "role" attribute in the database.
- **Password Encryption**: Secure passwords using `bcrypt` hashing.
- **Containerized Database**: Utilize Docker to ensure consistent database environments across different systems.

## Getting Started

### Prerequisites

- Python 3.x
- Docker (for database containerization)

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/rlindoso/sample-flask-auth.git
   cd sample-flask-auth
   ```

2. **Install Dependencies**:

   It's recommended to use a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set Up the Database**:

   The application uses a containerized database setup. Ensure Docker is installed and running on your system.

   ```bash
   docker-compose up -d
   ```

   This command will start the database container in detached mode.

4. **Configure Environment Variables**:

   Copy the example environment file and adjust as needed:

   ```bash
   cp .env.example .env
   ```

   Update `.env` with your specific configuration, such as database connection details.

5. **Initialize the Database**:

   Run the following commands to set up the database schema:

   ```bash
   alembic upgrade head
   ```

6. **Run the Application**:

   Start the Flask development server:

   ```bash
   PYTHONPATH=. python src/shared/infra/http/server.py
   ```

   The application will be accessible at `http://127.0.0.1:5000/`.

## API Endpoints

- **Register User**: `POST /user`
- **Login**: `POST /login`
- **Logout**: `GET /logout`
- **Get User by ID**: `GET /user/<id>` (Requires authentication)
- **Update User by ID**: `PUT /user/<id>` (Requires admin role)
- **Delete User by ID**: `DELETE /user/<id>` (Requires admin role)

**Note**: Endpoints marked with specific requirements need the user to be authenticated and/or have admin privileges.

## Testing the API

For testing purposes, tools like Postman can be used to interact with the API endpoints. Ensure to include the necessary authentication headers for protected routes.

## Creating an Admin User

By default, new users are assigned the "user" role. To promote a user to an admin:

1. Access the database directly.
2. Locate the user record.
3. Change the `role` field from `"user"` to `"admin"`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.
