import sys
import tracemalloc

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
