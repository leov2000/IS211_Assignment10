-- Check and see if the artists table already exists, if it does, drop it
DROP TABLE IF EXISTS artists;

-- Check and see if the albums table already exists, if it does, drop it
DROP TABLE IF EXISTS albums;

-- Check and see if the songs table already exists, if it does, drop it
DROP TABLE IF EXISTS songs;

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

-- Create song table
CREATE TABLE songs (
    song_id INTEGER NOT NULL PRIMARY KEY,
    song_name TEXT,
    track_number INT NOT NULL,
    song_length INT NOT NULL,
    album_id INT NOT NULL
);
