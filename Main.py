#-------
import machine
import network
import usocket as socket
import utime as time
import _thread
import json


# Configure GP14 as output and define it as redLED_pin 
waterled = machine.Pin(2, machine.Pin.OUT)
temperature_sensor = machine.ADC(27)
RedLed= machine.Pin(14, machine.Pin.OUT)
analog_value = machine.ADC(26)

# Initialize the LED control pin
gp9 = machine.Pin(9, machine.Pin.OUT)


waterled_status = "Off" # Define a variable called redLED_status and set it to "Off"
def getwater_status():
    return "On" if waterled.value() == 1 else "Off"
def getRedLed_status():
    return "On" if RedLed.value() == 1 else "Off"

def getREd():
    return "On" if gp9.value() == 1 else "Off"
def getyellowLed_status():
    return "On" if RedLed.value() == 1 else "Off"

# Define a function to get the red LED status
def check_adc_and_control_redLED():
# Initialize ADC object)


# Main loop
    while True:
        
        adc_value = temperature_sensor.read_u16()
        if(adc_value<54000):
            #alert the user that temperature is rising
            RedLed.value(1)
            
            
        else:
            #turn of light after threat is gone
            RedLed.value(0)
            
        # Print temperature voltage value

        reading = analog_value.read_u16()
   
        if reading > 60000:  # Blocked IR senor
            gp9.value(1)  # Turn on the LED connected to GP9
        else:
            gp9.value(0)  # Not Blocked IR senor Turn off the LED connected to GP9
       
        print("Temperature Sensor:"+str(adc_value)+" Status of AL:"+str(getRedLed_status())+" IR sensor: "+str(reading)+" Alert:"+str(getREd()))
    
        time.sleep(1)
# Note that the function returns the status.

# Define a function to periodically check the ADC pin and control the red LED pin.

ssid = 'RPI_PICO_BH'       #Set access point name 
password = '15646666'       #Set your access point password
ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password)
ap.active(True)            #activating

while ap.active() == False:
  pass
print('Connection is successful')
print(ap.ifconfig())

# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Below given code defines the web page response. Your html code must be used in this section.
# 
# Define HTTP response
def web_page():
    redLED_status = getRedLed_status()
    #greenLED = "green" if redLED_status == "Off" else "black"
    
# Modify the html portion appropriately.
# Style section below can be changed.
# In the Script section some changes would be needed (mostly updating variable names and adding lines for extra elements). 

    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lion Farms Interface</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Tilt+Warp&display=swap" rel="stylesheet">
    <style>
        html,body {
            height: 100%;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: rgb(203, 125, 243);
        }
        .container {
            text-align: center;
        }
        .f {
            font-size: 50px;
            margin-top: 100px; 
            font-family: 'Tilt Warp';
        }
        .whitebox {
            background-color: rgb(238, 235, 231);
            width: 400px;
            height: 80px;
            font-family: 'Tilt Warp';
            font-size: 35px;
            margin-top: 20px;
        }
        .brown-box {
            background-color:rgb(149, 81, 32);
            width: 400px;
            height: 400px;
            margin-top: 20px;
        }
        .orange-box {
            background-color: darkorange;
            width: 80px;
            height: 80px;
            font-family: 'Tilt Warp';
            position: relative;
            top: -400px;
        }
        .green-plant {
            width: 0;
            height: 0;
            border-left: 20px solid transparent;
            border-right: 20px solid transparent;
            border-bottom: 20px solid rgb(56, 190, 56);
            position: relative;
            transform: rotate(180deg);
        }
        .temperature-alert {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            display: none;
            background-color: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        }
        .temperature-alert p {
            margin: 10px 0;
            font-size: 20px;
        }
        .temperature-alert button {
            font-size: 20px;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            background-color: rgb(149, 81, 32);
            color: white;
        }
        .small-blue-circle {
        width: 40px; /* Adjust the size as needed */
        height: 40px;
        background-color: blue;
        border-radius: 50%; /* This makes it a circle */
        /* Ensures it is displayed as a block-level element */
        }


    </style>
