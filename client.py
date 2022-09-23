import requests

HOST = 'http://127.0.0.1:5000'

# resp = requests.post(f'{HOST}/adverts/', json={
#     'id': 7,
#     'header': 'Car 5 sa6le',
#     'description': 'good 666',
#     'create_date': '5353',
#     'owner': '1'
# })
# print(resp.status_code)
# print(resp.json())

resp = requests.delete(f'{HOST}/adverts/', json={
    'id': 7,
})

print(resp.status_code)
print(resp.json())