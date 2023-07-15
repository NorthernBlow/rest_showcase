# rest_showcase
online showcase with basic implementation of REST architecture using Django Rest Framework

Проект API интернет-магазина с использованием SwaggerUI 

Перед запуском проекта установить зависимости:

``` pip install -r requirements.txt```

Для запуска приложения сгенерировать секретный ключ в джанго-консоли 

```python
import sys
from django.core.management.utils import get_random_secret_key

sys.stdout.write(str(get_random_secret_key()))
```

полученный результат поместить в переменную SECRET_KEY в файле core/core/settings/.env

для генерации schema.yml:
```
python core/manage.py spectacular --file schema.yml
```


пример работы с API для вывода всех категорий с подкатегориями:

```
curl -X 'GET' 'http://127.0.0.1:8000/api/v1/categorylist/'
```

пример работы с API для вывода всех товаров:

```
curl -X 'GET' 'http://127.0.0.1:8000/api/product/'
```

и с пагинацией:

```
http://127.0.0.1:8000/api/product/?page=1&page_size=1
```



для просмотра более подробной документации по API в SwaggerUI: 

```
http://127.0.0.1:8000/api/shema/docs/
```