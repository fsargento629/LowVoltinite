#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pin_to_circuit = 7


def change_file(state):
    data=str(datetime.datetime.now())
    f = open("data_luzes.txt","a")
    
    f.write(data)
    f.write(",")
    #print("State = " + state)
    f.write(str(state))
    f.write(";\n")
def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    old_input = 0
    while True:
       print(rc_time(pin_to_circuit))
       new_input = rc_time(pin_to_circuit)
       if new_input != old_input:
           print("Cool!")
           change_file(new_input)
       old_input = new_input

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup() 