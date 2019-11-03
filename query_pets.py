import logging
import sqlite3

def query_db():
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    sql_query = """
    SELECT 
    person.first_name AS 'PersonFirst',
    person.last_name AS 'PersonLast',
	person.age AS 'PersonAge', 
	pet.name AS 'PetName',
    pet.breed AS 'PetBreed',
    pet.age AS 'PetAge',
    pet.dead AS 'PetDead',
    person_pet.person_id AS 'PersonID',
    person_pet.pet_id AS 'PetID'
    FROM person_pet
	JOIN person ON person_pet.person_id = person.id
    JOIN pet ON person_pet.pet_id = pet.id;
    """
    cursor.executescript(sql_query)
    print(cursor.fetchall())
    conn.close()

    # return cursor.fetchall()


def safe_int_checker(int_str):
    """
    A function that checks if the string is actually an int. used for the CLI.
    Parameters:
        int_str(str): A string representing an int.
    Returns:
        A tuple with a boolean as the first item and a value if its successfuly cast or None if it isnt.
    """

    try:
        num = int(int_str)
        return (True, num)
    except ValueError:
        return (False, None)


def main():
    """
    The primary function of this application.
    Parameters:
        None
    Logs:
        An error if the string url is entered incorrectly.
    """

    logging.basicConfig(filename='errors.log',
                        level=logging.ERROR, format='%(message)s')
    logging.getLogger('assignment10')

    CLI = True 

    while CLI:
        keyed = input('Ask the user for a person’s ID number\n')
        (is_int, cast_num) = safe_int_checker(keyed)

        if (is_int and cast_num) and (cast_num > -1):
            print('Query here....')
            print(cast_num, 'num')
            results = query_db()
        else:
            CLI = False
            print('Exit')
            SystemExit

if __name__ == '__main__':
    main()