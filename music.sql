-- Check and see if the schema already exists, if it does, drop it
DROP SCHEMA IF EXISTS MUSIC;

-- Check and see if the artists table already exists, if it does, drop it
DROP TABLE IF EXISTS artists;

-- Check and see if the albums table already exists, if it does, drop it
DROP TABLE IF EXISTS albums;

-- Check and see if the songs table already exists, if it does, drop it
DROP TABLE IF EXISTS songs;

-- Create the schema if we can confirm it doesn't exist 
-- (we dropped it if does exist earlier. This is a safey precaution) 
-- assign it to utf8 char set.

CREATE SCHEMA IF NOT EXISTS MUSIC DEFAULT CHARACTER SET utf8;

-- Create artist table
CREATE TABLE artists (
    artist_id INTEGER NOT NULL PRIMARY KEY,
    artist_name TEXT
);

-- Create albums table
CREATE TABLE albums (
    album_id INTEGER NOT NULL PRIMARY KEY,
    album_name TEXT,
    artist_id INT NOT NULL
);

-- Create artist table
CREATE TABLE songs (
    song_id INTEGER NOT NULL PRIMARY KEY,
    song_name TEXT,
    track_number INT NOT NULL,
    song_length INT NOT NULL,
    album_id INT NOT NULL
);


INSERT INTO artist
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
(1, 'Come Together', 1, 300, 1)
(2, 'Something', 2, 280, 1)
(3, 'Maxwells Silver Hammer', 3, 200, 1)
(4, 'Oh! Darling', 4, 180, 1)
(7, 'In the Wee Small Hours of the Morning', 1, 260, 2)
(5, 'Mood Indigo', 2, 190, 2)
(6, 'Glad to Be Unhappy', 3, 155, 2)
(8, 'I Get Along Without You Very Well', 4, 205, 2)