#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Copyright 2014,2018 Mario Gomez <mario.gomez@teubi.co>
#
#    This file is part of MFRC522-Python
#    MFRC522-Python is a simple Python implementation for
#    the MFRC522 NFC Card Reader for the Raspberry Pi.
#
#    MFRC522-Python is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    MFRC522-Python is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with MFRC522-Python.  If not, see <http://www.gnu.org/licenses/>.
#

import RPi.GPIO as GPIO
import MFRC522
import signal
import bruteForce

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:

    # Scan for cards
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        print "Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])

        # This is the default key for authentication
        keys = [[0xFF,0xFF,0xFF,0xFF,0xFF,0xFF],
        [0xA0,0xA1,0xA2,0xA3,0xA4,0xA5],
        [0xB0,0xB1,0xB2,0xB3,0xB4,0xB5],
        [0x4D,0x3A,0x99,0xC3,0x51,0xDD],
        [0x1A,0x98,0x2C,0x7E,0x45,0x9A],
        [0xD3,0xF7,0xD3,0xF7,0xD3,0xF7],
        [0xAA,0xBB,0xCC,0xDD,0xEE,0xFF],
        [0x00,0x00,0x00,0x00,0x00,0x00],
        [0xD3,0xF7,0xD3,0xF7,0xD3,0xF7],
        [0xA0,0xB0,0xC0,0xD0,0xE0,0xF0],
        [0xA1,0xB1,0xC1,0xD1,0xE1,0xF1],
        [0x58,0x7E,0xE5,0xF9,0x35,0x0F],
        [0xA0,0x47,0x8C,0xC3,0x90,0x91],
        [0x53,0x3C,0xB6,0xC7,0x23,0xF6],
        [0x8F,0xD0,0xA4,0xF2,0x56,0xE9]
        ]

        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
        check=False
        for key in keys:
            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 1, key, uid)

            # Check if authenticated
            if status == MIFAREReader.MI_OK:
                MIFAREReader.MFRC522_Read(0)
                MIFAREReader.MFRC522_StopCrypto1()
                print("[i] Default key founded! --> "+str(key))
                check=True
                break

        if(!check):
            print "[-] Authentication error, there aren't default key."
            r=raw_input("Do you want to use brute force? y/n: ")

            if(r=="y"):
                bruteForce.run()
