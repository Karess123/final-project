import final_doc
import sqlite3
import csv

def create_db():
    conn = sqlite3.connect('final_doc.sqlite3')
    cur = conn.cursor()


    create_movies_sql = '''
        CREATE TABLE IF NOT EXISTS "movie_info"(
            "Title" TEXT NOT NULL,
            "Review_Score" INTEGER NOT NULL,
            "Genre_Id" INTEGER NOT NULL,
            "Rating" REAL NOT NULL,
            FOREIGN KEY(Genre_Id) REFERENCES Genre(Id)
        )
        '''


    create_genre_sql = '''
        CREATE TABLE IF NOT EXISTS 'Genre' (
            "Id" INTEGER PRIMARY KEY AUTOINCREMENT,
            "Genre" TEXT NOT NULL
            )
        '''

    cur.execute(create_movies_sql)
    cur.execute(create_genre_sql)
    conn.commit()
    conn.close()

def load_movies(movie_results):
    
    select_genre_id = '''
        Select Id from Genre
        WHERE Genre = ? 
    '''

    insert_movie_sql = '''
        INSERT INTO Movie_Info
        Values (NULL, ?, ?, ?, ?, ?)
    '''

    conn = sqlite3.connect('final_doc.sqlite3')
    cur = conn.cursor()
    for row in movie_results:
        #get genre id
        cur.execute(select_genre_id, [row[2]])
        res = cur.fetchone()
        genre_Id = None
        if res is not None: 
            genre_Id = res[0]
        pass    

    cur.execute(insert_movie_sql, [
        row[0], #title
        row[1], #review_score
        genre_Id,
        row[4] #rating
    ])
    conn.commit()
    conn.close()
    
def load_genre():
    file_contents = open('genre.csv', 'r')
    csv_reader = csv.reader(file_contents)
    next(csv_reader)

    insert_genre_sql = '''
        INSERT INTO GENRE
        VALUES (NULL, ?)
    '''
    
    conn = sqlite3.connect('final_doc.sqlite3')
    cur = conn.cursor()
    for c in csv_reader:
        cur.execute(insert_genre_sql,
           c['Genre']
        )
    conn.commit()
    conn.close()

#print(question())


if __name__ == "__main__":
    movie_links = final_doc.get_top_movie_links()
    movie_results = final_doc.get_movie(movie_links)
    
    create_db()
    load_genre()
