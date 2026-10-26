from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Chennai", "Kolkata"],
        "answer": 1
    },
    {
        "question": "Which language is used with Flask?",
        "options": ["Python", "Java", "C++", "HTML"],
        "answer": 0
    },
    {
        "question": "Which HTML tag creates a link?",
        "options": ["<p>", "<h1>", "<a>", "<br>"],
        "answer": 2
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Utility",
            "Control Processing User"
        ],
        "answer": 0
    },
    {
        "question": "Which symbol starts a Python comment?",
        "options": ["//", "#", "/*", "&"],
        "answer": 1
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return """
    <h1>About Simple Quiz</h1>
    <p>This is a beginner Flask quiz project.</p>
    <a href="/">Home</a>
    """


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "GET":
        return redirect(url_for("home"))

    name = request.form.get("name", "").strip()

    if not name:
        return render_template(
            "index.html",
            error="Please enter your name."
        )

    return render_template(
        "quiz.html",
        name=name,
        questions=questions
    )


@app.route("/result", methods=["POST"])
def result():
    name = request.form.get("name", "").strip()

    if not name:
        return render_template(
            "index.html",
            error="Please enter your name."
        )

    answers = []

    for i in range(len(questions)):
        selected = request.form.get(f"q{i}")

        if selected not in ("0", "1", "2", "3"):
            return render_template(
                "quiz.html",
                name=name,
                questions=questions,
                error="Please answer every question."
            )

        answers.append(int(selected))

    score = sum(
        answers[i] == questions[i]["answer"]
        for i in range(len(questions))
    )

    return render_template(
        "result.html",
        name=name,
        score=score,
        total=len(questions)
    )


if __name__ == "__main__":
    app.run(debug=True)