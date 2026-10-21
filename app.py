from flask import Flask

app = Flask(__name__)

# Static Routing
@app.route("/")
def home():
    return "Welcome to our Home Page"

@app.route("/users")
def users():
    return "Welcome to User page!"

# Dynamic Routing
@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/student/<name>/<course>")
def student(name, course):
    return f"{name} is learning {course}"

if __name__ == '__main__':
    app.run(debug=True)