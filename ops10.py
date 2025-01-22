from urllib import response
import requests

url = "https://github.com/HornScrub?tab=repositories"
while True:
    method = input("Get, Post, Put, Delete , Head, Patch, Options:")
    confirm = input(f"You're about to send a {method} request to {url}. Are you sure (y/n)?")
    if confirm == "y":
        break

match method:
    case "Get":
        userResponse = requests.get(url)
    case "Post":
        userResponse = requests.post(url)
    case "Put":
        userResponse = requests.put(url)
    case "Delete":
        userResponse = requests.delete(url)
    case "Head":
        userResponse = requests.head(url)
    case "Patch":
        userResponse = requests.patch(url)
    case "Options":
        userResponse = requests.options(url)
    case _:
        print("Invalid request type")
        exit()

print(userResponse.status_code)
match userResponse.status_code:
    case 200:
        print("Success")
    case 403:
        print("Forbidden")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown Error")

