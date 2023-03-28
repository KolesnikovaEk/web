from requests import get, post, delete

print(get('http://127.0.0.1:8030/api/v2/jobs').json())
print(get('http://127.0.0.1:8030/api/v2/jobs/4').json())
print(get('http://127.0.0.1:8030/api/v2/jobs/6').json())
print(get('http://127.0.0.1:8030/api/v2/jobs/q').json())
print(post('http://127.0.0.1:8030/api/v2/jobs').json())
print(post('http://127.0.0.1:8030/api/v2/jobs', json={'job': 'artist'}).json())
print(post('http://127.0.0.1:8030/api/v2/jobs', json={
    'job': 'actor',
    'work_size': 5,
    'collaborators': '1',
    'is_finished': False,
    'hazard': 1,
    'team_leader': 1}).json())
print(delete('http://127.0.0.1:8030/api/v2/jobs/999').json())
print(delete('http://127.0.0.1:8030/api/v2/jobs/2').json())
