from application import application
from flask import render_template, request

@app.route("/tasks/new/")
def tasks_farm():
    return render_template("tasks/new.html")

@app.route("/tasks/", methods=["POST"])
def tasks_create():
    print(request.form.get("name"))

    return "hello world!"
