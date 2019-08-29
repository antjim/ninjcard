#!/usr/bin/env python

# -*- coding: utf-8 -*-

__author__ = "Antonio J."
__license__ = "https://github.com/antjim/ninjcard/blob/master/LICENSE"
__version__ = "0.1.0"
__web__ = "https://github.com/antjim"
__status__ = "Production"

import os
import sys
import time

class ninjcard():

    def welcome(self):
        print "      _)      _)                    |"
        print      " __ \  | __ \  |  __|  _` |  __| _` |"
        print      " |   | | |   | | (    (   | |   (   |"
        print      "_|  _|_|_|  _| |\___|\__,_|_|  \__,_|"
        print      "           ___/ "

    def mfcuk(self):
        print("")

        try:
            os.system("mfcuk -C -R 0:A -s 250 -S 250 -v 3")
            raw_input("[i] Completed.")

        except Exception as e:
            print("[-] There are a problem with the command.\n")
            print("[i] "+str(e))

    def mfoc(self):
        print("")
        r=raw_input("Do you have key? y/n: ")

        if( (r == "y") or (r == "n") or (r == "Y") or (r=="N") ):
            pass
        else:
            print("[i] Please, use 'y' or 'n'.")
            time.sleep(3)
            ninjcard.mfoc(self)

        if("y" == r):
            keya=raw_input("key A: ")
            keyb=raw_input("key B: ")
            request=raw_input("number of probes per sector, instead of default of 20: ")

            try:
                if("" == request):
                    request=20

                if(int(request)<0):
                    request=request*-1
                    print("[i] number of probes has been changed to positive number.")

            except:
                print("[-] you can't use words in this field or negative numbers.")
                ninjcard.mfoc(self)

            name=raw_input("name of output: ")

            if(""==name):
                print("[-] you can't leave an empty name.")
                ninjcard.mfoc(self)

            try:
                os.system("mfoc -k {} -k {} -P {} -O {}".format(keya,keyb,request,name))
                raw_input("[i] Completed.")
                main()

            except Exception as e:
                print("[-] There are a problem with the command.\n")
                print("[i] "+str(e))
                main()

        else:
            request=raw_input("number of probes per sector, instead of default of 20: ")
            name=raw_input("name of output: ")

            try:
                if("" == request):
                    request=20

                if(int(request)<0):
                    request=request*-1
                    print("[i] number of probes has been changed to positive number.")

            except Exception as e:
                    print("[-] you can't use words in this field or negative numbers.")
                    ninjcard.mfoc(self)

            if(""==name):
                print("[-] you can't leave an empty name.")
                ninjcard.mfoc(self)

            try:
                os.system("mfoc -P {} -O {}".format(request,name))
                raw_input("[i] Completed.")
                main()

            except Exception as e:
                print("[-] There are a problem with the command.\n")
                print("[i] "+str(e))
                main()

    def lazyCracker(self):
        print("")
        os.system("sudo miLazyCracker")
        raw_input("[i] Completed.")

    def clone(self):
        print("")
        dump=raw_input("Name of dump: ")
        key=raw_input("Name of Magic Card: ")

        if( (dump =='') or (key=='')):
            print("[i] Please, you don't leave an empty name.")
            time.sleep(3)
            ninjcard.clone(self)

        try:
            os.system("nfc-mfclassic w a {} {}".format(key,dump))
            raw_input("[i] Completed.")

        except e:
            print("[-] There are a problem with the command.\n")
            print("[i] "+str(e))

def main():
    nin=ninjcard()
    while True:
      os.system("clear")
      nin.welcome()
      print("######################################")
      print("[1] Use mfcuk.")
      print("[2] Use mfoc.")
      print("[3] Use miLazy Cracker (hardened mifare classic).")
      print("[4] Clone a card.")
      print("")
      print("[i] Ctrl + C for exit.")
      print("######################################")
      r=raw_input("[*] Please, select an option: ")


      if ("1" == r):
          print "[i] Selected mfcuk option ..."
          time.sleep(3)
          nin.mfcuk()


      if ("2" == r):
          print "[i] Selected mfoc option ..."
          time.sleep(3)
          nin.mfoc()

      if ("3" == r):
          print "[i] Selected miLazy Cracker option ..."
          time.sleep(3)
          nin.lazyCracker()

      if ("4" == r):
          print "[i] Selected Clone a card option ..."
          time.sleep(3)
          nin.clone()

      else:
          print "[i] Select a valid number."
          time.sleep(3)

if __name__== "__main__":
  main()
