# Personal Blog Website
This is a blog type personal website written in Python Flask. You can use it is as a reference or a starting point for your website if you will. All you need to do is to clone it and change the environment variables. All explained below.

Website is live: https://lukaskotatko.com

## Implementation

This site is a static web page that implements common blog-type functionality as adding/editing/deleting posts or projects and sending emails via forms. It can be extended in any way since Flask is a very modular framework.

## Instalation

Installation via requirements.txt:
```
git clone https://https://github.com/ExperimentalHypothesis/flask-personal-blog
cd flask-personal-blog
python -m venv myenv
source myenv/bin/activate (on Windows myenv\Scripts\activate.bat)
pip install -r requirements.txt
```

In order to run it, you need to create an file where you store your environment variables. You should call it simply .env and put it in the root of your project. This is the file that is references in config.py. In that file, you need to store your environment variables. Your .env file need to contain at least the basic variables and should look something like this:

```
ENV = development
SECRET_KEY = whatever

SQLALCHEMY_DATABASE_URI = sqlite:///blog.db

ADMIN_EMAIL = <your@email.com>

MAIL_SERVER = <your mail server> 
MAIL_USERNAME = <your@email.com>
MAIL_PASSWORD = <yourpassword>
```

You can store other environment vars there as well, but these are sufficient in order to run it. Store this .env file in the root of the project.

## Run 
run command:
```
python wsgi.py
```
