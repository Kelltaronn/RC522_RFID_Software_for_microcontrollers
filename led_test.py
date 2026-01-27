import time, os, sys
from lib.mfrc522 import SimpleMFRC522
from lib.keyboard_layouts import klavye
from machine import Pin, Timer
from time import sleep, ticks_ms, ticks_diff

red_led = Pin(13, Pin.OUT)
yellow_led = Pin(12, Pin.OUT)
green_led = Pin(11,Pin.OUT)

red_led.on()
red_led.on()
yellow_led.on()
green_led.on()