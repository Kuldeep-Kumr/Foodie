# Foodie
Welcome to the README for Foodies App!

This repository contains a secure API developed using Django Rest Framework and consumed with Angular. It's designed to provide a robust backend system along with a sleek frontend interface.

## Features

- **User and Owner Authentication**:I have implemented authentication mechanisms using Django Rest Token for both users and owners, ensuring secure access to the system.
- **Data Serialization**: Django's powerful serializers are utilized to efficiently manage data serialization, enabling seamless communication between the frontend and backend.
- **Admin Panel**: The integration of Django's admin panel offers an intuitive interface for administrators to manage various aspects of the application effortlessly.
- **API Versioning**: I've adopted API versioning strategies to effectively manage changes and updates, ensuring backward compatibility and smooth transitions.
- **Optimized Database Queries**: Database queries are optimized for performance, enhancing the overall responsiveness and scalability of the system.
- **Dependency Management**: Pipenv is used for dependency management, facilitating easy installation and maintenance of project dependencies.
- **ViewSets**: ViewSets are employed for better API structure and organization, streamlining the development process and improving code readability.

## Installation

To run the application locally, follow these steps:

1. **Install Python 3.11**: Make sure you have Python 3.11 installed on your system.
2. **Install Pipenv**: If you haven't already, install Pipenv by running `pip install pipenv`.
3. **Install Dependencies**: Navigate to the project directory and install dependencies with `pipenv install`.
4. **Activate Virtual Environment**: Activate the virtual environment with `pipenv shell`.
5. **Perform Database Migrations**: Run database migrations with `python manage.py makemigrations` followed by `python manage.py migrate`.
6. **Run the Server**: Start the Django server by running `python manage.py runserver`.

For the frontend part, follow these additional steps:

7. **Serve the Frontend**: Navigate to the frontend directory and run `ng serve` to start the Angular development server.

## Development

For development purposes, ensure you have Angular CLI installed. You can install it globally using npm:
