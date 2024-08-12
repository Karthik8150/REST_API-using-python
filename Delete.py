import requests

# Replace with the actual player ID you want to delete
player_id = '4'
url = f'http://localhost:5000/players/{player_id}'

response = requests.delete(url)
if response.status_code == 200:
    print("Player deleted successfully")
elif response.status_code == 404:
    print("Player not found")
else:
    print(f"Failed to delete player. Status code: {response.status_code}")
