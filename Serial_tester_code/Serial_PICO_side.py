import sys
import time

print("READY")

buffer = ""

while True:
    line = sys.stdin.readline().strip()
    if line == "PING":
        print("READY")
    # -------------------
    # WRITE COMMAND
    # -------------------
    elif line.startswith("WRITE:"):
        print("DATA_OK")

        payload = line.replace("WRITE:", "")

        # fake RFID write
        time.sleep(2)

        print("WRITTEN")
        print("DONE")
        print("READY")