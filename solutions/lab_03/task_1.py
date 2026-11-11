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


#Практическое расширение
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
