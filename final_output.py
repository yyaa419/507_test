import json
from bs4 import BeautifulSoup
import requests

final_movie_list=json.load(open("final_movie_list.json"))
sorted_movie_list=sorted(final_movie_list, key=lambda k: k['popularity'], reverse=True)
# print(sorted_movie_list)
print("movie number:",len(sorted_movie_list))
movie_count=0
for movie in sorted_movie_list:
    movie_name=movie["title"]
    movie_name_processed=movie_name.replace(" ","%20")
    rotten_tomatoes_url=f"https://www.rottentomatoes.com/search?search={movie_name_processed}"
    response = requests.get(rotten_tomatoes_url)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(rotten_tomatoes_url)
    movie_divs=soup.find("div", { "id" :"search-results"})
    movie_div=movie_divs.find("search-page-result",{"type":"movie"})
    movie_info=movie_div.find("search-page-media-row")
    score=movie_info["tomatometerscore"]
    print(movie_name, ":", movie["popularity"], score)
    movie_count+=1

# rotten_tomatoes_url="https://www.rottentomatoes.com/search?search=Trolls%20Band%20Together"
# response = requests.get(rotten_tomatoes_url)
# soup = BeautifulSoup(response.text, "html.parser")
# movie_div=soup.find("div", { "id" :"search-results"})
# movie=movie_div.find("search-page-result",{"type":"movie"})
# movie_info=movie.find("search-page-media-row")
# score=movie_info["tomatometerscore"]
# print(score)