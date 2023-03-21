
import prefix

from flask import Flask, url_for, make_response, render_template
from markupsafe import escape

# create app to use in this Flask application
app = Flask(__name__)


prefix.use_PrefixMiddleware(app)   

# test route to show prefix settings
@app.route('/prefix_url')  
#homepage
@app.route('/')
#about us
@app.route('/aboutus')
#adoption form
@app.route('/adoptionform')
#cat page
@app.route('/cats')
#dog page
@app.route('/dogs')
# 5 ids for dogs page 
@app.route('/36636186')
@app.route('/42904054')
@app.route('/43078721')
@app.route('/45447002')
@app.route('/48818187')
# 5 ids for cat page 
@app.route('/51289678')
@app.route('/52058185')
@app.route('/52072231')
@app.route('/52106194')
@app.route('/52167059')

###############################################################################
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)