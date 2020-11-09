# This is the main file for the file-developers website.
# You can read more about it at https://github.com/file-developers/web
# cc - file developers [2020]
# Under the MIT license.
from flask import Flask, render_template, url_for, redirect

# create the app instance
app = Flask(__name__)

@app.route('/')
def index():
    """
    This is the main route for the app, it renders the index.html template
    and then returns it to the browser.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000) # IMPORTANT: Set debug=False in production
