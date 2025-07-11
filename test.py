import requests

address, user_id = input(), input()
requests.delete(f'http://{address}/users/{user_id}')