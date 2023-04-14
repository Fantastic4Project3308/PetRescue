#!/usr/bin/python3
# Functions to pull data from sql databases and test against data found in source files.

import sqlite3

# Function gets data type of every column in table and stores it as a list
def get_column_datatypes(db_name, table_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Get a list of all columns in the table
    c.execute("PRAGMA table_info({})".format(table_name))
    columns = c.fetchall()

    column_datatypes = []
    for column in columns:
        column_datatypes.append(column[2]) # Column in position 2 holds data types

    conn.close()
    
    return column_datatypes


# Function tests data types in Dog, Cat, and Adoption tables
# if condition returns true, print message; otherwise, AssertionError is raised
def test_column_datatypes(db_name):
    dogDataTypes = get_column_datatypes('Furever.db', 'Dog')
    catDataTypes = get_column_datatypes('Furever.db', 'Cat')
    adoptionDataTypes = get_column_datatypes('Furever.db', 'adoption')
    
    # test dog table
    assert dogDataTypes == ['INT', 'varchar(45)', 'varchar(1000)', 'varchar(20)', 'varchar(50)', 
                            'varchar(10)', 'varchar(10)', 'varchar(10)', 'varchar(10)'], f"expected data match"
    print("Test passed - Data types for columns in Dog table match as expected")
    
    # test cat table
    assert catDataTypes == ['INT', 'varchar(45)', 'varchar(1000)', 'varchar(20)', 'varchar(50)', 
                            'varchar(10)', 'varchar(10)', 'varchar(10)', 'varchar(10)'], f"expected data match"
    print("Test passed - Data types for columns in Cat table match as expected")
    
    # test adoption table
    assert adoptionDataTypes == ['varchar(45)', 'varchar(45)', 'varchar(100)', 'varchar(50)', 
                                 'varchar(15)', 'varchar(50)'], f"expected data match"
    print("Test passed - Data types for columns in Adoption table match as expected")

# call function
test_column_datatypes('Furever.db')


# Function gets data from table and stores it
def get_data(db_name, table_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table_name}")
    data = c.fetchall()
    conn.close()
    
    return data


# Function tests data in Dog, Cat, and Adoption tables
# if condition returns true, print message; otherwise, AssertionError is raised
def test_table_data(db_name):
    dogData = get_data('Furever.db', 'Dog')
    catData = get_data('Furever.db', 'Cat')
    
    # test dog table
    assert dogData == [(36636186, 'Mojo', "He is a perfect dog in many ways. He can be left alone with the roam of the house and just sleeps. He only chews on his toys. He's potty trained. He's a hilarious home companion.  He has no resource guarding and is great with body handling, he just loves any attention!  He's smart and can be desensitized to triggers like vacuums and blenders with steady positive association.  He may not have had socialization as a puppy to normal household things like this.", 'Terrier, American Pit Bull/Mix', '6 years 7 months 7 days', 'Male', 'Brindle/White', 'Medium', 'Foster Care'), 
                       (42904054, 'Jane', "I'm a Golden Girl in dog form: sassy, sprightly, and a card-carrying member of the AARP. An athletic and active gal, my hobbies include food puzzles, enjoying belly rubs, and tap dancing! I need a kind adopter to make me feel safe and loved for the rest of my years: someone to appreciate my marvelous, unique qualities. I'm a resilient, physically strong, sweetie-pie: well-mannered indoors, and don't require long walks, but would be happiest with a quiet yard of my own. No humans under 12 years, or kitties or doggos please.", 'Terrier,Pit Bull/Mix', '10 years 8 months 22 days', 'Female', 'Brindle', 'Large', 'Foster Care'), 
                       (43078721, 'Ra', "Ra is a spirited and smart boy with loads of personality. He's looking for the perfect forever home with the right balance of love, training and structure to help him continue to blossom.", 'Terrier,American Pit Bull/Mix', '4 years 4 months 4 days', 'Male', 'Brown/white', 'Medium', 'Foster Care'), 
                       (45447002, 'Puck', "Hi, I'm Puck, and like most everyone, I have some quirks but that just makes me more interesting. My foster mom says I have lots of nuance... If you don't know what a Belgian Malinois is, you should read up about us - we are known for loyalty, herding and protection. Me personally, well I'm almost five years old, and have often been told that I'm a handsome boy with my shiny brindle coat and expressive ears. I'm also a fast sprinter with quick reflexes and I love to hunt for small critters outside and chase soccer balls!", 'Terrier, American Pit Bull/Mix', '5 years 5 months 8 days', 'Male', 'Brindle/white', 'Large', 'Foster Care'), 
                       (48818187, 'Pickles', "Pickles didn't have the best start to his life...he came to us from a situation where he was not consistently treated with love and kindness. It takes a little bit of time for him to warm up and trust, but once you're in he is totally in love with you! He spent some time in a foster home, and his foster parent told us Pickles was so sweet and loving. He was an incredibly polite houseguest! His favorite nap spots were on the couch or on the floor next to it with his people nearby for some petting and affection. In the morning he likes to run his zoomies out and is always up for a game of ball in the yard. He's super athletic and very fast! He walks fairly well on leash, but will pull sometimes. The good news is that he's treat motivated and is a quick study, so he's ready to learn to have better leash manners.", 'Terrier, Pit Bull/Mix', '3 years 3 months 17 days', 'Male', 'Brindle/white', 'Large', 'Dog Kennels')], f"expected data match"
    
    print("Test passed - Data in Dog table match as expected")
    
    # test cat table
    assert catData == [(51289679, 'Mocha', "Mocha is an intelligent cat who, after getting over her initial shyness, is friendly and social. Although she doesn't care for full body pets or being picked up, she loves head and ear scritches and will hang out next to you on the couch. She also enjoys playing, looking out the window, and finding high perches where she can survey the room and take a nap. She's a graceful girl who doesn't break things, and she's a pro with her scratching pad. Mocha is looking for a home with no other cats and mature guardians who can read cat body language and respect her boundaries. In return you will be getting a sweet, lovely companion.", 'Domestic Shorthair/Mix', '8 years 4 months 15 days', 'Female', 'Brown', 'Medium', 'Foster Care'), 
                       (52058185, 'Peppi', "Like peanut butter and jelly, cups and saucers, Kermit and Miss Piggy, some things are meant to be together. And that's especially true for Peppi and Stanley. This adorable mom and son pair were brought to SAS together, and were briefly separated, but when staff saw how much they missed each other, they were reunited at their foster parent's home. Peppi didn't eat while they were apart. When Stanley saw Peppi again, he mewed happily for the first time! They were so happy to be back together. Now they sleep together like magnets and Stanley follows his mom devotedly wherever she goes.", 'Domestic Medium Hair/Mix', '4 years 5 days', 'Female', 'Orange/Black', 'Medium', 'Foster Care'), 
                       (52072231, 'Stanley', "Like peanut butter and jelly, cups and saucers, Kermit and Miss Piggy, some things are meant to be together. And that's especially true for Peppi and Stanley. This adorable mom and son pair were brought to SAS together, and were briefly separated, but when staff saw how much they missed each other, they were reunited at their foster parent's home. Peppi didn't eat while they were apart. When Stanley saw Peppi again, he mewed happily for the first time! They were so happy to be back together. Now they sleep together like magnets and Stanley follows his mom devotedly wherever she goes.", 'Domestic Longhair/Mix', '2 years 5 days', 'Male', 'Orange', 'Medium', 'Foster Care'), 
                       (52106194, 'Lily', "Hi! I'm a sweet, timid kitty who loves head scratches and Churu treats! Once I feel comfortable with you, I'm inquisitive and playful. Toys with strings and feathers are my favorite. I also enjoy snuggling in blankets, giving head bumps and bird watching. I have very polite litter box manners. When I'm not curled up next to you, I'll be napping nearby because I like the company.", 'Domestic Medium Hair/Mix', '2 years', 'Female', 'Brown/white', 'Small', 'Foster Care'), 
                       (52167059, 'Boris', 'Boris is a gentle cat who true to his breed is a chatty boy.', 'Siamese/Mix', '6 years 12 days', 'Male', 'Seal', 'Large', 'Cat Free Roaming Room')], f"expected data match"
    print("Test passed - Data in Cat table match as expected")

# call function
test_table_data('Furever.db')