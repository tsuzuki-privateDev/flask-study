from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

favorite_list = ["野球", "競馬", "釣り", "お笑い"]


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        favorite_list.append(request.form["favorite_add"])
        return redirect(url_for("index"))

    return render_template("index.html", favorite_list=favorite_list)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
