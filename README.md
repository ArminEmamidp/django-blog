This is a blog created with Python3 and Django

Project implementation steps:

1: Go to the project path in the terminal

2: Write the following commands in the terminal:

    pip install -r requirements.txt
  
    python manage.py migrate
  
    python manage.py runserver

3: Open the browser and go to this address:

    localhost:8000

To create content on blog, you need to use the admin panel:

Open the browser and write the following commands:

    localhost:8000/admin
    
    Username: admin
    
    password: a

To create superuser for manage the admin panel, you can write the under commands in the project path:
    python manage.py createsuperuser

    Write the user info in later steps

