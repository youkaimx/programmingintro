from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def mainpage():
    return render_template("index.html")

@app.route("/list")
def listpage():
    return render_template("list.html")


@app.route("/add")
def addpage():
    return render_template("add.html")

@app.route("/delete")
def deletepage():
    return render_template("delete.html")


@app.route("/demo")
def demofunction():
    return "<h1>Esto seria otra pagina</h1>"
#if __name__ == "__main__":
app.run()