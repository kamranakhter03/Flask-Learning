from flask import Flask, render_template

app = Flask(__name__)

# Pass single & multiple Variable
@app.route("/")
def home():
    name="Kamran Akhter"
    course="Data Science"
    city = "Delhi"
    age = 23
    return render_template("index.html", 
                           name=name,
                           course=course,
                           city=city,
                           age=age)

@app.route("/<student_name>")
def name(student_name):
    return render_template("index.html", name=student_name)

if __name__ == "__main__":
    app.run(debug=True)