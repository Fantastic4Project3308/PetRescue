#!/usr/bin/python3
import prefix
from flask import Flask, url_for, make_response, render_template
from markupsafe import escape
import sqlite3

conn = sqlite3.connect('Furever.db', check_same_thread=False)
c= conn.cursor()

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
@app.route('/dog_36636186')
def dog_366():
    c.execute("select name from Dog")
    myresult = c.fetchall()
    name =  myresult[0][0]
    c.execute("select description from Dog")
    myresult2 = c.fetchall()
    description =  myresult2[0][0]
    c.execute("select breed from Dog")
    myresult3 = c.fetchall()
    breed = myresult3[0][0]
    c.execute("select age from Dog")
    myresult4 = c.fetchall()
    age = myresult4[0][0]
    c.execute("select gender from Dog")
    myresult5 = c.fetchall()
    gender = myresult5[0][0]
    c.execute("select color from Dog")
    myresult6 = c.fetchall()
    color = myresult6[0][0]
    c.execute("select size from Dog")
    myresult7 = c.fetchall()
    size = myresult7[0][0]
    c.execute("select location from Dog")
    myresult8 = c.fetchall()
    location = myresult8[0][0]
    
    return render_template('dog_36636186.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/dog_42904054')
def dog_429():
    c.execute("select name from Dog")
    myresult = c.fetchall()
    name =  myresult[1][0]
    c.execute("select description from Dog")
    myresult2 = c.fetchall()
    description =  myresult2[1][0]
    c.execute("select breed from Dog")
    myresult3 = c.fetchall()
    breed = myresult3[1][0]
    c.execute("select age from Dog")
    myresult4 = c.fetchall()
    age = myresult4[1][0]
    c.execute("select gender from Dog")
    myresult5 = c.fetchall()
    gender = myresult5[1][0]
    c.execute("select color from Dog")
    myresult6 = c.fetchall()
    color = myresult6[1][0]
    c.execute("select size from Dog")
    myresult7 = c.fetchall()
    size = myresult7[1][0]
    c.execute("select location from Dog")
    myresult8 = c.fetchall()
    location = myresult8[1][0]
    return render_template('dog_42904054.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/dog_43078721')
def dog_430():
    c.execute("select name from Dog")
    myresult = c.fetchall()
    name =  myresult[2][0]
    c.execute("select description from Dog")
    myresult2 = c.fetchall()
    description =  myresult2[2][0]
    c.execute("select breed from Dog")
    myresult3 = c.fetchall()
    breed = myresult3[2][0]
    c.execute("select age from Dog")
    myresult4 = c.fetchall()
    age = myresult4[2][0]
    c.execute("select gender from Dog")
    myresult5 = c.fetchall()
    gender = myresult5[2][0]
    c.execute("select color from Dog")
    myresult6 = c.fetchall()
    color = myresult6[2][0]
    c.execute("select size from Dog")
    myresult7 = c.fetchall()
    size = myresult7[2][0]
    c.execute("select location from Dog")
    myresult8 = c.fetchall()
    location = myresult8[2][0]
    return render_template('dog_43078721.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/dog_45447002')
def dog_454():
    c.execute("select name from Dog")
    myresult = c.fetchall()
    name =  myresult[3][0]
    c.execute("select description from Dog")
    myresult2 = c.fetchall()
    description =  myresult2[3][0]
    c.execute("select breed from Dog")
    myresult3 = c.fetchall()
    breed = myresult3[3][0]
    c.execute("select age from Dog")
    myresult4 = c.fetchall()
    age = myresult4[3][0]
    c.execute("select gender from Dog")
    myresult5 = c.fetchall()
    gender = myresult5[3][0]
    c.execute("select color from Dog")
    myresult6 = c.fetchall()
    color = myresult6[3][0]
    c.execute("select size from Dog")
    myresult7 = c.fetchall()
    size = myresult7[3][0]
    c.execute("select location from Dog")
    myresult8 = c.fetchall()
    location = myresult8[3][0]
    return render_template('dog_45447002.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/dog_48818187')
