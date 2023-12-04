from flask import Flask, url_for, redirect, render_template, request, abort

app = Flask(__name__)

# Temporary users database, database implementation needed
users = {"username":"password"}

@app.route("/")
def default():
    print("Redirecting to login page...")
    return redirect(url_for("login"))

@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        print("Login route: GET request: displaying the login page...")
        return render_template("login.html")
    elif request.method == "POST":
        if request.form["username"] in users:
            if users[request.form["username"]] == request.form["password"]:
                return redirect(url_for("homepage", username=request.form["username"]))
            else:
                abort(401)
        else:
            abort(404)

@app.route("/profile/<username>")
def homepage(username):
    return render_template("homepage.html", username = username)

if __name__ == "__main__":
    app.run(debug=True)