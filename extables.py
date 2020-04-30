from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('table.html')


@app.route('/movies/<sort>')
def bars(sort):
    return render_template('results.html', 
        sort=sort)


if __name__ == '__main__':
    app.run(debug=True)