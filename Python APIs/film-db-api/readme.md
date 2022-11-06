# Requirements
Requirements can be installed via conda from project's root dir:
```sh
conda env create -f ./environment.yml
```

# Running
## Starting Server
From the `/src` project directory run
```sh
uvicorn main:app --reload
```
This will start the server on `http://localhost:8000`

## Calling Endpoints
Command-line examples provided below for `GET` and `POST` methods.

### `POST`
```powershell
>_ Invoke-RestMethod -Method POST -Uri "http://localhost:8000/api/v1/films/" -Headers @{"Content-Type"="application/json"} -Body '{"title": "A View to a Kill", "release_year": "1985", "genre": ["spy"], "rating": 4}'
```
```sh
$ curl -X 'POST' -H "Content-Type: application/json" -d '{"title": "A View to a Kill", "release_year": "1985", "genre": "spy", "rating": 4}' "http://localhost:8000/api/v1/films/"
```

### `GET`
```powershell
>_ Invoke-RestMethod -Method GET -Uri "http://localhost:8000/api/v1/$endpoint/" -Headers @{"Content-Type"="application/json"}
```
```sh
$ curl -X 'GET' -H "Content-Type: application/json" "http://localhost:8000/api/v1/$endpoint/"
```
