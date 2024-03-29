from flask import render_template
from sheets import sheet

def landing_page():
    '''
        Construct the landing page and returns the view
    '''
    data_list = sheet.get_titles()
    return render_template('landing.html', data=data_list['data'], last_updated=data_list['last_updated'])
