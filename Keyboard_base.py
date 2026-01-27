from lib.keyboard_layouts import klavye
from lib.keyboard_layouts import hu_iso_mac, hu_iso_win, en_iso_win,

#Tests:
#k = klavye.hidkeyboard()
k = en_iso_win.hidkeyboard()
data = "1234567890öüóqwertzuiíopőúasdfghjkléáűyxcvbnm,.-"
        #"1234567890   qwertzui op  asdfghjkl   yxcvbnm,.-"
data_en = "1234567890qwertzuiopasdfghjklyxcvbnm,.-"
           #1234567890qwertzuiopasdfghjklyxcvbnm,.-
        
data_shift = '!\\"$%&/()ÖÜÓQWERTZUIOPŐÚASDFGHJKLÉÁŰYXCVBNM,;.:_@?'
                  
data_shift_en ='!\\"$%&/()QWERTZUIOPASDFGHJKLYXCVBNM,;.:_@?'        
                #! \"$%&/()QWERTZUIOPASDFGHJKLYXCVBNM,;.:_@?
data_all = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
           #a b c d e f g h i j k l m n o p q r s t u v w x y z

#k.write(data)
k.write(data_en)


