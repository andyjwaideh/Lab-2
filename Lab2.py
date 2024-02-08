import pyb
import time

PinB6 = pyb.Pin(pyb.Pin.board.PB6, pyb.Pin.OUT_PP)
PinB7 = pyb.Pin(pyb.Pin.board.PB7, pyb.Pin.OUT_PP)
PinC6 = pyb.Pin(pyb.Pin.board.PC6, pyb.Pin.OUT_PP)
PinC7 = pyb.Pin(pyb.Pin.board.PC7, pyb.Pin.OUT_PP)



# tim4 = pyb.Timer(4, prescaler=0, period=0xFFFF) # Prof said to not use frequency need to instead prescalar set to zero and set the period instead
# ch1 = tim4.channel(1, pyb.Timer.ENC_AB, pin=PinB6)
# ch2 = tim4.channel(2, pyb.Timer.ENC_AB, pin=PinB7)

tim8 = pyb.Timer(8, prescaler=0, period=0xFFFF) # Prof said to not use frequency need to instead prescalar set to zero and set the period instead
ch1 = tim8.channel(1, pyb.Timer.ENC_AB, pin=PinC6) 
ch2 = tim8.channel(2, pyb.Timer.ENC_AB, pin=PinC7)

while True:
    print(tim8.counter())
    time.sleep(1)
    

