from flask import Flask , render_template ,request
from inputform import InputForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "#sammyboy/url-shortner"

shortened_urls=[{"destination_url": "http://google.com ,"id":"1234" }]

@app.route("/",methods=["GET", "POST"])
def home():
    form=InputForm()
    if request.method=="POST":
            if form.validate_on_submit(): 
                 print(form.url_input.data)
            else:
                 print("failed")
    return render_template("index.html",form=form)

if __name__ == "__main__":
    app.run(debug=True)

