import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)


fyear = input("from: ")
tyear = input("to: ")

for movie in data:
    if movie["year"] > int(fyear) and movie["year"] < int(tyear):
        print(movie["title"])