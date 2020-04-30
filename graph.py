
from flask import Flask, render_template
import sqlite3
import plotly.graph_objects as go

@app.route('/plot')
def plot():
    x_vals = ['Action', 'Drama', 'Crime', 'Adventure', 'Western', 'Biography']
    y_vals = [1, 2, 3, 1, 1, 1]

    movie_data = go.Bar(
        x=x_vals,
        y=y_vals
    )
    fig = go.Figure(data=movie_data)
    div = fig.to_html(full_html=False)
    return render_template("plot.html", plot_div=div)


if __name__ == '__main__':
    app.run(debug=True)