![Workflow badge](https://github.com/petra-khrushcheva/ozon_scraper/actions/workflows/main.yml/badge.svg)

# Парсер маркетплейса

Парсер товаров с сайта  $O_3$ с управлением через FastAPI приложение и получением результатов через телеграм бот. 
Парсинг осуществляется с помощью Selenium и Beautiful Soup.
Информация сохраняется в базу данных PostgresQL.
***
### Технологии
Python 3.11  
FastAPI 0.104  
SQLAlchemy 2.0  
Pydantic 2.5  
Aiogram 3.4  
Alembic 1.13  
Selenium 4.19  
BeautifulSoup 4.12  
PostgreSQL  
***
### Установка
- Клонируйте проект:
```
git clone git@github.com:petra-khrushcheva/ozon_scraper.git
``` 
- Перейдите в директорию ozon_scraper:
```
cd ozon_scraper
``` 
- Создайте и активируйте виртуальное окружение:
```
python3 -m venv venv
source venv/bin/activate
``` 
- Cоздайте переменные окружения по [образцу](https://github.com/petra-khrushcheva/ozon_scraper/blob/main/.env.example).
- Установите зависимости:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
``` 
- Выполните миграции:
```
alembic upgrade head
``` 
- Запустите проект:
```
uvicorn src.main:app
``` 