import final_doc
import sqlite3
import csv

def create_db():
    conn = sqlite3.connect('final_doc.sqlite3')
    cur = conn.cursor()


    create_movies_sql = '''
        CREATE TABLE IF NOT EXISTS "movie_info"(
            "Title" TEXT,
            "Review_Score" INTEGER,
            "Genre_Id" INTEGER,
            "Rating" REAL,
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
        Values (?, ?, ?, ?)
    '''

    conn = sqlite3.connect('final_doc.sqlite3')
    cur = conn.cursor()
    row_values = []
    #print("movie_results", movie_results)
    
    for row in movie_results:
        row_values.append(row)
    
    cur.execute(select_genre_id, [row_values[2]])
    res = cur.fetchone()
    Genre_Id = None
    if res is not None: 
        Genre_Id = res[0]
    print("row_values", row_values)
    cur.execute(insert_movie_sql, [
        row_values[0], #title
        row_values[1], #review_score
        Genre_Id,
        row_values[3] #rating
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
        print(c)
        cur.execute(insert_genre_sql, [
           c[1]
        ])
    
    conn.commit()
    conn.close()


#print(question())


if __name__ == "__main__":
    movie_links = final_doc.get_top_movie_links()
    movie_results = final_doc.get_movie(movie_links)
    
    create_db()
    load_genre()
    print("first movie results", movie_results)
    load_movies(movie_results)