
import prefix

from flask import Flask, url_for, make_response, render_template
from markupsafe import escape

# create app to use in this Flask application
app = Flask(__name__)


prefix.use_PrefixMiddleware(app)   

# test route to show prefix settings
@app.route('/prefix_url')  
def prefix_url():
    return 'The URL for this page is {}'.format(url_for('prefix_url'))
#homepage
@app.route('/')
def homepage():
    return render_template('Homepage.html')
#about us
@app.route('/aboutus')
def aboutus():
    return render_template('AboutUs.html')
#adoption form
@app.route('/adoptionform')
def adoptionform():
    return render_template('AdoptionForm.html')
#cat page
@app.route('/cats')
def catpage():
    return render_template('CatPage.html')
#dog page
@app.route('/dogs')
def dogpage():
    return render_template('DogPage.html')
# 5 ids for dogs page 
# @app.route('/36636186')
# @app.route('/42904054')
# @app.route('/43078721')
# @app.route('/45447002')
# @app.route('/48818187')
# # 5 ids for cat page 
# @app.route('/51289678')
# @app.route('/52058185')
# @app.route('/52072231')
# @app.route('/52106194')
# @app.route('/52167059')
###############################################################################
# main driver function
