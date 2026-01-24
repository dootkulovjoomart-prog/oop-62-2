import sqlite3
tarantino = sqlite3.connect('tarantino.db')
c = tarantino.cursor()
c.execute("""
    CREATE TABLE IF NOT EXISTS tarantino_movies (
        movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )""")

c.execute("""
    CREATE TABLE IF NOT EXISTS movies_rating (
        movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
        rating REAL NOT NULL CHECK (rating >= 0 AND rating <= 10),
        income INTEGER NOT NULL ,
        tarantino_id INTEGER ,
        FOREIGN KEY (tarantino_id) REFERENCES tarantino_movies(movie_id)
)""")

def create_tarantino_movies(name):
    c.execute(
        "INSERT INTO tarantino_movies(name) VALUES (?)",
        (name,)
    )
# create_tarantino_movies("Django Unchained")
# create_tarantino_movies("Once Upon a Time in Hollywood")
# create_tarantino_movies("Pulp Fiction")

def create_tarantino_rating(rating,income,tarantino_id):
    c.execute(
        "INSERT INTO movies_rating(rating , income, tarantino_id) VALUES (?,?,?)",
        (rating,income,tarantino_id)
    )
# create_tarantino_rating(8.4 , 426 ,  1 )
# create_tarantino_rating(7.7 , 377 , 2)
# create_tarantino_rating(8.9 , 214 , 3)

def get_tarantino_movies():
    c.execute('''
        SELECT tarantino_movies.name , movies_rating.rating
        FROM tarantino_movies INNER JOIN movies_rating 
        ON tarantino_movies.movie_id = movies_rating.tarantino_id
    ''')
    data = c.fetchall()
    for i in data:
        print(f'Movie: {i[0]}, Rating: {i[1]}')
get_tarantino_movies()

def get_tarantino_rating_by_tarantino_movies(movie_id):
    c.execute("""
        SELECT tarantino_movies.name, movies_rating.rating , movies_rating.income
        FROM tarantino_movies
        LEFT JOIN movies_rating
        ON  tarantino_movies.movie_id = movies_rating.tarantino_id
        WHERE tarantino_movies.movie_id =  ?
    """,
        (movie_id ,))
    data = c.fetchall()
    if not data:
        return None
    for row in data:
        print(f'Movie: {row[0]}, Rating: {row[1]}, Income: {row[2]}')
get_tarantino_rating_by_tarantino_movies(3)

tarantino.commit()
tarantino.close()