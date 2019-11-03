import sqlite3

conn = sqlite3.connect('pets.db')

def create_tables():

    sql_table = """
    DROP TABLE IF EXISTS person;
    DROP TABLE IF EXISTS pet;
    DROP TABLE IF EXISTS person_pet;

    CREATE TABLE person (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER
    );

    CREATE TABLE pet (
        id INTEGER PRIMARY KEY,
        name TEXT,
        breed TEXT,
        age INTEGER,
        dead INTEGER
    );

    CREATE TABLE person_pet (
        person_id INTEGER,
        pet_id INTEGER
    );
    """

    return sql_table

def insert_data():

    sql_insert = """
    INSERT INTO person
    (id, first_name, last_name, age)
    VALUES
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23);

    INSERT INTO pet
    (id, name, breed, age, dead)
    VALUES
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1);


    INSERT INTO person_pet 
    (person_id, pet_id)
    VALUES
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6);
    """
    
    return sql_insert

def load_data():
    conn.executescript(create_tables())
    conn.executescript(insert_data())
    conn.commit()
    conn.close()

if __name__ == '__main__':
    load_data()
