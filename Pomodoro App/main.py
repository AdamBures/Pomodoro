from flask import Flask, redirect, url_for, render_template, jsonify
import datetime
app = Flask(__name__, template_folder="templates")


class Timer:
    def __init__(self, current_time):
        self.current_time = current_time

    def decrement(self):
        if self.current_time > 0:
            self.current_time = self.current_time - 1
        return self.current_time


@app.route("/_timer", methods=["GET", "POST"])
def timer():
    global t
    new_time = t.decrement()
    return jsonify({"result": str(datetime.timedelta(seconds=new_time))})


@app.route("/")
def home():
    global t
    t = Timer(current_time=25*60)
    return render_template("main.html")


@app.route("/<name>")
def user(name):
    global t
    if name == "five_minutes.html":
        t = Timer(current_time=5*60)
        return render_template(f"{name}")
    elif name == "main.html":
        t = Timer(current_time=25*60)
        return render_template(f"{name}", )


@app.route("/admin")
def admin():
    # Now we when we go to /admin we will redirect to user with the argument "Admin!"
    return redirect(url_for("user", name="Admin!"))


if __name__ == "__main__":
    app.run()
