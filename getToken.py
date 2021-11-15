import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth

username = input("Enter a username: ")
password = getpass("Enter a password: ")

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

payload = {}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
}

response = requests.request("POST", url, auth=HTTPBasicAuth(username, password), headers=headers, data = payload)

print(response.text.encode('utf8'))
