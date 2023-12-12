import sqlite3


def insert_user_with_zero_clicks(user_id: int) -> None:
    """
    Inserts a user record into the 'users' table in the 'mydatabase.db' SQLite database
    with zero clicks.

    :param user_id: User identifier to be recorded in the table.

    Connects to 'mydatabase.db', creates a 'users' table if it doesn't exist,
    and inserts the provided user_id with zero clicks into the table.
    """
    db_name = 'mydatabase.db'

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    try: 
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                clicks INTEGER
            )
        ''')

        cursor.execute(
            'INSERT INTO users (user_id, clicks) VALUES (?, 0)', (user_id,))
    except sqlite3.IntegrityError as error:
        print(error)
    finally:
        conn.commit()
        conn.close()


def increment_clicks(user_id: int):
    """
    Increments the number of clicks by one for a given user_id in the 'users' table 
    of the 'mydatabase.db' SQLite database. The user_id is provided as a string.

    :param user_id: User identifier as an integer.
    """
    db_name = 'mydatabase.db'

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Check if the user exists
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    if cursor.fetchone():
        # Increment clicks
        cursor.execute(
            'UPDATE users SET clicks = clicks + 1 WHERE user_id = ?', (user_id,))
    else:
        # If user does not exist, insert new user with 1 click
        cursor.execute(
            'INSERT INTO users (user_id, clicks) VALUES (?, 1)', (user_id,))

    conn.commit()
    conn.close()


def reset_clicks_if_over_three(user_id: int) -> bool:
    """
    Checks the number of clicks for a given user_id in the 'users' table of 
    the 'mydatabase.db' SQLite database. If the number of clicks is greater 
    than three, it resets the clicks to zero and returns True. Otherwise, 
    it returns False.

    :param user_id: User identifier to check and potentially reset clicks.
    :return: True if clicks were reset, False otherwise.
    """
    db_name = 'mydatabase.db'

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Check current clicks for the user
    cursor.execute('SELECT clicks FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()

    if result and result[0] >= 3:
        # Reset clicks if they are over three
        cursor.execute(
            'UPDATE users SET clicks = 0 WHERE user_id = ?', (user_id,))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False
