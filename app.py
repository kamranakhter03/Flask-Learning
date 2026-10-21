from flask import Flask

app = Flask(__name__)

# Static Routing

@app.route("/")
def home():
    return "Welcome to our Home Page"

@app.route("/about")
def about():
    return "Welcome to our About page!"

@app.route("/contact")
def contact():
    return "Welcome to our Contact Page"

if __name__ == '__main__':
    app.run(debug=True)
