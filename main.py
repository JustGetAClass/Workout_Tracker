import requests
from datetime import datetime
import os

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

bearer_header = {
        "Authorization": os.getenv("AUTH")
}


def nutritionix():
    exercise_params = {
        "query": input("what was your workout? "),
        "gender": "male",
        "weight_kg": 130,
        "height_cm": 175,
        "age": 26
    }

    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY
    }

    response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",
                             json=exercise_params,
                             headers=headers)
    response.raise_for_status()
    return response.json()["exercises"]


# sheety
def add_workout(exercise):
    date = datetime.now().strftime("%d/%m/%Y")
    time = datetime.now().strftime("%X")
    workout = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': exercise["name"].title(),
            'duration': exercise["duration_min"],
            'calories': exercise["nf_calories"],
            }
                    }
    post_response = requests.post(url="https://api.sheety.co/2874157e0caacca0738b505c1fb28ee9/mohaWorkouts/workouts",
                                  json=workout,
                                  headers=bearer_header)


for exercise in nutritionix():
    add_workout(exercise)
