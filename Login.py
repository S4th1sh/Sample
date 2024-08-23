import requests

def login_to_hexaware(email, password, token):
    # URL for the login endpoint
    url = "https://www.hexaware.com/login"

    # Data to be sent in the POST request
    data = {
        'email': email,
        'password': password,
        'token': token
    }

    # Sending POST request to login
    response = requests.post(url, data=data)

    # Checking if the login was successful
    if response.status_code == 200:
        print("Login successful!")
        # Handle further actions after successful login
    else:
        print("Login failed. Status code:", response.status_code)
        # Handle login failure

# User details
email = "SathishTest@hexaware.com"
password = "Password12345"
token = "testabc123xyz456sampleTOKEN789"

# Call the login function
login_to_hexaware(email, password, token)
