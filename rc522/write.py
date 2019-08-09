#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import ninjcard
import bruteForce

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

def op(continue_reading):

    # Hook the SIGINT
    signal.signal(signal.SIGINT, end_read)

    # Create an object of the class MFRC522
    MIFAREReader = MFRC522.MFRC522()

    # This loop keeps checking for chips. If one is near it will get the UID and authenticate
    while continue_reading:

        # Scan for cards
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # If a card is found
        if status == MIFAREReader.MI_OK:
            print "[i] Card detected"

        # Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()

        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:

            # Print UID
            print "[i] Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])

            # Default keys for authentication
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
            check=True

            s=raw_input("[i] Select your sector, by default 8: ")

            try:
                if(s==""):
                    s=8
                else:
                    int(s)
            except:
                print("[-] Please, use a number.")
                op(True)

            for key in keys:
                status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, s, key, uid)
                print "\n"

                # Check if authenticated
                if status == MIFAREReader.MI_OK:

                    # Variable for the data to write
                    data = []


                    # Fill the data with 0xFF
                    for x in range(0,16):
                        data.append(0xFF)

                    print "[i] Sector {} looked like this:".format(s)
                    # Read block 8
                    MIFAREReader.MFRC522_Read(s)
                    print "\n"

                    print "Sector {} will now be filled with 0xFF:".format(s)
                    # Write the data
                    MIFAREReader.MFRC522_Write(s, data)
                    print "\n"

                    print "[i] It now looks like this:"
                    # Check to see if it was written
                    MIFAREReader.MFRC522_Read(s)
                    print "\n"

                    data = []
                    # Fill the data with 0x00
                    for x in range(0,16):
                        data.append(0x00)

                    print "[i] Now we fill it with 0x00:"
                    MIFAREReader.MFRC522_Write(s, data)
                    print "\n"

                    print "[i] It is now empty:"
                    # Check to see if it was written
                    MIFAREReader.MFRC522_Read(s)
                    print "\n"

                    # Stop
                    MIFAREReader.MFRC522_StopCrypto1()

                    # Make sure to stop reading for cards
                    continue_reading = False

                    print ""
                    r=raw_input("[*] Continue writing? y/n: ")

                    if("y" in r):
                        check=False
                        break
                    else:
                        GPIO.cleanup()
                        ninjcard.main()



            if(check):
                print "[-] Authentication error, there aren't default key."
                r=raw_input("[*] Do you want to use brute force? y/n: ")

                if(r=="y"):
                    bruteForce.run()

                else:
                    GPIO.cleanup()
                    ninjcard.main()
def run():
    op(True)

if __name__== "__main__":
    run()
