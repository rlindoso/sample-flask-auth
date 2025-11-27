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

## Testing

This project includes comprehensive unit tests for all service layer functionality with a minimum of 80% code coverage.

### Quick Start

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov

# Generate HTML coverage report
pytest --cov --cov-report=html

# Open coverage report
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

### Test Structure

The project uses pytest with the following test organization:

```
src/modules/users/tests/
├── authenticate_user_service_test.py  # Authentication tests
├── create_user_service_test.py        # User creation tests
├── update_user_service_test.py        # User update tests
├── delete_user_service_test.py        # User deletion tests
└── show_user_by_username_service_test.py  # User retrieval tests
```

### Running Specific Tests

```bash
# Run a specific test file
pytest src/modules/users/tests/create_user_service_test.py

# Run a specific test function
pytest src/modules/users/tests/create_user_service_test.py::test_create_user

# Run tests matching a pattern
pytest -k "create"

# Run only smoke tests
pytest -m smoke

# Run only regression tests
pytest -m regression
```

### Test Reports

The project generates multiple types of test reports:

- **HTML Report**: `report.html` (auto-generated after each test run)
- **Coverage Report**: `htmlcov/index.html` (shows line-by-line coverage)
- **Allure Report**: Advanced reporting with trends (requires allure installation)

```bash
# Generate and view Allure report
pytest --alluredir=allure-results
allure serve allure-results
```

### Comprehensive Testing Documentation

For detailed information about testing, including:
- Test coverage and reporting
- Writing new tests
- Test architecture and patterns
- Troubleshooting
- CI/CD integration

**See [TESTING.md](TESTING.md) for complete testing documentation.**

## Testing the API

For testing purposes, tools like Postman can be used to interact with the API endpoints. Ensure to include the necessary authentication headers for protected routes.

## Creating an Admin User

By default, new users are assigned the "user" role. To promote a user to an admin:

1. Access the database directly.
2. Locate the user record.
3. Change the `role` field from `"user"` to `"admin"`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.
