from flask import Flask, render_template, request, redirect
from utils import clean_string, remove_hyphen

app = Flask(__name__)


@app.route("/")
def landing_page():
    return render_template("landing.html")


@app.route("/search", methods=["POST", "GET"])
def search_result():
    if request.method == "POST":
        _clean_string = clean_string(request.form.get("search", "none"))
        return redirect(f"/search?s={_clean_string}")

    search_param = request.args.get("s", "")
    return render_template("search.html", search=remove_hyphen(search_param))


if __name__ in "__main__":
    app.run(debug=True)
