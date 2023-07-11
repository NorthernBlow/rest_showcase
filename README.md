# rest_showcase
online showcase with basic implementation of REST architecture using Django Rest Framework



Перед запуском проекта установить зависимости:

``` pip install -r requirements.txt```

Для запуска приложения сгенерировать секретный ключ в джанго-консоли 

```python
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
```

полученный результат поместить в переменную SECRET_KEY в файле core/core/settings/.env
