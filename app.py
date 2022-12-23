import requests

# Make a GET request to the API
response = requests.get('https://api.example.com/endpoint')

# Check the status code of the response
if response.status_code == 200:
  # Print the response data
  print(response.json())
else:
  # Print an error message
  print('An error occurred: {}'.format(response.status_code))
