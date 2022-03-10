import requests
from termcolor import colored

target_url = input("[*] Enter target url:")
file_name = input("[*] Enter name of the file containing directories -- suggestion: use common.txt provided by the dirb tool")


def request(url):
    try:
        return requests.get(f"http://{url}")
    except requests.exceptions.ConnectionError:
        pass


with open(file_name, 'r') as file:
    for line in file:
        directory = line.strip()
        full_url = f'{target_url}/{directory}'
        response = request(full_url)
        if response:
            print(colored(f"[+] Discovered directory at: {full_url}", 'green'))
