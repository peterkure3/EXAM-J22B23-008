import csv 
from cs50 import SQL

#opening database file
open("songs.db", "w").close()

#directing sqlite to the database file
db=SQL("sqlite:///songs.db")

#creating tables
# title table
db.execute("CREATE TABLE songs(id INTEGER PRIMARY KEY, title TEXT,artist TEXT, genre TEXT, year INTEGER, length INTEGER)")

#ratings table
db.execute("CREATE TABLE ratings(id INTEGER PRIMARY KEY, liveness INTEGER, danceability INTEGER, energy INTEGER, popularity INTEGER)")

#relational table
db.execute("CREATE TABLE song_rating(songsid INTEGER, ratingid INTEGER, FOREIGN KEY(songsid) REFERENCES songs(id), FOREIGN KEY(ratingid) REFERENCES ratings(id))")

with open("songs.csv","r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        title=row["title"].strip().capitalize()
        genre_name=row["top genre"].split(",")
        artist = row["artist"].strip().capitalize()
        
        year = row["year"].strip().capitalize()
        danceability = row["danceability"].strip().capitalize()
        energy = row["energy"].strip().capitalize()
        
        popularity = row["popularity"].strip().capitalize()
        genre = row["top genre"].strip().capitalize()
        length = row["length"].strip().capitalize()
        liveness = row["liveness"].strip().capitalize()
      
        
        
        songs = db.execute("INSERT INTO songs(title, artist, year, genre, length) VALUES(?, ?, ?, ?, ?)", title, artist, year, genre, length)
        
        rates = db.execute("INSERT INTO ratings(liveness, danceability, energy, popularity) VALUES(?, ?, ?, ?)", liveness, danceability, energy, popularity)
        
        db.execute("INSERT INTO song_rating(songsid, ratingid) VALUES(?, ?)", songs, rates)

        
        