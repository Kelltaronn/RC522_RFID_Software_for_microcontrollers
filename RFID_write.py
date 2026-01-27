#============================================================================
# Imports:
#============================================================================
from lib.mfrc522 import SimpleMFRC522
from machine import Pin, Timer
from time import sleep, ticks_ms, ticks_diff
from main import blink_for_time
#============================================================================
# Device:
#============================================================================
reader = SimpleMFRC522(spi_id=0,sck=18,miso=16,mosi=19,cs=17,rst=9) #Pin kiosztást lásd a main.py-ban

#============================================================================
# LED_PINS:
#============================================================================
red_led = Pin(13, Pin.OUT)
yellow_led = Pin(12, Pin.OUT)
green_led = Pin(11,Pin.OUT)


#============================================================================
# Funkció_blokkok, RFC522_höz write
#============================================================================

def wait_until_card_removed(reader, poll_ms=80):
    while True:
        try:
            #Card_check
            r = getattr(reader, "rfid", None) or getattr(reader, "_reader", None) or getattr(reader, "reader", None)
            if r is None:
                # CPU lekapcsolása
                sleep(poll_ms / 1000)
                continue

            # MFRC522 API request:
            if hasattr(r, "request") and hasattr(r, "REQIDL"):
                stat, _ = r.request(r.REQIDL)
                # Lib stat.OK Run_forward:
                if hasattr(r, "OK"):
                    if stat != r.OK:
                        return
                else:
                    # ha nincs OK konstans, akkor ha "falsy" kiütjük:
                    if not stat:
                        return
            else:
                # fallback state minimál sleep mode
                sleep(poll_ms / 1000)

        except Exception:
            # Loop újraindítás.
            sleep(poll_ms / 1000)

def write():
    username = input("Give me the username:")
    password = input("Give me the password:")
    confirm_password = input("Confirm the password:")
    
    if password == confirm_password:
        data = str(username)+ " / " + str(password)
        print(data)
        print("....Place the RFID tag for writting....")
        blink_for_time(yellow_led, 10, 2)
        reader.write(data)
        print("Written card")
    else:
        raise Exception('Run_Error')

       
        
while True:
    write()
    