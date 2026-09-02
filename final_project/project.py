import json
import os

menu = {
    1: "Add movie",
    2: "View movies",
    3: "Search movies",
    4: "Update movie",
    5: "Delete movie",
    6: "Exit"
}
movie_keys = {
    1: "genre",
    2: "status",
    3: "rating"
}
keys = menu.items()
def main():
    while True:
     for key, value in menu.items():
        print(f"{key}. {value}")
     choice = input("choose an option: ")

     if not choice.isdigit() or int(choice) not in (1,2,3,4,5,6): 
      continue
     elif choice == "6":
      break
     menu_option(choice)




def menu_option(option):
    match option:
      case "1":
        add_movie()
      case "2":
        view_movies()
      case "3":
        search_movie(input("search movie: "))
      case "4":
        movie = input("movie name: ")
        for key, value in movie_keys.items():
          print(f"{key}. {value}")
        update = input("what to update: ")
        update_value = input("which value to put: ")
        update_movie(movie, update, update_value)
      case "5":
        delete_movie(input("delete movie: "))
        


def add_movie():
    title = input("Movie title: ")
    genre = input("Genre: ")
    status = input("Status: ")
    rating = input("Rating: ")
    movie = {
        "title": title,
        "genre": genre,
        "status": status,
        "rating": rating,
    }
    movies = [movie]
    if not os.path.exists("movies.json"):
      with open("movies.json", "w") as file:
        json.dump(movies, file, indent=4)
        print("added")
    else:
     with open("movies.json", "r") as file:
       movies = json.load(file)
     movies.append(movie)
     with open("movies.json", "w") as file:
        json.dump(movies, file, indent=4)
        print("added")


def view_movies():
    with open("movies.json", "r") as file:
      movies = json.load(file)
      for movie in movies:
        for key, value in movie.items():
          print(f"{key}. {value}")

def search_movie(movie_name):
    with open("movies.json", "r") as file:
       movies = json.load(file)
       for movie in movies:
        if movie['title'] == movie_name:
          for key,value in movie.items():
           print(f"{key}. {value}")

def update_movie(movie_name, update, update_value):
    with open("movies.json", "r") as file:
       movies = json.load(file)
       for movie in movies:
        if movie["title"] == movie_name:
            movie[update] = update_value
            with open("movies.json", "w") as writefile:
              json.dump(movies, writefile, indent=4)
              print("updated",movie)

def delete_movie(movie_name):
    with open("movies.json", "r") as file:
       movies = json.load(file)
       for index, movie in enumerate(movies):
        if movie["title"] == movie_name:
           movies.pop(index)
           with open("movies.json", "w") as writefile:
              json.dump(movies, writefile, indent=4)
              print("deleted")




if __name__ == "__main__":
    main()