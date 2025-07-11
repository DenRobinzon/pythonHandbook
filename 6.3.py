# A.Проверка системы

from requests import get

response = get('http://127.0.0.1:5000/')
answer = response.content.decode('utf-8')
print(answer)

# B.Суммирование ответов

from requests import get

url = f'http://{input()}/'
suma = 0
while num := int(get(url).text):
    suma += num
print(suma)

# C.Суммирование ответов 2

from requests import get

response = get(f'http://{input()}/').json()
print(sum([i for i in response if isinstance(i, int)]))

# D.Конкретное значение
from requests import get

response = get(f'http://{input()}/').json()
key = input()
print(response.get(key, 'No data'))

# E.Суммирование ответов 3
from requests import get
import sys

address, *path = map(str.strip, sys.stdin)
results = [get(f'http://{address}{path_}').json() for path_ in path]
print(sum(map(sum, results)))

# F.Список пользователей

from requests import get

users = get(f'http://{input()}/users').json()
names = sorted([f'{user['last_name']} {user['first_name']}' for user in users])
print(*names, sep='\n')

# Рассылка сообщений
from requests import get
from sys import stdin
user = get(f'http://{input()}/users/{input()}')

if user.status_code == 200:
    print(stdin.read().format(**user.json()))
else:
    print('Пользователь не найден')
# H.Регистрация нового пользователя

import requests
import sys

address, *data = map(str.strip, sys.stdin)
user = dict(zip(['username', 'last_name', 'first_name', 'email'], data))
requests.post(f'http://{address}/users', json=user)

# I.Изменение данных
import requests
import sys

address, id, *data = map(str.strip, sys.stdin)
new_user_data = {
    key: value
    for key, value in
    map(lambda x: x.split('='), data)
}

requests.put(f'http://{address}/users/{id}', json=new_user_data)

# J.Удаление данных
import requests

address, user_id = input(), input()
requests.delete(f'http://{address}/users/{user_id}')

# K.
# L.
# M.
# N.
# O.
# P.
# Q.
# R.
# S.
# T.