import machine
import utime as time

# Define ADC pin number
adcpin = 27       
# Initialize ADC object
temperature_sensor = machine.ADC(27)
RedLed= machine.Pin(9, machine.Pin.OUT)


# Main loop
while True:
    
    adc_value = temperature_sensor.read_u16()
    if(adc_value<51000):
        #alert the user that temperature is rising
        RedLed.value(1)
        
    else:
         #turn of light after threat is gone
        RedLed.value(0)
    # Print temperature voltage value
    print("Temperature Sensor", adc_value)
   
    time.sleep(1)
