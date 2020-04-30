# final-project

To successfully see results picked for the top 10 movies from the IMDb website you must follow these steps. 
First, you will need the final_doc.py to cache all of the top 10 movies from the website. From there you will get the following information:
        - title
        - genre
        - rating
        - review score
Once these four things are gathered about each movie you will then see the database.py file. This file will allow two table to be created (genre_id and movie_info). These tables will load in the information about the Top 10 movies into the movie_info table. Then an additional table called genre_id so that each movie will be given a genre id based from the genres there are. 

For the visuals:
First the extables.py file will show a table with every genre included inside of it and its id number. In order for this to happen a template called table.hmtl was created to so that the genres would display. 
Then, the next webpage will show each movie and their ratings. This webpage will be created using the application.py file. In order for this to correctly work, the index.html and the results.html file needed to be created. 
Lastly, the graph to visually display how many movies are in each genre is displayed in the graph.py file. 

If you follow along to these instructions, the html files are already created for you so that all the user needs to do is run the python files. 