</head>
<body>
    <header>
        <hr/>
    </header>
    <div class="container">
        <div class="f">
             <div id="one" style="font-size:35px;margin-top: 200px;display: block" class="whitebox"> Farm Systems ✅ </div>
            <div id="two" style="font-size:35px;margin-top: 200px;display: none;" class="whitebox"> Intrusion Alert🚨</div>
            <div id="three" style="font-size:35px;margin-top: 200px;display: none;" class="whitebox"> Crop Damage Alert🔥🧊</div>
      
        </div>
        <div class="brown-box"></div>
        <div class="orange-box">House</div>
        <Row1>
            
            <plant1>
                <div style="top: -150px;left: 140px;" class="green-plant"></div>
                <div style="top: -150px;left: 140px;" class="green-plant"></div>
            </plant1>
            <plant2>
                <div style="top: -190px;left: 240px;" class="green-plant"></div>
                <div style="top: -190px;left: 240px;" class="green-plant"></div>
            </plant2>
            <plant3>
                <div style="top: -230px;left: 340px;" class="green-plant"></div>
                <div style="top: -230px;left: 340px;" class="green-plant"></div>
            </plant3>
        </Row1>
        <Row2>
            <plant1>
                <div style="top: -400px;left: 140px;" class="green-plant"></div>
                <div style="top: -400px;left: 140px;" class="green-plant"></div>
            </plant1>
            <plant2>
                <div style="top: -440px;left: 240px;" class="green-plant"></div>
                <div style="top: -440px;left: 240px;" class="green-plant"></div>
            </plant2>
            <plant3>
                <div style="top: -480px;left: 340px;" class="green-plant"></div>
                <div style="top: -480px;left: 340px;" class="green-plant"></div>
            </plant3>
        </Row2>
        <Row3>
            <plant1>
                <div style="top: -650px;left: 140px;" class="green-plant"></div>
                <div style="top: -650px;left: 140px;" class="green-plant"></div>
            </plant1>
            <plant2>
                <div style="top: -690px;left: 240px;" class="green-plant"></div>
                <div style="top: -690px;left: 240px;" class="green-plant"></div>
            </plant2>
            <plant3>
                <div style="top: -730px;left: 340px;" class="green-plant"></div>
                <div style="top: -730px;left: 340px;" class="green-plant"></div>
            </plant3>
        </Row3>
    </div>
    <div id="watersymbol" style="color:white;font-family: 'Tilt Warp';font-size:small;position:absolute;margin-top: -200px;margin-left: -150px  ;display: none;" class="small-blue-circle">Water</div>
    <checkbox style="margin-left: -250px">
        <p style="margin-top:500px;font-family: 'Tilt Warp';font-size: medium;">Water Plants</p>
        <input style="margin-left: 40px" id="checkbox1" type="checkbox" onchange="toggleLED()">
    </checkbox>
    <checkbox3 >
            <p style="margin-top:650px;margin-left: -150px;font-family: 'Tilt Warp';font-size: medium;"> Provide Artifical Light Source</p>
            <input style="margin-left: -60px" id="PA" type="checkbox">
        </checkbox3>
  
    
    <script>
        function toggleLED() {
        if(document.getElementById("checkbox1").checked){
        document.getElementById("watersymbol").style.display="block";
        }
        else{
        document.getElementById("watersymbol").style.display="none";
        }
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "/status?waterled=" + (document.getElementById("checkbox1").checked ? "on" : "off"), true);
        xhr.send();
        }
    </script> 
    <script>  
    function image(){
        var redLedStatus = """+redLED_status+""";
            const x = document.getElementById("one");
            const x2=document.getElementById("two");
            const x3=document.getElementById("three");
           
        if (redLedStatus == "On") {
            x.style.display = "none";
            x3.style.display = "block";
        } 
        
        else {
            x.style.display = "block";
            x3.style.display = "none";
        }
      
    setInterval(image, 1000);
    </script> 
    }
</body>
</html>

"""
    return html
# --------------------------------------------------------------------
# This section could be tweaked to return status of multiple sensors or actuators.

# Define a function to get the status of the red LED.
# The function retuns status. 
def get_status(request):
    if "waterled=on" in request:
        waterled.value(1)
    elif "waterled=off" in request:
        waterled.value(0)
    status = {
        "water_status": getwater_status(),
    }
    return json.dumps(status)
# ------------------------------------------------------------------------

# -------------------------------------------------------------------------
# This portion of the code remains as it is.

# Start the ADC monitoring function in a separate thread
_thread.start_new_thread(check_adc_and_control_redLED, ())

# Create a socket server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

# --------------------------------------------------------------------------

# --------------------------------------------------------------------------

# This section of the code will have minimum changes. 
while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    if request:
        request = str(request)
        print('Content = %s' % request)

# this part of the code remains as it is. 
    if request.find("/status") == 6:
        response = get_status(request)
        conn.send("HTTP/1.1 200 OK\n")
        conn.send("Content-Type: application/json\n")
        conn.send("Connection: close\n\n")
        conn.sendall(response)
    else:
        response = web_page()
        conn.send("HTTP/1.1 200 OK\n")
        conn.send("Content-Type: text/html\n")
        conn.send("Connection: close\n\n")
        conn.sendall(response)
    conn.close()