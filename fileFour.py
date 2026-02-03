import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)

year = input("year: ")

for movie in data:
    if movie["year"] == int(year):
        print(movie["title"])