import sys

students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}
CATEGORIES = (
    "Отлично",
    "Хорошо",
    "Удовлетворительно",
    "Неудовлетворительно",
    "Нет результатов",
)

def mean(values):
    if not values:
        return None
    return sum(values) / len(values)

def minimum(values):
    if not values:
        return None
    result = values[0]
    for value in values:
        if value < result:
            result = value
    return result

def maximum(values):
    if not values:
        return None
    result = values[0]
    for value in values:
        if value > result:
            result = value
    return result

def classify(score):
    if score is None:
        return "Нет результатов"
    if not (0 <= score <= 100):
        raise ValueError("Результат должен быть от 0 до 100")
    if score >= 90:
        return "Отлично"
    if score >= 75:
        return "Хорошо"
    if score >= 60:
        return "Удовлетворительно"
    return "Неудовлетворительно"

def student_summary(name, results):
    avg = mean(results)
    return {
        "name": name,
        "count": len(results),
        "mean": avg,
        "minimum": minimum(results),
        "maximum": maximum(results),
        "category": classify(avg),
    }

def find_top_students(students):
    top_mean = None
    leaders = []
    for name, results in students.items():
        average = mean(results)
        if average is None:
            continue
        if top_mean is None or average > top_mean:
            top_mean = average
            leaders = [name]
        elif average == top_mean:
            leaders.append(name)
    return leaders

def group_summary(students):
    student_data = []
    categories = {category: 0 for category in CATEGORIES}
    total = 0
    total_results = 0
    for name, results in students.items():
        data = student_summary(name, results)
        student_data.append(data)
        categories[data["category"]] += 1
        total += sum(results)
        total_results += len(results)
    graded = [data for data in student_data if data["count"] > 0]
    rating = sorted(graded, key=lambda data: -data["mean"])
    avg = None
    if total_results > 0:
        avg = total / total_results
    return {
        "students": student_data,
        "total_students": len(students),
        "graded_students": len(graded),
        "total_results": total_results,
        "mean": avg,
        "minimum": minimum([data["minimum"] for data in graded]),
        "maximum": maximum([data["maximum"] for data in graded]),
        "categories": categories,
        "rating": rating,
        "top_students": find_top_students(students),
    }

def format_report(student_data, group_data):
    def number(value):
        if value is None:
            return "—"
        return f"{value:.2f}"
    lines = ["РЕЗУЛЬТАТЫ СТУДЕНТОВ"]
    if not student_data:
        lines.append("Группа пуста.")
    for data in student_data:
        lines.append(
            f"{data['name']}: попыток — {data['count']}; "
            f"среднее — {number(data['mean'])}; "
            f"минимум — {number(data['minimum'])}; "
            f"максимум — {number(data['maximum'])}; "
            f"категория — {data['category']}"
        )
    lines.extend([
        "",
        "СТАТИСТИКА ГРУППЫ",
        f"Студентов: {group_data['total_students']}",
        f"Студентов с результатами: {group_data['graded_students']}",
        f"Всего результатов: {group_data['total_results']}",
        f"Общее среднее: {number(group_data['mean'])}",
        f"Общий минимум: {number(group_data['minimum'])}",
        f"Общий максимум: {number(group_data['maximum'])}",
        "Лидеры: " + (", ".join(group_data["top_students"]) or "нет"),
        "",
        "КАТЕГОРИИ",
    ])
    for category, count in group_data["categories"].items():
        lines.append(f"{category}: {count}")
    lines.extend(["", "РЕЙТИНГ ПО СРЕДНЕМУ"])
    if not group_data["rating"]:
        lines.append("Нет студентов с результатами.")
    for position, data in enumerate(group_data["rating"], start=1):
        lines.append(f"{position}. {data['name']} — {number(data['mean'])}")
    return "\n".join(lines)

group_data = group_summary(students)
print(format_report(group_data["students"], group_data))
