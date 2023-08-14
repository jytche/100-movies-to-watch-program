import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
empire_page = response.text

soup = BeautifulSoup(empire_page, "html.parser")
titles = soup.find_all("h3", class_="title")
movie_list = []

for title in titles:
    movie = title.getText()
    movie_list.append(movie)

movie_list.reverse()

with open("movies.txt", mode="w", encoding="utf8") as file:
    for item in movie_list:
        file.write(item + "\n")

