import os,sys,time
from os import system as s
def slowtype(t):
   for D in t + "\n":
   	sys.stdout.write(D)
   	sys.stdout.flush()
   	time.sleep(6/100)
s('clear')
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    # Red
PU = "\033[2;35m" #purple



print(R+""" _____   _____        ___   _____   _____   __   _  
|  _  \ |  _  \      /   | /  ___| /  _  \ |  \ | | 
| | | | | |_| |     / /| | | |     | | | | |   \| | 
| | | | |  _  /    / / | | | |  _  | | | | | |\   | 
| |_| | | | \ \   / /  | | | |_| | | |_| | | | \  | 
|_____/ |_|  \_\ /_/   |_| \_____/ \_____/ |_|  \_| """)

time.sleep(15/10)
s("clear")
print (PU+""" _____   _____  
|_   _| /  ___/ 
  | |   | |___  
  | |   \___  \ 
  | |    ___| | 
  |_|   /_____/ """)
  
print("")  
slowtype("TYPE (1) TO INSTALL TERMUX START")
k2=input(G+"❯❯❯ ")
if k2 == "1" : 
    s("apt update && termux-setup-storage && pkg install python -y && pkg install python2 -y && pkg install git -y && pkg install ruby -y && pkg install nmap -y && pkg install unzip -y && pkg install nano -y && apt install php -y && apt install golang -y && apt install nano -y && apt install hydra -y && apt install cmatrix -y && pkg install figlet -y && pkg install git && pkg install python2 -y && pkg install cowsay -y && pkg install toilet -y && pkg install ruby -y && pkg install unzip && pkg install curl -y && pkg install openssh -y && pkg install tor -y && pkg install clang -y && pkg install w3m -y && pkg install proot -y && pip2 install wget && pip2 install requests && pip2 install wget && pip2 install requests && apt update && apt upgrade")
else :
	exit()
