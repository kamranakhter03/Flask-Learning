from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    courses = [
        "Python",
        "Flask",
        "React",
        "Django",
        "Data Science",
        "Data Analyst"
    ]
    student = {
        "name" : "Kamran",
        "course" : "Flask",
        "city" : "Delhi"
    }
    return render_template("index.html", course=courses, student=student)

if __name__ == "__main__":
    app.run(debug=True)