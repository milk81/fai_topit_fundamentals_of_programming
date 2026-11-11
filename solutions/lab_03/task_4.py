def arithmetic_mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def normalize_name(name: str) -> str:
    if not name.strip():
        return ""
    return " ".join(name.split()).title()


def build_report(student: str, results: list[int], *, precision: int = 2, prefix: str = "Результат", ) -> str:
    student = normalize_name(student)
    if not student or not results or precision < 0:
        return ""
    mean = arithmetic_mean(results)
    return f"{prefix}: {student} — {mean:.{precision}f}"


def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    if not tags:
        return ()
    result = []
    have = set()
    for tag in tags:
        tag = tag.strip()
        if lowercase:
            tag = tag.lower()
        if tag and tag not in have:
            have.add(tag)
            result.append(tag)
    return tuple(result)


assert arithmetic_mean([2.0, 4.0, 6.0]) == 4.0
assert arithmetic_mean([5.0]) == 5.0
assert arithmetic_mean([]) == 0.0

assert normalize_name("  анНА   иВАНОВА ") == "Анна Иванова"
assert normalize_name("БОРИС") == "Борис"
assert normalize_name("   ") == ""

assert build_report("анна", [4, 5]) == "Результат: Анна — 4.50"
assert build_report("борис", [3, 4], precision=1, prefix="Среднее") == "Среднее: Борис — 3.5"
assert build_report("анна", []) == ""
assert build_report(" ", [5]) == ""
assert build_report("анна", [5], precision=-1) == ""

assert collect_tags(" Python ", "python", "", " SQL ") == ("python", "sql")
assert collect_tags("Python", "python", lowercase=False) == ("Python", "python")
assert collect_tags() == ()
assert collect_tags(" ", "") == ()

values = [3.0, 5.0]
original_values = values.copy()
arithmetic_mean(values)
assert values == original_values

results = [4, 5, 5]
original_results = results.copy()
build_report("анна", results)
assert results == original_results

print(arithmetic_mean([2.0, 4.0]))
print(arithmetic_mean(values=[2.0, 4.0]))

print(normalize_name("  анНА иВАНОВА "))
print(normalize_name(name="  боРИС пЕТРОВ "))

print(build_report("анна", results, precision=1))
print(build_report(student="борис", results=[3, 5], prefix="Среднее"))

tags = [" Python ", "SQL", "python"]
print(collect_tags(*tags, lowercase=True))

options = {"precision": 3, "prefix": "Итог"}
print(build_report("анна", results, **options))

arguments = ["дарья", [3, 4, 5]]
print(build_report(*arguments, **options))

print("\n---------------------------------------------------------------\n")

#Исследование LEGB
course = "Python"

def f():
    course = "C++"

    def g():
        nonlocal course
        course += " курс"
        return course

    return g()

print(f())
print(course)

print('\n--------------------------------------------------------\n')

#Ошибка изменяемого значения по умолчанию
## Ошибочный вариант
def add_result(value, results=[]):
    results.append(value)
    return results

print(add_result(0))
print(add_result(1))

## Корректный вариант
def add_result(value, results=None):
    if results is None:
        results = []

    results.append(value)
    return results

print(add_result(0))
print(add_result(1))

print('\n--------------------------------------------------------\n')

#Практическое расширение
def apply_to_results(operation, values):
    result = []
    for value in values:
        result.append(operation(value))
    return result

def add(value):
    return value + 1

def make_threshold_checker(threshold):
    def check(value):
        return value >= threshold

    return check


values = [1, 2, 3]

print(apply_to_results(add, values))
print(apply_to_results(lambda value: value * 2, values))

check1 = make_threshold_checker(6)
check2 = make_threshold_checker(7)

print(apply_to_results(check1, values))
print(apply_to_results(check2, values))

assert check1(9) is True
assert check2(3) is False
assert values == [1, 2, 3]