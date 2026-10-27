import sys

data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))

print('\n------------------------------------------------------------------------------------\n')

import weakref


class Record:
    pass


record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())

print('\n------------------------------------------------------------------------------------\n')

#Практическая задача

import weakref

class Record:
    pass

registry = weakref.WeakValueDictionary()

first = Record()
second = Record()

registry["first"] = first
registry["second"] = second
registry["third"] = Record()

print("Исходный реестр:", list(registry.keys()))

print("Первый объект существует:", "first" in registry)
print("Второй объект существует:", "second" in registry)
print("Третий объект существует:", "third" in registry)

del first

print("\nПосле удаления первой сильной ссылки:")
print("Записи в реестре:", list(registry.keys()))

del second

print("\nПосле удаления второй сильной ссылки:")
print("Записи в реестре:", list(registry.keys()))