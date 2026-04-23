import time
from lib.LED_functions.LED_blink import blink_for_time
#============================================================================
# Funkció_blokkok, Géptípusok:
#============================================================================ 
def manufacturing_machine(machine,progress_led,alarm_led,keyboard,user,pwd):

    frequency = 10
    blink_time = 10

    if machine == "antares":
        blink_for_time(progress_led,frequency,blink_time)
        keyboard.write(user)
        keyboard.tab()
        time.sleep(1)
        keyboard.write(pwd)
        keyboard.enter()

    elif machine == "1040":
        #Ciklus: USER,ENTER,PWD,ENTER,ENTER
        #Com_start:
        blink_for_time(progress_led, frequency, blink_time)
        
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
        progress_led.off()
            
    elif machine == "dmc":  
        #Com_start:
        blink_for_time(progress_led, frequency, blink_time)
        
        #Writing:
        keyboard.write(pwd)
        keyboard.enter()
        
        #Com_end:
        progress_led.off()
    else:
        alarm_led.on()
        raise ValueError
