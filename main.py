import urllib.request
import json
import os
import platform

menu = {}
local_path = os.path.expanduser("~")
current_storefront = ""

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def draw_menu(items):
    print(current_storefront+":\n")
    if (current_storefront != "Home Storefront"):
        print("x: <home>")
    for i in range(len(items)):
            print(str(i)+": "+items[i])

def open_storefront(id):
    global menu, current_storefront
    url = "https://drive.google.com/uc?export=download&id="+id

    urllib.request.urlretrieve(url, "storefront.json")
    with open("storefront.json") as f:
        menu_json = f.read()
    menu = json.loads(menu_json)

with open("home.3sf") as f:
    id = f.read()
current_storefront = "Home Storefront"
while (True):
    clear()
    print("Loading...")
    open_storefront(id)
    clear()
    items = list(menu.keys())
    draw_menu(items)
    sel = input()
    if (sel == "x"):
        with open("home.3sf") as f:
            id = f.read()
        current_storefront = "Home Storefront"
        continue
    ind = int(sel)
    item = menu[items[ind]]
    if (item[1] == "storefront"):
        id = item[0]
        current_storefront = items[ind]
    else:
        clear()
        print("Downloading...")
        os.makedirs(local_path+item[2], exist_ok=True)
        urllib.request.urlretrieve(item[0], local_path+item[2]+"/"+item[1])
        clear()
        print('Download successfull.\nEnter any symbol to return to storefront...')
