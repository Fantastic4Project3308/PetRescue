#!/usr/bin/python3
import prefix
from flask import Flask, url_for, make_response, render_template, request, json
from markupsafe import escape
import sqlite3
import psycopg2


app = Flask(__name__)

conn = sqlite3.connect('Furever.db', check_same_thread=False)
c = conn.cursor()

# create app to use in this Flask application
app = Flask(__name__)


prefix.use_PrefixMiddleware(app)   

def query_db(query, args=(), one=False):
    c.execute(query, args)
    r = [dict((c.description[i][0], value) \
               for i, value in enumerate(row)) for row in c.fetchall()]
    return (r[0] if r else None) if one else r

# test route to show prefix settings
@app.route('/prefix_url')  
def prefix_url():
    return 'The URL for this page is {}'.format(url_for('prefix_url'))
#homepage
@app.route('/')
def homepage():
    #cat_url = url_for('catpage')
    #dog_url = url_for('dogpage')
    return render_template('Homepage.html')
#about us
@app.route('/aboutus')
def aboutus():
    return render_template('AboutUs.html')
#adoption form
@app.route('/adoptionform')
def adoptionform():
    return render_template('AdoptionForm.html')
#insert a new contact
@app.route('/contact', methods = ['POST'])
def contact():
    data = json.dumps(request.form.to_dict(flat=False))
    data = json.loads(data)
    # for entry in data(some range or len(range)):
        # c.executemany(change fname to entry) what does the 0 mean?
    c.execute('''
        INSERT INTO Contact (Name,
                    Occupation,
                    Address,
                    DurationOfResidence,
                    Phone,
                    Email,
                    AdultCount,
                    KidCount,
                    HomeType,
                    HouseholdDescription,
                    Landlord,
                    Allergy,
                    Agreement,
                    TimeCommitment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
    str(data['fname'][0] or ''), # replace 0 with entry; this should go thrpough every entry in json dict
    str(data['occupation'][0]  or ''),
    str(data['address'][0]  or ''),
    data['addresslen'][0],
    str(data['phone'][0]  or ''),
    str(data['email'][0]  or ''),
    data['adultcount'][0],
    data['kidcount'][0],
    str(data['hometype'][0]  or ''),
    str(data['household'][0]  or ''),
    str(data['landlord'][0]  or ''),
    1 if 'allergy' in data and data['allergy'][0]  == 'allergy-yes' else 0,
    1 if 'decision' in data and data['decision'][0]  == 'decision-yes' else 0,
    1 if 'time' in data and data['time'][0]  == 'time-yes' else 0
    ))
    conn.commit()
    return 'Success!'
#show contacts
@app.route('/contacts')
def contacts():
    contacts = query_db("select * from Contact")
    return render_template('userInformation.html', contacts = contacts)

#helper function for both dog and cat search pages
def get_filtered_petIDs(petType):
    ''' 
    Input validation/fix.
    '''
    if petType != 'Dog': petType = 'Cat';
    
    '''
    Get multiple attributes of pets from the user input.
    The default value is a Kleen star if unassigned.
    '''
    petType = 'Dog';
    breed = request.args.get('breed', '*');
    age = request.args.get('age', '*');
    size = request.args.get('size', '*');
    gender = request.args.get('gender', '*');
    color = request.args.get('color', '*');
    print('bread: ', breed, 'age: ', age, 'size: ', size, 'gender: ', gender, 'color: ', color);
    '''
    Instantiate an empty set to collect IDs of user-preferred pets.
    Find the intersection of pet IDs among different attributes.
    '''
    petIDsByBreed = set();
    petIDsByAge = set();
    petIDsBySize = set();
    petIDsByGender = set();
    petIDsByColor = set();
    
    c.execute(f'SELECT * FROM {petType}');
    allPets = c.fetchall();
    
    for pet in allPets: 
        if breed == '*' or breed in pet[3]: petIDsByBreed.add(pet[0]);
    
    for pet in allPets:
        if age == '*' or pet[4] == age: petIDsByAge.add(pet[0]);

    for pet in allPets:
        if size == '*' or pet[7] == size: petIDsBySize.add(pet[0]);
    
    for pet in allPets:
        if gender == '*' or pet[5] == gender: petIDsByGender.add(pet[0]);
    
    for pet in allPets: 
        if color == '*' or pet[6] == color: petIDsByColor.add(pet[0]);
    
    petIDSet = petIDsByBreed.intersection(petIDsByAge).intersection(petIDsBySize).intersection(petIDsByGender).intersection(petIDsByColor);
    
    return petIDSet;

#cat page
@app.route('/cats')
def catpage():
    petType = 'Cat'
    petIDSet = get_filtered_petIDs(petType);
    return render_template('CatPage.html', petIDSet=petIDSet, petType=petType)

#dog page
@app.route('/dogs')
def dogpage():
    petType = 'Dog'
    petIDSet = get_filtered_petIDs(petType);
    return render_template('DogPage.html', petIDSet=petIDSet, petType=petType)

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
