#experiment A
a = 10
b = a

print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))

print('\n------------------------------------------------------------\n')

#experiment B
first = [10, 20]
second = first

print(first, second)
print(id(first), id(second))

second.append(30)

print(first, second)
print(id(first), id(second))

first = [10, 20]
second = [10, 20]
print(first == second, first is second)
print(id(first), id(second))
second.append(50)
print(first, second)

print('\n--------------------------------------------------------------------\n')

#Практическая задача

import copy

config1 = {
    "name": "Учебный проект",
    "participants": ["Глеб", "Аким"],
    "par": [[1], [2]]
}
config2 = config1

config2["participants"].append("Саня")
print("После изменения через alias:")
print(config1)
print(config2)
assert config1["participants"] == config2["participants"]

config3 = copy.deepcopy(config1)
config3["participants"].append("Виктор")
config3["par"].append([3])

assert "Виктор" not in config1["participants"]
assert [3] not in config1["par"]
print("\nНезависимая конфигурация:")
print(config1)
print(config3)

