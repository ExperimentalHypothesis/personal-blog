""" THIS IS THE ENTRY POINT """
from application import create_app
app = create_app()

if __name__ == "__main__":
    if app.config["ENV"] == "development":
        app.run(host='localhost', debug=True)
    else:
        app.run(host='0.0.0.0')