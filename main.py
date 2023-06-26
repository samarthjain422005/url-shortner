from flask import Flask , render_template
from inputform import InputForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "#sammyboy/url-shortner"

@app.route("/")
def home():
    form=InputForm()
    return render_template("index.html",form=form)

if __name__ == "__main__":
    app.run(debug=True)

