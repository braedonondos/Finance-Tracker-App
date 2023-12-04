from flask import Flask, url_for, redirect, render_template, request, abort
import psycopg2

app = Flask(__name__)

# Temporary users database, database implementation needed
users = {"username":"password"}

@app.route("/")
def default():
    conn = psycopg2.connect("postgresql://postgres:sie_final_project@localhost:5432/postgres")
    
    # Creating a table example with some dummy data
    cur = conn.cursor()
    cur.execute("CREATE TABLE users (username VARCHAR(255), password VARCHAR(255))")
    cur.execute("INSERT INTO users (username, password) VALUES (\'user1234\', \'temp_pass\')")
    
    # Put all the data in the users table into the cursor
    cur.execute("SELECT * FROM users")
    result = cur.fetchall()

    #Print all table data
    for x in result:
        print(x)
    
    #Delete all table data
    cur.execute("DROP TABLE users")
    

    print("Connection to db successful...")
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