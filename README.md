# flask-personal-blog
This is a blog type personal website written in python Flask. You can use it is as a reference or a starting point for your own website if you will. All you need to do is to clone it, and change environment variables. All explained bellow.

Website is running here: https://lukaskotatko.com

## Instalation

Installation via requirements.txt:
```
git clone https://https://github.com/ExperimentalHypothesis/flask-personal-blog
cd flask-personal-blog
python -m venv myenv
source myenv/bin/activate (on Windows myenv\Scripts\activate.bat)
pip install -r requirements.txt
```

## Run 
In order to run it, you need to make an file where you store environment variables. You should call it simply .env. This is the file that is references in config.py. In that file, you store SECRET_KEY and SQLALCHEMY_DATABASE_URI. You can store other environment vars, but these two are necessary in order to make it run.

run command:
```
python wsgi.py
```


