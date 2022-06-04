# TelegramDH
## dh исследование новостных тг каналов


Наш проект позволяет извлечь именнованые сущности(имена, топонимы, названия организаций) и визуализировать их взаимоотношения в виде графа.

Для примера использовались данные из телеграм каналов Медуза, Mash, РИА новости и Варламов News, которые были предварительно выгружены в виде json файла. Затем к ним применялась библиотека Natasha, а точнее NER модель из нее.
Обработка одного канала занимала примерно 10-15 минут. После этого данные были очищены и из них был создан интерактивный граф с использованием библиотеки pyvis.

Структура проекта:
1. data/ – папка для json файлов с сообщениями каналов и файлов с извлеченными сущностями
    1. channelname.json – сообщения канала
    2. channelname_ents.json – сущности выделенные из сообщений
2. visualizations/ – html файлы с визуализациями графов
3. scripts/ – питоновские файлы
    1. aggregate.py – скрипт для объединения данных нескольких каналов
    2. entity_naming.py - 
4. main.py – файл для запуска

Что еще можно сделать:
1. Научиться объединять сущности, которые являются одним и тем же (например Владимир Путин и Путин или Россия и РФ) – частично сделано
2. Подключить telegram api для того чтобы автоматически выгружать каналы
3. Найти другие способы отбирать связи между сущностями, кроме ограничения на количество соединений для одной сущности.
4. Использовать другую библиотеку или написать собственное решение для визуализации, так как pyvis довольно медленный.
