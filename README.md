# Модуль логгирования

Модуль логгирования создан для повторного использования в различных проектах.


## Установка

1. Клонировать репозиторий:
```
git clone https://github.com/ArkJzzz/my_logger.git
```

2. Установить зависимости: 
```
pip3 install -r requirements.txt

```


## Использование

Импортируйте модуль:
```
from my_logger import get_logger
```

Создайте диспетчер журналирования:
```
logger = get_logger('App name')
```

Далее используйте этот диспетчер как обычно:
```
logger.debug("This is a DEBUG message")
logger.info("INFO message")
logger.warning("WARNING message")
logger.error("An ERROR has happened!")
logger.critical("CRITICAL message")
```

## Результат выполнения
```
2019-Sep-24 16:13:00 (UTC) App name - main:6 - This is a DEBUG message
2019-Sep-24 16:13:00 (UTC) App name - main:7 - INFO message
2019-Sep-24 16:13:00 (UTC) App name - main:8 - WARNING message
2019-Sep-24 16:13:00 (UTC) App name - main:9 - An ERROR has happened!
2019-Sep-24 16:13:00 (UTC) App name - main:10 - CRITICAL message
```

так же появится файл `logfile.log`:
```
2019-Sep-24 16:13:00 (UTC) App name - main:7 - INFO message
2019-Sep-24 16:13:00 (UTC) App name - main:8 - WARNING message
2019-Sep-24 16:13:00 (UTC) App name - main:9 - An ERROR has happened!
2019-Sep-24 16:13:00 (UTC) App name - main:10 - CRITICAL message
```





 