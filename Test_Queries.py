#!/usr/bin/python3
# Functions to test queries in Furever.py are pulling data from database tables correctly.
# The functions in Furever.py were used to render the information on the website. 
# We are using the same code used in Furever.py to pull attribute so this way we are testing that the functions in Furever.py pulled the information correctly.
# Table contents have already been tested in Test_tables.py 

import sqlite3

# Function to test all names in dog table
# if condition returns true, print message; otherwise, AssertionError is raised
def test_dog_name(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # pull all names from table
    c.execute("select name from Dog")
    myresult = c.fetchall()
    name_36636186 =  myresult[0][0]
    name_42904054 =  myresult[1][0]
    name_43078721 =  myresult[2][0]
    name_45447002 =  myresult[3][0]
    name_48818187 =  myresult[4][0]
    
    # test names
    assert name_36636186 == 'Mojo'  
    assert name_42904054 == 'Jane' 
    assert name_43078721 == 'Ra'
    assert name_45447002 == 'Puck'
    assert name_48818187 == 'Pickles'
    
    print("Test passed - Names in Dog table matched as expected.")
    

# call function
test_dog_name('Furever.db')


# Function to test all descriptions in dog table
# if condition returns true, print message; otherwise, AssertionError is raised
def test_dog_description(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # pull all descriptions from table
    c.execute("select description from Dog")
    myresult = c.fetchall()
    desc_36636186 =  myresult[0][0]
    desc_42904054 =  myresult[1][0]
    desc_43078721 =  myresult[2][0]
    desc_45447002 =  myresult[3][0]
    desc_48818187 =  myresult[4][0]
    
    # test descriptions
    assert desc_36636186 == "He is a perfect dog in many ways. He can be left alone with the roam of the house and just sleeps. He only chews on his toys. He's potty trained. He's a hilarious home companion.  He has no resource guarding and is great with body handling, he just loves any attention!  He's smart and can be desensitized to triggers like vacuums and blenders with steady positive association.  He may not have had socialization as a puppy to normal household things like this."  
    assert desc_42904054 == "I'm a Golden Girl in dog form: sassy, sprightly, and a card-carrying member of the AARP. An athletic and active gal, my hobbies include food puzzles, enjoying belly rubs, and tap dancing! I need a kind adopter to make me feel safe and loved for the rest of my years: someone to appreciate my marvelous, unique qualities. I'm a resilient, physically strong, sweetie-pie: well-mannered indoors, and don't require long walks, but would be happiest with a quiet yard of my own. No humans under 12 years, or kitties or doggos please." 
    assert desc_43078721 == "Ra is a spirited and smart boy with loads of personality. He's looking for the perfect forever home with the right balance of love, training and structure to help him continue to blossom."
    assert desc_45447002 == "Hi, I'm Puck, and like most everyone, I have some quirks but that just makes me more interesting. My foster mom says I have lots of nuance... If you don't know what a Belgian Malinois is, you should read up about us - we are known for loyalty, herding and protection. Me personally, well I'm almost five years old, and have often been told that I'm a handsome boy with my shiny brindle coat and expressive ears. I'm also a fast sprinter with quick reflexes and I love to hunt for small critters outside and chase soccer balls!"
    assert desc_48818187 == "Pickles didn't have the best start to his life...he came to us from a situation where he was not consistently treated with love and kindness. It takes a little bit of time for him to warm up and trust, but once you're in he is totally in love with you! He spent some time in a foster home, and his foster parent told us Pickles was so sweet and loving. He was an incredibly polite houseguest! His favorite nap spots were on the couch or on the floor next to it with his people nearby for some petting and affection. In the morning he likes to run his zoomies out and is always up for a game of ball in the yard. He's super athletic and very fast! He walks fairly well on leash, but will pull sometimes. The good news is that he's treat motivated and is a quick study, so he's ready to learn to have better leash manners."
    
    print("Test passed - Descriptions in Dog table matched as expected.")
    

# call function
test_dog_description('Furever.db')


# Function to test all breeds in dog table
# if condition returns true, print message; otherwise, AssertionError is raised
def test_dog_breed(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # pull all breeds from table
    c.execute("select breed from Dog")
    myresult = c.fetchall()
    breed_36636186 =  myresult[0][0]
    breed_42904054 =  myresult[1][0]
    breed_43078721 =  myresult[2][0]
    breed_45447002 =  myresult[3][0]
    breed_48818187 =  myresult[4][0]
    
    # test breeds
    assert breed_36636186 == 'Terrier, American Pit Bull/Mix'  
    assert breed_42904054 == 'Terrier,Pit Bull/Mix' 
    assert breed_43078721 == 'Terrier,American Pit Bull/Mix'
    assert breed_45447002 == 'Terrier, American Pit Bull/Mix'
    assert breed_48818187 == 'Terrier, Pit Bull/Mix'
    
    print("Test passed - Breeds in Dog table matched as expected.")
    

# call function
test_dog_breed('Furever.db')


# Function to test all ages in dog table
# if condition returns true, print message; otherwise, AssertionError is raised
def test_dog_age(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # pull all ages from table
    c.execute("select age from Dog")
    myresult = c.fetchall()
    age_36636186 =  myresult[0][0]
    age_42904054 =  myresult[1][0]
    age_43078721 =  myresult[2][0]
    age_45447002 =  myresult[3][0]
    age_48818187 =  myresult[4][0]
    
    # test ages
    assert age_36636186 == '6 years 7 months 7 days'  
    assert age_42904054 == '10 years 8 months 22 days' 
    assert age_43078721 == '4 years 4 months 4 days'
    assert age_45447002 == '5 years 5 months 8 days'
    assert age_48818187 == '3 years 3 months 17 days'
    
    print("Test passed - Ages in Dog table matched as expected.")
    

# call function
test_dog_age('Furever.db')


# Function to test all genders in dog table
# if condition returns true, print message; otherwise, AssertionError is raised
def test_dog_gender(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # pull all genders from table
    c.execute("select gender from Dog")
    myresult = c.fetchall()
    gender_36636186 =  myresult[0][0]
    gender_42904054 =  myresult[1][0]
    gender_43078721 =  myresult[2][0]
    gender_45447002 =  myresult[3][0]
    gender_48818187 =  myresult[4][0]
    
    # test genders
    assert gender_36636186 == 'Male'  
    assert gender_42904054 == 'Female' 
    assert gender_43078721 == 'Male'
    assert gender_45447002 == 'Male'
    assert gender_48818187 == 'Male'
    
    print("Test passed -  Genders in Dog table matched as expected.")
    

# call function
test_dog_gender('Furever.db')


# Function to test all colors in dog table
# if condition returns true, print message; otherwise, AssertionError is raised
def test_dog_color(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # pull all colors from table
    c.execute("select color from Dog")
    myresult = c.fetchall()
    color_36636186 =  myresult[0][0]
    color_42904054 =  myresult[1][0]
    color_43078721 =  myresult[2][0]
    color_45447002 =  myresult[3][0]
    color_48818187 =  myresult[4][0]
    
    # test colors
    assert color_36636186 == 'Brindle/White'  
    assert color_42904054 == 'Brindle'
    assert color_43078721 == 'Brown/white'
    assert color_45447002 == 'Brindle/white'
    assert color_48818187 == 'Brindle/white'
    
    print("Test passed -  Colors in Dog table matched as expected.")
    

# call function
test_dog_color('Furever.db')


# Function to test all sizes in dog table
# if condition returns true, print message; otherwise, AssertionError is raised
def test_dog_size(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # pull all sizes from table
    c.execute("select size from Dog")
    myresult = c.fetchall()
    size_36636186 =  myresult[0][0]
    size_42904054 =  myresult[1][0]
    size_43078721 =  myresult[2][0]
    size_45447002 =  myresult[3][0]
    size_48818187 =  myresult[4][0]
    
    # test sizes
    assert size_36636186 == 'Medium' 
    assert size_42904054 == 'Large'
    assert size_43078721 == 'Medium'
    assert size_45447002 == 'Large'
    assert size_48818187 == 'Large'
    
    print("Test passed - Sizes in Dog table matched as expected.")
    

# call function
test_dog_size('Furever.db')

# Function to test all locations in dog table
# if condition returns true, print message; otherwise, AssertionError is raised
def test_dog_location(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # pull all locations from table
    c.execute("select location from Dog")
    myresult = c.fetchall()
    location_36636186 =  myresult[0][0]
    location_42904054 =  myresult[1][0]
    location_43078721 =  myresult[2][0]
    location_45447002 =  myresult[3][0]
    location_48818187 =  myresult[4][0]
    
    # test locations
    assert location_36636186 == 'Foster Care' 
    assert location_42904054 == 'Foster Care'
    assert location_43078721 == 'Foster Care'
    assert location_45447002 == 'Foster Care'
    assert location_48818187 == 'Dog Kennels'
    
    print("Test passed - Locations in Dog table matched as expected.")
    

# call function
test_dog_location('Furever.db')