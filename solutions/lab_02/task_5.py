import sys
import tracemalloc

#Часть 1
a = []
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
d = 'abcdefghij'
e = 1
f = None
print(sys.getsizeof(a), ' - Пустой список')
print(sys.getsizeof(b), ' - Список из десяти целых чисел')
print(sys.getsizeof(c), ' - Кортеж с теми же значениями')
print(sys.getsizeof(d), ' - Строка из десяти символов')
print(sys.getsizeof(e), ' - Целое число')
print(sys.getsizeof(f), ' - Объект None')

print('\n---------------------------------------------------------------\n')

#Часть 2
x = []
last = sys.getsizeof(x)
for i in range(100):
    x.append(i)
    if (last != sys.getsizeof(x)):
        last = sys.getsizeof(x)
        print(len(x), last)

print('\n---------------------------------------------------------------\n')

#Часть 3

tracemalloc.start()
numbers = list(range(100_000))
current, peak = tracemalloc.get_traced_memory()
current_mb = current / 1024
peak_mb = peak / 1024
print(f"Текущая (общая) память: {current_mb:.2f} KB")
print(f"Пиковая память: {peak_mb:.2f} KB")
tracemalloc.stop()

print()

tracemalloc.start()
numbers = range(100_000)
current, peak = tracemalloc.get_traced_memory()
current_mb = current / 1024
peak_mb = peak / 1024
print(f"Текущая (общая) память: {current_mb:.2f} KB")
print(f"Пиковая память: {peak_mb:.2f} KB")
tracemalloc.stop()

print('\n---------------------------------------------------------------\n')

#Практическая задача

def measure(name, factory, n=100_000):
    tracemalloc.start()
    obj = factory(n)
    current, peak = tracemalloc.get_traced_memory()
    size = sys.getsizeof(obj)
    tracemalloc.stop()
    return {
        "Название сценария": name,
        "Число элементов": n,
        "Размер внешнего объекта": size,
        "Текущий объем выделенной памяти": current / 1024,
        "Пиковый объем выделенной памяти": peak / 1024,
    }

results = [
    measure("list()", lambda n: list(range(n))),
    measure("tuple()", lambda n: tuple(range(n))),
]

for result in results:
    print(
        f"Название сценария: {result['Название сценария']}\n"
        f"Число элементов: {result['Число элементов']}\n"
        f"Размер внешнего объекта: {result['Размер внешнего объекта']} B\n"
        f"Текущий объем выделенной памяти: {result['Текущий объем выделенной памяти']:.2f} KB\n"
        f"Пиковый объем выделенной памяти: {result['Пиковый объем выделенной памяти']:.2f} KB\n"
    )

if results[1]["Пиковый объем выделенной памяти"] > 0:
    print("Отношение пиков list/range:",
          f"{results[0]['Пиковый объем выделенной памяти'] / results[1]['Пиковый объем выделенной памяти']:.2f}")