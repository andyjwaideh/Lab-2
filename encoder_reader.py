"""
Created on Fri Feb  9 13:40:38 2024
"""
import pyb
import time


class Encoder:
    """!
     This class represents an incremental encoder connected to our
     given microcontoller. Where we have the following attrivutes:
     
     enc_name : Is the name of the encoder
     pin1 (pyb.Pin): This pin is representing encoder channel A.
     
     pin2 (pyb.Pin): This pin is representing encoder channel B.
     
     Timer (pyb.Timer): The timer used for the encoder counting.
                        Using the manuel given for our board, we
                        set timer 4 and timer 8 for our encoders.
                        
     @author Alia Wolken, Eduardo Santos, Andrew Jwaideh
     """
    
    def __init__(self, enc_name, pin1, pin2, timer):
        """
        Here we initialize the Encoder Object. Where we have the
        following:
        
        enc_name: The name given to the encoder
        pin1 (int): The pin number for the first encoder channel.
        pin2 (int): The pin number for the second encoder channel.
        timer_num (int): The number of the timer to be used, in this
                         lab we combined both AB to the same timer.
        
        """
        
        #initialize encoder pins
        self.enc_name = enc_name
        self.pin1 = pyb.Pin(pin1, pyb.Pin.OUT_PP)
        self.pin2 = pyb.Pin(pin2, pyb.Pin.OUT_PP)
        
        #initialize timer channels
        self.tim = pyb.Timer(8, prescaler=0, period=0xFFFF)
        self.ch1 = self.tim.channel(1, pyb.Timer.ENC_AB, pin=pin1) 
        self.ch2 = self.tim.channel(2, pyb.Timer.ENC_AB, pin=pin2)
        
        #self.tim.counter(0) # set to zero when initialize
        
    def read(self):
        """
         Reads the current count of the encoder.
         
         When it returns;
         
         int: The current count of the encoder
        """        
        while True:
            # Alia's code here
            # add delta (pos - prev_pos) to previous position
            
            print('words')
            # calculate delta in count
            
            # if delta > (AR+1)/2 :
                # delta -= (AR+1) # underflow
            
            # if delta < (AR+1)/2 :
                # delta += (AR+1) # overflow
                
            # add up delta vals
            
            self.counter_val = self.tim.counter()
            print('counter_val before yield',self.counter_val)
            yield self.counter_val # gives us current position
            print('counter_val after yield',self.counter_val)
        
    def zero(self):
        """
         Resets the encoder back to zero.
         
         When it returns;
         
         int: The new count after resetting back to zero.
        """       
        self.tim.counter(0)
        yield self.tim.counter()
        

if __name__ == "__main__":

    #enc1 = Encoder("enc1", pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
    enc2 = Encoder("enc2", pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
    
    #read_enc1 = enc1.read()
    read_enc2 = enc2.read()
    #print('read_enc2',read_enc2)
    
    #read_enc2 = Encoder.read(4)
    
    
    # continues to read encoder values for testing until "Ctrl-C" is pressed
    while True:
        try:
            #iterate class
            #next(read_enc1)
            print('loop')
            next(read_enc2) # recalls defn, updates position with Alia code
            print('at next')
            
            #make space between iterations
            print("")
            
            time.sleep(0.5)
        
        # Trying to catch the "Ctrl-C" keystroke to break out
        # of the program cleanly
        except KeyboardInterrupt:
            break
        
        
        
    
    