#!/usr/bin/python3
import sqlite3

conn = sqlite3.connect('Furever.db')
c= conn.cursor()

c.execute("DROP TABLE IF EXISTS Cat")
c.execute("Create table Cat(id int, name varchar(45), description varchar(1000), breed varchar(20), age varchar(50), gender varchar(10),color varchar(10),size varchar(10), location varchar(10), primary key (id));")

cat_51289679_dict = {
    'id':51289679,
    'name': 'Mocha',
    'description': "Mocha is an intelligent cat who, after getting over her initial shyness, is friendly and social. Although she doesn't care for full body pets or being picked up, she loves head and ear scritches and will hang out next to you on the couch. She also enjoys playing, looking out the window, and finding high perches where she can survey the room and take a nap. She's a graceful girl who doesn't break things, and she's a pro with her scratching pad. Mocha is looking for a home with no other cats and mature guardians who can read cat body language and respect her boundaries. In return you will be getting a sweet, lovely companion.",
    'breed': 'Domestic Shorthair/Mix',
    'age': '8 years 4 months 15 days',
    'gender': 'Female',
    'color': 'Brown',
    'size': 'Medium',
    'location': 'Foster Care'
}

cat = cat_51289679_dict
c.execute("INSERT INTO Cat (id, name, description, breed, age, gender, color, size, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (cat['id'], cat['name'], cat['description'], cat['breed'], cat['age'], cat['gender'], cat['color'], cat['size'], cat['location']))


try:
    c.execute("select * from Cat")
    myresult = c.fetchall()
    for x in myresult:
        print(x)
except:
    print("Error")
conn.commit()

