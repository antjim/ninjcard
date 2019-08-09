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
import read
import write
import dumper
import bruteForce

class ninjcard():

    def welcome(self):
        print "      _)      _)                    |"
        print      " __ \  | __ \  |  __|  _` |  __| _` |"
        print      " |   | | |   | | (    (   | |   (   |"
        print      "_|  _|_|_|  _| |\___|\__,_|_|  \__,_|"
        print      "           ___/ "

    def read(self):
        read.operation(True)

    def write(self):
        write.run()

    def dump(self):
        dumper.run()

    def bruteF(self):
        bruteForce.run()

def main():
    nin=ninjcard()
    while True:
      os.system("clear")
      nin.welcome()
      print("######################################")
      print("[1] Read a Card.")
      print("[2] Write a Card.")
      print("[3] Dump a Card.")
      print("[4] Brute Force a Card.")
      print("")
      print("[i] Ctrl + C for exit.")
      print("######################################")
      r=raw_input("[*] Please, select an option: ")


      if ("1" in r):
          print "[i] Selected Read Option ..."
          time.sleep(3)
          nin.read()


      if ("2" in r):
          print "[i] Selected Write Option ..."
          time.sleep(3)
          nin.write()


      if ("3" in r):
          print "[i] Selected Dump Option ..."
          time.sleep(3)
          nin.dump()


      if ("4" in r):
          print "[i] Selected Brute Force Option ..."
          time.sleep(3)
          nin.bruteF()

if __name__== "__main__":
  main()
