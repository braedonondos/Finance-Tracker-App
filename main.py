from flask import Flask, url_for, redirect, render_template, request, abort
# import psycopg2

app = Flask(__name__)

# Dummy user
users = {"Bob":"1234"}

@app.route("/")
def default():
    # conn = psycopg2.connect("postgresql://postgres:sie_final_project@localhost:5432/postgres")
    
    # # Creating a table example with some dummy data
    # cur = conn.cursor()
    # cur.execute("CREATE TABLE users (username VARCHAR(255), password VARCHAR(255))")
    # cur.execute("INSERT INTO users (username, password) VALUES (\'user1234\', \'temp_pass\')")
    
    # # Put all the data in the users table into the cursor
    # cur.execute("SELECT * FROM users")
    # result = cur.fetchall()

    # #Print all table data
    # for x in result:
    #     print(x)
    
    # #Delete all table data
    # cur.execute("DROP TABLE users")
    

    # print("Connection to db successful...")
    # print("Redirecting to login page...")
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

    expense1 = Expense("11/23/23", 500, "Groceries")
    expense2 = Expense("11/25/23", 450, "Tech")
    expenses = {expense1, expense2}
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
