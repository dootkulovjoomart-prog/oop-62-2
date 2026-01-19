import sqlite3
db = sqlite3.connect('Zhoomart.db')
#create cursor
c = db.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS Zhoomart (
    title text,
    full_text text,
    views integer,
    avtor text

)""")
#добавление данных
def creat_zhoomart(title, full_text, views, avtor):
    c.execute(

        'INSERT INTO Zhoomart(title,full_text,views,avtor) VALUES (?,?,?,?)',
                (title, full_text, views,avtor)
    )
#creat_zhoomart('News Biskeke','shit',2335627,'Zhohn')

def get_all_zhoomarts():
    c.execute('SELECT * FROM Zhoomart')
    zhoma = c.fetchall()
    for z in zhoma:
        print(f'Title: {z[0]}, Full Text: {z[1]}, Views: {z[2]}, Avtor: {z[3]}')

#get_all_zhoomarts()

def update_zhoomart(avtor,rowid):
    c.execute(
        'UPDATE Zhoomart SET avtor = ? WHERE rowid = ?',
        (avtor,rowid)
    )
update_zhoomart('Zhoomart',2)
get_all_zhoomarts()
def get_delet_zhoomart(rowid):
    'DELETE FROM Zhoomart WHERE rowid = ?',
    (rowid,)
get_delet_zhoomart([4,5,6,7,8])
get_all_zhoomarts()
db.commit()
db.close()






    

