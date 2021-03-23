import requests
import time
import random
import threading
import json

from colorama import Fore, Style, init

init(autoreset=True)

with open('config.json') as json_data:
    config = json.load(json_data)


class Logger:
    printLock = threading.Lock()


def startup():
    print("------------------------------------------------")
    print("Created by @saigorupati")
    print("------------------------------------------------")
    time.sleep(1)

    thread()

def format_proxy(proxy):
        try:
            ip = proxy.split(":")[0]
            port = proxy.split(":")[1]
            userpassproxy = '%s:%s' % (ip, port)
            proxyuser = proxy.split(":")[2].rstrip()
            proxypass = proxy.split(":")[3].rstrip()
            proxies = {'http': 'http://%s:%s@%s' % (proxyuser, proxypass, userpassproxy),
                       'https': 'http://%s:%s@%s' % (proxyuser, proxypass, userpassproxy)}

        except:
            proxies = {'http': 'http://%s' % proxy, 'https': 'http://%s' % proxy}

        return proxies


def thread():
    global url
    ask = input("Would you like to begin ebay view bot? (y/n) ")
    url = input("Enter ebay product link: ")
    ask2 = input("Enter number of view to be added (40 max without proxies): ")
    if ask == "y":
        for i in range(int(ask2)):
            t = threading.Thread(target=create)
            t.start()
    else:
        quit()


def create():

    useproxies = config['useproxies']

    proxy_list = []
    with open('proxies.txt') as f:
        for line in f:
            proxy_list.append(line.strip())

    if useproxies:
        proxee = random.choice(proxy_list)
    else:
        proxee = None

    try:
        r = requests.get(url.strip(), proxies=format_proxy(proxee))
        with Logger.printLock:
            print(time.strftime("[%H:%M:%S]") + Fore.CYAN + 'View successfully added')
    except:
        with Logger.printLock:
            print(time.strftime("[%H:%M:%S]") + Fore.RED + 'Error adding view')

startup()