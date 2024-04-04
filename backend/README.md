## Installation

To run the application locally, follow these steps:

1. **Install Python 3.11**: Make sure you have Python 3.11 installed on your system. You can download and install Python from the [official Python website](https://www.python.org/downloads/).

2. **Install Pipenv**: If you haven't already, install Pipenv by running the following command in your terminal or command prompt:

    ```
    pip install pipenv
    ```

    Pipenv is a tool that helps manage Python dependencies and virtual environments.

3. **Install Dependencies**: Navigate to the project directory in your terminal or command prompt and install dependencies with the following command:

    ```
    pipenv install
    ```

    This command will read the `Pipfile` in your project directory and install all the required Python packages specified there.

4. **Activate Virtual Environment**: Activate the virtual environment created by Pipenv with the following command:

    ```
    pipenv shell
    ```

    Activating the virtual environment ensures that you are working within an isolated Python environment where project dependencies are installed.

5. **Perform Database Migrations**: Run database migrations to set up the database schema according to the application models. First, create migration files with the following command:

    ```
    python manage.py makemigrations
    ```

    Then, apply the migrations to the database with the following command:

    ```
    python manage.py migrate
    ```

6. **Create Superuser**: Create a superuser account to access the Django admin panel and perform administrative tasks. Run the following command and follow the prompts to set up the superuser account:

    ```
    python manage.py createsuperuser
    ```

    This command will ask you to provide a username, email (optional), and password for the superuser.

7. **Run the Server**: Start the Django development server by running the following command:

    ```
    python manage.py runserver
    ```

    This command will start the development server locally, allowing you to access the API endpoints and interact with the application.
