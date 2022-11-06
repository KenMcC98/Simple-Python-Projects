from fastapi import FastAPI
from pydantic import BaseModel
from film_lib.film_repository import Repository
from film_lib.film import Film, Year, Genre, Rating

BASE_API = "/api/v1"

repo = Repository()
app = FastAPI()


class Body(BaseModel):
    title: str
    release_year: str
    genre: list[Genre]
    rating: Rating


@app.post(f"{BASE_API}/films/", status_code=204)
async def add_film(body: Body,):
    request_body = body.dict()
    new_film = Film(
        request_body.get("title", None),
        Year(request_body.get("release_year", None)),
        request_body.get("genre", None),
        request_body.get("rating", None),
        film_id=repo.available_id
    )
    repo.save_film(new_film)


@app.get(f"{BASE_API}/films/")
async def get_films():
    films = repo.get_films()
    return {"films": [film.to_json() for film in films]}


# bond = Film("A View to a Kill", Year(1985), [Genre.SPY], Rating.FOUR, repo.available_id)
# star = Film("Star Trek First Contact", Year(1996), [Genre.SCIFI], Rating.FIVE, repo.available_id)
# repo.save_film(bond)
# repo.save_film(star)
# print(repo.get_films())
