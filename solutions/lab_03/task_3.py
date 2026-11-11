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

print('\n-----------------------------------------------------\n')

#Дополнительное добавление
submission = ("daria", "lab_02", 5)
submissions.append(submission)

student, lab, score = submission

students.add(student)
labs.add(lab)
if student not in attempts:
    attempts[student] = []
attempts[student].append((lab, score))

key = (student, lab)
best[key] = max(best.get(key, score), score)
counts[key] = counts.get(key, 0) + 1

if lab == "lab_01":
    lab_01.add(student)
elif lab == "lab_02":
    lab_02.add(student)

print("Все студенты:", students)
print("Все лабораторные:", labs)
print("Попытки студентов:", attempts)
print("Лучшие результаты:", best)
print("Количество попыток:", counts)
print("Сдавали обе работы:", sorted(lab_01 & lab_02))

print('\n-----------------------------------------------------\n')

#Практическое расширение
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