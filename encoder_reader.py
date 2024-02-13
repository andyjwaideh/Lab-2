"""
Created on Fri Feb  9 13:40:38 2024
"""
import pyb
import time


class Encoder:
    """!
     This class represents an incremental encoder connected to our
     given microcontoller. Where we have the following attributes:
     
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
        AR = 0xFFFF
        self.tim = pyb.Timer(timer, prescaler=0, period=AR) # period is AR, if just period w/out PS -> actual period in [s]
        self.ch1 = self.tim.channel(1, pyb.Timer.ENC_AB, pin=pin1) 
        self.ch2 = self.tim.channel(2, pyb.Timer.ENC_AB, pin=pin2)
        
        #self.tim.counter(0) # set to zero when initialize ?
        
    def read(self):
        """
         Reads the current count of the encoder.
         
         When it returns;
         
         int: The current count of the encoder
        """        
        
        # Alia's code here
 
        # calculate delta in count -> RETURN previous counter val
        # RETURN TUPLE store delta val
        
        # if delta > (AR+1)/2 :
            # delta -= (AR+1) # underflow
        
        # if delta < (AR+1)/2 :
            # delta += (AR+1) # overflow
            
        # add up delta vals -> RETURN total elapsed encoder pos += delta val

        # Previous code:
        self.counter_val = self.tim.counter() # counter_val
        self.counter_val_prev = self.counter_val
        print('counter_val before yield',self.counter_val_prev)
        #yield self.counter_val # gives us current position
        print('counter_val after yield',self.counter_val)
        
    def zero(self):
        """
         Resets the encoder back to zero.
         
         When it returns;
         
         int: The new count after resetting back to zero.
        """       
        self.tim.counter(0)
        #yield self.tim.counter()
        

if __name__ == "__main__":

    enc1 = Encoder("enc1", pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
    enc2 = Encoder("enc2", pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
    
    state = 0
    
    S0_INIT = 0
    S1_RUN = 1
    
    #read_enc1 = enc1.read()
    #read_enc2 = enc2.read()
    #print('read_enc2',read_enc2)
    
    #read_enc2 = Encoder.read(4)
    
    
    # continues to read encoder values for testing until "Ctrl-C" is pressed
    while True:
        try:
            if (state == S0_INIT):
                print('Init State')
                state = S1_RUN
            #iterate class
            #next(read_enc1)
            elif (state == S1_RUN):
                print('Run State')
                 
                read_enc1 = enc1.read()
                read_enc2 = enc2.read()
            else:
                pass
            
            print('loop')
            #next(read_enc2) # recalls defn, updates position with Alia code
            print('at next')
            
            #make space between iterations
            print("")
            
            time.sleep(0.5)
        
        # Trying to catch the "Ctrl-C" keystroke to break out
        # of the program cleanly
        except KeyboardInterrupt:
            break
        
        
        
    
    