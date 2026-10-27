import copy

original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)

original.append(["Databases", 5])

print('1 изменение\n')
print('original - ', original)
print('alias - ', alias)
print('shallow - ', shallow)
print('deep - ', deep)
print(id(original), id(alias), id(shallow), id(deep), ' - id внешних списков')
print(id(original[0]), id(alias[0]), id(shallow[0]), id(deep[0]), ' - id первого вложенного списка')
print(id(original[0][0]), id(alias[0][0]), id(shallow[0][0]), id(deep[0][0]), ' - id объекта содержащего первую оценку')

print('\n------------------------------------------------------------------\n')

original[0][1] = 3

print('2 изменение\n')
print('original - ', original)
print('alias - ', alias)
print('shallow - ', shallow)
print('deep - ', deep)
print(id(original), id(alias), id(shallow), id(deep), ' - id внешних списков')
print(id(original[0]), id(alias[0]), id(shallow[0]), id(deep[0]), ' - id первого вложенного списка')
print(id(original[0][0]), id(alias[0][0]), id(shallow[0][0]), id(deep[0][0]), ' - id объекта содержащего первую оценку')

print('\n-----------------------------------------------------------------------\n')

wrong_matrix = [[0] * 3] * 3
wrong_matrix[0][0] = 1


print(wrong_matrix[0], wrong_matrix[1], wrong_matrix[2], '-  внутренние списки')
print(id(wrong_matrix[0]), id(wrong_matrix[1]), id(wrong_matrix[2]), '-  id внутренних списков')

print('\n-----------------------------------------------------------------------\n')

correct_matrix = [[0] * 3 for _ in range(3)]
correct_matrix[0][0] = 1

print(correct_matrix[0], correct_matrix[1], correct_matrix[2], '-  внутренние списки')
print(id(correct_matrix[0]), id(correct_matrix[1]), id(correct_matrix[2]), '-  id внутренних списков')
