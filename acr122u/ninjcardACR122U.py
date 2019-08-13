#!/usr/bin/env python

# -*- coding: utf-8 -*-

__author__ = "Antonio J."
__license__ = "https://github.com/antjim/ninjcard/blob/master/LICENSE"
__version__ = "0.0.1"
__web__ = "https://github.com/antjim"
__status__ = "Preduction"

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
        os.system("mfcuk -C -R 0:A -s 250 -S 250 -v 3")
        raw_input("[i] Completed.")

    def mfoc(self):
        print("")
        r=raw_input("Do you have key? y/n: ")

        if("y" in r):
            keya=raw_input("key A: ")
            keyb=raw_input("key B: ")
            request=raw_input("number of probes per sector, instead of default of 20: ")
            name=raw_input("name of output: ")

            if("" == request):
                request=20

            os.system("mfoc -k {} -k {} -P {} -O {}".format(keya,keyb,request,name))
            raw_input("[i] Completed.")

        else:
            request=raw_input("number of probes per sector, instead of default of 20: ")
            name=raw_input("name of output: ")

            if("" == request):
                request=20

            os.system("mfoc -P {} -O {}".format(request,name))
            raw_input("[i] Completed.")

    def lazyCracker(self):
        print("")
        os.system("sudo miLazyCracker")
        raw_input("[i] Completed.")

    def clone(self):
        print("")
        dump=raw_input("Name of dump: ")
        os.system("nfc-mfclassic W a {}".format(dump))
        raw_input("[i] Completed.")


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


      if ("1" in r):
          print "[i] Selected mfcuk option ..."
          time.sleep(3)
          nin.mfcuk()


      if ("2" in r):
          print "[i] Selected mfoc option ..."
          time.sleep(3)
          nin.mfoc()

      if ("3" in r):
          print "[i] Selected miLazy Cracker option ..."
          time.sleep(3)
          nin.lazyCracker()

      if ("4" in r):
          print "[i] Selected Clone a card option ..."
          time.sleep(3)
          nin.clone()

if __name__== "__main__":
  main()
