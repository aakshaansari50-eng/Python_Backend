titles = ["Dangal", "3 Idiots", "Pathaan"]
genres = ["Drama", "Comedy", "Action"]
ratings = [4.8, 4.9, 4.2]

movies = []

for title, genre, rating in zip(titles, genres, ratings):
    movies.append({
        "title": title,
        "genre": genre,
        "rating": rating
    })

print(movies)