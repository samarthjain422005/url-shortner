from flask import Flask , render_template ,request,flash
from inputform import InputForm
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = "#sammyboy/url-shortner"

shortened_urls=[{"destination_url": "http://google.com ,"id":"1234" }]

@app.route("/",methods=["GET", "POST"])
def home():
    form=InputForm()
    if request.method=="POST":
            if form.validate_on_submit(): 
                 destination_url=form.url_input.data
                 id=secrets.token_urlsafe(8)
                 shortened_urls.append({"destination_url":destination_url,"id":id})
                 form.url_input.data=""
                 flash(f"Success!! your shortned url is: {request.base_url+id}",category="success message")
            else:
                 print("failed")
    return render_template("index.html",form=form)

if __name__ == "__main__":
    app.run(debug=True)

