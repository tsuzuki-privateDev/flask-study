from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    favorite_list = ["野球", "競馬", "釣り", "お笑い"]
    return render_template("index.html", favorite_list=favorite_list)


if __name__ == "__main__":
    app.run(debug=True)
