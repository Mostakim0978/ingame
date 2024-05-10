# -*- coding: utf-8 -*-
 #DECODE BY TEAM-69 HENTAI
# FB Itz Hentai

# PyEncryptor
# Tool: A Python2 and Python3 Code Encoder
#Author: Tutulking
# Coder: 🙄🙄
 
import os
import sys
import time
import marshal
import zlib
import base64
import compileall
import shutil
print('\033[0;93m [ My Personal Facebook Account ]')
os.system('xdg-open https://www.facebook.com/Tutul.King.Ok.Bro')
time.sleep(3)
print('\033[0;92m [ Checking Update...? ]')
time.sleep(10)
 
#Setting Up Logo#
try:
	columns = shutil.get_terminal_size().columns
	column1 = columns + 15
	column2 = columns + 5
	column3 = columns + 19
except:
	rows, columns = os.popen('stty size', 'r').read().split()
	column1 = 0
	column2 = 0
	column3 = 0
 
#Logo
os.system('xdg-open https://github.com/Tutul-King')
os.system('espeak -a 300 " welcome,  to,   Tutul King,   V,i,p,  Encrypt Tools"')
def logo():
	os.system("clear")
	print (f"""
\033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\033[0;91m ████████\033[0;92m ██    ██\033[0;91m ████████\033[0;92m ██    ██\033[0;91m ██ \033[0;92m     ║
║\033[0;91m    ██ \033[0;92m   ██    ██\033[0;91m    ██\033[0;92m    ██    ██\033[0;91m ██  \033[0;92m    ║
║\033[0;91m    ██ \033[0;92m   ██    ██\033[0;91m    ██\033[0;92m    ██    ██\033[0;91m ██  \033[0;92m    ║
║\033[0;91m    ██ \033[0;92m   ██    ██\033[0;91m    ██\033[0;92m    ██    ██\033[0;91m ██   \033[0;92m   ║
║\033[0;91m    ██ \033[0;92m    ██████\033[0;91m     ██\033[0;92m     ██████\033[0;91m  ███████\033[0;92m ║
\033[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝               \033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\33[0;41m       YOUR SCRIPT ENCRYPT VERSION 4.2       \033[0;92m║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
\033[0;94m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\033[1;33m 
╠══[Author                   • \33[1;38mMR-TUTUL ]\33[1;38m     ║\033[1;31m 
╠══[Facebook                 • Tutul King ]   ║  \033[1;97m  
╠══[Github                   • \33[1;38mTutul-King ]   ║\33[1;34m   
╠══[Whatsapp                 • 01608843956 ]  ║\33[1;35m 
╠══[TOOLS                    • Marshal  ]     ║ \33[1;32m   
\033[0;94m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\033[1;31m""")
#Exit Tool Massage
def logout():
    psb("\n\033[94m[\033[92m*\033[94m]\033[92m Thanks For Using Our Tool")
    psb("\033[94m[\033[92m*\033[94m]\033[92m For More Tools, Visit: \n")
    print("\033[93m[ \033[92mhttps://github.com/Tutul-King/ \033[93m]\033[37m\n".center(column3))
    sys.exit()
 #Python Version Banner
def banner():
    version = str(sys.version_info[:3][0]) + "." + str(sys.version_info[:3][1]) + "." + str(sys.version_info[:3][2])
    
   #  print("\033[93m-" * int(columns))
    if (sys.version_info[:3][0] < 3):
        print("\033[92m\t\tPython Version : \033[37m"+version)
    else:
        print(("\033[92m \033[37m"))
    print('\033[92m===============================================') 
 
