
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
@app.route('/36636186')
def dog_366():
    return render_template('dog_36636186.html')
@app.route('/42904054')
def dog_429():
    return render_template('dog_42904054.html')
@app.route('/43078721')
def dog_430():
    return render_template('dog_43078721.html')
@app.route('/45447002')
def dog_454():
    return render_template('dog_45447002.html')
@app.route('/48818187')
def dog_488():
    return render_template('dog_48818187.html')
# # 5 ids for cat page 
@app.route('/51289678')
def cat_512():
    return render_template('cat_51289678.html')
@app.route('/52058185')
def cat_520():
    return render_template('cat_52058185.html')
@app.route('/52072231')
def cat_5207():
    return render_template('cat_52072231.html')
@app.route('/52106194')
def cat_521():
    return render_template('cat_52106194.html')
@app.route('/52167059')
def cat_5216():
    return render_template('cat_52167059.html')
###############################################################################
# main driver function
