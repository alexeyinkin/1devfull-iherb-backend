## iHerb -- backend

### Нейронная сеть предупреждения о риске

Находится в `/python-safety`. Используется Python 3.8 и TensorFlow.

Установка на Ubuntu:
```bash
apt install python3-pip
pip3 install tensorflow pyyaml h5py virtualenv gunicorn flask
```

- Входные данные для обучения: `data.tsv`
- Обучение: `python3 fit.py`
- Запуск сервера: `python3 serve.py`

После запуска сервер доступен на порте `5000` и принимает POST-запросы:

```
POST / HTTP/1.1

{"features":[1, 0],"substances":[1, 1, 0]}
```
Здесь:
- `features` -- массив фич пользователя: принадлежности к классам пищевых привычек, пол, возраст, рост, масса, подтверждённые врачом диагнозы и результаты анализов.
- `substances` -- дозировки каждого вещества в одном товаре или в сумме по нескольким.


### Триггер и индекс Firebase для справочника болезней

Находятся в `/firebase`

Триггер используется, чтобы при добавлении или изменении записи проиндексировать её подстроки -- чтобы работал поиск по частичному вводу.

Деплой:

```bash
firebase deploy --only functions
```

Индексы в `firestore.indexes.json` необходимы для поиска. Деплой:
```bash
firebase deploy --only firestore:indexes
```


### Конвертор справочника болезней

Находится в `/conditions-to-json`. Для загрузки в Firebase записи должны быть в JSON, но оригинал справочника доступен в интернете в CSV. Данный скрипт конвертирует данные.

Запуск:
```bash
python3 conditions-to-json.py --tsv FILE [--limit N]
```
