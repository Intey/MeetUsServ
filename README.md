# HOW TO
В спецификации мы указываем имя модуля и имя функции, которые будут
отрабарывать указанный запрос в ключе `operationId`.
К примеру, есть файл `app/api.py`:

    # api.py content
    def get_user(username):
      payload = serialize(store.get_user(usename))
      return payload

С точки зрения Python есть модуль `app`, в нем подмодуль `api` в котором есть
функция `get_user`. Поэтому в спецификации, `operationId`  должен быть:

    operationId: app.api.get_user


