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

    cursor.execute(sql_query)
    query_result = cursor.fetchall()
    header = [i[0] for i in cursor.description]

    return [header, query_result]

def value_getter(dict, key, tup):
    index = dict[key]

    return tup[index]

def print_person_info(tup_info):
    (name, age) = tup_info

    print(f"{name}, {age} years old")

def print_pet_owner_details(owner, pet_details):
    print(f"{owner} {pet_details}")

def print_results(query_result, key_dict):
    head = query_result[0]

    person_name = f"{value_getter(key_dict, 'PersonFirst', head)} {value_getter(key_dict, 'PersonLast', head)}"
    person_age = f"{value_getter(key_dict, 'PersonAge', head)}"

    print_person_info((person_name, person_age))

    for pet in query_result:
        pet_info = f"owned {value_getter(key_dict, 'PetName', pet)}, a {value_getter(key_dict, 'PetBreed', pet)}, that was {value_getter(key_dict, 'PetAge', pet)} years old."

        print_pet_owner_details(person_name, pet_info)
    
def find_person(query_results, keys_dict, user_input):
    person_id = keys_dict['PersonID']
    filtered_list = filter(lambda x: x[person_id] == user_input, query_results)

    return list(filtered_list)
    

def get_keys(header_list):
    config_fields = [
        'PersonFirst',
        'PersonLast',
        'PersonAge',
        'PetName',
        'PetBreed',
        'PetAge',
        'PetDead',
        'PersonID',
        'PetID'
    ]

    return { k:header_list.index(k) for k in config_fields }


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

def print_error(num):
    print(f'Sorry the personId of {num} does not exist')
    logging.error(f'Error processing <{num}>')


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
        keyed = input('\nPlease enter in a numerical ID\n')
        (is_int, cast_num) = safe_int_checker(keyed)

        if is_int and cast_num > -1 :
            db_query = query_db()
            [header, db_data] = db_query
            header_index_dict = get_keys(header)
            plucked_values = find_person(db_data, header_index_dict, cast_num)

            print_error(cast_num) if not plucked_values else print_results(plucked_values, header_index_dict)

        elif is_int == False:
            print('It looks like you entered a non-numerical key, please enter in a numerical key')
            logging.error(f'Error processing <{keyed}>')

        else:
            CLI = False
            print('Terminal Exiting....')
            SystemExit

if __name__ == '__main__':
    main()