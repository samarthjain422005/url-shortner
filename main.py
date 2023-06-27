from flask import Flask, render_template, request, flash, redirect, abort
from inputform import InputForm , SearchForm
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = "sammyboy/url-shortner"

shortened_urls = []

@app.route("/", methods=["GET", "POST"])
def home():
    form = InputForm()
    if request.method == "POST":
        if form.validate_on_submit():
            id = form.pseudoname_input.data.index(form.pseudoname_input.data)
            shortened_url = request.base_url + id
            shortened_urls.append({"destination_url": form.url.data , "id": id})
            flash(f"Shortened URL: {shortened_url}", "success message")
            form.url.data=''
        else:
            flash("Invalid URL!", "error message")
    return render_template("index.html", form=form)

@app.route("/<id>")
def shortened(id):
    for shortened_url in shortened_urls:
        if shortened_url["id"] == id:
            return redirect(shortened_url["destination_url"])
    return abort(404)

@app.route("/search")
def search():
    form=SearchForm()
    if request.method == "POST":
        if form.validate_on_submit():
            for i in shortened_urls:
                if form.pseudoname_input.data.index(form.pseudoname_input.data) in i[id]:
                    j=i[destination_url]
                    flash("URL: "+ j, "success message")
        else:
            flash("URL not found !", "error message")

    return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=True)