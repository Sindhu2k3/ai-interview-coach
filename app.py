from flask import Flask, render_template, request, session, redirect
from utils.engine import generate_questions, evaluate_full

app = Flask(__name__)
app.secret_key = "interview_secret"


@app.route("/", methods=["GET","POST"])
def index():

    if request.method == "POST":

        role = request.form["role"]
        level = request.form["level"]

        session["role"] = role
        session["level"] = level

        qs = generate_questions(role, level)

        session["questions"] = qs
        session["answers"] = []
        session["step"] = 0

        return redirect("/interview")

    return render_template("index.html")


@app.route("/interview", methods=["GET","POST"])
def interview():

    step = session.get("step", 0)
    questions = session.get("questions")

    if request.method == "POST":

        ans = request.form["answer"]
        session["answers"].append(ans)

        session["step"] += 1
        step += 1

        if step >= 3:
            return redirect("/result")

    return render_template(
        "interview.html",
        question=questions[step],
        number=step+1
    )


@app.route("/result")
def result():

    role = session["role"]
    questions = session["questions"]
    answers = session["answers"]

    feedback = evaluate_full(
    questions,
    answers,
    session["role"],
    session["level"]
)


    return render_template("result.html", result=feedback)


if __name__ == "__main__":
    app.run(debug=True)
