from flask import Flask, render_template, request, redirect

from user import User

app = Flask(__name__)
@app.route("/")
def index():
    return redirect('/users')

@app.route("/users")
def users():
    users = User.get_all()
    return render_template("read.html", users=users)


@app.route("/user/new")
def new():
    return render_template("create.html")

@app.route('/user/create', methods=["POST"])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/users')



if __name__ == "__main__":
    app.run(debug=True)
