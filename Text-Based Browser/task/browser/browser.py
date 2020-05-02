import os
import sys
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

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
init()
while command != "exit":
    if command == "back":
        url = history.pop()
    else:
        previousURL = url
        url = command
    if "." in url:

        r = requests.get(url if url.startswith(("http://", "https://")) else 'https://'+url)

        content = BeautifulSoup(r.content)
        content = content.body

        content.a.insert_before(Fore.BLUE)
        content.a.insert_after(Style.RESET_ALL)
        content.a.insert_after(Style.RESET_ALL)
        [x.decompose() for x in content.findAll('script')]

        print(content.get_text())
        filepath = url.split(".")
        filepath = ".".join(filepath[:-1])

        savedFile[filepath] = url

        with open(os.path.join(directory, url), "w") as f:
            f.write(content.get_text())

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

