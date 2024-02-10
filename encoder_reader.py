"""
Created on Fri Feb  9 13:40:38 2024

@author: andyjwaideh
"""
import pyb
import time


class Encoder:
    
    def __init__(self, enc_name, pin1, pin2, timer):
        
        #initialize encoder pins
        self.enc_name = enc_name
        self.pin1 = pyb.Pin(pin1, pyb.Pin.OUT_PP)
        self.pin2 = pyb.Pin(pin2, pyb.Pin.OUT_PP)
        
        #initialize timer channels
        self.tim = pyb.Timer(timer, prescaler=0, period=0xFFFF)
        self.ch1 = self.tim.channel(1, pyb.Timer.ENC_AB, pin=pin1) 
        self.ch2 = self.tim.channel(2, pyb.Timer.ENC_AB, pin=pin2)
        
        
    def read(self):
        
        # Alia's code here
        
        
        yield self.tim.count()
        
    def zero(self):
        
        self.tim.counter(0)
        yield self.tim.count()
        

if __name__ == "__main__":

    enc1 = Encoder("enc1", pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
    enc2 = Encoder("enc2", pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
    
    read_enc1 = enc1.read()
    read_enc2 = enc2.read()
    
    
    # continues to read encoder values for testing until "Ctrl-C" is pressed
    while True:
        try:
            #iterate class
            next(read_enc1)
            next(read_enc2)
            
            #make space between iterations
            print("")
            
            time.sleep(0.5)
        
        # Trying to catch the "Ctrl-C" keystroke to break out
        # of the program cleanly
        except KeyboardInterrupt:
            break
        
        
        
    
    