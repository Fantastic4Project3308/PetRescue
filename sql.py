#!/usr/bin/python3
import sqlite3

#connecting to database
conn = sqlite3.connect('Furever.db')
c= conn.cursor()

#creating cat table
c.execute("DROP TABLE IF EXISTS Cat")
c.execute("Create table Cat(id int, name varchar(45), description varchar(1000), breed varchar(20), age varchar(50), gender varchar(10),color varchar(10),size varchar(10), location varchar(10), primary key (id));")

#creating dog table
c.execute("DROP TABLE IF EXISTS Dog")
c.execute("Create table Dog(id int, name varchar(45), description varchar(1000), breed varchar(20), age varchar(50), gender varchar(10),color varchar(10),size varchar(10), location varchar(10), primary key (id));")

#creating adoption form table
c.execute("DROP TABLE IF EXISTS adoption")
c.execute("Create table adoption(name varchar(45), occupation varchar(45), address varchar(100), duration varchar(50), phone varchar(15),email varchar(50));")


#creating dictionaries of all the cat information 
cat_51289679_dict = {
    'id':51289678,
    'name': 'Mocha',
    'description': "Mocha is an intelligent cat who, after getting over her initial shyness, is friendly and social. Although she doesn't care for full body pets or being picked up, she loves head and ear scritches and will hang out next to you on the couch. She also enjoys playing, looking out the window, and finding high perches where she can survey the room and take a nap. She's a graceful girl who doesn't break things, and she's a pro with her scratching pad. Mocha is looking for a home with no other cats and mature guardians who can read cat body language and respect her boundaries. In return you will be getting a sweet, lovely companion.",
    'breed': 'Domestic Shorthair/Mix',
    'age': '8 years 4 months 15 days',
    'gender': 'Female',
    'color': 'Brown',
    'size': 'Medium',
    'location': 'Foster Care'
}
cat_52058185_dict = {
    'id' : 52058185,
    'name': 'Peppi',
'description': "Like peanut butter and jelly, cups and saucers, Kermit and Miss Piggy, some things are meant to be together. And that's especially true for Peppi and Stanley. This adorable mom and son pair were brought to SAS together, and were briefly separated, but when staff saw how much they missed each other, they were reunited at their foster parent's home. Peppi didn't eat while they were apart. When Stanley saw Peppi again, he mewed happily for the first time! They were so happy to be back together. Now they sleep together like magnets and Stanley follows his mom devotedly wherever she goes.",
'breed':'Domestic Medium Hair/Mix',
'age':'4 years 5 days',
'gender':'Female',
'color':'Orange/Black',
'size':'Medium',
'location':'Foster Care' }
cat_3_dict = {
    'id' : 52072231,
    'name': 'Stanley',
'description': "Like peanut butter and jelly, cups and saucers, Kermit and Miss Piggy, some things are meant to be together. And that's especially true for Peppi and Stanley. This adorable mom and son pair were brought to SAS together, and were briefly separated, but when staff saw how much they missed each other, they were reunited at their foster parent's home. Peppi didn't eat while they were apart. When Stanley saw Peppi again, he mewed happily for the first time! They were so happy to be back together. Now they sleep together like magnets and Stanley follows his mom devotedly wherever she goes.",
'breed':'Domestic Longhair/Mix',
'age':'2 years 5 days',
'gender':'Male',
'color':'Orange',
'size':'Medium',
'location':'Foster Care'
}
cat_4_dict = {
    'id' : 52106194,
    'name': 'Lily',
'description': "Hi! I'm a sweet, timid kitty who loves head scratches and Churu treats! Once I feel comfortable with you, I'm inquisitive and playful. Toys with strings and feathers are my favorite. I also enjoy snuggling in blankets, giving head bumps and bird watching. I have very polite litter box manners. When I'm not curled up next to you, I'll be napping nearby because I like the company.",
    'breed':'Domestic Medium Hair/Mix',
'age':'2 years',
'gender':'Female',
'color':'Brown/white',
'size':'Small',
'location':'Foster Care'
}
cat_5_dict = {
    'id' : 52167059,
    'name': 'Boris',
'description': "Boris is a gentle cat who true to his breed is a chatty boy.",
    'breed':'Siamese/Mix',
'age':'6 years 12 days',
'gender':'Male',
'color':'Seal',
'size':'Large',
'location':'Cat Free Roaming Room'
}

