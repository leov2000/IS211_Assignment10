import logging

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
        keyed = input('Ask the user for a person’s ID number')
        (is_int, cast_num) = safe_int_checker(keyed)

        if (is_int and cast_num) and (cast_num > -1):
            print('Query here....')

        else:
            CLI = False
            SystemExit

if __name__ == '__main__':
    main()