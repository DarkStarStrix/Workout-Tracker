from datetime import datetime

import requests

response = requests.get(url="https://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
print(data)

# Constants
SHEETLY_API_KEY = ""
SHEETLY_PROJECT_NAME = ""
SHEETLY_ENDPOINT = ""
NUTRITIONIX_API_ID = ""

# Get the exercise details from the user
connection = requests.post(url="https://api.sheety.co/6b9e0b0b4b0b0b0b0b0b0b0b0b0b0b0b/myWorkouts/workouts")
print(connection.text)

connection = requests.get(url="https://api.nutritionix.com/v1/natural/exercise",
                          headers={"x-app-id": NUTRITIONIX_API_ID, })
print(connection.text)

input_data = input("Tell me which exercises you did: ")
# then get the exercise details from the user and then give the exercise details to the nutritionix api
# and then get how many calories the user burned and then add the exercise details to the Google sheet using the sheetly api
# Create the body of the post request
body = {
    "query": input_data,
}


# Get the response code
print(response.status_code)
if response.status_code == 200:
    print("Successfully got the exercise details")
else:
    print("Failed to get the exercise details")

# Get the date and time
today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

# Get the exercise details from the user
for exercise in data["workouts"]:
    # Get the exercise name
    exercise_name = exercise["name"]
    # Get the exercise duration
    exercise_duration = exercise["duration"]
    # Get the exercise calories
    exercise_calories = exercise["calories"]

    # Create the body of the post request
    body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise_name.title(),
            "duration": exercise_duration,
            "calories": exercise_calories
        }
    }

    # Make the post request to add the exercise to the Google sheet
    response = requests.post(url="https://api.sheety.co/6b9e0b0b4b0b0b0b0b0b0b0b0b0b0b0b/myWorkouts/workouts",
                             json=body)
    print(response.text)

    # Get the response code
    print(response.status_code)
    if response.status_code == 200:
        print("Successfully added the exercise to the google sheet")
    else:
        print("Failed to add the exercise to the google sheet")

# Get the response data
print(response.json())

# Get the response headers
print(response.headers)

# Get the response body
print(response.text)

# Get the response encoding
print(response.encoding)

# Get the response cookies
print(response.cookies)

# Get the response elapsed time
print(response.elapsed)

# Get the response history
print(response.history)

# Get the response request
print(response.request)

# Get the response reason
print(response.reason)

# Get the response url
print(response.url)

# Get the response raw
print(response.raw)

# Get the response content
print(response.content)
