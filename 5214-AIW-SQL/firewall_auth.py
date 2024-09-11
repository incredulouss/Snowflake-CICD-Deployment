import requests
import time

def get_public_ip():
    response = requests.get('https://api.ipify.org')
    return response.text

public_ip = get_public_ip()
print(public_ip)

