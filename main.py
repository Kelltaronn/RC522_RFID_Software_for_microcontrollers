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
keyboard = en_iso_win.hidkeyboard()
machine = "1040" #Selectable modes: [antares,1040,dmc]
mode = "write" #Selectable modes: [read,write]
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
#Time_parameters:
frequency = 10
blink_time = 5

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
    time.sleep(1)
    return textRead

def write_card(username,password):
    
    data = str(username)+ " / " + str(password)
    
    yellow_led.on()
    print("Place card to write...")
    blink_for_time(yellow_led, frequency, blink_time)
    reader.write(data)
       
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
    blink_for_time(yellow_led, frequency, blink_time)
    
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
    blink_for_time(yellow_led, frequency, blink_time)
    
    #Writing:
    #Space beírása és teszt
    keyboard.space()
    keyboard.write(user)
    keyboard.enter()
    time.sleep(0.5)
    
    keyboard.write(pwd)
    keyboard.enter()
    time.sleep(0.5)
    
    keyboard.enter()
    
    #Com_end:
    yellow_led.off()
    
def send_dmc(keyboard, user, pwd):
    
    #Com_start:
    blink_for_time(yellow_led, frequency, blink_time)
    
    #Writing:
    keyboard.write(pwd)
    keyboard.enter()
    
    #Com_end:
    yellow_led.off()
                                   
#============================================================================
# Parse
#============================================================================
def parse_command(cmd):
    parts = cmd.strip().split("|")
    
    if parts[0] == "WRITE" and len(parts) == 3:
        return ("WRITE", parts[1], parts[2])
    
    elif parts[0] == "READ":
        return ("READ",)
    
    return None
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

"PIN_SETTER_AT_START"
red_led.off()
yellow_led.off()
green_led.off()

#============================================================================
# Main_cycle:
#============================================================================
while True:
            
            green_led.on()
            
            if mode == "read":
                print("System start to run")
                #Data Read and parseing:
                data = read()
                username, password = parse_credentials(data)
                
                if not username or not password:
                    red_led.on()
                    print("Error:Data format incorrect", data)
                    continue
                
                #Line_mode_shifter:                         
                if machine == "antares":
                    send_antares(keyboard, username, password)

                elif machine == "1040":
                    send_bec1040(keyboard, username, password)
                
                elif machine == "dmc":
                    send_dmc(keyboard, username, password)
                
                else:
                    red_led.on()
                    print("Not found machine name error.Please change name.")
                    raise NameError("Not found machine name.")
                wait_until_card_removed(reader)
                
            elif mode == "write":
                cmd = sys.stdin.readline().strip()

                if not cmd:
                    continue

                print("CMD from PC:", cmd)

                # handshake
                if cmd == "PING":
                    print("READY")

                # write command
                elif cmd.startswith("WRITE:"):
                    print("DATA_OK")

                    try:
                        payload = cmd.replace("WRITE:", "")
                        user, pwd = payload.split("/")

                        write_card(user, pwd)

                        print("WRITTEN")
                        print("DONE")

                    except Exception as e:
                        print("ERROR", e)

            time.sleep(0.05)
            

            




            
            