#Flush Print
def psb(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
 
#Taking Input Depending on Python Version
def verInput(data):
    version = sys.version_info[:2]
    if (version < (3, 0)):
        dataInput = raw_input(data)
    else:
        dataInput = input(data)
    return dataInput
 
 
#Marshal_Code_Executor#
marshalHead = "# Encoded By Tutul-King\n# Fb Link: https://www.facebook.com/Tutul.King.Ok.Bro\n# Fb Link: https://www.facebook.com/Tutul.Official.Account\n# https://github.com/Tutul-King\n\nimport marshal\nexec(marshal.loads("
 
marshalTail = "))"
 
#Base64_Code_Executor#
b64Head = "# Encoded By Tutul-King\n# Fb Link: https://www.facebook.com/Tutul.King.Ok.Bro\n# Fb Link: https://www.facebook.com/Tutul.Official.Account\n# https://github.com/Tutul-King\n\nimport base64\nexec(base64.b64decode("
 
b64Tail = "))"
 
#Zlib_Code_Executor#
zlibHead = "# Encoded By Tutul-King\n# Fb Link: https://www.facebook.com/Tutul.King.Ok.Bro\n# Fb Link: https://www.facebook.com/Tutul.Official.Account\n# https://github.com/Tutul-King\n# https://github.com/Tutul-King\n\nimport zlib\nexec(zlib.decompress("
 
zlibTail = "))"
 
#Zlib+B64+Mar_Code_Executor#
allHead = "# Encoded By Tutul-King\n# Fb Link: https://www.facebook.com/Tutul.King.Ok.Bro\n# Fb Link: https://www.facebook.com/Tutul.Official.Account\n# https://github.com/Tutul-King\n\nimport marshal, base64, zlib\nexec(marshal.loads(zlib.decompress(base64.b64decode("
 
allTail = "))))"
 
#Encode Marshal
def encodeMarshal(data, power):
    powerData = data
    for i in range(power):
        code = compile(powerData, "Tutulking", "exec")
        dump = marshal.dumps(code)
        powerData = marshalHead +repr(dump) + marshalTail
    
    return powerData
 
#Encode Zlib
def encodeZlib(data, power):
    powerData = data
    for i in range(power):
        code = powerData.encode()
        dump = zlib.compress(code, 2)
        powerData = zlibHead + repr(dump) + zlibTail
    
    return powerData
 
#Encode Base64
def encodeBase64(data, power):
    powerData = data
    for i in range(power):
        code = powerData.encode()
        dump = base64.b64encode(code)
        powerData = b64Head + repr(dump) + b64Tail
    
    return powerData
 
#Python Bytecode Encode
def encodePyc(data):
    tmp = open("temp.py", "w")
    tmp.write(data)
    tmp.close()
    if (sys.version_info[:2] < (3, 0)):
        compileall.compile_file("temp.py")
    else:
        compileall.compile_file("temp.py", legacy=True)
    
    return True
 
#Marshal + Zlib + Base64
def encodeAllOnce(data, power):
    powerData = data
    for i in range(power):
        code = compile(powerData, "Tutulking", "exec")
        code = marshal.dumps(code)
        code = zlib.compress(code)
        dump = base64.b64encode(code)
        powerData = allHead + repr(dump) + allTail
    
    return powerData
 
# Marshal + Zlib + Base64 with One By One
def encodeAllStep(data, power):
    powerData = data
    for i in range(power):
        code = encodeBase64(powerData, power=1)
        code = encodeZlib(code, power=1)
        powerData = encodeMarshal(code, power=1)
    
    return powerData
 
 
# Get power amount
def getPower():
    power = verInput("\033[92m[\033[37m•\033[92m]\033[37m Enter Repeat Amount :> \033[92m")
    while not power.isdigit():
        psb("\n\033[92m[\033[91m!\033[92m]\033[37m Enter a Correct Amount!")
        power = verInput("\033[92m[\033[37m•\033[92m]\033[37m Enter Repeat Amount (\033[92mMAX: 15\033[37m):> \033[92m")
    
    power = int(power)
    
    while (power > 5000):
        psb("\n\033[92m[\033[91m!\033[92m]\033[37m Maximum amount is 15")
        power = getPower()
    
    return int(power)
 
#Get File Data
def getFile():
    path = verInput("\n\033[92m[\033[37m•\033[92m]\033[37m Enter Your File Name:> \033[92m")
    
    while not os.path.exists(path):
        psb("\n\033[92m[\033[91m!\033[92m]\033[37m File Does Not Exists!")
        time.sleep(0.4)
        path = verInput("\033[92m[\033[37m•\033[92m]\033[37m Enter Your File Name:> \033[92m")
    
    fileData = open(path, "r").read()
    
    global filepath
    if ("/" in path):
        filepath = path.split("/")[-1]
    else:
        filepath = path
    
    return fileData
 
#Save File Data
def saveFile(encData):
    if (".py" in filepath):
        savefilepath = filepath.replace(".py", "_Tutul-Enc.py")
    else:
        savefilepath = filepath + "_Tutul-Enc.py"
    
    savepath = "/sdcard/" + savefilepath
    
    file = open(savepath, "w")
    file.write(encData)
    file.close()
 
#PYC Move File
def moveFile():
    if (".py" in filepath):
        savefilepath = filepath.replace(".py", "_Tutul-Enc.py")
    else:
        savefilepath = filepath + "_Tutul-Enc.py"
    
    savepath = "/sdcard/" + savefilepath
    os.system("mv temp.pyc " + savepath + " >/dev/null 2>&1")
    os.system("rm temp.py > /dev/null 2>&1")
 
 
#Encoding Process
def encode(type):
    fileData = getFile()
    
    if not (type == "pyc"):
        power = getPower()
    
    psb("\n\033[92m[\033[37m•\033[92m]\033[37m Encoding Your File...\033[30m")
    
    if (type == "marshal"):
        encData = encodeMarshal(fileData, power)
        saveFile(encData)
        
    elif (type == "zlib"):
        encData = encodeZlib(fileData, power)
        saveFile(encData)
        
    elif (type == "base64"):
        encData = encodeBase64(fileData, power)
        saveFile(encData)
        
    elif (type == "pyc"):
        encData = encodePyc(fileData)
        moveFile()
        
    elif (type == "all_once"):
        encData = encodeAllOnce(fileData, power)
        saveFile(encData)
    
    elif (type == "all_step"):
        encData = encodeAllStep(fileData, power)
        saveFile(encData)
    
    
    time.sleep(1)
    psb("\n\033[92m[\033[37m•\033[92m]\033[37m Encoding Complete!")
    psb("\033[92m[\033[37m•\033[92m]\033[37m Saved File path: \033[92m/sdcard/" + filepath.replace(".py", "_Tutul-Enc.py") + " \033[37m\n")
 
 
#Update Tool
def update():
    logo()
    psb("\n\033[92m[\033[37m•\033[92m]\033[37m Please Wait!")
    psb("\033[92m[\033[37m•\033[92m]\033[37m Checking Update...")
    import requests
    try:
        toolVersion = open(".version", "r").read()
    except:
        toolVersion = "Tutulking"
    try:
        mainVersion = requests.get("https://raw.githubusercontent.com/Tutul-King/main/.version").text
    except:
        psb("\n\033[92m[\033[91m!\033[92m]\033[37m Please Turn On Internet Connection!")
        l = verInput("\n\033[92m[\033[37m•\033[92m]\033[37m Press Enter To Continue....")
        update()
    if (toolVersion == mainVersion):
        psb("\n\033[92m[\033[37m•\033[92m]\033[37m You are Using the Latest Version of PyEncryptor!")
        l = verInput("\033[92m[\033[37m•\033[92m]\033[37m Press Enter To Go Back....")
        logo()
        main()
    else:
        psb("\n\033[92m[\033[37m•\033[92m]\033[37m Tool Update Found!!")
        psb("\033[92m[\033[37m•\033[92m]\033[37m Updating Tool...")
        os.system("cd .. && rm -rf PyEncryptor && git clone https://github.com/Tutul-King/PyEncryptor > /dev/null 2>&1")
        
        psb("\n\033[92m[\033[37m•\033[92m]\033[37m Tool Updated Successfully!")
        psb("\033[92m[\033[37m•\033[92m]\033[37m Starting Latest Version of PyEncryptor...")
        time.sleep(1)
        os.system("cd .. && cd PyEncryptor && python PyEnc.py")
 #Main Menu
def main():
    print("\n\033[92m[\033[37m1\033[92m]\x1b[38;5;208m Marshal [\033[92mVIP-1\x1b[38;5;208m]")
    print("\033[92m[\033[37m2\033[92m]\x1b[38;5;208m Zlib")
    print("\033[92m[\033[37m3\033[92m]\x1b[38;5;208m Base64")
    print("\033[92m[\033[37m4\033[92m]\x1b[38;5;208m Python Bytecode (\033[92m.pyc\x1b[38;5;208m) [\033[92mVIP-2\x1b[38;5;208m]")
    print("\033[92m[\033[37m5\033[92m]\x1b[38;5;208m Marshal \033[92m+\x1b[38;5;208m Zlib \033[92m+\x1b[38;5;208m Base64 ")
    print("\033[92m[\033[37m6\033[92m]\x1b[38;5;208m Marshal \033[92m+ \x1b[38;5;208mZlib \033[92m+\x1b[38;5;208m Base64 ")
    print("\033[92m[\033[37m7\033[92m]\x1b[38;5;208m Update Tool")
    print("\033[92m[\033[37m8\033[92m]\x1b[38;5;208m Exit")
    
    op = verInput("\n\033[92m[\033[37m•\033[92m]\033[37m Enter Your Choice:> \033[92m").replace("0", "")
    
    while not (op in ["1", "2", "3", "4", "5", "6", "7", "8"]):
        psb("\n\033[92m[\033[91m!\033[92m]\033[37m Please Enter a Correct Option!")
        op = verInput("\033[92m[\033[37m•\033[92m]\033[37m Enter Your Choice:> \033[92m").replace("0", "")
    
    if (op == "1"):
        encode("marshal")
    elif (op == "2"):
        encode("zlib")
    elif (op == "3"):
        encode("base64")
    elif (op == "4"):
        encode("pyc")
    elif (op == "5"):
        encode("all_once")
    elif (op == "6"):
        encode("all_step")
    elif (op == "7"):
        update()
    elif (op == "8"):
        logout()
 
 
 
if (__name__ == "__main__"):
    logo()
    banner()
    main()