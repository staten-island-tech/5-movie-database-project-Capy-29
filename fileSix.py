import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)

genre = input("Genre: ")

for movie in data:
    if genre in movie["genres"]:
        print(movie["title"])