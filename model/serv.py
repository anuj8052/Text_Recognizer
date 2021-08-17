from flask import Flask, render_template
from flask.wrappers import Request

import model


app = Flask(__name__)



@app.route("/")
def hello():
    if Request.method == "POST":
        file = Request.form['file']
        text_pred = model.ocr_model("images")

        print(text_pred)





    return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True)