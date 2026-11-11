# Лабораторная работа № 3. Алгоритмы, коллекции и функции

## 1. Общая информация

**Темы курса:**

1. Управление потоком выполнения,
2. Базовые алгоритмы, коллекции,
3. Хеширование, функции и области видимости.

## 2. Цель работы

Научиться переводить условие задачи в алгоритм, выбирать подходящую структуру данных и разделять программу на небольшие
функции с понятными контрактами.

## 3. Планируемые результаты

После выполнения работы студент должен уметь:

- применять условия, циклы и сопоставление с образцом;
- реализовывать поиск, подсчет и накопление;
- работать со списками, кортежами, словарями и множествами;
- выбирать структуру данных с учетом назначения и сложности операций;
- создавать функции с позиционными и именованными параметрами;
- использовать аннотации типов и строки документации;
- объяснять области видимости имен по правилу LEGB;
- декомпозировать прикладную задачу на функции;
- оценивать сложность простых алгоритмов.

## 4. Условия выполнения

1. Используйте Python 3.11 или новее.
2. Разместите решение в директории lab_03.
3. Для заданий 1–4 создайте файлы task_1.py, ..., task_4.py.
4. Интеграционное задание разместите в task_5.py.
5. Ответы, псевдокод, оценки сложности и результаты проверок оформите в REPORT.md.
6. Сторонние библиотеки использовать нельзя.
7. Встроенные функции min(), max(), sum(), sorted() и метод list.count() нельзя применять там, где задание требует
   самостоятельно реализовать соответствующий алгоритм.
8. Для каждого алгоритма подготовьте запускаемый демонстрационный сценарий и проверки ожидаемых результатов.

## Задание 1. Условия и классификация данных

### Часть 1-3

```python
res = int(input())
type = input()
cnt_miss = int(input())

if 0 <= res <= 100 and 0 <= cnt_miss <= 5:
    if cnt_miss > 3:
        res = max(min(60, res), res - 15)
    if res >= 90:
        print('Отличный уровень')
    elif res >= 75:
        print('Хороший уровень')
    elif res >= 60:
        print('Удовлетворительный уровень')
    else:
        print('Недостаточный уровень')

    match type:
        case "exam":
            print('Экзаменационная работа')
        case "project":
            print('Экзаменационная работа')
        case "practice":
            print('Практическая работа')
        case _:
            print('Неизвестное значение')

else:
    print('Некорректные входные данные')
```

### Часть 4. Тестовые сценарии

| №  | Балл `res` | Тип работы `type` | Пропуски `cnt_miss` | Ожидаемый результат                                | Фактический результат                              |
|----|------------|-------------------|---------------------|----------------------------------------------------|----------------------------------------------------|
| 1  | 0          | exam              | 0                   | Недостаточный уровень; Экзаменационная работа      | Недостаточный уровень; Экзаменационная работа      |
| 2  | 59         | exam              | 0                   | Недостаточный уровень; Экзаменационная работа      | Недостаточный уровень; Экзаменационная работа      |
| 3  | 60         | exam              | 0                   | Удовлетворительный уровень; Экзаменационная работа | Удовлетворительный уровень; Экзаменационная работа |
| 4  | 74         | exam              | 0                   | Удовлетворительный уровень; Экзаменационная работа | Удовлетворительный уровень; Экзаменационная работа |
| 5  | 75         | exam              | 0                   | Хороший уровень; Экзаменационная работа            | Хороший уровень; Экзаменационная работа            |
| 6  | 89         | exam              | 0                   | Хороший уровень; Экзаменационная работа            | Хороший уровень; Экзаменационная работа            |
| 7  | 90         | exam              | 0                   | Отличный уровень; Экзаменационная работа           | Отличный уровень; Экзаменационная работа           |
| 8  | 100        | exam              | 0                   | Отличный уровень; Экзаменационная работа           | Отличный уровень; Экзаменационная работа           |
| 9  | 100        | practice          | 3                   | Отличный уровень; Практическая работа              | Отличный уровень; Практическая работа              |
| 10 | 100        | practice          | 4                   | Хороший уровень; Практическая работа               | Хороший уровень; Практическая работа               |
| 11 | 75         | project           | 5                   | Удовлетворительный уровень; Экзаменационная работа | Удовлетворительный уровень; Экзаменационная работа |
| 12 | 59         | other             | 4                   | Недостаточный уровень; Неизвестное значение        | Недостаточный уровень; Неизвестное значение        |
| 13 | -1         | exam              | 0                   | Некорректные входные данные                        | Некорректные входные данные                        |
| 14 | 101        | exam              | 0                   | Некорректные входные данные                        | Некорректные входные данные                        |
| 15 | 60         | exam              | -1                  | Некорректные входные данные                        | Некорректные входные данные                        |

