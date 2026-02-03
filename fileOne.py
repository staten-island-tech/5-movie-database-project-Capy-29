import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)

for movie in data:
    print(movie["title"])