from requests import get, post, delete
import datetime

print(get('http://127.0.0.1:8030/api/v2/users').json())
print(get('http://127.0.0.1:8030/api/v2/users/4').json())
print(get('http://127.0.0.1:8030/api/v2/users/6').json())
print(get('http://127.0.0.1:8030/api/v2/users/q').json())
print(post('http://127.0.0.1:8030/api/v2/users').json())
print(post('http://127.0.0.1:8030/api/v2/users', json={'name': 'Foma'}).json())
print(post('http://127.0.0.1:8030/api/v2/users', json={
    'name': 'Kate',
    'about': 'student',
    'email': 'a@mail.ru',
    'hashed_password': 123,
    'created_date': str(datetime.datetime.now)}).json())
print(delete('http://127.0.0.1:8030/api/v2/users/999').json())
print(delete('http://127.0.0.1:8030/api/v2/users/10').json())
