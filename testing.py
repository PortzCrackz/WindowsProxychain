from rotatingproxy import RotatingProxy

rproxy = RotatingProxy()

def get_proxy_from_file():

    # fetches proxy from proxy.txt

    with open("proxies.txt", "r") as f:

        return loads(f.read())

    proxy = get_proxy_from_file()
get_proxy_from_file()

import requests

response = requests.get("url-to-fetch", proxies=proxy)