### Практическое расширение

```python
students = [
    (0, "exam", 0),
    (59, "practice", 2),
    (60, "project", 1),
    (74, "exam", 3),
    (75, "practice", 0),
    (89, "project", 2),
    (90, "exam", 0),
    (100, "practice", 3),
    (100, "exam", 4),
    (75, "project", 5),
    (101, "exam", 0),
    (60, "other", 1)
]

results = []
counts = {
    "Отличный уровень": 0,
    "Хороший уровень": 0,
    "Удовлетворительный уровень": 0,
    "Недостаточный уровень": 0
}
invalid = 0

for i, (score, work_type, absences) in enumerate(students, 1):
    if not (0 <= score <= 100 and 0 <= absences <= 5):
        results.append(f"{i}. Некорректные входные данные")
        invalid += 1
        continue

    res = score
    if absences > 3:
        res = max(min(60, res), res - 15)

    if res >= 90:
        level = "Отличный уровень"
    elif res >= 75:
        level = "Хороший уровень"
    elif res >= 60:
        level = "Удовлетворительный уровень"
    else:
        level = "Недостаточный уровень"

    match work_type:
        case "exam":
            work = "Экзаменационная работа"
        case "project":
            work = "Проектная работа"
        case "practice":
            work = "Практическая работа"
        case _:
            work = "Неизвестное значение"

    counts[level] += 1
    results.append(f"{i}. {work}; балл: {res}; {level}")

print("Индивидуальные результаты:")
print("\n".join(results))

print("\nИтоговая сводка:")
for level, count in counts.items():
    print(f"{level}: {count}")
print(f"Некорректные входные данные: {invalid}")
```

## Задание 2. Циклы и базовые алгоритмические схемы

```python
measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]

min = 10 ** 10
max = -min
sum = 0
count_even = 0

# O(n)
for i in measurements:
    if i < min:
        min = i
    elif i > max:
        max = i
    if abs(i) % 2 == 0:
        count_even += 1
    sum += i
print(f'min: {min}')
print(f'max: {max}')
print(f'sum: {sum}')
print(f'count_even: {count_even}')

avg = sum / len(measurements)
count_over_avg = 0

# O(n)
for i in measurements:
    if i > avg:
        count_over_avg += 1

print(f'count_over_avg: {count_over_avg}')

find = int(input())

# O(n)
for i in range(len(measurements)):
    if measurements[i] == find:
        print(f'find_first_index_in: {i}')
        break
else:
    print('find_first_index_in: -1')
```

Результат работы на некоторых примере:

```text
Тест 1:

min: 7
max: 21
sum: 144
count_even: 4
count_over_avg: 6
100
find_first_index_in: -1

Тест 2:

min: 7
max: 21
sum: 144
count_even: 4
count_over_avg: 6
11
find_first_index_in: 2
```

### Дополнительный алгоритмический эксперимент

```python
x = int(input())
if x == 1:
    print('Не простое число')
else:
    i = 2
    # O(n^(0.5))
    while i * i <= x:
        if x % i == 0:
            print('Составное число')
            break
    else:
        print('Простое число')
```

Для алгоритма проверки на простоту.

- Данный алгоритм проверки на простоту работает за $O(\sqrt{n})$.
- От минимального делителя $n$ отличного от $1$.
- Требуется $O(1)$ дополнительной памяти.
- Для каждого делителя $i$ до $\sqrt{n}$, есть еще один делитель $\frac{n}{i}$, который больше или равен $\sqrt{n}$.
  Почему второй делитель больше или равен $\sqrt{n}$, потому что предположим, что он меньше $\sqrt{n}$, тогда при
  перемножении они дадут число меньшее $n$, исключая случай, когда число является квадратом. В таком случае мы точно
  переберем все делители. Если их не найдется значит число простое.

