from flask import render_template
from sheets import sheet

def search_page(params):
    '''
        Construct the landing page and returns the view
    '''
    return render_template('search.html' )
