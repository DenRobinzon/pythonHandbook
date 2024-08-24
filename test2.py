import datetime
lst = [i for i in range(100002)]

start = datetime.datetime.now()
for i in range(100000):
    lst.pop(-2)
finish = datetime.datetime.now()
print(str(finish - start))

lst = [i for i in range(100002)]


start = datetime.datetime.now()
for i in range(100000):
    lst.pop()
finish = datetime.datetime.now()

print(str(finish - start))
