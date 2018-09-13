import RPi.GPIO as GPIO
import time

from bottle import request, route, run, static_file, template

# start with BCM
GPIO.setmode(GPIO.BCM)

#WHEELS

WHEELS_PIN1 = 7
WHEELS_PIN2 = 8
WHEELS_PIN3 = 9

TIMEOUT = 5

@route('/')
def index():
    return template('index.html')

def wheelsSetup():
    print("Setup wheels")
    GPIO.setup([WHEELS_PIN1, WHEELS_PIN2, WHEELS_PIN3], GPIO.OUT)
    return

@route('/forward')
def moveForward():
    wheelsSetup()

    print("Move forward start")

    GPIO.output([WHEELS_PIN1, WHEELS_PIN2, WHEELS_PIN3], GPIO.HIGH)
    time.sleep(TIMEOUT)

    GPIO.cleanup([WHEELS_PIN1, WHEELS_PIN2, WHEELS_PIN3])

    print("Move forward end")

    return template('index.html')

@route('/backward')
def moveBackward():
    wheelsSetup()

    print("Move backward start")

    GPIO.output([WHEELS_PIN1, WHEELS_PIN2], GPIO.HIGH)
    GPIO.output([WHEELS_PIN3], GPIO.LOW)
    time.sleep(TIMEOUT)

    GPIO.cleanup([WHEELS_PIN1, WHEELS_PIN2, WHEELS_PIN3])

    print("Move backward end")

    return template('index.html')

@route('/left')
def moveLeft():
    wheelsSetup()

    print("Move left start")

    GPIO.output([WHEELS_PIN1], GPIO.HIGH)
    GPIO.output([WHEELS_PIN2, WHEELS_PIN3], GPIO.LOW)
    time.sleep(TIMEOUT)

    GPIO.cleanup([WHEELS_PIN1, WHEELS_PIN2, WHEELS_PIN3])

    print("Move left end")

    return template('index.html')

@route('/right')
def moveRight():
    wheelsSetup()

    print("Move right start")

    GPIO.output([WHEELS_PIN2], GPIO.HIGH)
    GPIO.output([WHEELS_PIN1, WHEELS_PIN3], GPIO.LOW)
    time.sleep(TIMEOUT)

    GPIO.cleanup([WHEELS_PIN1, WHEELS_PIN2, WHEELS_PIN3])

    print("Move right end")

    return template('index.html')

def blinkLight():
    print("Blink light")
    GPIO.setup(RED_LIGHT, GPIO.OUT)

    try:
        for x in range(5):
            print("Looping")
            # do stuff
            GPIO.output(RED_LIGHT, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(RED_LIGHT, GPIO.LOW)
            time.sleep(1)

    finally:
        GPIO.cleanup()

run(host='0.0.0.0', port=80)