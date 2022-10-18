
## **Step 1: Download and install python**

  

Navigate to <https://www.python.org/downloads/> and download any version of python.

Check add python to path when installing.

  

## **Step 2: Git clone clone the repository**

  

Do a `git clone https://github.com/skynette/paystack-django-integration.git`

and then navigate into the folder created

  

## **Step 3: Install project dependencies**

  

in requirements file using: `pip install -r requirements.txt`

  

## **Step 4: Make and Run Migrations**

  

makemigrations wih `python manage.py makemigrations`

then migrate with `python manage.py migrate`

  

## **Step 5: Create a superuser**

  

to create a superuser run `python manage.py createsuperuser`

follow the instructions to complete the process

  

## **Step 6: Run the project in local server**

  

run `python manage.py runserver`

this will start a local server with the project on `port 8000`

now you can navigate to `127.0.0.1:8000` to view the application
