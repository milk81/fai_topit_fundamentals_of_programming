import gc
import sys
import tracemalloc


def measure_scenario(scenario_name, item_count, setup_func):
    gc.collect()
    tracemalloc.clear_traces()
    tracemalloc.start()

    container = setup_func(item_count)

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    outer_size = sys.getsizeof(container)

    return {
        "name": scenario_name,
        "count": item_count,
        "outer_size": outer_size,
        "current_mem": current,
        "peak_mem": peak,
    }


def main():
    N = 100_000

    def create_list(n):
        return [i for i in range(n)]

    def create_tuple(n):
        return tuple(i for i in range(n))

    def create_wrong_matrix(n):
        return [[0] * 10] * (n // 10)

    def create_correct_matrix(n):
        return [[0] * 10 for _ in range(n // 10)]

    def create_strong_refs(n):
        class Record:

            def __init__(self, val):
                self.val = val

        return [Record(i) for i in range(n)]

    def create_cyclic_refs(n):
        class CyclicNode:

            def __init__(self):
                self.self_ref = self

        return [CyclicNode() for _ in range(n)]

    results = []

    results.append(measure_scenario("Динамический список (List)", N, create_list))
    results.append(measure_scenario("Фиксированный кортеж (Tuple)", N, create_tuple))

    results.append(
        measure_scenario("Ошибочная матрица (Ссылки)", N, create_wrong_matrix)
    )
    results.append(
        measure_scenario("Корректная матрица (Объекты)", N, create_correct_matrix)
    )

    results.append(
        measure_scenario("Линейные сильные ссылки", N, create_strong_refs)
    )
    results.append(
        measure_scenario("Изолированные циклы (Циклические)", N, create_cyclic_refs)
    )

    comparison_pairs = [(0, 1), (2, 3), (4, 5)]
    ratios = {}
    for idx1, idx2 in comparison_pairs:
        p1 = results[idx1]["peak_mem"]
        p2 = results[idx2]["peak_mem"]
        ratio = p2 / p1 if p1 > 0 else 1.0
        ratios[(idx1, idx2)] = ratio

    print("=" * 110)
    print(
        f"{'Название сценария':<35} | {'Элементов':<10} | {'Размер объекта':<15} | {'Текущая RAM':<15} | {'Пиковая RAM':<15}"
    )
    print("=" * 110)

    for i, res in enumerate(results):
        print(
            f"{res['name']:<35} | {res['count']:<10,} | {res['outer_size']:<10} байт | {res['current_mem']:<10} байт | {res['peak_mem']:<10} байт"
        )

        if i == 1:
            print(
                f"   --> Отношение пикового объема (Tuple / List): {ratios[(0, 1)]:.4f}"
            )
            print("-" * 110)
        elif i == 3:
            print(
                f"   --> Отношение пикового объема (Correct / Wrong): {ratios[(2, 3)]:.4f}"
            )
            print("-" * 110)
        elif i == 5:
            print(
                f"   --> Отношение пикового объема (Cyclic / Linear): {ratios[(4, 5)]:.4f}"
            )

    print("=" * 110)


if __name__ == "__main__":
    main()
