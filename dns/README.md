# DNS Server

Кэширующий DNS сервер. Сервер прослушивает 53 порт. При первом запуске кэш пустой. 
Сервер получает от клиента рекурсивный запрос и выполняет разрешение запроса. 
Получив ответ, сервер разбирает пакет ответа, извлекает из него полезную информацию, 
т. е. все ресурсные записи, а не только то, о чем спрашивал клиент. Полученная информация сохраняется в кэше сервера. 

Сервер регулярно просматривает кэш и удаляет просроченные записи (использует поле TTL). 
При повторных запусках сервер считывает данные с диска и удаляет просроченные записи, инициализирует таким образом свой кэш.

### Необходимые модули: 
dnslib, pickle
### Запуск программы:
python3 server.py
