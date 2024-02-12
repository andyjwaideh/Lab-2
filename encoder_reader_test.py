import pyb
import time

from encoder_reader import Encoder

def test_encoder(encoder):
    
    print (encoder.read())
    
    for _ in range(20):
        encoder.update_position(1)
        print encoder.read())
        time.sleep(1) #we can adjust delay
        
    time.sleep(2)
    
    # Turning motor by hand
    
    for _ in range(20):
        enoder.update_position(-1)
        print(encoder.read())
        time.sleep(0,1) #adjust
    
    print(encoder.read())
    
    
    # Run the motor under power
    for _ in range(10):
        
        pyb.LED(1).toggle()
        time.sleep(0.5) #Adjust
        
        print (encoder.read())
        time.sleep(0.1) #Adjust

if__name__ == "__main__"
    encoder = Encoder(tiner=2, pin_a)
    
    test_encoder(encoder)
        