### Практическое расширение

```python
def selection_sort(a):
    for i in range(len(a) - 1):
        p = i
        for j in range(i + 1, len(a)):
            if a[j] < a[p]:
                p = j
        a[i], a[p] = a[p], a[i]
    return a


def linear_search(a, x):
    cnt = 0
    for i in range(len(a)):
        cnt += 1
        if a[i] == x:
            return cnt
    return cnt


def binary_search(a, x):
    l = 0;
    r = len(a) - 1
    cnt = 0
    while r - l > 1:
        m = (l + r) // 2
        cnt += 1
        if a[m] == x:
            return cnt
        if a[m] < x:
            l = m + 1
        else:
            r = m - 1
        cnt += 1
    return cnt


for n in [10, 100, 1000]:
    a = list(range(n - 1, -1, -1))
    selection_sort(a)
    x = n - 1

    c1 = linear_search(a, x)
    c2 = binary_search(a, x)
    print(n, c1, c2)
```

| Размер списка | Искомое значение | Сравнений: линейный поиск | Сравнений: бинарный поиск |
|---------------|------------------|---------------------------|---------------------------|
| 10            | 9                | 10                        | 4                         |
| 100           | 99               | 100                       | 12                        |
| 1000          | 999              | 1000                      | 18                        |

## Задание 3. Коллекции и выбор структуры данных

```python
submissions = [
    ("anna", "lab_01", 5),
    ("boris", "lab_01", 4),
    ("anna", "lab_02", 5),
    ("daria", "lab_01", 3),
    ("boris", "lab_02", 5),
    ("anna", "lab_01", 4),
]

students = set()
labs = set()
attempts = {}
best = {}
counts = {}

for student, lab, score in submissions:
    students.add(student)
    labs.add(lab)
    if student not in attempts:
        attempts[student] = []
    attempts[student].append((lab, score))

    key = (student, lab)
    best[key] = max(best.get(key, score), score)
    counts[key] = counts.get(key, 0) + 1

lab_01 = {student for student, lab, score in submissions if lab == "lab_01"}
lab_02 = {student for student, lab, score in submissions if lab == "lab_02"}

print("Все студенты:", students)
print("Все лабораторные:", labs)
print("Попытки студентов:", attempts)
print("Лучшие результаты:", best)
print("Количество попыток:", counts)
print("Сдавали обе работы:", sorted(lab_01 & lab_02))
```

Вывод программы

```text
Все студенты: {'anna', 'daria', 'boris'}
Все лабораторные: {'lab_01', 'lab_02'}
Попытки студентов: {'anna': [('lab_01', 5), ('lab_02', 5), ('lab_01', 4)], 'boris': [('lab_01', 4), ('lab_02', 5)], 'daria': [('lab_01', 3)]}
Лучшие результаты: {('anna', 'lab_01'): 5, ('boris', 'lab_01'): 4, ('anna', 'lab_02'): 5, ('daria', 'lab_01'): 3, ('boris', 'lab_02'): 5}
Количество попыток: {('anna', 'lab_01'): 2, ('boris', 'lab_01'): 1, ('anna', 'lab_02'): 1, ('daria', 'lab_01'): 1, ('boris', 'lab_02'): 1}
Сдавали обе работы: ['anna', 'boris']
```

**Ответы на пункты к добавленной записи**

- Потому что множество хранит в себе только уникальные значения.
- Потому что в данном случае кортеж и все его элементы являются хешируемыми.
- Потому что список нехуишруемый тип.
- Потому что у словаря поиск в среднем $O(1)$, при переборе списка — $O(n)$, также и проверка ключа работает за $O(1)$,
  тогда как в списке будет проверка за всю длину ключа.

**Таблица средней сложности добавления**

| Коллекция | Добавление элемента                     | Поиск элемента |
|-----------|-----------------------------------------|----------------|
| Множество | $O(1)$                                  | $O(1)$         |
| Список    | $O(1)$ амортизированно через `append()` | $O(n)$         |
| Словарь   | $O(1)$                                  | $O(1)$         |
| Кортеж    | Не поддерживается                       | $O(n)$         |

