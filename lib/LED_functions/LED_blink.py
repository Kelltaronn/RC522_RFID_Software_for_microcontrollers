from time import sleep, ticks_ms, ticks_diff

def blink_for_time(led, freq, duration_sec):
    period = 1 / freq
    start = ticks_ms()

    while ticks_diff(ticks_ms(), start) < duration_sec * 1000:
        led.on()
        sleep(period / 2)
        led.off()
        sleep(period / 2)