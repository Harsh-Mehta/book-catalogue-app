NOTE: This repository is a part of Livi UK's technical test interview for Python Engineer position.

# Introduction
Book Catalogue is a web application that allows users to find or discover books and populate their personal reading list. Users can search for books and authors that they know, or browse for books by author, genre or popularity, etc.

The application allows administrators of the system to manage the site content.

# Technology Stack
- Frontend: HTML, Bootstrap
- Backend: Django
- Database: Sqlite 3

# Set up instructions
1. Clone the repo and create a virtual environment
2. Activate the environment and install the dependencies
3. Navigate inside the *book_catalogue* directory
4. Run all the necessary migrations using the following command:  
    ```python manage.py migrate```
5. Create a super user to be able to access the admin portal using the following command:  
    ```python manage.py createsuperuser```
6. Run the application using the following command:  
    ```python manage.py runserver```

# Usage
1. Login into the admin portal and populate the _Books_ and _Authors_ so as to view data on the public facing website.