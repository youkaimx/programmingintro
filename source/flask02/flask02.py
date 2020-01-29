from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def mainpage():
    return render_template("index.html")

@app.route("/demo")
def demofunction():
    return "<h1>Esto seria otra pagina</h1>"
#if __name__ == "__main__":
app.run()