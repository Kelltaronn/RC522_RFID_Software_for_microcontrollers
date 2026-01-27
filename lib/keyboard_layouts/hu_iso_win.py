# HU ISO Windows scancode layout
from lib.keyboard_layouts import keyboard

class hidkeyboard:
    
    k = keyboard.Keyboard()

    keys = {

        # ---------------- LETTERS ----------------
        "a": [0x04], "A": [k.MOD_LEFT_SHIFT, 0x04],
        "b": [0x05], "B": [k.MOD_LEFT_SHIFT, 0x05],
        "c": [0x06], "C": [k.MOD_LEFT_SHIFT, 0x06],
        "d": [0x07], "D": [k.MOD_LEFT_SHIFT, 0x07],
        "e": [0x08], "E": [k.MOD_LEFT_SHIFT, 0x08],
        "f": [0x09], "F": [k.MOD_LEFT_SHIFT, 0x09],
        "g": [0x0A], "G": [k.MOD_LEFT_SHIFT, 0x0A],
        "h": [0x0B], "H": [k.MOD_LEFT_SHIFT, 0x0B],
        "i": [0x0C], "I": [k.MOD_LEFT_SHIFT, 0x0C],
        "j": [0x0D], "J": [k.MOD_LEFT_SHIFT, 0x0D],
        "k": [0x0E], "K": [k.MOD_LEFT_SHIFT, 0x0E],
        "l": [0x0F], "L": [k.MOD_LEFT_SHIFT, 0x0F],
        "m": [0x10], "M": [k.MOD_LEFT_SHIFT, 0x10],
        "n": [0x11], "N": [k.MOD_LEFT_SHIFT, 0x11],
        "o": [0x12], "O": [k.MOD_LEFT_SHIFT, 0x12],
        "p": [0x13], "P": [k.MOD_LEFT_SHIFT, 0x13],
        "q": [0x14], "Q": [k.MOD_LEFT_SHIFT, 0x14],
        "r": [0x15], "R": [k.MOD_LEFT_SHIFT, 0x15],
        "s": [0x16], "S": [k.MOD_LEFT_SHIFT, 0x16],
        "t": [0x17], "T": [k.MOD_LEFT_SHIFT, 0x17],
        "u": [0x18], "U": [k.MOD_LEFT_SHIFT, 0x18],
        "v": [0x19], "V": [k.MOD_LEFT_SHIFT, 0x19],
        "w": [0x1A], "W": [k.MOD_LEFT_SHIFT, 0x1A],
        "x": [0x1B], "X": [k.MOD_LEFT_SHIFT, 0x1B],
        "y": [0x1D], "Y": [k.MOD_LEFT_SHIFT, 0x1D],
        "z": [0x1C], "Z": [k.MOD_LEFT_SHIFT, 0x1C],

        # Magyarbetűk kívételek (Ezekt küldi a magyarbillenytűzet.
        "á": [0x34], "Á": [k.MOD_LEFT_SHIFT, 0x34],
        "é": [0x33], "É": [k.MOD_LEFT_SHIFT, 0x33],
        "í": [0x64], "Í": [k.MOD_LEFT_SHIFT, 0x2F],
        "ó": [0x2E], "Ó": [k.MOD_LEFT_SHIFT, 0x2E],
        "ö": [0x27], "Ö": [k.MOD_LEFT_SHIFT, 0x27],
        "ő": [0x2F], "Ő": [k.MOD_LEFT_SHIFT, 0x2F],
        "ú": [0x30], "Ú": [k.MOD_LEFT_SHIFT, 0x30],
        "ü": [0x2D], "Ü": [k.MOD_LEFT_SHIFT, 0x2D],
        "ű": [0x32], "Ű": [k.MOD_LEFT_SHIFT, 0x32],

        # ---------------- NUMBERS ----------------
        "0": [0x35], 
        "1": [0x1E], "2": [0x1F], "3": [0x20],
        "4": [0x21], "5": [0x22], "6": [0x23],
        "7": [0x24], "8": [0x25], "9": [0x26],

        # ---------------- SPECIAL_SYMBOLS ----------------
        "!": [k.MOD_LEFT_SHIFT, 0x1E],
        '\\': [k.MOD_RIGHT_ALT, 0x14], #"Kettõbõl lesz egy"
        "+": [k.MOD_LEFT_SHIFT, 0x20],
        "!": [k.MOD_LEFT_SHIFT, 0x21],
        "?": [k.MOD_LEFT_SHIFT, 0x36],
        "/": [k.MOD_LEFT_SHIFT, 0x23],
        "(": [k.MOD_LEFT_SHIFT, 0x25],
        ")": [k.MOD_LEFT_SHIFT, 0x26],
        '"': [k.MOD_LEFT_SHIFT, 0x1F],
        "$": [k.MOD_RIGHT_ALT, 0x33], #"Alt + é"
        "%": [k.MOD_LEFT_SHIFT, 0x22],
        "&": [k.MOD_RIGHT_ALT, 0x06],
        "=": [k.MOD_LEFT_SHIFT, 0x24],
        "@": [k.MOD_RIGHT_ALT, 0x19],

        # ---------------- PUNCTUATION / SYMBOLS ----------------
        " ": [0x2C],
        ",": [0x36], ";": [k.MOD_RIGHT_ALT, 0x36],
        ".": [0x37], ":": [k.MOD_LEFT_SHIFT, 0x37],
        "-": [0x38], "_": [k.MOD_LEFT_SHIFT, 0x38],

        "'": [0x31], "*": [k.MOD_LEFT_SHIFT, 0x31],
        "`": [0x35], "~": [k.MOD_LEFT_SHIFT, 0x35],

        "<": [0x64], ">": [k.MOD_LEFT_SHIFT, 0x64],
        # ---------------- CONTROL CHARACHTERS ----------------
        #Lenti részben inkább külön funkció lett rájuk írva:
        
        #"\t":  [0x2B],#TAB
        #"\n":  [0x28], #ENTER 
    }

    def _find_char_and_send(self, character : str) -> None:
        if character in self.keys:
            values = self.keys[character]
            if len(values) > 1:
                self.k.press(values[0], values[1])
            else:
                self.k.press(values[0])
            self.k.release_all()

    def write(self, string_data : str) -> None:
        for s in string_data:
            self._find_char_and_send(s)
            
    def tab(self):
        self.k.press(0x2B)
        self.k.release_all()
        
    def enter(self):
        self.k.press(0x28)
        self.k.release_all()
