import requests
from bs4 import BeautifulSoup
import os

gp = False
if os.system("gp")==0:
    gp = True

def cls():
    os.system("clear")

def main():

    storeurl = input("URL: ").split("?")[0]
    if storeurl == "stop" and gp:
        os.system("gp stop")

    url = "https://store.rg-adguard.net/api/GetFiles"

    payload = "url="+storeurl+"&type=url"
    headers = {"content-type": "application/x-www-form-urlencoded"}

    response = requests.request("POST", url, data=payload, headers=headers)


    if "<p>The server returned an empty list.<br>Either you have not entered the link correctly, or this service does not support generation for this product.</p>" in response.text:
        print("Invalid URL, or not supported")
        input("Press enter to continue ")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    recommended = []
    works = []
    other = []

    for i in soup.find_all('a'):
        if 'bundle' in i.string:
            recommended.append([i.get('href'), i.string])
        elif 'x86' in i.string:
            works.append([i.get('href'), i.string])
        elif 'x64' in i.string:
            works.append([i.get('href'), i.string])
        else:
            other.append([i.get('href'), i.string])

    if not len(recommended) == 0:
        cls()
        print("Recommended:")
        for i in recommended:
            print(i[1], i[0])
            print()
        if input("Press enter or m to see more ") == 'm':
            cls()
            print("Works:")
            for i in works:
                print(i[1], i[0])
                print()
            if input("Press enter or m to see more ") == 'm':
                cls()
                print("Other:")
                for i in other:
                    print(i[1], i[0])
                    print()
                input("Press enter to continue ")
    elif not len(works) == 0:
        cls()
        print("Works:")
        for i in works:
            print(i[1], i[0])
            print()
        if input("Press enter or m to see more ") == 'm':
            cls()
            print("Other:")
            for i in other:
                print(i[1], i[0])
                print()
            input("Press enter to continue ")
    else:
        cls()
        print("Other:")
        for i in other:
            print(i[1], i[0])
            print()


if __name__ == "__main__":  
    while True:
        cls()
        main()
