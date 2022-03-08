import socket
import termcolor


def scan(target, ports):
    print(f"\n Starting scan for {str(target)}")
    for port in range(1, int(ports)):
        scan_port(target, port)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f"[+] Port {str(port)} opened")
        sock.close()
    except:
        # print(f"[-] Port {str(port)} closed")
        pass


targets = input("[*] Enter targets to scan (separated by ,):")
ports = input("[*] How many ports to scan (int):")

if ',' in targets:
    print(termcolor.colored("[*] Scanning multiple targets", 'green'))
    for target in targets.split(','):
        scan(target.strip(), ports)
else:
    scan(targets, ports)
