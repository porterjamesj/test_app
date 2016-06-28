from flask import Flask, request, render_template
# # imaginary:
# from models import User

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/user", methods=["POST"])
def user():
    print request.form["name"]
    print request.form["status"]
    # # also imaginary:
    # new_user = User(name=request.form["name"],
    #                 status=request.form["status"])
    # db.session.add(new_user)
    # db.session.commit()
    return "success"

if __name__ == "__main__":
    app.run(debug=True)
