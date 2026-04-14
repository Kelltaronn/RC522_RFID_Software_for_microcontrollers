
import sys
import serial
import serial.tools.list_ports
import threading
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QLineEdit, QTextEdit, QComboBox, QLabel
)


class RFIDApplication(QWidget):
    def __init__(self):
        super().__init__()

        self.ser = None
        self.state = "WAIT_READY"

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # COM selector
        self.port_box = QComboBox()
        self.refresh_ports()
        layout.addWidget(QLabel("Select COM Port:"))
        layout.addWidget(self.port_box)

        self.refresh_btn = QPushButton("Refresh Ports")
        self.refresh_btn.clicked.connect(self.refresh_ports)
        layout.addWidget(self.refresh_btn)

        self.connect_btn = QPushButton("Connect")
        self.connect_btn.clicked.connect(self.connect_serial)
        layout.addWidget(self.connect_btn)

        # Username / Password
        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")
        layout.addWidget(self.username)

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        layout.addWidget(self.password)

        self.send_btn = QPushButton("Write to RFID")
        self.send_btn.clicked.connect(self.send_write)
        layout.addWidget(self.send_btn)

        # Log output
        self.log = QTextEdit()
        self.log.setReadOnly(True)
        layout.addWidget(self.log)

        self.setLayout(layout)
        self.setWindowTitle("RFID Writer")

    # -------------------------
    # SERIAL PORT HANDLING
    # -------------------------
    def refresh_ports(self):
        self.port_box.clear()
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.port_box.addItem(port.device)

    def connect_serial(self):
        port = self.port_box.currentText()

        try:
            self.ser = serial.Serial(port, 9600, timeout=1)
            self.log.append(f"Connected to {port}")

            threading.Thread(target=self.read_thread, daemon=True).start()

            self.send("PING")

        except Exception as e:
            self.log.append(f"Connection error: {e}")

    # -------------------------
    # SERIAL COMMUNICATION
    # -------------------------
    def send(self, cmd):
        if self.ser:
            self.ser.write((cmd + "\n").encode())

    def read_thread(self):
        while True:
            try:
                line = self.ser.readline()
                if line:
                    text = line.decode().strip()
                    self.handle_line(text)
            except:
                pass

    # -------------------------
    # STATE MACHINE
    # -------------------------
    def handle_line(self, line):
        self.log.append(f"[PICO] {line}")

        if self.state == "WAIT_READY":
            if line == "READY":
                self.log.append("Ready for write")

        elif self.state == "WAIT_DONE":
            if line == "DONE":
                self.log.append("RFID write finished")
                self.state = "WAIT_READY"

    def send_write(self):
        user = self.username.text()
        pw = self.password.text()

        if not user or not pw:
            self.log.append("Username/password missing")
            return

        self.send(f"WRITE:{user}/{pw}")
        self.state = "WAIT_DONE"


# -------------------------
# RUN APP
# -------------------------
app = QApplication(sys.argv)
window = RFIDApplication()
window.show()
sys.exit(app.exec())