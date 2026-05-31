# How to create a Django project?

## Step 1
Create a folder for the project

## Step 2
Open in VS Code and open a terminal

## Step 3
Create a virtual environment for the project

Mac OS: python3 -m venv venv
Windows: python -m venv venv

## Step 4
Activate the virtual environment

Mac OS: source venv/bin/activate
Windows: .\venv\Scripts\activate

## Step 5
Install Django dependency

Mac OS: pip3 install django
Windows: pip install django

## Step 6
Run the startproject command to create the project settings

Both OS: django-admin startproject NAME_OF_PROJECT
Note: replace NAME_OF_PROJECT with config or any other name

Expected Output: two folders and a single file called **manage.py**

Alright — here’s the **whole thing from Step 7 and below, clean and exact** 👇

---

## Step 7

Running the django project

Mac OS: python3 manage.py runserver
Windows: python manage.py runserver

---

## Step 8

Creating django apps

Both OS: python manage.py startapp NAME_OF_THE_APP

---

## Models in Django

When we finish a model structure we need to run these commands in order:

1. python manage.py makemigrations
2. python manage.py migrate
