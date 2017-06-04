from flask import Flask, render_template
app = Flask(__name__)

test = {"richmond":["10", "20"], "irvine":["90"]}
@app.route("/")
def hello():
    return render_template('display.html', trains=test)

if __name__ == "__main__":
    app.run()
