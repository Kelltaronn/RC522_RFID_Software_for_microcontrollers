import serial
import time
import threading

ser = serial.Serial('/dev/cu.usbmodem11301', baudrate=9600, timeout=1)

time.sleep(2)


# -------------------------
# 🔵 READ THREAD (Pico → PC)
# -------------------------
def read_from_pico():
    while True:
        line = ser.readline()

        if not line:
            continue

        try:
            text = line.decode('utf-8').strip()
            print("[PICO]", text)
        except Exception as e:
            print("Decode error:", e)


# -------------------------
# 🟢 WRITE LOOP (PC → Pico)
# -------------------------
def write_to_pico():
    while True:
        cmd = input("Send command: ")
        ser.write((cmd + "\n").encode('utf-8'))


# -------------------------
# START BOTH
# -------------------------
t1 = threading.Thread(target=read_from_pico, daemon=True)
t1.start()

write_to_pico()

#WRITE THIS TO THE PICO TO TEST THE SERIAL COMMUNICATION:
'''
import sys
import time
import select


while True:
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        cmd = sys.stdin.readline().strip()

        if cmd:
            print("RECEIVED:", cmd)

            if cmd == "LED_ON":
                print("LED would turn ON here")

            elif cmd == "PING":
                print("PONG")

    time.sleep(0.01)
'''