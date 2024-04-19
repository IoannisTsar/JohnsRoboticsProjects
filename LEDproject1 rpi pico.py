import machine
import utime

led1 = machine.Pin(13, machine.Pin.OUT)
led2 = machine.Pin(14, machine.Pin.OUT)
led3 = machine.Pin(15, machine.Pin.OUT)

led1.value(0)
led2.value(0)
led3.value(0)

while True:
    led1.value(1)
    utime.sleep(0.1)
    led1.value(0)
    led2.value(1)
    utime.sleep(0.1)
    led2.value(0)
    led3.value(1)
    utime.sleep(0.1)
    led3.value(0)
    led2.value(1)
    utime.sleep(0.1)
    led2.value(0)