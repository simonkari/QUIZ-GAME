import requests

# Define parameters for the Open Trivia Database API request
parameters = {
    "amount": 20,
    "type": "boolean",
    "category": 18
}

# Send a GET request to the Open Trivia Database API with the specified parameters
response = requests.get(url="https://opentdb.com/api.php", params=parameters)

# Check if the request was successful; raise an exception for bad responses (4xx and 5xx status codes)
response.raise_for_status()

# Parse the JSON response and extract the "results" key to obtain question data
question_data = response.json()["results"]
