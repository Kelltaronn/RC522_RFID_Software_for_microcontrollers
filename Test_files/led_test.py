from machine import Pin, Timer
from time import sleep, ticks_ms, ticks_diff
#============================================================================
#DESCRIPTION:
#Testing LEDS to had been soldered correctly.
#============================================================================
frequency = 10
blink_time = 5
def blink_for_time(led, freq, duration_sec):
    period = 1 / freq
    start = ticks_ms()

    while ticks_diff(ticks_ms(), start) < duration_sec * 1000:
        led.on()
        sleep(period / 2)
        led.off()
        sleep(period / 2)


red_led = Pin(13, Pin.OUT)
yellow_led = Pin(12, Pin.OUT)
green_led = Pin(11,Pin.OUT)

blink_for_time(red_led, frequency, blink_time)
blink_for_time(yellow_led, frequency, blink_time)
blink_for_time(green_led, frequency, blink_time)