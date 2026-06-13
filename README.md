# MyShop

Учебный проект интернет-магазина на Django.

## Возможности

* Главная страница сайта
* Каталог товаров
* Страница контактов
* Боковое меню навигации
* Статические файлы (CSS, изображения)
* Шаблоны Django
* Административная панель Django
* Авторизация пользователей

## Структура проекта

```text
myshop/
│
├── config/
│ ├── __init__.py
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ └── wsgi.py
│
├── catalog/
│ ├── migrations/
│ ├── fixtures/
│ │ ├── categories.json
│ │ └── products.json
│ │
│ ├── management/
│ │ └── commands/
│ │ └── load_data.py
│ │
│ ├── templates/
│ │ └── catalog/
│ │ ├── home.html
│ │ └── contacts.html
│ │
│ ├── static/
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
│
├── media/
├── screenshots/
├── .env
├── .env.sample
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

## Установка

Клонируйте репозиторий:

```bash
git clone <repository_url>
cd myshop
```

Создайте виртуальное окружение:

```bash
python -m venv venv
```

macOS

Активируйте виртуальное окружение:

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

## Применение миграций

```bash
python3 manage.py migrate
```

## Создание суперпользователя

```bash
python3 manage.py createsuperuser
```

## Запуск проекта

```bash
python3 manage.py runserver
```

После запуска приложение будет доступно по адресу:

```text
http://127.0.0.1:8000/
```

## Используемые технологии

* Python 3.x
* Django 5.x
* HTML5
* CSS3
* SQLite
* 