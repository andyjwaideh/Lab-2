import pyb
import time

from encoder_reader import Encoder

def test_encoder(encoder):
    
    print (encoder.read()) # print initial val
    
    # Turning motor by hand
    for _ in range(20): 
        encoder.update_position(1)
        print (encoder.read())
        time.sleep(1) #we can adjust delay in data collection
        
    time.sleep(2)  
    print(encoder.read())
    
    # Run the motor under power
    for _ in range(10):
        
        pyb.LED(1).toggle() # gives power
        time.sleep(0.5) #Adjust
        
        print (encoder.read()) 
        time.sleep(0.1) #Adjust

if __name__ == "__main__":
    
    # encoder = Encoder(timer=2, pin_a) # add motor pins
    enc2 = Encoder("enc2", pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
    
    test_encoder(enc2)
        