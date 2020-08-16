# Covid19-bot
Телеграм-бот, предоставляющий актуальную информацию o заболевших COVID-19 в разных странах (t.me/Virus2020Covid19_bot)
Проект размещен на Heroku.
___________________________________________________
Программа написана на Python с использованием:
- beautifulsoup4 (парсинг данных в формате HTML, XML)
- COVID19Py (доступ к последним данным о случаях заболевания коронавирусом COVID-19)
- python-dotenv (загрузка и считывание переменных окружения из файла .env)
- pyTelegramBotAPI (работа с Телеграм-ботом)

## Как работает программа:
Чат-бот Телеграм обращается к API, которое возвращает актуальную информацию о случаях заболевания вирусом COVID-19 в выбранной стране.

## Как запустить программу:

1) Клонируйте репозитроий с программой:
```
git clone https://github.com/leks20/Covid19-bot
```
2) В созданной директории установите виртуальное окружение, активируйте его и установите необходимые зависимости:
```
python3 -m venv venv

. venv/bin/activate

pip install -r requirements.txt
```
3) Создайте чат-бота Телеграм
4) Создайте в директории файл .env и поместите туда токен в формате teleram_token = 'ххххххххх'
5) Откройте файл main.py и запустите код

### Пример ответа чат-бота:
Выбрать страну -> Россия

Данные по стране:
- Население: 146,745,098
- Последнее обновление: 2020-08-16 14:53:38
- Последние данные:
- Заболевших: 915,808
- Смертей: 15,585




