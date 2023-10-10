from tkgpio import TkCircuit

# initialize the circuit inside the GUI

configuration = {
    "width": 300,
    "height": 200,
    "leds": [
        {"x": 50, "y": 40, "name": "LED 1", "pin": 21},
        {"x": 100, "y": 40, "name": "LED 2", "pin": 22},
        {"x": 150, "y": 40, "name": "LED 2", "pin": 23}
    ],
    "buttons": [
        {"x": 50, "y": 130, "name": "Press to toggle LED 2", "pin": 11},
        {"x": 100, "y": 130, "name": "Press to toggle LED 33", "pin": 12}
    ]
}

circuit = TkCircuit(configuration)
@circuit.run
def main ():
    
    # now just write the code you would use on a real Raspberry Pi
    
    from gpiozero import LED, Button
    from time import sleep
     
    
    led1 = LED(21)
    led2 = LED(22)
    led3 = LED(23)
    print("Iniciando")
    
    led1.blink(1)
    sleep(10)
    