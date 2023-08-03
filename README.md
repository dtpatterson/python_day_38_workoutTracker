# python_day_38_workoutTracker

Uses Nutritionix API to get exercise stats with natural language queries.
Utilized Google Sheety API to perform HTTP requests GET and POST to a Google spreadsheet.

This program makes it simple to chart your progress in the gym by giving a basic description of your workout.
input - Tell me which exercises you did: Ran 5 miles in 45 minutes
Output - {
  "workout": {
    "date": "03/08/2023",
    "time": "14:33:01",
    "exercise": "Running",
    "duration": "45 min",
    "calories": 632.1,
    "id": 5
  }
}

This output is then sent to a personal Google spreadsheet showing the output in a readable format by using HTTP POST.

For the public's use, each individual will have to create an account with Nutritionix and Sheety to access their API key.

Day 38 of 100 Python coding challenge from Udemy - 100 Days of Code
