from flask import render_template
from sheets import sheet


def search_page(params):
    """
    Construct the landing page and returns the view
    """
    data = sheet.search_title(params)
    print(data)
    return render_template(
        "search.html",
        search=params,
        data=data["data"],
        last_updated=data["last_updated"],
    )
