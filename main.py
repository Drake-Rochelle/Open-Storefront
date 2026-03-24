import urllib.request
import json
import os
import platform
from pathlib import Path
import sys
menu = {}
if getattr(sys, 'frozen', False):
    SCRIPT_DIR = Path(sys.executable).resolve().parent
else:
    SCRIPT_DIR = Path(__file__).resolve().parent
local_path = os.path.expanduser("~")
if (Path.exists(SCRIPT_DIR / "download_path.txt")):
    with open(SCRIPT_DIR / "download_path.txt") as f:
        d = f.read()
        if (d!="C:/Path/To/Custom/Download/Folder"):
            local_path = d
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

if (not os.path.exists("home.3sf")):
    id = "1m99FhKG-zpNd7VoAOjFV11dyJsDbnUv9"
else:
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
        if (not os.path.exists("home.3sf")):
            id = "1m99FhKG-zpNd7VoAOjFV11dyJsDbnUv9"
        else:
            with open("home.3sf") as f:
                id = f.read()
        current_storefront = "Home Storefront"
        continue
    elif len(sel) >= 15:
            current_storefront = "Unknown Storefront"
            id = sel
            continue
    ind = int(sel)
    item = menu[items[ind]]
    if (item[1] == "storefront"):
        id = item[0]
        current_storefront = items[ind]
    else:
        clear()
        print("Downloading...")
        p = item[2].replace("/3DS Storefront/", "/Open Storefront/")
        os.makedirs(local_path+p, exist_ok=True)
        urllib.request.urlretrieve(item[0], local_path+p+"/"+item[1])
        clear()
        print('Download successfull.\nEnter any symbol to return to storefront...')
        input()
