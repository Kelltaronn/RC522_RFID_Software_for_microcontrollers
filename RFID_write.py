#============================================================================
# Imports:
import time
import sys
from main import write_card
#============================================================================
def rfid_write():
    cmd = sys.stdin.readline().strip()

    if not cmd:
        pass

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
            