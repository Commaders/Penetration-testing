# -*- coding: utf-8 -*-
import os,time
os.system("clear")

\033[1;93m        HELLO I AM Commaders
\033[1;92m╔══════════════════════════════════════════════╗
\033[1;92m║AUTHOR      : Commaders                  ║
\033[1;92m║FACEBOOK    : John Ry                    ║
║GITHUB      : https://github.com/Commaders║
\033[1;92m╚══════════════════════════════════════════════╝     """

cusr = "Commaders"
cpwd = "Commaders"
def ABIR():
    os.system("clear")
    print(logo)
    print
    usr=raw_input(" \033[1;96m ENTER USERNAME :  \033[1;95m")
    if usr == cusr:
        HOM()
    else:
        os.system("clear")
        print
        print("  \033[1;96mENTER USERNAME : \033[1;95m "+usr+"  \033[1;91m(wrong)")
        time.sleep(1)
        os.system('xdg-open https://facebook.com/DEAUTH3R//?substory_index=0')
        Commaders()
def HOM():
    os.system("clear")
    print(logo)
    print
    print("  \033[1;96mENTER USERNAME :  \033[1;95mCommaders \033[1;92m (correct)")
    pwd=raw_input("  \033[1;96mENTER PASSWORD :  \033[1;95m")
    if pwd == cpwd:
        GO()
    else:
        os.system("clear")
        print(logo)
        print
        print("  \033[1;96mENTER USERNAME :  \033[1;95mCommaders  \033[1;92m(correct)")
        print("  \033[1;96mENTER PASSWORD : \033[1;95m "+pwd+"  \033[1;91m(wrong)")
        time.sleep(1)
        os.system('xdg-open https://facebook.com/DEAUTH3R/?substory_index=0')
        HOM()
    
def GO():
    os.system("clear")  
    print(logo)
    print
    print(" \033[1;96m ENTER USERNAME : \033[1;95m Commaders\033[1;92m (correct)")
    print("\033[1;96m  ENTER PASSWORD : \033[1;95m Commaders \033[1;92m (correct)")
    print(" \033[1;92mLogin Successfull\033[0m")  
    time.sleep(1)
if __name__=="__main__":
    Commaders()
os.system("clear")
print(logo)
print
print"\033[1;96m[1] 06 Digit cloning"
print"\033[1;96m[2] 07 Digit cloning"
print"\033[1;96m[3] 08 Digit cloning"
print"\033[1;96m[4] 09 Digit cloning"
print"\033[1;96m[5] 10 Digit cloning"
print"\033[1;96m[6] 11 Digit cloning"
print"\033[1;96m[0] Back"
Commaders=str(raw_input("\033[1;91m\n[★] Select Your Option : \033[1;93m"))

if Abirhossain=="1" or Commaders=="01":
	os.system("python2 06DEGIT.py")
elif Commaders=="2" or Commaders=="02":
	os.system("python2 07DEGIT.py")
elif Commaders=="3" or Commaders=="03":
	os.system("python2 08DEGIT.py")
elif Commaders=="4" or Commaders=="04":
	os.system("python2 09DEGIT.py")
elif Commaders=="5" or Commaders=="05":
	os.system("python2 10DEGIT.py")
elif Commaders=="6" or Commaders=="06":
	os.system("python2 11DEGIT.py")
elif Commaders=="0" or Commaders=="00":
	exit()
else:
	os.system("python2 Cloning.py")
