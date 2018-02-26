import requests


def curiosityrover():
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&page=1"
    app_token = "ApEztOfnuLutAfibTJmSuorcTQMHxQkozbocepVm"
    payload = {'api_key': app_token}
    response = requests.get(url, args=payload)

    return response.json()
