from flask import Flask, url_for, redirect, render_template, request, abort
import psycopg2

app = Flask(__name__)

# Dummy user
users = {"Bob":"1234", "Alice":"4321"}
conn = psycopg2.connect(
    host="localhost",
    database="finance_app",
    user="postgres",
    password="sie_final_project")

@app.route("/")
def default():
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

class Expense:
    def __init__(self, date, price, name):
        self.date = date
        self.price = price
        self.name = name

@app.route("/profile/<username>")
def homepage(username):
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM expenses_user WHERE username = \'" + username + "\'")
    result = cur.fetchall()

    expense = None
    expenses = []
    
    for x in result:
        expense = Expense(x[3], x[1], x[0])
        expenses.append(expense)
    
    highlightExpense = None
    highPrice = 0
    for expense in expenses:
        price = expense.price
        if price > highPrice:
            highPrice = price
            highlightExpense = expense

    return render_template("homepage.html", username = username, expenses = expenses, highlightExpense = highlightExpense)

if __name__ == "__main__":
    app.run(debug=True)
