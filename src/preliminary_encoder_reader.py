import pyb
import time
"""
     Here we can read encoder signals using a timer. While using a
     specific Timer number and pins. 
     
     
     Where,
     tim8 (pyb.Timer): The Pyboard Timer instance where timer 8 was used
     
     ch1 (tim8.channel): Is the first encoder channel using timer 8
                         channel 1
                         
     ch2 (tim8.channel): Is the second encoder channel using timer 8
                         channel 1
"""

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
    """
     Reads the counter value of the Timer.
     
     int: The counter value.
    """    
    print(tim8.counter())
    time.sleep(1)
    

