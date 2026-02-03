import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)

search = input("search: ")

for movie in data:
    if search in movie["title"]:
        print(movie["title"])