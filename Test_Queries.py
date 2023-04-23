#!/usr/bin/python3
# Functions to test queries in Furever.py are pulling data from database tables correctly.
# The functions in Furever.py were used to render the information on the website. 
# Table contents have already been tested in Test_tables.py 

import sqlite3
from Furever import app

###############################################################################################
#             Dog Query Test - Test Data Rendered on Webpages Matches Database                                          
###############################################################################################

# Function tests data used to render dog_36636186.html against data in Furever.db
def test_dog_366(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_36636186' and store the response
    response = app.test_client().get('/dog_36636186')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=36636186
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=36636186''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "He is a perfect dog in many ways. He can be left alone with the roam of the house and just sleeps. He only chews on his toys. He&#39;s potty trained. He&#39;s a hilarious home companion.  He has no resource guarding and is great with body handling, he just loves any attention!  He&#39;s smart and can be desensitized to triggers like vacuums and blenders with steady positive association.  He may not have had socialization as a puppy to normal household things like this."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("Test passed - Data used to render @app.route('/dog_36636186') matched as expected.")

# Call the function with the name of the database file
test_dog_366('Furever.db')


# Function tests data used to render dog_42904054.html against data in Furever.db
def test_dog_429(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_42904054' and store the response
    response = app.test_client().get('/dog_42904054')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=42904054
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=42904054''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "I&#39;m a Golden Girl in dog form: sassy, sprightly, and a card-carrying member of the AARP. An athletic and active gal, my hobbies include food puzzles, enjoying belly rubs, and tap dancing! I need a kind adopter to make me feel safe and loved for the rest of my years: someone to appreciate my marvelous, unique qualities. I&#39;m a resilient, physically strong, sweetie-pie: well-mannered indoors, and don&#39;t require long walks, but would be happiest with a quiet yard of my own. No humans under 12 years, or kitties or doggos please."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("Test passed - Data used to render @app.route('/dog_42904054') matched as expected.")

# Call the function with the name of the database file
test_dog_429('Furever.db')


# Function tests data used to render dog_43078721.html against data in Furever.db
def test_dog_430(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_42904054' and store the response
    response = app.test_client().get('/dog_43078721')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=43078721
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=43078721''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Ra is a spirited and smart boy with loads of personality. He&#39;s looking for the perfect forever home with the right balance of love, training and structure to help him continue to blossom."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
     # Print a message indicating that the test passed
    print("Test passed - Data used to render @app.route('/dog_43078721') matched as expected.")

# Call the function with the name of the database file    
test_dog_430('Furever.db')


# Function tests data used to render dog_45447002.html against data in Furever.db
def test_dog_454(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_45447002' and store the response
    response = app.test_client().get('dog_45447002')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=45447002
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=45447002''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Hi, I&#39;m Puck, and like most everyone, I have some quirks but that just makes me more interesting. My foster mom says I have lots of nuance... If you don&#39;t know what a Belgian Malinois is, you should read up about us - we are known for loyalty, herding and protection. Me personally, well I&#39;m almost five years old, and have often been told that I&#39;m a handsome boy with my shiny brindle coat and expressive ears. I&#39;m also a fast sprinter with quick reflexes and I love to hunt for small critters outside and chase soccer balls!"
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
     # Print a message indicating that the test passed
    print("Test passed - Data used to render @app.route('/dog_45447002') matched as expected.")

# Call the function with the name of the database file   
test_dog_454('Furever.db')


# Function tests data used to render dog_48818187.html against data in Furever.db
def test_dog_488(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_48818187' and store the response
    response = app.test_client().get('dog_48818187')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=48818187
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=48818187''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Pickles didn&#39;t have the best start to his life...he came to us from a situation where he was not consistently treated with love and kindness. It takes a little bit of time for him to warm up and trust, but once you&#39;re in he is totally in love with you! He spent some time in a foster home, and his foster parent told us Pickles was so sweet and loving. He was an incredibly polite houseguest! His favorite nap spots were on the couch or on the floor next to it with his people nearby for some petting and affection. In the morning he likes to run his zoomies out and is always up for a game of ball in the yard. He&#39;s super athletic and very fast! He walks fairly well on leash, but will pull sometimes. The good news is that he&#39;s treat motivated and is a quick study, so he&#39;s ready to learn to have better leash manners."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("Test passed - Data used to render @app.route('/dog_48818187') matched as expected.")

# Call the function with the name of the database file   
test_dog_488('Furever.db')


# Function tests data used to render dog_50272539.html against data in Furever.db
def test_dog_5027(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_50272539' and store the response
    response = app.test_client().get('dog_50272539')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=50272539
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=50272539''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "We understand that Thomas may seem shy and anxious at first (especially with men), but with the right training and patience, he has the potential to become a loyal and loving companion. He know lots of cues: sit, stay, come, shake, spin, and leave it! If you&#39;re willing to give him a chance, Thomas will reward you with his playful and affectionate personality. Come meet Thomas and see if he&#39;s the perfect match for your family."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("Test passed - Data used to render @app.route('/dog_50272539') matched as expected.")

# Call the function with the name of the database file   
test_dog_5027('Furever.db')


# Function tests data used to render dog_51599202.html against data in Furever.db
def test_dog_515(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_51599202' and store the response
    response = app.test_client().get('dog_51599202')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=51599202
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=51599202''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "He gets along well with other most other dogs and most children, making him a great addition to your family. With his curious personality, he&#39;ll keep you entertained for hours! Chase is prone to mood swings, so we recommend an adopter with extensive dog experience."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("Test passed - Data used to render @app.route('/dog_51599202') matched as expected.")

# Call the function with the name of the database file   
test_dog_515('Furever.db')


# Function tests data used to render dog_51962699.html against data in Furever.db
def test_dog_519(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_51962699' and store the response
    response = app.test_client().get('dog_51962699')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=51962699
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=51962699''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Very affectionate and loves attention. He looks so serious in his photos - but he is not! What we love most is that Debo is a young pup with a lot of energy and a lot of love to give. He is already learned Sit, Down and Touch. What he loves most: Debo loves to explore and sniff everything in sight. He hasn&#39;t really figured out fetch yet, but he&#39;s eager to learn new things and loves to please his humans. He also loves attention and cuddles, and he&#39;s always up for a good belly rub."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("Test passed - Data used to render @app.route('/dog_51962699') matched as expected.")

# Call the function with the name of the database file   
test_dog_519('Furever.db')


# Function tests data used to render dog_52006141.html against data in Furever.db
def test_dog_5200(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_52006141' and store the response
    response = app.test_client().get('dog_52006141')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=52006141
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=52006141''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Ruby is looking for her forever home where she can feel safe and loved. She&#39;s an affectionate and loyal companion who just needs a little patience and love to help her come out of her shell. Come meet Ruby at the Seattle Animal Shelter and give her the chance to steal your heart!"
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("Test passed - Data used to render @app.route('/dog_52006141') matched as expected.")

# Call the function with the name of the database file   
test_dog_5200('Furever.db')


# Function tests data used to render dog_52053831.html against data in Furever.db
def test_dog_5205(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_52053831' and store the response
    response = app.test_client().get('dog_52053831')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=52053831
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=52053831''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Hoss is a sweet-natured, easy-going lovebug. His favorite thing in the world is snuggling up with a human, and his second favorite is burrowing under a blanket. In his foster home, he has shown that he gets along well with cats and other small dogs. He&#39;ll snuggle with any critter that will let him! When he&#39;s not busy snuggling or burrowing, Hoss enjoys playing with squeaky toys and going for short walks. He loves car rides, but he&#39;s also happy to stay home while you&#39;re out stocking up on kibble. This affectionate little guy would love to meet you!"
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("Test passed - Data used to render @app.route('/dog_52053831') matched as expected.")

# Call the function with the name of the database file  
test_dog_5205('Furever.db')


# Function tests data used to render dog_52086329.html against data in Furever.db
def test_dog_5208(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_52086329' and store the response
    response = app.test_client().get('dog_52086329')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=52086329
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=52086329''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Peter is a sweet boy who just needs the right home to thrive. He can be shy at first, but once he warms up to you, he&#39;s an absolute love bug. He&#39;s house-trained and knows basic commands, making him a joy to have around the house. He hasn&#39;t yet been crate trained."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("Test passed - Data used to render @app.route('/dog_52086329') matched as expected.")

# Call the function with the name of the database file   
test_dog_5208('Furever.db')


# Function tests data used to render dog_50858047.html against data in Furever.db
def test_dog_5085(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_50858047' and store the response
    response = app.test_client().get('dog_50858047')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=50858047
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=50858047''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Chewy is an active guy who loves to be outside regardless of the weather. He is a true PNW pup, he would spend all day playing in the rain if we let him! He is a busy guy looking for an equally busy home, with a routine he can learn, and plenty of outdoor adventuring. Chewy would do best in a home without younger children. His greatest wish is to go home with another dog who will run, chase, wrestle and tug with him all day. Chewy loves other dogs so much he doesn&#39;t mind sharing all of his toys, bowls, and people with them. He LOVES going for walks, and is making progress working on his leash behavior but will need a patient and persistent parent to continue his training so that everyone can love the walk as much as him!"
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("Test passed - Data used to render @app.route('/dog_50858047') matched as expected.")

# Call the function with the name of the database file   
test_dog_5085('Furever.db')


# Function tests data used to render dog_52129288.html against data in Furever.db
def test_dog_52129288(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_52129288' and store the response
    response = app.test_client().get('dog_52129288')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=50858047
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=52129288''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Hello, my name is Cotton! I enjoy walks and playing with my sister Nova. I&#39;m a friendly dog that loves to hangout!"
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("Test passed - Data used to render @app.route('/dog_52129288') matched as expected.")

# Call the function with the name of the database file  
test_dog_52129288('Furever.db')


# Function tests data used to render dog_52129291.html against data in Furever.db
def test_dog_52129291(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_52129291' and store the response
    response = app.test_client().get('dog_52129291')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=52129291
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=52129291''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Hello, my name is Nova! I enjoy walks and playing with my brother Cotton. I&#39;m a friendly dog that loves to hangout!"
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("Test passed - Data used to render @app.route('/dog_52129291') matched as expected.")

# Call the function with the name of the database file  
test_dog_52129291('Furever.db')


# Function tests data used to render dog_52091971.html against data in Furever.db
def test_dog_520919(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/dog_52091971' and store the response
    response = app.test_client().get('dog_52091971')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Dog table for data associated with id=52091971
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Dog WHERE id=52091971''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    expected_description = expected_data[1]
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("Test passed - Data used to render @app.route('/dog_52091971') matched as expected.")

# Call the function with the name of the database file   
test_dog_520919('Furever.db')

# ###############################################################################################
#              Cat Query Test - Test Data Rendered on Webpages Matches Database                                            
# ###############################################################################################

# Function tests data used to render cat_51289678.html against data in Furever.db
def test_cat_512(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/cat_51289678' and store the response
    response = app.test_client().get('cat_51289678')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Cat table for data associated with id=51289678
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Cat WHERE id=51289678''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Mocha is an intelligent cat who, after getting over her initial shyness, is friendly and social. Although she doesn&#39;t care for full body pets or being picked up, she loves head and ear scritches and will hang out next to you on the couch. She also enjoys playing, looking out the window, and finding high perches where she can survey the room and take a nap. She&#39;s a graceful girl who doesn&#39;t break things, and she&#39;s a pro with her scratching pad. Mocha is looking for a home with no other cats and mature guardians who can read cat body language and respect her boundaries. In return you will be getting a sweet, lovely companion."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("Test passed - Data used to render @app.route('/cat_51289678') matched as expected.")

# Call the function with the name of the database file   
test_cat_512('Furever.db')


# Function tests data used to render cat_52058185.html against data in Furever.db
def test_cat_520(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/cat_52058185' and store the response
    response = app.test_client().get('cat_52058185')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Cat table for data associated with id=52058185
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Cat WHERE id=52058185''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Like peanut butter and jelly, cups and saucers, Kermit and Miss Piggy, some things are meant to be together. And that&#39;s especially true for Peppi and Stanley. This adorable mom and son pair were brought to SAS together, and were briefly separated, but when staff saw how much they missed each other, they were reunited at their foster parent&#39;s home. Peppi didn&#39;t eat while they were apart. When Stanley saw Peppi again, he mewed happily for the first time! They were so happy to be back together. Now they sleep together like magnets and Stanley follows his mom devotedly wherever she goes."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("Test passed - Data used to render @app.route('/cat_52058185') matched as expected.")

# Call the function with the name of the database file    
test_cat_520('Furever.db')


# Function tests data used to render cat_52072231.html against data in Furever.db
def test_cat_5207(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/cat_52072231' and store the response
    response = app.test_client().get('cat_52072231')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Cat table for data associated with id=52072231
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Cat WHERE id=52072231''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Like peanut butter and jelly, cups and saucers, Kermit and Miss Piggy, some things are meant to be together. And that&#39;s especially true for Peppi and Stanley. This adorable mom and son pair were brought to SAS together, and were briefly separated, but when staff saw how much they missed each other, they were reunited at their foster parent&#39;s home. Peppi didn&#39;t eat while they were apart. When Stanley saw Peppi again, he mewed happily for the first time! They were so happy to be back together. Now they sleep together like magnets and Stanley follows his mom devotedly wherever she goes."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("Test passed - Data used to render @app.route('/cat_52072231') matched as expected.")

# Call the function with the name of the database file    
test_cat_5207('Furever.db')


# Function tests data used to render cat_52106194.html against data in Furever.db
def test_cat_521(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/cat_52106194' and store the response
    response = app.test_client().get('cat_52106194')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Cat table for data associated with id=52106194
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Cat WHERE id=52106194''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    # hard coded decsription with HTML character entity to represent '
    # ' renders correctly on webpage, but unable to compare to DB without hardcoding
    expected_description = "Hi! I&#39;m a sweet, timid kitty who loves head scratches and Churu treats! Once I feel comfortable with you, I&#39;m inquisitive and playful. Toys with strings and feathers are my favorite. I also enjoy snuggling in blankets, giving head bumps and bird watching. I have very polite litter box manners. When I&#39;m not curled up next to you, I&#39;ll be napping nearby because I like the company."
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed
    print("Test passed - Data used to render @app.route('/cat_52106194') matched as expected.")

# Call the function with the name of the database file    
test_cat_521('Furever.db')


# Function tests data used to render cat_52167059.html against data in Furever.db
def test_cat_5216(db_name):
    # Connect to the database.
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    # Send a GET request to '/cat_52167059' and store the response
    response = app.test_client().get('cat_52167059')
    # check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Query the Cat table for data associated with id=52167059
    c.execute('''SELECT name, description, breed, age, gender, color, size, location
                 FROM Cat WHERE id=52167059''')
    expected_data = c.fetchone()

   # Retrieve the expected values for each data field
    expected_name = expected_data[0]
    expected_description = expected_data[1]
    expected_breed = expected_data[2]
    expected_age = str(expected_data[3])
    expected_gender = expected_data[4]
    expected_color = expected_data[5]
    expected_size = expected_data[6]
    expected_location = expected_data[7]
    
    # Convert the string to a byte-like object and check if it's in the response data
    assert expected_name.encode() in response.data
    assert expected_description.encode() in response.data
    assert expected_breed.encode() in response.data
    assert expected_age.encode() in response.data
    assert expected_gender.encode() in response.data
    assert expected_color.encode() in response.data
    assert expected_size.encode() in response.data
    assert expected_location.encode() in response.data
    
    # Print a message indicating that the test passed

    print("Test passed - Data used to render @app.route('/cat_52167059') matched as expected.")

# Call the function with the name of the database file     
test_cat_5216('Furever.db')


# try this first
# if not then do visual test and write queries to check data
# import unittest

# # import the function to be tested
# from my_module import my_function

# class TestMyFunction(unittest.TestCase):
    
#     def test_valid_input(self):
#         petType = 'Dog'
#         breed = 'Labrador'
#         age = '2'
#         size = 'Medium'
#         gender = 'Female'
#         color = 'Yellow'
#         expected_output = {1, 5, 8}  # sample pet IDs that match the input criteria
#         self.assertEqual(my_function(petType, breed, age, size, gender, color), expected_output)
    
#     def test_invalid_petType(self):
#         petType = 'Catssss'
#         breed = '*'
#         age = '*'
#         size = '*'
#         gender = '*'
#         color = '*'
#         expected_output = {1, 2, 3, 4, 5, 6}  # sample pet IDs of all cats
#         self.assertEqual(my_function(petType, breed, age, size, gender, color), expected_output)
    
#     def test_invalid_breed(self):
#         petType = 'Dog'
#         breed = 'Gol'
#         age = '*'
#         size = '*'
#         gender = '*'
#         color = '*'
#         expected_output = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}  # sample pet IDs of all dogs
#         self.assertEqual(my_function(petType, breed, age, size, gender, color), expected_output)
    
#     def test_invalid_age(self):
#         petType = 'Dog'
#         breed = '*'
#         age = 'One'
#         size = '*'
#         gender = '*'
#         color = '*'
#         expected_output = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}  # sample pet IDs of all dogs
#         self.assertEqual(my_function(petType, breed, age, size, gender, color), expected_output)
    
#     def test_invalid_size(self):
#         petType = 'Dog'
#         breed = '*'
#         age = '*'
#         size = 'Smallll'
#         gender = '*'
#         color = '*'
#         expected_output = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}  # sample pet IDs of all dogs
#         self.assertEqual(my_function(petType, breed, age, size, gender, color), expected_output)
    
#     def test_invalid_gender(self):
#         petType = 'Dog'
#         breed = '*'
#         age = '*'
#         size = '*'
#         gender = 'Not known'
#         color = '*'
#         expected_output = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}  # sample pet IDs of all dogs
#         self.assertEqual(my_function(petType, breed, age, size, gender, color), expected_output)
    
#     def test_invalid_color(self):
#         petType = 'Dog'
#         breed = '*'
#         age = '*'
#         size = '*'
#         gender = '*'
#         color = 'Not available'
#         expected_output = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}  # sample pet IDs of all dogs
#         self.assertEqual(my_function(petType, breed, age, size, gender, color), expected_output)
    
#     def test