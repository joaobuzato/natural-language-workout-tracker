import os
from datetime import datetime
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

today = datetime.now()

sheety_url = "https://api.sheety.co/de21026eb64e4f9375c8bb7d7ab06f1a/day38Yu/workouts"
exercises = response.json()['exercises']
for exercise in exercises:

    params = {
        "workout": {
            "date": datetime.strftime(today, "%d/%m/%Y"),
            "time": datetime.strftime(today, "%H:%M:%S"),
            "exercise": exercise['name'],
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }
    sheety_headers = {
        "Authorization": os.environ.get('SHEETY_AUTH')
    }
    requests.post(sheety_url, json=params, headers=sheety_headers)
