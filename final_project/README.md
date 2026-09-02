# Movie Tracker

#### Video Demo: https://youtu.be/MbWzrhGdRPE

#### Description:

Movie Tracker is a command-line application written in Python that allows users to manage a personal collection of movies. The application stores movie information in a JSON file, allowing the collection to remain saved after the program is closed.

The program starts by displaying a menu with six options: Add Movie, View Movies, Search Movies, Update Movie, Delete Movie, and Exit.

The Add Movie option allows the user to enter a movie's title, genre, status, and rating. The movie is then saved to `movies.json`. The View Movies option displays all movies currently stored in the collection. The Search Movies option allows the user to search for a movie by its title. The Update Movie option allows the user to change a movie's genre, status, or rating. Finally, the Delete Movie option removes a movie from the collection.

The main application is contained in `project.py`. The `main()` function controls the program's main loop and displays the menu. The `menu_option()` function determines which operation the user selected. The `add_movie()` function adds a movie to the JSON file, while `view_movies()` displays the saved movies. The `search_movie()` function searches for a movie by title. The `update_movie()` function changes information about an existing movie, and the `delete_movie()` function removes a movie from the collection.

Movie data is stored in `movies.json`. I chose JSON because it is simple, human-readable, and can be handled directly using Python's built-in `json` module. The `os` module is also used to check whether the JSON file already exists before attempting to read or write data. Using a JSON file instead of a database keeps the project simple while still providing persistent data storage.

The project includes `test_project.py`, which contains pytest tests for three of the application's functions: `add_movie()`, `view_movies()`, and `update_movie()`. The tests use pytest features such as `capsys` to check program output and `monkeypatch` to provide input during testing. The tests help verify that important parts of the application work as expected.

* `requirements.txt` — Lists the project's external Python dependencies. The application itself uses only Python's standard library.

I designed the project as a command-line application because I wanted to focus on Python fundamentals rather than building a graphical interface. While developing it, I practiced functions, loops, conditionals, dictionaries, lists, user input, file I/O, JSON data handling, exception-aware file operations, and automated testing. The project also gave me experience organizing a small Python program into separate functions instead of putting all of the logic into one large block of code.

To run the application, use:

```bash
python project.py
```

To run the tests, use:

```bash
python -m pytest test_project.py
```

The project files are:

* `project.py` — Contains the Movie Tracker application and its functions.
* `test_project.py` — Contains pytest tests for the application.
* `movies.json` — Stores the movie collection.
* `requirements.txt` — Lists the project's external Python dependencies; none are required.
* `README.md` — Provides information about the project and how to use it.
