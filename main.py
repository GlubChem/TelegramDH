from scripts.extract import extract_from_json
from scripts.analyze import count_connections, drop_connections, make_graph
from scripts.entity_naming import fix_names

print("Введите название файла с данными(без расширения)")
filename = input()
print("Извлекаем данные...")
data = extract_from_json(f"./data/{filename}.json")
print("Переименовываем сущности...")
data = fix_names(data)
print("Считаем соединения...")
connections = count_connections(data)
print("Строим граф...")
connections = drop_connections(connections)
graph = make_graph(connections)
graph.show_buttons()
graph.show(f"./visualizations/{filename}.html")
print(f"Граф сгенерирован в файле \"./visualizations/{filename}.html\"")