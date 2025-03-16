# t-invest

## Клонирование репозиттория

- Скопировать HTTPS ссылку в <button type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-c50BI" data-loading="false" data-size="medium" data-variant="primary" aria-describedby=":R55ab:-loading-announcement" id=":R55ab:"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-HKbr-"><span data-component="leadingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="hide-sm" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; vertical-align: text-bottom; overflow: visible;"><path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path></svg></span><span data-component="text" class="prc-Button-Label-pTQ3x">Code</span><span data-component="trailingVisual" class="prc-Button-Visual-2epfX prc-Button-VisualWrap-Db-eB"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display: inline-block; vertical-align: text-bottom; overflow: visible;"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button>
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