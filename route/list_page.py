from flask import render_template
from sheets import sheet
from utils.string import remove_hyphen


def list_page(params):
    """
    Construct the list page and returns the view
    """
    data = sheet.get_list_items(remove_hyphen(params))
    return render_template(
        "list.html",
        search=params,
        data=data['data'],
        last_updated=data['timestamp']
    )
