# This is the main file for the file-developers website.
# You can read more about it at https://github.com/file-developers/web
# cc - file developers [2020]
# Under the MIT license.
from flask import Flask, render_template, url_for, redirect
import os
import script.loads
# NOT READY YET
#import script.forms as forms

# create the app instance
app = Flask(__name__)
# get the tokens and credentials of the app and config it.
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# Load all the files needed.
ERROR = script.loads.load_errors()

@app.route('/')
def index():
    """
    This function reads the index.html and returns it to the 
    browser.

    Returns: The index.html template
    """
    return render_template('index.html')

@app.route('/projects')
def projects():
    """
    This function renders the projects.html template and then 
    returns it to the browser.

    Returns: the projects.html template
    """
    return render_template('projects.html', title='Projects')


@app.route('/projects/new')
def new_projects():
    """
    This function renders the new_project.html template and then 
    returns it to the browser.

    Returns: the new_project.html template
    """
    return render_template('new_project.html', title='New)

@app.route('/terms_conditions')
def terms_conditions():
    """
    This function reads the terms-conditions.html template 
    and returns it to the browser.

    Returns: The terms-conditions.html template
    """
    return render_template('terms-conditions.html', title="Terms and Conditions")

@app.route('/privacy_policy')
def privacy_policy():
    """
    This function reads the privacy-policy.html template 
    and returns it to the browser.

    Returns: The privacy-policy.html template
    """
    return render_template('privacy-policy.html', title="Privacy Policy")

@app.route('/e')
def error():
    """
    This function is used as the medium part between the errors
    route and the index route, it redirects to the index.

    Returns: A reddirection to the index page
    """
    return redirect(url_for('index'))

@app.errorhandler(400)
@app.route('/e/400')
def error400(err=None):
    """
    This function handles the HTTP 400 error

    Parameters: 
        err => The error itself

    Returns: The error.html template
    """
    return render_template('error.html', e=ERROR["400"], title="400"), 400

@app.errorhandler(401)
@app.route('/e/401')
def error401(err=None):
    """
    This function handles the HTTP 401 error

    Parameters: 
        err => The error itself

    Returns: The error.html template
    """
    return render_template('error.html', e=ERROR["401"], title="401"), 401

@app.errorhandler(403)
@app.route('/e/403')
def error403(err=None):
    """
    This function handles the HTTP 403 error

    Parameters: 
        err => The error itself

    Returns: The error.html template
    """
    return render_template('error.html', e=ERROR["403"], title="403"), 403

@app.errorhandler(404)
@app.route('/e/404')
def error404(err=None):
    """
    This function handles the HTTP 404 error

    Parameters: 
        err => The error itself

    Returns: The error.html template
    """
    return render_template('error.html', e=ERROR["404"], title="404"), 404

@app.errorhandler(500)
@app.route('/e/500')
def error500(err=None):
    """
    This function handles the HTTP 500 error

    Parameters: 
        err => The error itself

    Returns: The error.html template
    """
    return render_template('error.html', e=ERROR["500"], title="500"), 500
if __name__ == '__main__':
    app.run(debug=True, port=5000) # IMPORTANT: Set debug=False in production
