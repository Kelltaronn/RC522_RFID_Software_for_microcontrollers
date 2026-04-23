from lib.keyboard_layouts import hu_iso_mac, hu_iso_win, en_iso_win
#============================================================================
#TESTS:
#============================================================================
#DESCRIPTION:
#This file is for testing the HID interface.
#============================================================================
#Defining keyboard object:
k = en_iso_win.hidkeyboard()
#============================================================================
#KEYBOARD_TESTS:
#============================================================================

data_HU = "1234567890öüóqwertzuiíopőúasdfghjkléáűyxcvbnm,.-"
#OUTPUT:  
        #"1234567890   qwertzui op  asdfghjkl   yxcvbnm,.-"

data_en = "1234567890qwertzuiopasdfghjklyxcvbnm,.-"
#OUTPUT:  
           #1234567890qwertzuiopasdfghjklyxcvbnm,.-

#Keyboard letters with shift pressed:
data_shift = '!\\"$%&/()ÖÜÓQWERTZUIOPŐÚASDFGHJKLÉÁŰYXCVBNM,;.:_@?'
#OUTPUT:
                #         
data_shift_en ='!\\"$%&/()QWERTZUIOPASDFGHJKLYXCVBNM,;.:_@?'
#OUTPUT:        
                #! \"$%&/()QWERTZUIOPASDFGHJKLYXCVBNM,;.:_@?

#Simple letters of ABC:
data_all = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
#OUTPUT:
           #a b c d e f g h i j k l m n o p q r s t u v w x y z
#============================================================================
#OUTPUTS:
#============================================================================
k.write(data_HU)
k.write(data_en)


