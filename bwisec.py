import os
import sys
import time

os.system("clear")
os.system("figlet BwiSec")
print
print("Author: Rabbit.X")
print
print("[1] DDoS")
print("[2] Brute Force")
print("[3] Create Payload")
print("[4] Create Malware")
print("[5] Database Dump")
print("[6] RED HAWK")
print("[7] Crack Password")
Pilih = raw_input('Pilih = ')
if Pilih =="1":
  os.system("apt-get install python")
  os.system("apt-get install python2")
  os.system("apt-get install git")
  os.system("git clone https://github.com/EH30/byte-ddos")
  os.system("python byte-ddos/byte-ddos.py")
elif Pilih =="2":
  os.system("clear")
  os.system("apt-get install hydra")
  os.system("clear")
  os.system("hydra -h")
elif Pilih =="3":
  os.system("clear")
  os.system("apt-get install metasploit-fremawork")
  os.system("clear")
  os.system("msfconsole")
elif Pilih =="4":
  os.system("clear")
  os.system("apt-get install python")
  os.system("apt-get install git")
  os.system("git clone https://github.com/Cyser-Inc/Virus-Maker.git")
  os.system("python Virus-Maker/vbug.py")
elif Pilih =="5":
  os.system("clear")
  os.system("apt-get install sqlmap")
  os.system("clear")
  os.system("sqlmap")
elif Pilih =="6":
  os.system("clear")
  os.system("apt-get install python git php-curl php-xml")
  os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK")
  os.system("php RED_HAWK/rhawk.php")
elif Pilih == "7":
  os.system("clear")
  os.system("apt-get install hashcat")
  os.system("clear")
  os.system("hashcat -h")