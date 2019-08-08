#!/usr/bin/python

import RPi.GPIO as GPIO, MFRC522, signal, sys, re
from time import time

# Capture SIGINT for cleanup when the script is aborted.

def end_read(signal, frame):
    global continue_reading
    print("[!] INTERRUPT [!] - Ctrl+C captured, stopping program and cleaning up.")
    continue_reading = False
    GPIO.cleanup()

def Reader(attempt, ishex, time_start):
    # Hook the SIGINT.
    signal.signal(signal.SIGINT, end_read)

    # Create an object of the class MFRC522.
    MIFAREReader = MFRC522.MFRC522()

    # This loop keeps checking for chips. If one is near it will get the UID and authenticate.

    continue_reading = True

    while continue_reading:

        # Scan for cards.
        (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # If a card is found.
        if status == MIFAREReader.MI_OK:
            print("[+] Card detected.")

            # Get the UID of the card.
            (status, uid) = MIFAREReader.MFRC522_Anticoll()

            # If we have the UID, continue.
            if status == MIFAREReader.MI_OK:

                # Print UID
                print("[+] Card read UID: " + ",".join(str(u) for u in uid) + ".")

                if ishex:
                    # Strip the imported UID of commas.
                    key = [int(byte.strip(), 16) for byte in attempt.split(',')]
                else:
                    key = attempt

                print("[i] Trying the authentication key: " + str(key) + ". Please tap RFID card on now.")

                # Select the scanned tag.
                MIFAREReader.MFRC522_SelectTag(uid)

                # Authenticate.
                status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

                # Check if authenticated.
                if status == MIFAREReader.MI_OK:
                    MIFAREReader.MFRC522_Read(8)
                    MIFAREReader.MFRC522_StopCrypto1()
                    time_r=time()-time_start
                    sys.exit("[!] SUCCESS [!] - The correct key is " + str(key)+" time: "+str(time_r))
                    break

                else:
                    print("[-] Authentication error")
                    continue_reading = False
                    GPIO.cleanup()


def run(i1,i2,i3,i4,i5,i6):
    print("[i] Generating all 274,941,996,890,625 combinations... Please be patient.")
    time_start=time()

    try:

        def tempcombo(t1, t2, t3, t4, t5, t6):
            temp_combo = []
            temp_combo.extend([i1, i2, i3, i4, i5, i6])
            return temp_combo

        while (i1 >= 1):
            temp_combo = tempcombo(i1, i2, i3, i4, i5, i6)
            Reader(temp_combo, False, time_start)

            while (i2 >= 1):
                temp_combo = tempcombo(i1, i2, i3, i4, i5, i6)
                Reader(temp_combo, False, time_start)

                while (i3 >= 1):
                    temp_combo = tempcombo(i1, i2, i3, i4, i5, i6)
                    Reader(temp_combo, False, time_start)

                    while (i4 >= 1):
                        temp_combo = tempcombo(i1, i2, i3, i4, i5, i6)
                        Reader(temp_combo, False, time_start)

                        while (i5 >= 1):
                            temp_combo = tempcombo(i1, i2, i3, i4, i5, i6)
                            Reader(temp_combo, False, time_start)

                            while (i6 >= 1):
                                temp_combo = tempcombo(i1, i2, i3, i4, i5, i6)
                                Reader(temp_combo, False, time_start)
                                i6 -= 1

                            i6 = 255
                            i5 -= 1

                        i5 = 255
                        i4 -= 1

                    i4 = 255
                    i3 -= 1

                i3 = 255
                i2 -= 1

            i2 = 255
            i1 -= 1

        i1 = 255

    except:
        print("[-] Error, Try it again!")
        run(i1,i2,i3,i4,i5,i6)

if __name__== "__main__":
    i1 = 255
    i2 = 255
    i3 = 255
    i4 = 255
    i5 = 255
    i6 = 255
    run(i1,i2,i3,i4,i5,i6)
