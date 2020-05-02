import os
import sys
from collections import deque
import requests

# write your code here
args = sys.argv

directory = args[1]
history = deque()

if not os.path.exists(directory):
    os.mkdir(directory)

url = ""
savedFile = {}
previousURL = ""
command = input()
while command != "exit":
    if command == "back":
        url = history.pop()
    else:
        previousURL = url
        url = command
    if "." in url:

        r = requests.get(url if url.startswith(("http://", "https://")) else 'https://'+url)

        content = str(r.content)

        filepath = url.split(".")
        filepath = ".".join(filepath[:-1])

        savedFile[filepath] = url

        with open(os.path.join(directory, url), "w") as f:
            f.write(content)

        print()
    elif url != "exit":
        if url in savedFile:
            with open(os.path.join(directory, savedFile[url]), "r") as f:
                print(f.read())
        else:
            print("Error: Incorrect URL")
        print()
    if command != "back":
        history.append(previousURL)
    command = input()

