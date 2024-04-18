import machine
import utime

# Initialize the ADC for IR sensor reading on GP26
analog_value = machine.ADC(26)

# Initialize the LED control pin
gp14 = machine.Pin(14, machine.Pin.OUT)

gp15.value(1)
while True:  # Use True instead of False to create an infinite loop
    reading = analog_value.read_u16()
   
    if reading > 60000:  # Blocked IR senor
        gp14.value(1)  # Turn on the LED connected to GP14
    else:
        gp14.value(0)  # Not Blocked IR senor Turn off the LED connected to GP14
       
    print("IR sensor: ", reading)
    utime.sleep(1)  