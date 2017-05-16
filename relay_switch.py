# Copyright (c) CMNWorks
# Licensed under The MIT License
#
# @copyright     Copyright (c) CMNWorks Christopher M. Natan
# @author        Christopher M. Natan
# @link          http://cmnworks.com
# @license       http://www.opensource.org/licenses/mit-license.php MIT License

import RPi.GPIO as GPIO


GPIO_PIN = 14
TIME_OUT = 150000


class RelaySwitch:
    def __init__(self):
        pass

    def turn(self, state):
        GPIO.setup(GPIO_PIN, GPIO.IN)
        GPIO.setup(GPIO_PIN, GPIO.OUT)

        if state == 'off':
            print("I am off")
            GPIO.output(pin_switch, GPIO.LOW)
            self.get_state()
            GPIO.cleanup()

        if state == 'on':
            print("I am on")
            GPIO.output(pin_switch, GPIO.HIGH)
            self.get_state()

    def get_state(self):
        switch_state = GPIO.input(pin_switch)
        print('Current state is ' + str(switch_state))
        return switch_state
