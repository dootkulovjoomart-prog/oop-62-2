import sqlite3
hw = sqlite3.connect('homework.db')
c = hw.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS movies (
        id  INTEGER PRIMARY KEY  AUTOINCREMENT,
        name  TEXT NOT NULL,
        year  INTEGER NOT NULL,
        kino_poisk INTEGER NOT NULL CHECK (kino_poisk >= 0 AND kino_poisk <= 10),
        comentario TEXT NOT NULL 
        
) """)

def created_movies(name , year , kino_poisk, comentario):
    c.execute(
        'INSERT INTO movies(name,year,kino_poisk,comentario) VALUES (?,?,?,?) ',
        (name,year,kino_poisk,comentario)

    )
#created_movies('Avengers endgame', 2019 , 9 ,'Bomba')

def select_all_movies():
    c.execute('SELECT * FROM movies')
    movie = c.fetchall()
    print(movie)

#select_all_movies()

def update_movie(id, name, year, kino_poisk, comentario):
    c.execute(
        'UPDATE movies SET name=? , year = ?, kino_poisk = ?, comentario = ? WHERE id=?',
        (name, year, kino_poisk, comentario,id)

    )
#update_movie(3 , 'Spider man' ,2018 ,7 ,'govno')
#update_movie(4,'Avatar 3',2025,9 ,'Beatifull movies' )
hw.commit()

def get_delet_movie(id):
    c.execute(
        'DELETE FROM movies WHERE id=?',
        (id,)
    )
get_delet_movie(5)
hw.commit()
hw.close()

