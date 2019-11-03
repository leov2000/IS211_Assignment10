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
    album_id INT NOT NULL
);
