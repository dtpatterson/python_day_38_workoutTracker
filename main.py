# Uses Nutritionix API to get exercise stats with natural language queries
# Uses Google Sheety API to perform HTTP requests GET and POST to a Google spreadsheet

import requests
from datetime import datetime
import os

GENDER = "Male"
WEIGHT_KG = 86
HEIGHT_CM = 185.4
AGE = 31

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
GS_USERNAME = os.environ["GS_USERNAME"]
GS_PASSWORD = os.environ["GS_PASSWORD"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["sheet_endpoint"]

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    duration_in_minutes = exercise["duration_min"]
    duration_str = f"{duration_in_minutes} min"
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": duration_str,
            "calories": exercise["nf_calories"]
        }
    }

    # Basic Authentication
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(GS_USERNAME, GS_PASSWORD)
    )

    print(sheet_response.text)
