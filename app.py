from flask import Flask
from uuid import UUID

app = Flask(__name__)

# Static Routing
@app.route("/")
def home():
    return "Welcome to our Home Page"

# URL Converters

# int converter
@app.route("/user/<int:id>")
def user_id(id):
    return f"User ID: {id}"

# float converter
@app.route("/price/<float:amount>")
def price(amount):
    return f"Price: {amount}"

# string converter
@app.route("/user/<string:name>")
def user_name(name):
    return f"User Name: {name}"

# path converter
@app.route("/files/<path:file_path>")
def files(file_path):
    return file_path

# UUID converter (use for large unique id)
@app.route("/student/<uuid:user_id>")
def student(user_id):
    return str(user_id)


if __name__ == '__main__':
    app.run(debug=True)