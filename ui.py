from flask import Flask, render_template
import jellybean
app = Flask(__name__)

test = {"richmond":["10", "20"], "irvine":["90"]}
@app.route("/")
def hello():
    return render_template('display.html', trains=jellybean.bart_info())

if __name__ == "__main__":
    app.run()
