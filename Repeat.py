import playsound
import time
import subprocess
import sys

from subprocess import call

def main():
    theproc = subprocess.Popen([sys.executable, "audio.py"])
    ask1 = input("Turn Music off? (Y/N): ")
    if ask1 == "Y":
        print("OK Turning off")
        print("")
        theproc.kill()
        music_off()
    elif ask1 == "N":
        print("OK. Keeping Music on.")
        print("")
        music_on()
main()

def music_on():
    ask1 = input("Turn Music off? (Y/N): ")
    if ask1 == "Y":
        theproc.kill()
        print
music_on()

def music_off():
    ask1 = input("Turn music back on? (Y/N): ")
    if ask1 == "N":
        print("OK. Exiting.")
        exit()
    elif ask1 == "Y":
        print("OK. Turning the Music back on.")
        print("")
        main()
music_off()
