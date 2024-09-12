import requests
from toolz import curry,pipe
@curry
def make_request( url, **kwargs):
    """General function to make API requests."""
    response = requests.request("GET", url, **kwargs)
    return response.json()

