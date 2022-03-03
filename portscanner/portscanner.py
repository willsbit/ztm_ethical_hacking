import socket
import termcolor


def scan(target, ports):
    for port in range(1, ports):
        scan_port(target, port)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f"[+] Port {str(port)} opened")
        sock.close()
    except:
        print(f"[-] Port {str(port)} closed")


targets = input("[*] Enter targets to scan (separated by ,):")
ports = input("[*] How many ports to scan (int):")

if ',' in targets:
    print("[*] Scanning multiple targets")
    for target in targets.split(','):
        scan(target.strip(), ports)
else:
    scan(targets, ports)