### Практическое расширение

```python
while True:
    try:
        command = input().split()
    except EOFError:
        break
    if not command:
        continue
    if command == ["exit"]:
        break
    if command[0] == "student" and len(command) == 2:
        student = command[1]
        if student in attempts:
            print(attempts[student])
        else:
            print("Студент не найден")
    elif command[0] == "best" and len(command) == 3:
        key = (command[1], command[2])
        if key in best:
            print(best[key])
        else:
            print("Результат не найден")
    elif command[0] == "attempts" and len(command) == 3:
        key = (command[1], command[2])
        if key in counts:
            print(counts[key])
        else:
            print("Попытки не найдены")
    elif command[0] == "completed" and len(command) == 2:
        lab = command[1]
        if lab in labs:
            result = {student for student, lab2 in best if lab == lab2}
            print(sorted(result))
        else:
            print("Лабораторная работа не найдена")
    else:
        print("Неизвестная команда или неверное число аргументов")
```

## Задание 4. Функции, параметры и области видимости

```python
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
```

**Вывод программы**

```text
3.0
3.0
Анна Иванова
Борис Петров
Результат: Анна — 4.7
Среднее: Борис — 4.00
('python', 'sql')
Итог: Анна — 4.667
Итог: Дарья — 4.000
```

### Исследование LEGB

```python
course = "Python"


def f():
    course = "C++"

    def g():
        nonlocal course
        course += " курс"
        return course

    return g()
```

**Схема**

```
L - область g()
E - область f(), переменные course и g
G - переменные course и f
B - встроенная функция print
L -> E
E -> G
G -> B
```

### Ошибка изменяемого значения по умолчанию

В исходной функции список создаётся один раз при определении функции. Этот объект хранится среди значений по умолчанию и
используется повторно при каждом вызове без аргумента `results`.

```python
## Ошибочный вариант
def add_result(value, results=[]):
    results.append(value)
    return results


## Корректный вариант
def add_result(value, results=None):
    if results is None:
        results = []

    results.append(value)
    return results
```

### Практическое расширение

```python
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
```

**Вывод программы**

```text
[2, 3, 4]
[2, 4, 6]
[False, False, False]
[False, False, False]
```

## Задание 5. Анализатор учебных результатов

**Декомпозиция**

`mean()`, `minimum()` и `maximum()` выполняют базовые вычисления.

`classify()` определяет категорию.

`find_top_students()` хранит текущий наибольший средний результат и список соответствующих имён.

`student_summary()` объединяет базовые вычисления и категорию в один словарь. `group_summary()` вызывает её для каждого
студента, накапливает общие показатели и счётчики категорий, создаёт рейтинг и получает лидеров через
`find_top_students()`.

`format_report()` работает с готовыми итогами и возвращает текст. Она не пересчитывает показатели и не печатает их сама.
Вложенная функция `number()` оформляет число с двумя знаками после точки или заменяет `None` на `«—»`.

**Cложность построения общей статистики**

Пусть `n` — число студентов, `m` — общее число их оценок, `r` — число оценок одного студента, `t` — число лидеров, `L` —
длина готового текста.

| Функция                                   | Время            | Дополнительная память |
|-------------------------------------------|------------------|-----------------------|
| `mean(values)`                            | $O(r)$           | $O(1)$                |
| `minimum(values)`                         | $O(r)$           | $O(1)$                |
| `maximum(values)`                         | $O(r)$           | $O(1)$                |
| `classify(score)`                         | $O(1)$           | $O(1)$                |
| `student_summary(name, results)`          | $O(r)$           | $O(1)$                |
| `find_top_students(students)`             | $O(m + n)$       | $O(t)$                |
| `group_summary(students)`                 | $O(m + nlog(n))$ | $O(n)$                |
| `format_report(student_data, group_data)` | $O(n + L)$       | $O(L)$                |

**Вывод**

Декомпозиция сделала решение понятнее: каждая функция отвечает за отдельную задачу — вычисление показателей, определение категории, построение рейтинга или оформление отчёта. Благодаря понятным именам функций общую логику можно проследить без изучения всех деталей. Повторяющийся код вынесен в функции, поэтому решение стало удобнее проверять и изменять.