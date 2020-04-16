""" THIS IS THE ENTRY POINT """
from application import create_app


def main():
    app = create_app()
    app.run(host='localhost', debug=True)


if __name__ == "__main__":
    main()