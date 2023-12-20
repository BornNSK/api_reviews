# api_reviews
### Описание

Проект Reviews собирает отзывы пользователей на произведения («Книги», «Фильмы», «Музыка»)

### Стек:
- Python 3.7.0
- Django 3.2
- DRF 3.12.4
- Nginx
- docker-compose


### Как запустить проект:

Клонировать проект из репозитория:

- git
- docker

```
git clone https://github.com/BornNSK/api_reviews

docker pull bornnsk/api_reviews
```

Перейти в папку infra и запустить docker-compose.yaml
(при запущенном Docker)

```
cd api_reviews/infra

docker-compose up
```

Для новой сборки контейнеров выполнять команду:
```
docker-compose up -d --build
```

Командля для выполнения миграции в контейнере web:

```
docker-compose exec web python manage.py migrate
```

Создать суперпользователя:

```
docker-compose exec web python manage.py createsuperuser
```

Собрать резервную копию базы данных:

```
docker-compose exec web python manage.py dumpdata > fixtures.json
```

Проверьте работоспособность приложения, для этого перейдите на страницу:

```
 http://localhost/admin/
```

Документация по API в формате Redoc:

``` 
http://127.0.0.1:8000/redoc/
``` 

##
Авторы:

Гриценко vkontaktensk@yandex.ru
Евсюков Bornki11@yandex.ru
Sunduyool ssedu.s@yandex.ru
