Проект API интернет-магазина с использованием SwaggerUI 

Перед запуском проекта установить зависимости:

``` pip install -r requirements.txt```

Для запуска приложения сгенерировать секретный ключ в джанго-консоли 

```python
import sys
from django.core.management.utils import get_random_secret_key

with open('core/core/settings/.env', 'a') as f:
   sys.stdout.write(f'SECRET_KEY={get_random_secret_key()}n')
```

для генерации schema.yml:
```shell
python core/manage.py spectacular --file schema.yml
```


пример работы с API для вывода всех категорий с подкатегориями:

```shell
curl -X 'GET' 'http://127.0.0.1:8000/api/v1/categorylist/'
```

пример работы с API для вывода всех товаров:

```shell
curl -X 'GET' 'http://127.0.0.1:8000/api/product/'
```

и с пагинацией:

```shell
http://127.0.0.1:8000/api/product/?page=1&page_size=1
```



для просмотра более подробной документации по API в SwaggerUI: 

```
http://127.0.0.1:8000/api/shema/docs/
```