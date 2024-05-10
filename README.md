![](https://badgen.net/badge/Editor.js/v2.0/blue)


# This is a blog created with Python3 and Django

# Instaling
## Go to the project path in the terminal and run the following commands:

```shell
pip install -r requirements.txt

python manage.py makemigrations account blog

python manage.py migrate
  
python manage.py runserver
```
#### 3: Open the browser and go to this address:

    localhost:8000

## To add post or managing the blog, you must create a superuser account and go to the admin panel. for this, you can write the under command in the project path:

```shell
python manage.py createsuperuser
```
