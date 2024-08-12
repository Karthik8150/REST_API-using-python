import requests

url = 'http://localhost:5000/players'
data = {
    'name': 'Virat',
    'description': 'Batsman'
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Player added successfully")
    print("Player ID:", response.json().get('id'))
else:
    print(f"Failed to add player. Status code: {response.status_code}")
