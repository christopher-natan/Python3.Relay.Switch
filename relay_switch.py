# @author        Christopher M. Natan
# @version       1.0

import RPi.GPIO as GPIO
GPIO_RELAY_PIN = 14


class RelaySwitch:
    def __init__(self):
        pass

    def set_gpio(self):
        print("Include amount gpio initialize..")
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_RELAY_PIN, GPIO.OUT)

    def turn(self, action):
        if action == 'on': self.on()
        if action == 'off': self.off()

    def on(self):
        self.set_gpio()
        if  self.get_state() == 1:
            print ('Turning on')
            GPIO.output(GPIO_RELAY_PIN, GPIO.HIGH)

    def off(self):
        self.set_gpio()
        if  self.get_state() == 0:
            print ('Turning off')
            GPIO.cleanup()

    def get_state(self):
        state = GPIO.input(GPIO_RELAY_PIN)
        print('Current state is ' + str(state))
        return state
