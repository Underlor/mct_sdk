# MCT Python SDK 
https://mc-t.ru/api_info/ - документация

### Установка:
pip install mct-sdk

### Пример использования:

```pythonstub
from mct_sdk.client import MctClient

client = MctClient('Your key')
client.get_votes(30)

# Response example
# {'data': {'votes': 999}, 'error': '', 'status': 'ok'}
```
#### 

Больше примеров работы можно найти в документации