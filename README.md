# t-invest

## Клонирование репозиттория

- Скопировать HTTPS ссылку в Code
<img width="100" alt="Снимок экрана 2025-03-16 в 12 00 48" src="https://github.com/user-attachments/assets/e348e8f6-d330-4b3c-ae62-116377e34382" />

- В [Git cmd](https://git-scm.com/downloads) перейти в любую папку и выполнить команду
```commandline
cd PATH_TO_FOLDER

git clone https://...
```
- Репозиторий склонирован и можно приступать к разработке

## Настройка проекта

### Установка зависимостей

```commandline
pip install -r requirements.txt
```

### .env
Нужно добавить файл __.env__ для хранения токена и режима работы 
Доступ к этим переменным идет через файл __config.py__
```py
# .env

TOKEN="tinkoff_token"

ENV="dev или production"
```
__.env__ записан в __.gitignore__, поэьтому он не попадет в репозиторий. 

##  Ссылки
- [Про git](https://habr.com/ru/articles/541258/)
