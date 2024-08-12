import requests

# Replace with the actual player ID you want to update
player_id = 2
url = f'http://localhost:5000/players/{player_id}'

# Data to update
data = {
    "name":"Rohit",
    "description" : "Batsman"

}

response = requests.put(url, json=data)

if response.status_code == 200:
    print("Player updated successfully")
elif response.status_code == 404:
    print("Player not found")
else:
    print(f"Failed to update player. Status code: {response.status_code}")
