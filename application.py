
from flask import Flask, render_template
import sqlite3


app = Flask(__name__)

def get_movie_by_rating():
    conn = sqlite3.connect('final_doc.sqlite3')
    cur = conn.cursor()
    q = '''
        SELECT Title, Rating
        FROM movie_info
        ORDER BY Rating DESC
    '''
    results = cur.execute(q).fetchall()
    conn.close()
    return results

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies/<sort>')
def movie(sort):
    results = get_movie_by_rating()
    return render_template('results.html', 
        sort=sort, results=results)


if __name__ == '__main__':
    app.run(debug=True)