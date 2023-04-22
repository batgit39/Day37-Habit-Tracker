import requests
from datetime import datetime

TODAY = datetime.today().strftime("%Y%m%d")

USERNAME = ""
TOKEN = ""
GRAPH_ID = ""

# add your details

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
update_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230415" # change date as required

def sign_up_user():

    user_params = {
        "token": USERNAME,
        "username": TOKEN,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(url= pixela_endpoint, json= user_params)
    print(response.text)

def make_graph():

    graph_config = {
            "id": GRAPH_ID,
            "name": "Reading Graph",
            "unit": "commit",
            "type": "float",
            "color": "ajisai",
            }

    headers = {
            "X-USER-TOKEN": TOKEN
            }

    response = requests.post(url = graph_endpoint,json = graph_config, headers = headers)
    print(response.text)

def post_a_pixel():

    pixel_params = {
            "date": TODAY,
            "quantity": "1"
            # "optionalData": ""
            }

    headers = {
            "X-USER-TOKEN": TOKEN
            }

    response = requests.post(url = post_pixel_endpoint,json = pixel_params, headers = headers)
    print(response.text)

def update_any_pixel():

    update_params = {
            "quantity": "6"
            # "optionalData": ""
            }

    headers = {
            "X-USER-TOKEN": TOKEN
            }

    response = requests.put(url = update_delete_endpoint,json = update_params, headers = headers)
    print(response.text)


def delete_pixel():

    headers = {
            "X-USER-TOKEN": TOKEN
            }

    response = requests.delete(url = update_delete_endpoint, headers = headers)
    print(response.text)

# sign_up_user()
# make_graph()
# post_a_pixel()
# update_any_pixel()
# delete_pixel()

# un-comment the functions as required they are all ready to use.
