from flask import Flask, request

app = Flask(__name__)

# Query Parameter

@app.route("/search")
def search():
    name = request.args.get("name")
    return f"Hello {name}"


# Query Parameter with default Value "Guest"
@app.route("/student")
def student():
    name = request.args.get("name", "Guest")
    return f"Hello {name}"


# Multiple Query Parameters
@app.route("/school")
def school():
    school_name = request.args.get("School_Name", "High School")
    course = request.args.get("Course_Name", "Unknown")
    return f"{school_name} is offering {course} course."

if __name__ == '__main__':
    app.run(debug=True)
