user_genre = input("Enter your preferred movie genre:")
user_rating = float(input("Enter your preferred movie rating (out of 10):"))
user_release_year = int(input("Enter your preferred movie release year:"))

# Sample movie data
movies = [{"Title":"Movie A","Genre":"action","rating": 8.5,"release_year":2010},
          {"Title":"Movie B","Genre":"drama","rating": 7.8,"release_year":2015},
          {"Title":"Movie C","Genre":"comedy","rating": 6.5,"release_year":2020},
          # Add more movies as needed
          ]

recommended_movies = []

for movie in movies:
    if(movie["Genre"] == user_genre
       and movie["rating"] >= user_rating
       and movie["release_year"] >= user_release_year
    ):
        recommended_movies.append(movie["Title"])

if recommended_movies:
    print("\nRecommended Movies:")
    for Title in recommended_movies:
        print(Title)
else:
    print("\nSorry, No movies match your preferences,")