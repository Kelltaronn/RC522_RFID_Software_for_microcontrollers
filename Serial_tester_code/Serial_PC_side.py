import serial
import time
import threading

ser = serial.Serial('/dev/cu.usbmodem11301', 9600, timeout=1)

time.sleep(2)

state = "WAIT_READY"
latest_line = None
lock = threading.Lock()


# -------------------------
# READ THREAD
# -------------------------
def read_from_pico():
    global latest_line

    while True:
        line = ser.readline()

        if line:
            try:
                text = line.decode().strip()

                with lock:
                    latest_line = text

                print("[PICO]", text)

            except:
                pass


# -------------------------
# WRITE HELP
# -------------------------
def send(cmd):
    ser.write((cmd + "\n").encode())


# -------------------------
# START THREAD
# -------------------------
threading.Thread(target=read_from_pico, daemon=True).start()



# -------------------------
# MAIN STATE MACHINE
# -------------------------
send("PING")
while True:
    time.sleep(0.05)

    with lock:
        line = latest_line
        latest_line = None

    if not line:
        continue

    # -------------------------
    # STATE LOGIC
    # -------------------------

    if state == "WAIT_READY":
        if line == "READY":
            print("Pico ready → asking user input")

            username = input("Username: ")
            password = input("Password: ")

            send(f"WRITE:{username}/{password}")

            state = "WAIT_DONE"


    elif state == "WAIT_DONE":
        if line == "DONE":
            print("RFID write finished")
            state = "WAIT_READY"