# Joe's Solebox Account Generator
# Created by joe aka @atcbackdoor
# Script is free to use, read the README.md file on how to use.



import requests, json, random, string, time
from colorama import Fore, init

init()
config = json.load(open("config.json"))
domain = config["domain"]
password = config["password"]
amount = config["amount"]
proxstat = config["proxies"]

def proxies():
    prox = open("proxies.txt", "r").read().splitlines()
    proxy = random.choice(prox)
    return proxy

def submit(t):
    proxy = proxies()
    ip = proxy.split(":")[0]
    port = proxy.split(":")[1]
    proxytype = "userpass"
    try:
        user = proxy.split(":")[2]
        passw = proxy.split(":")[3]
    except:
        proxytype = "ipauth"
    
    if proxytype == "userpass":
        prox = {'http': 'http://{}:{}@{}:{}/'.format(user, passw, ip, port)}
    elif proxytype == "ipauth":
        prox = {'http':'http://{}:{}'}
    else:
        print (Fore.RED + "Proxy formatting error")
        time.sleep(120)
        exit()

    fname = ''.join(random.choices(string.ascii_letters, k=6))
    lname = ''.join(random.choices(string.ascii_letters, k=6))
    housenum = random.randint(1111,9999)
    street = ''.join(random.choices(string.ascii_letters, k=6))
    zip_code = random.randint(1111,9999)
    city = ''.join(random.choices(string.ascii_letters, k=6))
    tel = random.randint(1111111,9999999)
    email = ''.join(random.choices(string.ascii_letters, k=6)) + str(random.randint(1,99999)) + "@" + domain

    headers = {
        'authority': 'www.solebox.com',
        'cache-control': 'max-age=0',
        'origin': 'https://www.solebox.com',
        'upgrade-insecure-requests': '1',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'referer': 'https://www.solebox.com/en/my-account/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
    }

    data = [
        ('stoken', 'DBC5CB51'),
        ('lang', '1'),
        ('listtype', ''),
        ('actcontrol', 'account'),
        ('cl', 'user'),
        ('fnc', 'createuser'),
        ('reloadaddress', ''),
        ('blshowshipaddress', '1'),
        ('invadr[oxuser__oxfname]', fname),
        ('invadr[oxuser__oxlname]', lname),
        ('invadr[oxuser__oxstreet]', street),
        ('invadr[oxuser__oxstreetnr]', housenum),
        ('invadr[oxuser__oxaddinfo]', ''),
        ('invadr[oxuser__oxzip]', zip_code),
        ('invadr[oxuser__oxcity]', city),
        ('invadr[oxuser__oxcountryid]', 'a7c40f631fc920687.20179984'),
        ('invadr[oxuser__oxstateid]', ''),
        ('invadr[oxuser__oxbirthdate][day]', ''),
        ('invadr[oxuser__oxbirthdate][month]', ''),
        ('invadr[oxuser__oxbirthdate][year]', ''),
        ('invadr[oxuser__oxfon]', tel),
        ('lgn_usr', email),
        ('lgn_pwd', password),
        ('lgn_pwd2', password),
        ('userform', ''),
    ]

    if proxies == False:
        f = requests.post('https://www.solebox.com/index.php?lang=1&', headers=headers, data=data)
    else:
        f = requests.post('https://www.solebox.com/index.php?lang=1&', headers=headers, data=data, proxies=prox)
    if "Your solebox Dashboard" in f.text:
        open("accounts.txt", "a").write("{}:{}\n".format(email, password))
        print (Fore.GREEN + "[{}] Account generated with email: {}".format(t, email))
    else:
        print (Fore.RED + "[{}] Error generating account")

if __name__ == "__main__":
    print (Fore.BLUE + "-----------------------------------")
    print (Fore.BLUE + "| " + Fore.WHITE +  "Joe's Solebox Account Generator" + Fore.BLUE + " |")
    print (Fore.BLUE + "-----------------------------------\n")
    for x in range(amount):
        try:
            submit(x)
        except:
            print (Fore.RED + "An unexpected error occurred, trying again.")
            continue
    print (Fore.GREEN + "\nDone.")