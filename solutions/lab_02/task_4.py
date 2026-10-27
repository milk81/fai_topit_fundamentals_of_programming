import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)

print('\n---------------------------------------------------------------\n')

print("Состояние сборщика мусора:", gc.isenabled())
print("Пороги поколений:", gc.get_threshold())
print("Статистика поколений:")
for i, stats in enumerate(gc.get_stats()):
    print(f"Поколение {i}: {stats}")

print('\n---------------------------------------------------------------\n')

print(id(first), id(second), '- id двух списков')
del first, second
p = gc.collect()
print('Количество удаленных объектов:', p)

print('\n---------------------------------------------------------------\n')

#Дополнительный эксперимент
gc.disable()
for i in range(2):
    a = []
    b = []
    a.append(b)
    b.append(a)
    del a, b

print('Количество удаленных объектов:', gc.collect())
gc.enable()

print('\n---------------------------------------------------------------\n')

#Практическая задача

collected_before = gc.collect()

node_A = {"name": "A", "edges": []}
node_B = {"name": "B", "edges": []}
node_C = {"name": "C", "edges": []}
node_D = {"name": "D", "edges": []}

node_A["edges"].append(node_B)
node_B["edges"].append(node_C)
node_C["edges"].append(node_A)

for node in [node_A, node_B, node_C, node_D]:
    edge_names = [edge["name"] for edge in node["edges"]]
    print(f"Узел {node['name']} ссылается на: {edge_names if edge_names else 'нет связей'}")

del node_A
del node_B
del node_C
del node_D

collected_after = gc.collect()

print(f'\nДо {collected_before}')
print(f'После {collected_after}')
print(f'Сравнение до и после {collected_after - collected_before}')