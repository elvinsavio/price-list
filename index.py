from flask import Flask, request, redirect
from utils import clean_string
from route import landing_page, search_page

app = Flask(__name__)


@app.route("/")
def _landing_page():
    """
    Route for landing page
    route: /
    """
    return landing_page()


@app.route("/search", methods=["POST", "GET"])
def search_result():
    if request.method == "POST":
        _clean_string = clean_string(request.form.get("search", "none"))
        if _clean_string == "":
            return redirect("/")
        return redirect(f"/search?s={_clean_string}")

    search_param = request.args.get("s", "")
    return search_page(search_param)


if __name__ in "__main__":
    app.run(debug=True)
