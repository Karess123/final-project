#################################
##### Name: karess taylor 
##### Uniqname: tkaress 
#################################

from bs4 import BeautifulSoup
import requests
import json

base_url = 'https://www.imdb.com'
CACHE_FILE_NAME = 'cache.json'
CACHE_DICT = {}

def load_cache():
    """opens cache file and loads json into cache_dict dictionary, if it exists 
    parameters:
    --------
    none 
    return:
    -------
    the opened cache: dict 
    """
    try:
        #print(CACHE_FILE_NAME)
        cache_file = open(CACHE_FILE_NAME, 'r')
        cache_file_contents = cache_file.read()
        cache = json.loads(cache_file_contents)
        cache_file.close()
    except:
        cache = {}
    return cache


def save_cache(cache):
    """saves the current cache
    parameters:
    --------
    none
    return:
    --------
    none 
    """
    contents_to_write = json.dumps(cache)
    cache_file = open(CACHE_FILE_NAME, 'w')
    cache_file.write(contents_to_write)
    cache_file.close()


def make_url_request_using_cache(url, cache):
    ''' searches through cache, if url not found then it makes request to url
    parameters:
    -----
    url:
        str (the url)
    cache: 
        dict (used for search)
    return:
    ------
        dict (data returned from making request)
    '''
    #print(CACHE_DICT.keys())
    #print(url, url in CACHE_DICT.keys())
    if url in CACHE_DICT.keys():
        print("Using cache")
        return CACHE_DICT[url]
    else:
        print("Fetching")
        response = requests.get(url)
        CACHE_DICT[url] = response.text
        save_cache(CACHE_DICT)
        return CACHE_DICT[url]

class TopMovies:                            
    """ Media within IMDb site
    Attributes 
    ----------
    title: str
        title of the media
    director: str
        author of the media 
    release_year: str
        year media was released
    url: str
        web address to other media info
    json: dict
        parsed dictionary used in the media class
    """                                                                            

    def __init__(self, title="No Title", release_year="No Release Year", genre="No Genre",  director="No Director", rating="No Rating",  review_score=""): 
            self.title = title
            self.release_year = release_year 
            self.director = director
            self.genre = genre
            self.rating = rating
            self.review_score = review_score
            

    def info(self):
        """ Get movie information
        parameters:
        -------
        none
        retruns:
        ---------
        str: info about the movies 
        """
        return f'{self.title}, {self.release_year}, {self.director}, {self.genre}, {self.rating}, {self.review_score}.'
        


def get_top_movie_links():
    #request w cache function to get top movies
    #parse top movie page with beautiful soup to get all the moviel links 
    links_path = '/chart/top'
    top_movie = base_url + links_path
    CACHE_DICT = load_cache()

    response = make_url_request_using_cache(top_movie, CACHE_DICT)
    soup = BeautifulSoup(response, 'html.parser')

    movie_parent = soup.find_all('td', class_='titleColumn')
    



    movies = {}
    #info = movie_parent.find_all('a')
    for movie in movie_parent[:100]:
        info = movie.find('a')
        #print(info)
        movies[info.text] = 'https://www.imdb.com' + info['href']

    return movies  


def get_movie(movies):
    #request w cache
    #site_url = 
    CACHE_DICT = load_cache()
    movie_info_dict = {'title': [], 'rating': [], 'review_score':[], 'genre': []} 
    for site_url in movies.values():

        response = make_url_request_using_cache(site_url, CACHE_DICT)
        soup = BeautifulSoup(response, 'html.parser')
    
    
        #title r
        title_parent = soup.find('div', class_='title_wrapper')
        title = title_parent.find('h1').contents[0]
        #print(title)
        
        #rating
        rating = soup.find('div', class_='subtext').contents[0].strip()
        
        #review score
        parent = soup.find('div', class_='ratingValue')
        review = parent.find('span', itemprop='ratingValue').contents[0]
        
        #genre    
        p = soup.find('div', class_='subtext')
        g1 = p.find_all('a')[0]
        #genre_link = g1['href']
        genre = g1.text
        #print(genre)
        

        #movie_info = f'({title}, {length}, {rating_p}, {review_o})'
        #{'title':['a','b','c'],'length':[1,None,3]}
        
        movie_info_dict['title'].append(title)
        movie_info_dict['rating'].append(rating)
        movie_info_dict['review_score'].append(review)
        movie_info_dict['genre'].append(genre)

        #print(movie_info_dict)
    return movie_info_dict 


if __name__ == "__main__":
    CACHE_DICT = load_cache()
    movie_links = get_top_movie_links()
    print(get_movie(movie_links))
    
   
    #movie_links = get_top_movie_links()
    #movie = []
    #for link in movie_links:
    #   movie.append(get_movie(link))
    #DB stuff
    #Create Table
    #Inserts
     