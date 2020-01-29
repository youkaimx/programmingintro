from flask import Flask

app = Flask(__name__)

@app.route("/")
def mainpage():
    return "Hello Kristoff Gamming!"

#if __name__ == "__main__":
app.run()