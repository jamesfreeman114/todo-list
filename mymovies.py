#Initialize an empty movies list.
favorite_movies = []

#function to add a movie.
def add_movie(movie):
    favorite_movies.append(movie)
    print(f"Movie '{movie}' added.")

#function to remove a movie.
def remove_movie(movie):
    if movie in favorite_movies:
        favorite_movies.remove(movie)
        print(f"Favorite movie '{movie}' removed.")
    else:
        print(f"Movie '{movie}' not found.") 

#function to display the movies in the list.
def display_movies():
    print(f"My Favorite Movies:")
    for movie in favorite_movies:
        print(f" - {movie}")

def count_movies():
    print(f"Number of movies: {len(favorite_movies)}")

def find_movie(movie):
    if movie in favorite_movies:
        print(f"Favorite movie '{movie}' found.")
    else:
        print(f"Movie '{movie}' not found.")

def clear_movies():
        favorite_movies.clear()
        print("All movies deleted.")


#Adding movies
add_movie("Goodfellas")
add_movie("There Will Be Blood")
add_movie("American Psycho")

display_movies()

count_movies()

remove_movie("American Psycho")

display_movies()

count_movies()

find_movie("Goodfellas")
find_movie("American Psycho")

clear_movies()

display_movies()

count_movies()