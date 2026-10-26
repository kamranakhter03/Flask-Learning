from flask import Flask, render_template

app = Flask(__name__)

# Pass single & multiple Variable
@app.route("/")
def home():
    first_name="Kamran"
    last_name="Akhter"
    course_name="Data Science"
    city_name = "Delhi"
    skills = ["Python", "SQL", "Flask", "ML", "DL"]
    student_age = 23
    course_fee = 500
    return render_template("index.html", 
                        f_name=first_name,
                        l_name=last_name,
                        course=course_name,
                        city=city_name,
                        age=student_age,
                        fee=course_fee,
                        skills_set=skills)

if __name__ == "__main__":
    app.run(debug=True)