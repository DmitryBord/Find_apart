### Консольная версия парсера
Это парсер, ищет квартиры на Циан по вашим критериям, а именно:
    - Тип сделки(rent/sale)
    - Кол-во комнат
    - Максимальная сумма аренды или покупки

По умолчанию парсит только первые пять страниц, но это можно изменить
в цикле `while pages <= n:`, где n - нужное количество страниц
По итогу создает файл `.xlsx` в корне проекта с записанными квартирами в формате "ссылка - цена"
Файл со всеми нужными библиотеки находятся в materials/