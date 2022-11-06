""" Defines the repository storing accounts"""
import sqlite3
from film_lib.film import Film, Genre, Rating, Year

SQLITE_DATABASE = "./film_repository_db.sqlite"
TABLE = "films"
COLUMN_DEF = (
    "title TEXT, release_year INTEGER, genre BLOB, rating INTEGER, film_id INTEGER PRIMARY KEY"
)
COLUMNS = "title, release_year, genre, rating, film_id"


class Repository:
    """Repository class connecting to SQLite DB"""

    @staticmethod
    def _construct_film(film_db_string):
        """static method for constructing Film object from a film's db string"""
        title = film_db_string[0]
        release_year = Year(film_db_string[1])
        genres = [Genre(genre) for genre in film_db_string[2].split("|")]
        rating = Rating(film_db_string[3])
        film_id = film_db_string[4]
        return Film(title, release_year, genres, rating, film_id)

    def __init__(self) -> None:
        connection = None
        connection = sqlite3.connect(SQLITE_DATABASE)
        cursor = connection.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE} ({COLUMN_DEF})")
        self._cursor = cursor
        self._db = connection
        self._available_id = self._get_available_id()

    def _get_available_id(self) -> int:
        """finds the highest assigned primary key value"""
        max_id = self._cursor.execute(f"SELECT MAX(film_id) from {TABLE}").fetchone()[0]
        match max_id:
            case int():
                return (max_id + 1)
            case other:
                return 0

    @property
    def available_id(self):
        db_id = self._available_id
        self._available_id += 1
        return db_id

    def save_film(self, film: Film) -> None:
        """Saves (or updates existing) Film object to the db."""
        sql_query = (
            f"INSERT OR REPLACE INTO {TABLE}"
            f"({COLUMNS})"
            f"VALUES('{film.title}', '{film.release_year}', '{film.genres}', '{film.rating}', '{film.film_id}')"
        )
        self._cursor.execute(sql_query)

    def get_film(self, film_id: int) -> Film | None:
        """returns Account object for given account id, or None"""
        sql_query = f"SELECT {COLUMNS} FROM {TABLE} WHERE film_id = {film_id}"
        found_film = self._cursor.execute(sql_query).fetchone()
        if found_film:
            return self._construct_film(found_film)
        return None

    def get_films(self) -> list[Film]:
        """retrieves all films stored in db"""
        sql_query = f"SELECT {COLUMNS} FROM {TABLE}"
        self._cursor.execute(sql_query)
        films = self._cursor.fetchall()
        return [self._construct_film(film) for film in films]

    def __del__(self) -> None:
        self._cursor.close()
        self._db.commit()
        self._db.close()
