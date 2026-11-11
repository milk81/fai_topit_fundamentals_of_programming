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

#Проверка на простоту
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

#Практическое решение
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
    l = 0; r =  len(a) - 1
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