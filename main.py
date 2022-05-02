import os

import requests

NUTRITIONIX_APP_ID = os.environ.get('NUTRITIONIX_APP_ID')
NUTRITIONIX_API_KEY = os.environ.get('NUTRITIONIX_API_KEY')


headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": "0"
}
nutritionix_natual_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

text = input("What did you do ?")

json_natural_exercises = {
    "query": text
}

response = requests.post(nutritionix_natual_url, json=json_natural_exercises, headers=headers)
print(response.json())