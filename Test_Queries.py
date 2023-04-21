#!/usr/bin/python3
# Functions to test queries in Furever.py are pulling data from database tables correctly.
# The functions in Furever.py were used to render the information on the website. 
# We are using the same code used in Furever.py to pull attribute so this way we are testing that the functions in Furever.py pulled the information correctly.
# Table contents have already been tested in Test_tables.py 

import sqlite3

###############################################################################################
#                                  Dog Query Testing                                          #
###############################################################################################

# Function tests data used to render dog_36636186.html against data in Furever.db
def test_dog_366(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Query the Dog table for data associated with id=36636186
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=36636186''')
    expected_data = c.fetchone()

    # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    expected_description = expected_data[1]
    expected_breed = expected_data[2]
    expected_age = expected_data[3]
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]

    # dog_366() code - retrieve values from table using exact code from function
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

    # Compare expected and actual values for each data field.
    # if condition returns true, print message; otherwise, AssertionError is raised
    assert name == expected_name
    assert description == expected_description
    assert breed == expected_breed
    assert age == expected_age
    assert gender == expected_gender
    assert color == expected_color
    assert size == expected_size
    assert location == expected_location

    print("Test passed - Data used to render @app.route('/dog_36636186') matched as expected.")

# call function
test_dog_366('Furever.db')


# Function tests data used to render dog_42904054.html against data in Furever.db
def test_dog_429(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Query the Dog table for data associated with id=42904054
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=42904054''')
    expected_data = c.fetchone()

    # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    expected_description = expected_data[1]
    expected_breed = expected_data[2]
    expected_age = expected_data[3]
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]

    # dog_429() code - retrieve values from table using exact code from function
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

    # Compare expected and actual values for each data field.
    # if condition returns true, print message; otherwise, AssertionError is raised
    assert name == expected_name
    assert description == expected_description
    assert breed == expected_breed
    assert age == expected_age
    assert gender == expected_gender
    assert color == expected_color
    assert size == expected_size
    assert location == expected_location

    print("Test passed - Data used to render @app.route('/dog_42904054') matched as expected.")

# call function    
test_dog_429('Furever.db')


# Function tests data used to render dog_43078721.html against data in Furever.db
def test_dog_430(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Query the Dog table for data associated with id=43078721
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=43078721''')
    expected_data = c.fetchone()

    # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    expected_description = expected_data[1]
    expected_breed = expected_data[2]
    expected_age = expected_data[3]
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]

    # dog_430() code - retrieve values from table using exact code from function
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

    # Compare expected and actual values for each data field.
    # if condition returns true, print message; otherwise, AssertionError is raised
    assert name == expected_name
    assert description == expected_description
    assert breed == expected_breed
    assert age == expected_age
    assert gender == expected_gender
    assert color == expected_color
    assert size == expected_size
    assert location == expected_location

    print("Test passed - Data used to render @app.route('/dog_43078721') matched as expected.")

# call function    
test_dog_430('Furever.db')


# Function tests data used to render dog_45447002.html against data in Furever.db
def test_dog_454(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Query the Dog table for data associated with id=45447002
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=45447002''')
    expected_data = c.fetchone()

    # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    expected_description = expected_data[1]
    expected_breed = expected_data[2]
    expected_age = expected_data[3]
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]

    # dog_454() code - retrieve values from table using exact code from function
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
    
    # Compare expected and actual values for each data field.
    # if condition returns true, print message; otherwise, AssertionError is raised
    assert name == expected_name
    assert description == expected_description
    assert breed == expected_breed
    assert age == expected_age
    assert gender == expected_gender
    assert color == expected_color
    assert size == expected_size
    assert location == expected_location

    print("Test passed - Data used to render @app.route('/dog_45447002') matched as expected.")

# call function    
test_dog_454('Furever.db')


