import urllib.request, sys, json, os, platform
from pathlib import Path
menu, input_buffer, input_log = {}, [], []
if getattr(sys, 'frozen', False): SCRIPT_DIR = Path(sys.executable).resolve().parent
else: SCRIPT_DIR = Path(__file__).resolve().parent
local_path = os.path.expanduser("~")
print(local_path)
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
    with open("storefront.json") as f: menu_json = f.read()
    menu = json.loads(menu_json)
def n_get_input(menu):
    global input_buffer
    if (len(input_buffer)>0):
        c = input_buffer.pop(0)
        print(c)
        if c == "all\n" and menu:
            b = []
            for index, (key, item) in enumerate(menu.items()):
                if item[1] == "storefront": continue
                b.append(str(index))
                b.append("n")
            input_buffer = b + input_buffer
            return input_buffer.pop(0)
        return c
    return input()
def get_input(menu):
    global input_log
    a = n_get_input(menu)
    if a == "dump":
        with open("input", "w") as f:
            f.write("\n".join(input_log) + "\n")
        a = n_get_input(menu)
        input_log = [a]
    else:
        input_log.append(a)
    return a
if (os.path.exists("input")):
    with open("input") as f:
        input_buffer = f.readlines()
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
    sel = get_input(menu)
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
        get_input(None)