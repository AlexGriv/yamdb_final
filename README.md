[![CI Actions Status](https://github.com/AlexGriv/yamdb_final/workflows/CI/badge.svg)](https://github.com/AlexGriv/yamdb_final/actions)
# Групповой проект Api_YaMDb запакованный в docker'е.
Проверка:
```
зайти на http://localhost/admin/
```
Документация по проекту доступна по адресу 'http://51.250.22.224/redoc/'
```
Пример POST-запроса:

POST .../api/v1/titles/


## Описание
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». 
В каждой категории есть произведения: книги, фильмы или музыка.
Произведению может быть присвоен жанр из списка предустановленных. Список категорий или жанров может быть расширен только администратором.
Пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти; из пользовательских оценок формируется усреднённая оценка произведения — рейтинг. 

## Технологии
* Python
* Django
* Django REST Framework
* Simple JWT
* django-filter
* Docker

## Как запустить проект
Клонировать репозиторий:
```
https://github.com/AlexGriv/infra_sp2.git
```
Проверьте разрешения доступа к папке Docker'у:
```
Open Docker and follow this -> settings ->Resources ->
FileSharing. Add required folder and hit Apply & Restart
```
Собрать и запустить:
```
docker-compose up -d --build из папки ./infra
```
Выполните по очереди команды:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```
Проверка:
```
зайти на http://localhost/admin/
```
Документация по проекту доступна по адресу 'http://51.250.22.224/redoc/'
```
Шаблон наполнения env-файла:
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
SECRET_KEY = ''
ALLOWED_HOSTS=example.com


## Регистрация новых пользователей

* Пользователь отправляет POST-запрос с параметрами email и username на эндпоинт '/api/v1/auth/signup/'
* Сервис YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на указанный адрес email
* Пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт '/api/v1/auth/token/', в ответе на запрос ему приходит token (JWT-токен)

## Пример POST-запроса:

GET .../api/v1/titles/
```
{
    "name": "string",
    "year": 0,
    "description": "string",
    "genre": [
        "string"
    ],
    "category": "string"
}
```
Пример ответа:
```
{
    "id": 0,
    "name": "string",
    "year": 0,
    "rating": 0,
    "description": "string",
    "genre": [
        {
        "name": "string",
        "slug": "string"
        }
    ],
    "category": {
        "name": "string",
        "slug": "string"
    }
}
```

## Над проектом работала команда студентов Яндекс.Практикума:
* Александр
* Шухрат
* Анна