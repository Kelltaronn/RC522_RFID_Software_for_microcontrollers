#!/usr/bin/env python
# Kelltaronn_Edition
#============================================================================
#Imports
#============================================================================
import time, os, sys
from lib.mfrc522 import SimpleMFRC522
from lib.keyboard_layouts import klavye,hu_iso_mac,hu_iso_win,en_iso_win
from machine import Pin, Timer
from time import sleep, ticks_ms, ticks_diff
#============================================================================
#VERSION NUMBER:
#============================================================================
version = 1.1
#============================================================================
#PIN_Layout set_up:(HELP)
#============================================================================
"""
GP17 = SDA
GP18 = SCK
GP19 = MOSI
GP16 = MISO
NA = IRQ
GND = GND
GP9 = RST
3v3 = 3v3
"""
"""
Port layout:
SDA = Orange
SCK = Yellow
MOSI =  Green
MISO = Blue
RST = White
3.3V = Black
GND = Grey
"""
#============================================================================
# LED_PINS:
#============================================================================
red_led = Pin(13, Pin.OUT)
yellow_led = Pin(12, Pin.OUT)
green_led = Pin(11,Pin.OUT)
"GND = PIN18"
#============================================================================
# READER:
#============================================================================
reader = SimpleMFRC522(spi_id=0,sck=18,miso=16,mosi=19,cs=17,rst=9)
#============================================================================
# KEYBOARD_AND_MODE_SETTING:
#============================================================================
k = en_iso_win.hidkeyboard()
mode = "antares" #Selectable modes: [antares,1040,dmc]
state = True #If True it's in read mode if it's in False mode then it will write
#============================================================================
# SECRET_KEY_FOR_ENCODING:
#============================================================================
'''
def load_secret_key(path="lib/secret_key.txt"):
    with open(path, "r") as f:
        return f.read().strip().encode("utf-8")
    
secret_key = load_secret_key()
print(secret_key)
'''
#============================================================================
# FUNCTION_BLOCKS_FOR_LED:
#============================================================================
timer_led = Timer()

def blink_for_time(led, freq, duration_sec):
    period = 1 / freq
    start = ticks_ms()

    while ticks_diff(ticks_ms(), start) < duration_sec * 1000:
        led.on()
        sleep(period / 2)
        led.off()
        sleep(period / 2)
#============================================================================
# FUNCTION_BLOCKS_FOR_MRFC522:
#============================================================================

def read():
    print("Reading...Please Place the Card...")
    idRead, textRead = reader.read()
    print("Login credentials:{} for ID:{}".format(textRead,idRead))
    time.sleep(2)
    return textRead
    
def write():
    username = input("Give me the username:")
    password = input("Give me the password:")
    confirm_password = input("Confirm the password:")
    try:
        if password == confirm_password:
            data = str(username)+ " / " + str(password)
            print(data)
            print("....Place the RFID tag for writting....")
            reader.write(data)
        else:
            raise Exception('Run_Error')
    except Exception as inst:
        print(type(inst))
        print(inst.arg)
        print(inst)
       
def parse_credentials(text):
    text = (text or "").strip()

    if " / " in text:
        u, p = text.split(" / ", 1)
    elif "/" in text:
        u, p = text.split("/", 1)
    else:
        return None, None

    return u.strip(), p.strip()

#============================================================================
# EDGE_TRIGGER_BLOCK
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


#============================================================================
# Funkció_blokkok, Géptípusok:
#============================================================================
            
def send_antares(keyboard, user, pwd):
    #Com_start:
    blink_for_time(yellow_led, 10, 2)
    
    keyboard.write(user)
    keyboard.tab()
    time.sleep(1)
    keyboard.write(pwd)
    keyboard.enter()
    
    #Com_end:
    yellow_led.off()
    
def send_bec1040(keyboard, user, pwd):
    #Ciklus: USER,ENTER,PWD,ENTER,ENTER
    
    #Com_start:
    blink_for_time(yellow_led, 10, 2)
    
    #Writing:
    keyboard.write(user)
    keyboard.enter()
    time.sleep(1.5)
    keyboard.write(pwd)
    keyboard.enter()
    time.sleep(1.5)
    keyboard.enter()
    
    #Com_end:
    yellow_led.off()
    
def send_dmc(keyboard, user, pwd):
    
    #Com_start:
    blink_for_time(yellow_led, 10, 2)
    
    #Writing:
    keyboard.write(pwd)
    keyboard.enter()
    
    #Com_end:
    yellow_led.off()
                                   
#============================================================================
# Funkció_blokkok, REPL_Kapcsolat
# Kelltaronn_Edition
#============================================================================

def wait_repl_connect(timeout=10):
    """Waiting for REPL"""
    print("I started to set up the REPL")
    for i in range(timeout * 10):
        if os.dupterm() is not None: #If this true the repl is up
            print("REPL is active app will start up.")
            return True
            
        else:
            print("REPL not active but app will start up anyway.")
            return False
        
#============================================================================
# Encryption_Decryption:
#============================================================================
secret_key = " "

def encryption():
    pass

def decryption():
    pass
#============================================================================
# Setting pin states
#============================================================================        

"PIN_SETTER"
red_led.off()
yellow_led.off()
green_led.off()

#============================================================================
# Main_cycle:
#============================================================================
while state:
            print("System start to run")
            green_led.on()
            
            #Data Read and parseing:
            data = read()
            username, password = parse_credentials(data)
            
            if not username or not password:
                red_led.on()
                print("Error:Data format incorrect", data)
                continue
            
            #Line_mode_shifter:                         
            if mode == "antares":
                send_antares(k, username, password)

            elif mode == "1040":
                send_bec1040(k, username, password)
            
            elif mode == "dmc":
                send_dmc(k, username, password)
            
            else:
                raise NameError("Not found machine name.")
                print("Not found machine name error.Please change name.")
                red_led.on()
            wait_until_card_removed(reader)
            

            




            
            
