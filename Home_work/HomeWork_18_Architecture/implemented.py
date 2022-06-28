# файл для создания DAO и сервисов чтобы импортировать их везде
from HomeWork_18_Architecture.application.dao.directors import DirectorDAO
from HomeWork_18_Architecture.application.dao.genres import GenreDAO
from HomeWork_18_Architecture.application.dao.movies import MovieDAO
from HomeWork_18_Architecture.application.service.directors import DirectorService
from HomeWork_18_Architecture.application.service.genres import GenreService
from HomeWork_18_Architecture.application.service.movies import MovieService
from HomeWork_18_Architecture.setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)