# completed-forms
Web-приложение для определения заполненных форм.

Стек: FastApi, MongoDB

# Запуск проекта без docker

### Подготовка виртуального окружения
```
pip install pipenv #если ранее не установлен
pipenv sync 
pipenv shell
```
### Запуск приложения
Запуск бд MongoDB
```
sudo docker run -d -p 27017:27017 -v ~/mongodb_data:/data/db mongo
```
Запуск FastApi сервера
```
uvicorn main:app --reload
```

# Запуск проекта с docker
```
docker-compose up --build
```

# API
После запуска проекта API будет доступно по адресу
<br>http://127.0.0.1:8000/docs/ 
<br>либо 
<br>http://127.0.0.1:8000/redoc

Пример запроса на определение формы:
```
http://127.0.0.1:8000/get_form?user_name=John&user_email=a_1@gmail.ru&user_password=123qwerty
```

# Дополнительно
Доступен post запрос 

```
/add_template?f_name=f_valie&
```

Этот запрос реализован для удобства добавления шаблонов форм в процессе разработки и никак не тестировался. Имя формируется из названия полей f_name