# Task Management App Documentation

## Introduction
The Task Management App is a web application built with Django, a high-level Python web framework. This app provides functionalities to manage tasks, user registration, user authentication, and leave application management. It allows users to create, update, and track their tasks, while administrators can manage tasks and leave applications.

https://github.com/Anuragsingh2003/Task-Reporter-django/assets/117331687/a0674495-8392-4e76-8458-a0c95efe7dd5



## Features
- **User Registration:** New users can register by providing a username and password. User registration is handled securely and efficiently.
- **User Login:** Registered users can log in using their credentials.
- **User Dashboard:** Once logged in, users are redirected to their personal dashboard. The dashboard displays the user's tasks and basic information.
- **Task Management:**
  - **Create Task:** Users can create new tasks by providing a description, start date, end date, and status.
  - **Update Task:** Users can update the status of their tasks.
  - **Task List:** Users can view a list of their tasks.
  - **Task Details:** Users can view detailed information about a specific task.
- **Leave Management:**
  - **Leave Application:** Users can apply for leave by providing a subject and message. The application is saved with a default "Null" status.
  - **Leave Status:** Users can view the status of their leave applications.

- **Admin Dashboard:** Administrators have access to an admin dashboard with additional functionalities.
- **Admin Task Management:**
  - **Create Task:** Administrators can create new tasks on behalf of users.
  - **Manage Tasks:** Administrators can view and manage all tasks in the system.
  - **Edit Task:** Administrators can edit the details of a specific task.
  - **Delete Task:** Administrators can delete tasks from the system.
- **Admin Leave Management:**
  - **Leave List:** Administrators can view a list of all leave applications.
  - **Accept/Reject Leave:** Administrators can approve or reject leave applications.
  - **View Full Leave Message:** Administrators can view the full message/details of a leave application.

## Installation and Setup
1. Clone the repository from GitHub.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Configure the database settings in the `settings.py` file.
4. Apply database migrations using `python manage.py migrate`.
5. Create a superuser account for administrative access using `python manage.py createsuperuser`.
6. Run the development server with `python manage.py runserver`.

## Usage
1. Access the Task Management App by visiting the provided URL in a web browser.
2. Register a new user account or log in with existing credentials.
3. Users will be redirected to their dashboard, where they can create, update, and view tasks.
4. Administrators can access the admin dashboard by visiting the `/admin` URL and logging in with superuser credentials.
5. Admins can create, manage, and delete tasks, as well as manage leave applications.




## Technology Stack
- Python
- Django
- HTML/CSS
- Bootstrap
- SQLite (default database)
- jQuery/JS

## Folder Structure
- `project_name/`: Django project directory.
  - `app_name/`: Django app directory.
    - `migrations/`: Database migration files.
    - `static/`: Static files (CSS, JS, images).
    - `templates/`: HTML templates.
    - `forms.py`: Django forms for user input validation.
    - `models.py`: Django models representing the database schema.
    - `urls.py`: URL configuration for the app.
    - `views.py`: View functions handling user requests and rendering templates.

## Conclusion

The Task Management App is a powerful and user-friendly application built with Django. It provides a seamless experience for users to manage their tasks and leave applications efficiently. For additional details, please refer to the `readme.txt` file on the GitHub repository.
