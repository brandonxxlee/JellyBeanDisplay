from flask import Flask, render_template
import jellybean
app = Flask(__name__)

current_display = None
test = {"richmond":["10", "20"], "irvine":["90"]}
@app.route("/")
def hello():
    try:
        current_display = render_template('display.html', trains=jellybean.bart_info())
    except:
        pass
    return current_display

if __name__ == "__main__":
    app.run()
