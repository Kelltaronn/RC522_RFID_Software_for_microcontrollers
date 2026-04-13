import tkinter as tk
from tkinter import ttk
import serial
import serial.tools.list_ports
import threading

class RFIDWriterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RFID Writer")

        self.port_var = tk.StringVar()
        self.user_var = tk.StringVar()
        self.pass_var = tk.StringVar()

        ttk.Label(root, text="COM Port").pack()
        self.port_box = ttk.Combobox(root, textvariable=self.port_var)
        self.port_box.pack()

        ttk.Button(root, text="Refresh", command=self.refresh_ports).pack()

        ttk.Label(root, text="Username").pack()
        ttk.Entry(root, textvariable=self.user_var).pack()

        ttk.Label(root, text="Password").pack()
        ttk.Entry(root, textvariable=self.pass_var, show="*").pack()

        ttk.Button(root, text="WRITE CARD", command=self.write_card).pack()

        self.status = ttk.Label(root, text="")
        self.status.pack()

        self.refresh_ports()

    def refresh_ports(self):
        ports = [p.device for p in serial.tools.list_ports.comports()]
        self.port_box['values'] = ports

    def write_card(self):
        port = self.port_var.get()
        user = self.user_var.get()
        pwd = self.pass_var.get()

        try:
            ser = serial.Serial(port, 115200, timeout=2)
            
            cmd = f"WRITE|{user}|{pwd}\n"
            ser.write(cmd.encode())

            response = ser.readline().decode().strip()
            
            self.status.config(text="Response: " + response)
            ser.close()

        except Exception as e:
            self.status.config(text=str(e))


root = tk.Tk()
app = RFIDWriterApp(root)
root.mainloop()