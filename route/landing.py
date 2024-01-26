from flask import render_template
from sheets import sheet

def landing_page():
    '''
        Construct the landing page and returns the view
    '''
    print(sheet.get_titles())
    return render_template('landing.html')
