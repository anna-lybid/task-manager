# Task-manager Project

Django project for task management in IT company.

## Check it out!

[Deployed to Render](https://task-manager-for-an-it-company.onrender.com/)

```
login: test_user
password: qawsed
```

## Installation

Python3 must be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```bash
git clone https://github.com/anna-lybid/task-manager.git
cd task-manager
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

## Features and usage

* Authentication functionality for Manager/User
* Manager can create/edit/delete tasks
* Operate with information about employees
* Sort and filter tasks by status, date, priority
* Search for information in a specific list by name or some other parameters


## Db Structure

![img_4.png](img_4.png)

## Demo 

![img.png](img.png)