# Function tests data used to render dog_48818187.html against data in Furever.db
def test_dog_488(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Query the Dog table for data associated with id=48818187
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=48818187''')
    expected_data = c.fetchone()

    # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    expected_description = expected_data[1]
    expected_breed = expected_data[2]
    expected_age = expected_data[3]
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]

    # dog_488() code - retrieve values from table using exact code from function
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
    
    # Compare expected and actual values for each data field.
    # if condition returns true, print message; otherwise, AssertionError is raised
    assert name == expected_name
    assert description == expected_description
    assert breed == expected_breed
    assert age == expected_age
    assert gender == expected_gender
    assert color == expected_color
    assert size == expected_size
    assert location == expected_location

    print("Test passed - Data used to render @app.route('/dog_48818187') matched as expected.")

# call function    
test_dog_488('Furever.db')

###############################################################################################
#                                  Cat Query Testing                                          #
###############################################################################################

# Function tests data used to render cat_51289678.html against data in Furever.db
def test_cat_512(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Query the Cat table for data associated with id=51289678
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Cat WHERE id=51289678''')
    expected_data = c.fetchone()

    # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    expected_description = expected_data[1]
    expected_breed = expected_data[2]
    expected_age = expected_data[3]
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]

    # cat_512() code - retrieve values from table using exact code from function
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
    
    # Compare expected and actual values for each data field.
    # if condition returns true, print message; otherwise, AssertionError is raised
    assert name == expected_name
    assert description == expected_description
    assert breed == expected_breed
    assert age == expected_age
    assert gender == expected_gender
    assert color == expected_color
    assert size == expected_size
    assert location == expected_location

    print("Test passed - Data used to render @app.route('/cat_51289678') matched as expected.")

# call function    
test_cat_512('Furever.db')


# Function tests data used to render cat_52058185.html against data in Furever.db
def test_cat_520(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Query the Cat table for data associated with id=52058185
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Cat WHERE id=52058185''')
    expected_data = c.fetchone()

    # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    expected_description = expected_data[1]
    expected_breed = expected_data[2]
    expected_age = expected_data[3]
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]

    # cat_520() code - retrieve values from table using exact code from function
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
    
    # Compare expected and actual values for each data field.
    # if condition returns true, print message; otherwise, AssertionError is raised
    assert name == expected_name
    assert description == expected_description
    assert breed == expected_breed
    assert age == expected_age
    assert gender == expected_gender
    assert color == expected_color
    assert size == expected_size
    assert location == expected_location

    print("Test passed - Data used to render @app.route('/cat_52058185') matched as expected.")

# call function    
test_cat_520('Furever.db')


# Function tests data used to render cat_52072231.html against data in Furever.db
def test_cat_5207(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Query the Cat table for data associated with id=52072231
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Cat WHERE id=52072231''')
    expected_data = c.fetchone()

    # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    expected_description = expected_data[1]
    expected_breed = expected_data[2]
    expected_age = expected_data[3]
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]

    # cat_5207() code - retrieve values from table using exact code from function
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
    
    # Compare expected and actual values for each data field.
    # if condition returns true, print message; otherwise, AssertionError is raised
    assert name == expected_name
    assert description == expected_description
    assert breed == expected_breed
    assert age == expected_age
    assert gender == expected_gender
    assert color == expected_color
    assert size == expected_size
    assert location == expected_location

    print("Test passed - Data used to render @app.route('/cat_52072231') matched as expected.")

# call function    
test_cat_5207('Furever.db')


# Function tests data used to render cat_52106194.html against data in Furever.db
def test_cat_521(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Query the Cat table for data associated with id=52106194
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Cat WHERE id=52106194''')
    expected_data = c.fetchone()

    # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    expected_description = expected_data[1]
    expected_breed = expected_data[2]
    expected_age = expected_data[3]
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]

    # cat_521() code - retrieve values from table using exact code from function
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
    
    # Compare expected and actual values for each data field.
    # if condition returns true, print message; otherwise, AssertionError is raised
    assert name == expected_name
    assert description == expected_description
    assert breed == expected_breed
    assert age == expected_age
    assert gender == expected_gender
    assert color == expected_color
    assert size == expected_size
    assert location == expected_location

    print("Test passed - Data used to render @app.route('/cat_52106194') matched as expected.")

# call function    
test_cat_521('Furever.db')


# Function tests data used to render cat_52167059.html against data in Furever.db
def test_cat_5216(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Query the Cat table for data associated with id=52167059
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Cat WHERE id=52167059''')
    expected_data = c.fetchone()

    # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    expected_description = expected_data[1]
    expected_breed = expected_data[2]
    expected_age = expected_data[3]
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]

    # cat_5216() code - retrieve values from table using exact code from function
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
    
    # Compare expected and actual values for each data field.
    # if condition returns true, print message; otherwise, AssertionError is raised
    assert name == expected_name
    assert description == expected_description
    assert breed == expected_breed
    assert age == expected_age
    assert gender == expected_gender
    assert color == expected_color
    assert size == expected_size
    assert location == expected_location

    print("Test passed - Data used to render @app.route('/cat_52167059') matched as expected.")

# call function    
test_cat_5216('Furever.db')