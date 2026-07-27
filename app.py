from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "cmms_secret_key"


# Sample User Database
users = {
    "admin": "12345",
    "engineer": "abcd"
}


# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:

            session["user"] = username

            return redirect("/")

        else:
            return render_template(
                "login.html",
                error="Invalid Username or Password"
            )


    return render_template("login.html")



# Dashboard
@app.route("/")
def dashboard():

    if "user" not in session:
        return redirect("/login")


    return render_template(
        "dashboard.html",
        user=session["user"]
    )



# Logout
@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect("/login")



# Work Order Page
@app.route("/workorders")
def workorders():

    return "Work Order Page"



# Create Work Order
@app.route("/create")
def create():

    return "Create Work Order"



if __name__ == "__main__":
    app.run(debug=True)