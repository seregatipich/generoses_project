from sqlite3 import connect, IntegrityError


def insert_user_with_zero_clicks(user_id: int) -> None:
    """
    Inserts a new user record into the 'users' table in the database with zero clicks.

    This function connects to a SQLite database named 'mydatabase.db' and ensures that the 'users' 
    table exists. It then attempts to insert a new user record with the specified user ID and 
    initializes their click count to zero. If a record with the same user ID already exists, 
    an IntegrityError is caught and printed. The database connection is committed and closed 
    irrespective of the result.

    Args:
        user_id (int): The unique identifier for the new user to be inserted.

    Returns:
        None: This function does not return anything.
    """
    from .constants import DB_NAME

    conn = connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                clicks INTEGER
            )
        ''')

        cursor.execute(
            'INSERT INTO users (user_id, clicks) VALUES (?, 0)',
            (user_id,)
        )
    except IntegrityError as error:
        print(error)
    finally:
        conn.commit()
        conn.close()


def increment_clicks(user_id: int) -> None:
    """
    Increments the click count for a specified user in the 'users' table of the database.

    This function establishes a connection to a SQLite database named 'mydatabase.db'. It checks 
    if a user with the given user_id exists in the 'users' table. If the user exists, their 'clicks' 
    count is incremented by 1. If the user does not exist, a new record for the user is created with 
    an initial 'clicks' count of 1. After executing the appropriate query, the database connection 
    is committed and closed.

    Args:
        user_id (int): The unique identifier of the user whose click count is to be incremented.

    Returns:
        None: This function does not return anything.
    """
    from .constants import DB_NAME

    conn = connect(DB_NAME)
    cursor = conn.cursor()

    # Check if the user exists
    cursor.execute(
        'SELECT * FROM users WHERE user_id = ?',
        (user_id,)
    )
    if cursor.fetchone():
        # Increment clicks
        cursor.execute(
            'UPDATE users SET clicks = clicks + 1 WHERE user_id = ?',
            (user_id,)
        )
    else:
        # If user does not exist, insert new user with 1 click
        cursor.execute(
            'INSERT INTO users (user_id, clicks) VALUES (?, 1)',
            (user_id,)
        )

    conn.commit()
    conn.close()


def reset_clicks_if_over_three(user_id: int) -> bool:
    """
    Resets the click count to zero for a specified user if their current count is three or more.

    This function connects to a SQLite database named 'mydatabase.db' and retrieves the current 
    click count for a user with the given user_id from the 'users' table. If the user's click count 
    is three or more, it resets the count to zero. The function commits the change to the database 
    and then closes the connection. It returns True if the click count was reset, and False if the 
    count was not reset (either because the user's count was less than three or the user was not 
    found).

    Args:
        user_id (int): The unique identifier of the user whose click count is checked and potentially reset.

    Returns:
        bool: True if the user's click count was reset, False otherwise.
    """
    from .constants import DB_NAME

    conn = connect(DB_NAME)
    cursor = conn.cursor()

    # Check current clicks for the user
    cursor.execute(
        'SELECT clicks FROM users WHERE user_id = ?',
        (user_id,)
    )
    result = cursor.fetchone()

    if result and result[0] >= 3:
        # Reset clicks if they are over three
        cursor.execute(
            'UPDATE users SET clicks = 0 WHERE user_id = ?',
            (user_id,)
        )
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False