#creating dictionaries of all the dog information
dog1_dict = {
    'id':36636186,
    'name': 'Mojo',
    'description': "He is a perfect dog in many ways. He can be left alone with the roam of the house and just sleeps. He only chews on his toys. He's potty trained. He's a hilarious home companion.  He has no resource guarding and is great with body handling, he just loves any attention!  He's smart and can be desensitized to triggers like vacuums and blenders with steady positive association.  He may not have had socialization as a puppy to normal household things like this.",
    'breed': 'Terrier, American Pit Bull/Mix',
    'age': '6 years 7 months 7 days',
    'gender': 'Male',
    'color': 'Brindle/White',
    'size': 'Medium',
    'location': 'Foster Care'
}
dog2_dict = {
    'id':42904054,
    'name': 'Jane',
    'description': "I'm a Golden Girl in dog form: sassy, sprightly, and a card-carrying member of the AARP. An athletic and active gal, my hobbies include food puzzles, enjoying belly rubs, and tap dancing! I need a kind adopter to make me feel safe and loved for the rest of my years: someone to appreciate my marvelous, unique qualities. I'm a resilient, physically strong, sweetie-pie: well-mannered indoors, and don't require long walks, but would be happiest with a quiet yard of my own. No humans under 12 years, or kitties or doggos please.",
    'breed': 'Terrier,Pit Bull/Mix',
    'age': '10 years 8 months 22 days',
    'gender': 'Female',
    'color': 'Brindle',
    'size': 'Large',
    'location': 'Foster Care'
}
dog3_dict = {
    'id':43078721,
    'name': 'Ra',
    'description': "Ra is a spirited and smart boy with loads of personality. He's looking for the perfect forever home with the right balance of love, training and structure to help him continue to blossom.",
    'breed': 'Terrier,American Pit Bull/Mix',
    'age': '4 years 4 months 4 days',
    'gender': 'Male',
    'color': 'Brown/white',
    'size': 'Medium',
    'location': 'Foster Care'
}
dog4_dict = {
    'id':45447002,
    'name': 'Puck',
    'description': "Hi, I'm Puck, and like most everyone, I have some quirks but that just makes me more interesting. My foster mom says I have lots of nuance... If you don't know what a Belgian Malinois is, you should read up about us - we are known for loyalty, herding and protection. Me personally, well I'm almost five years old, and have often been told that I'm a handsome boy with my shiny brindle coat and expressive ears. I'm also a fast sprinter with quick reflexes and I love to hunt for small critters outside and chase soccer balls!",
    'breed': 'Terrier, American Pit Bull/Mix',
    'age': '5 years 5 months 8 days',
    'gender': 'Male',
    'color': 'Brindle/white',
    'size': 'Large',
    'location': 'Foster Care'
}
dog5_dict = {
    'id':48818187,
    'name': 'Pickles',
    'description': "Pickles didn't have the best start to his life...he came to us from a situation where he was not consistently treated with love and kindness. It takes a little bit of time for him to warm up and trust, but once you're in he is totally in love with you! He spent some time in a foster home, and his foster parent told us Pickles was so sweet and loving. He was an incredibly polite houseguest! His favorite nap spots were on the couch or on the floor next to it with his people nearby for some petting and affection. In the morning he likes to run his zoomies out and is always up for a game of ball in the yard. He's super athletic and very fast! He walks fairly well on leash, but will pull sometimes. The good news is that he's treat motivated and is a quick study, so he's ready to learn to have better leash manners.",
    'breed':'Terrier, Pit Bull/Mix',
    'age': '3 years 3 months 17 days',
    'gender': 'Male',
    'color': 'Brindle/white',
    'size': 'Large',
    'location': 'Dog Kennels'
}


#inserting dictionary information into cat tables
c.execute("INSERT INTO Cat (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (cat_51289679_dict['id'], cat_51289679_dict['name'], cat_51289679_dict['description'], cat_51289679_dict['breed'], cat_51289679_dict['age'], cat_51289679_dict['gender'], cat_51289679_dict['color'], cat_51289679_dict['size'], cat_51289679_dict['location']))

c.execute("INSERT INTO Cat (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (cat_52058185_dict['id'], cat_52058185_dict['name'], cat_52058185_dict['description'], cat_52058185_dict['breed'], cat_52058185_dict['age'], cat_52058185_dict['gender'], cat_52058185_dict['color'], cat_52058185_dict['size'], cat_52058185_dict['location']))

c.execute("INSERT INTO Cat (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (cat_3_dict['id'], cat_3_dict['name'], cat_3_dict['description'], cat_3_dict['breed'], cat_3_dict['age'], cat_3_dict['gender'], cat_3_dict['color'], cat_3_dict['size'], cat_3_dict['location']))

c.execute("INSERT INTO Cat (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (cat_4_dict['id'], cat_4_dict['name'], cat_4_dict['description'], cat_4_dict['breed'], cat_4_dict['age'], cat_4_dict['gender'], cat_4_dict['color'], cat_4_dict['size'], cat_4_dict['location']))

c.execute("INSERT INTO Cat (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (cat_5_dict['id'], cat_5_dict['name'], cat_5_dict['description'], cat_5_dict['breed'], cat_5_dict['age'], cat_5_dict['gender'], cat_5_dict['color'], cat_5_dict['size'], cat_5_dict['location']))


#inserting dictionary information into dog tables
c.execute("INSERT INTO Dog (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (dog1_dict['id'], dog1_dict['name'], dog1_dict['description'], dog1_dict['breed'], dog1_dict['age'], dog1_dict['gender'], dog1_dict['color'], dog1_dict['size'], dog1_dict['location']))

c.execute("INSERT INTO Dog (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (dog2_dict['id'], dog2_dict['name'], dog2_dict['description'], dog2_dict['breed'], dog2_dict['age'], dog2_dict['gender'], dog2_dict['color'], dog2_dict['size'], dog2_dict['location']))

c.execute("INSERT INTO Dog (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (dog3_dict['id'], dog3_dict['name'], dog3_dict['description'], dog3_dict['breed'], dog3_dict['age'], dog3_dict['gender'], dog3_dict['color'], dog3_dict['size'], dog3_dict['location']))

c.execute("INSERT INTO Dog (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (dog4_dict['id'], dog4_dict['name'], dog4_dict['description'], dog4_dict['breed'], dog4_dict['age'], dog4_dict['gender'], dog4_dict['color'], dog4_dict['size'], dog4_dict['location']))

c.execute("INSERT INTO Dog (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (dog5_dict['id'], dog5_dict['name'], dog5_dict['description'], dog5_dict['breed'], dog5_dict['age'], dog5_dict['gender'], dog5_dict['color'], dog5_dict['size'], dog5_dict['location']))


#to go into test file
try:
    c.execute("select * from Cat")
    myresult = c.fetchall()
    for x in myresult:
        print(x)
except:
    print("Error")
conn.commit()

try:
    c.execute("select * from Dog")
    myresult = c.fetchall()
    for x in myresult:
        print(x)
except:
    print("Error")
conn.commit()

