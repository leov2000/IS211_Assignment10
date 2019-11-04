import sqlite3

def insert_data():
    sql_insert = """
    INSERT INTO artists
    (artist_id, artist_name)
    VALUES
    (1, "Frank Sinatra"),
    (2, "The Beatles");

    INSERT INTO albums
    (album_id, album_name, artist_id)
    VALUES
    (1, 'Abbey Road', 2),
    (2, 'In the Wee Small Hours', 1);

    INSERT INTO songs 
    (song_id, song_name, track_number, song_length, album_id)
    VALUES
    (1, 'Come Together', 1, 300, 1),
    (2, 'Something', 2, 280, 1),
    (3, 'Maxwells Silver Hammer', 3, 200, 1),
    (4, 'Oh! Darling', 4, 180, 1),
    (7, 'In the Wee Small Hours of the Morning', 1, 260, 2),
    (5, 'Mood Indigo', 2, 190, 2),
    (6, 'Glad to Be Unhappy', 3, 155, 2),
    (8, 'I Get Along Without You Very Well', 4, 205, 2);
    """
    
    return sql_insert

def load_data():
    conn = sqlite3.connect('music.db')

    sql_file = open('music.sql')
    sql_tables = sql_file.read()
    sql_insert = insert_data()

    conn.executescript(sql_tables)
    conn.executescript(sql_insert)
    conn.commit()
    conn.close()

    sql_file.close()

def query_data():
    conn = sqlite3.connect('music.db')
    cursor = conn.cursor()
    
    sql_query = """
    SELECT 
    artists.artist_name AS 'Artist Name',
    albums.album_name AS 'Album Title',
    songs.song_name AS 'Song Name',
    songs.track_number AS 'Track Number',
    songs.song_length AS 'Song Length'
    FROM songs
	JOIN artists ON albums.artist_id = artists.artist_id
    JOIN albums ON songs.album_id = albums.album_id;
    """

    cursor.execute(sql_query)
    query_result = cursor.fetchall()

    print(query_result)


if __name__ == '__main__':
    load_data()
    query_data()