def dog_488():
    c.execute("select name from Dog")
    myresult = c.fetchall()
    name =  myresult[4][0]
    c.execute("select description from Dog")
    myresult2 = c.fetchall()
    description =  myresult2[4][0]
    c.execute("select breed from Dog")
    myresult3 = c.fetchall()
    breed = myresult3[4][0]
    c.execute("select age from Dog")
    myresult4 = c.fetchall()
    age = myresult4[4][0]
    c.execute("select gender from Dog")
    myresult5 = c.fetchall()
    gender = myresult5[4][0]
    c.execute("select color from Dog")
    myresult6 = c.fetchall()
    color = myresult6[4][0]
    c.execute("select size from Dog")
    myresult7 = c.fetchall()
    size = myresult7[4][0]
    c.execute("select location from Dog")
    myresult8 = c.fetchall()
    location = myresult8[4][0]
    return render_template('dog_48818187.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
# # 5 ids for cat page 
@app.route('/cat_51289678')
def cat_512():
 
    c.execute("select name from Cat")
    myresult = c.fetchall()
    name =  myresult[0][0]
    c.execute("select description from Cat")
    myresult2 = c.fetchall()
    description =  myresult2[0][0]
    c.execute("select breed from Cat")
    myresult3 = c.fetchall()
    breed = myresult3[0][0]
    c.execute("select age from Cat")
    myresult4 = c.fetchall()
    age = myresult4[0][0]
    c.execute("select gender from Cat")
    myresult5 = c.fetchall()
    gender = myresult5[0][0]
    c.execute("select color from Cat")
    myresult6 = c.fetchall()
    color = myresult6[0][0]
    c.execute("select size from Cat")
    myresult7 = c.fetchall()
    size = myresult7[0][0]
    c.execute("select location from Cat")
    myresult8 = c.fetchall()
    location = myresult8[0][0]
    
    return render_template('cat_51289678.html', name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/cat_52058185')
def cat_520():
    c.execute("select name from Cat")
    myresult = c.fetchall()
    name =  myresult[1][0]
    c.execute("select description from Cat")
    myresult2 = c.fetchall()
    description =  myresult2[1][0]
    c.execute("select breed from Cat")
    myresult3 = c.fetchall()
    breed = myresult3[1][0]
    c.execute("select age from Cat")
    myresult4 = c.fetchall()
    age = myresult4[1][0]
    c.execute("select gender from Cat")
    myresult5 = c.fetchall()
    gender = myresult5[1][0]
    c.execute("select color from Cat")
    myresult6 = c.fetchall()
    color = myresult6[1][0]
    c.execute("select size from Cat")
    myresult7 = c.fetchall()
    size = myresult7[1][0]
    c.execute("select location from Cat")
    myresult8 = c.fetchall()
    location = myresult8[1][0]
    return render_template('cat_52058185.html', name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/cat_52072231')
def cat_5207():
    c.execute("select name from Cat")
    myresult = c.fetchall()
    name =  myresult[2][0]
    c.execute("select description from Cat")
    myresult2 = c.fetchall()
    description =  myresult2[2][0]
    c.execute("select breed from Cat")
    myresult3 = c.fetchall()
    breed = myresult3[2][0]
    c.execute("select age from Cat")
    myresult4 = c.fetchall()
    age = myresult4[2][0]
    c.execute("select gender from Cat")
    myresult5 = c.fetchall()
    gender = myresult5[2][0]
    c.execute("select color from Cat")
    myresult6 = c.fetchall()
    color = myresult6[2][0]
    c.execute("select size from Cat")
    myresult7 = c.fetchall()
    size = myresult7[2][0]
    c.execute("select location from Cat")
    myresult8 = c.fetchall()
    location = myresult8[2][0]
    return render_template('cat_52072231.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/cat_52106194')
def cat_521():
    c.execute("select name from Cat")
    myresult = c.fetchall()
    name =  myresult[3][0]
    c.execute("select description from Cat")
    myresult2 = c.fetchall()
    description =  myresult2[3][0]
    c.execute("select breed from Cat")
    myresult3 = c.fetchall()
    breed = myresult3[3][0]
    c.execute("select age from Cat")
    myresult4 = c.fetchall()
    age = myresult4[3][0]
    c.execute("select gender from Cat")
    myresult5 = c.fetchall()
    gender = myresult5[3][0]
    c.execute("select color from Cat")
    myresult6 = c.fetchall()
    color = myresult6[3][0]
    c.execute("select size from Cat")
    myresult7 = c.fetchall()
    size = myresult7[3][0]
    c.execute("select location from Cat")
    myresult8 = c.fetchall()
    location = myresult8[3][0]
    return render_template('cat_52106194.html',name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
@app.route('/cat_52167059')
def cat_5216():
    c.execute("select name from Cat")
    myresult = c.fetchall()
    name =  myresult[4][0]
    c.execute("select description from Cat")
    myresult2 = c.fetchall()
    description =  myresult2[4][0]
    c.execute("select breed from Cat")
    myresult3 = c.fetchall()
    breed = myresult3[4][0]
    c.execute("select age from Cat")
    myresult4 = c.fetchall()
    age = myresult4[4][0]
    c.execute("select gender from Cat")
    myresult5 = c.fetchall()
    gender = myresult5[4][0]
    c.execute("select color from Cat")
    myresult6 = c.fetchall()
    color = myresult6[4][0]
    c.execute("select size from Cat")
    myresult7 = c.fetchall()
    size = myresult7[4][0]
    c.execute("select location from Cat")
    myresult8 = c.fetchall()
    location = myresult8[4][0]
    return render_template('cat_52167059.html', name=name, description=description, breed=breed, age=age, gender=gender, color=color,size=size, location=location)
###############################################################################
# main driver function
