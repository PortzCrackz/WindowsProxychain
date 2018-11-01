import time
import random
import requests
import playsound
import sys
import subprocess
import os

from subprocess import call
from pynput import keyboard

    #############################################################
    ####################/ START OF THE CODE \####################
    #############################################################

    ########################################################
    #####################/ MUSIC BLOCK \####################
    ########################################################

theproc = subprocess.Popen([sys.executable, "audio.py"])
music_ask = input("Would you like to keep the music on? (Y/N): ")
if music_ask == "Y":
    print("")
    print("OK. Keeping the music on.")
    print("")
elif music_ask == "exit":
    print("Exiting.")
    exit()
else:
    print("")
    print("OK. Turning the music off.")
    theproc.kill()
    print("")
    time.sleep(1)

    ########################################################
    ###################/ WELCOME MESSAGE \##################
    ########################################################

def welcome_message():
    print("██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗")
    time.sleep(.750)
    print("██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝")
    time.sleep(.750)
    print("██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  ")
    time.sleep(.750)
    print("██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  ")
    time.sleep(.750)
    print("╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗")
    time.sleep(.750)
    print(" ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝")

    print("           // Welcome Te4mCrxckz's Proxychain \\\ ")
    print("      //If you are on windows, use TM to stop music\\\ ")
    print("  // If you are on linux, well use our Linux ProxyChain\\\ ")
    print("")
welcome_message()

    ########################################################
    ###################/ INPUT BLOCK \######################
    ########################################################

def input_block():
    def delay_inpt_block():
        delay_inpt = input('Please Input Delay: ')
        delay_inpt = float(delay_inpt)
        if delay_inpt == "":
            no_inpt = input("No Input. Try Again? (Y/N): ")
            if no_inpt == "":
                print("Exiting.")
                exit()
            elif no_inpt == "Y":
                print("OK. Trying again.")
                print("")
                delay_inpt_block()
            else:
                print("Exiting.")
                exit()
        elif delay_inpt == "":
            print("")
            print("Exiting.")
            print("")
            print("Delay must be above 0 seconds.")
            exit()
            
        elif delay_inpt == "exit":
            print("Exiting.")
            exit()

        else:
            print("OK. Using", delay_inpt, "second(s) of delay")

        proxylist = open('proxies.txt', 'r')
        print("")
        time.sleep(.500)
        
        f = open('proxies.txt', 'r+')
        for line in f.readlines():
            print("")
            print("Changing to: ", line)
            print("")
            print("Using: ", line)
            time.sleep(delay_inpt)
        f.close()

        print("")
        go_again = input("There are no more proxies. Go again? (Y/N): ")
        if go_again == "Y":
            delay_inpt_block()
        elif go_again == "N":
            print("OK. Exiting. . .")
        else:
            exit()
        
    delay_inpt_block()
input_block()
