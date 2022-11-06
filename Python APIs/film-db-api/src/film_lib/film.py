import json
import enum
# from film_lib.film_enums import Genre, Rating


class Genre(str, enum.Enum):
    ACTION = "action"
    SCIFI = "scifi"
    SPY = "spy"
    THRILLER = "thriller"
    HORROR = "horror"
    ROMANCE = "romance"
    WESTERN = "western"


class Rating(int, enum.Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    def encode(self):
        return int(self.value)


class Year:
    def __init__(self, year: int) -> None:
        MINYEAR = 1
        MAXYEAR = 9999
        if not (MINYEAR <= year <= MAXYEAR):
            raise ValueError("Year value %d is not a value year." % year)
        self._year = year

    @property
    def year(self) -> int:
        return self._year

    def encode(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return str(self.year)

    def __repr__(self) -> str:
        return str(self.year)


class Film:
    def __init__(
        self, title: str, release_year: Year, genre: list[Genre], rating: Rating, film_id: int
    ) -> None:
        self._title = title
        self._release_year = release_year
        self._genre = genre
        self._rating = rating
        self._film_id = film_id

    @property
    def title(self) -> str:
        return self._title

    @property
    def release_year(self) -> Year:
        return self._release_year

    @property
    def genres(self) -> list[Genre]:
        return '|'.join([genre.value for genre in self._genre])

    @property
    def rating(self) -> Rating:
        return self._rating.value

    @rating.setter
    def rating(self, new_rating: Rating):
        self._rating = new_rating

    @property
    def film_id(self):
        return self._film_id

    def add_genre(self, new_genre: Genre):
        self._genre.append(new_genre)

    def to_json(self):
        dict = {
            "title": self.title,
            "release_year": self.release_year.encode(),
            "genre": self.genres,
            "rating": self.rating,
            "film_id": self.film_id
        }
        return json.dumps(dict)

    def __str__(self) -> str:
        return f"Film(id:{self.film_id}--{self.release_year}--{self.title})"

    def __repr__(self) -> str:
        return f"Film(id:{self.film_id}--{self.release_year}--{self.title})"


if __name__ == '__main__':
    some_movie = Film("A View to a Kill", Year(1985), [Genre.SPY], Rating.FOUR, 1)
    print(some_movie.genres)
    print(some_movie.rating)
    print(some_movie.to_json())
    some_movie.rating = Rating.FIVE
    print(some_movie.add_genre(Genre.THRILLER))
    print(some_movie.genres)
    print(some_movie.to_json())
