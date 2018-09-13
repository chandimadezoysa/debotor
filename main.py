import RPi.GPIO as GPIO
import time

from bottle import request, route, run, static_file, template, response

# start with BCM
GPIO.setmode(GPIO.BCM)

#WHEELS

WHEELS_PIN1 = 7
WHEELS_PIN2 = 8
WHEELS_PIN3 = 9

TIMEOUT = 5

def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

@route('/')
def index():
    enable_cors()
    return template('index.html')

def wheelsSetup():
    print("Setup wheels")
    GPIO.setup([WHEELS_PIN1, WHEELS_PIN2, WHEELS_PIN3], GPIO.OUT)
    return

@route('/forward')
def moveForward():
    enable_cors()
    wheelsSetup()

    print("Move forward start")

    GPIO.output([WHEELS_PIN1, WHEELS_PIN2, WHEELS_PIN3], GPIO.HIGH)
    time.sleep(TIMEOUT)

    GPIO.output([WHEELS_PIN1, WHEELS_PIN2, WHEELS_PIN3], GPIO.LOW)

    print("Move forward end")

    return template('index.html')

@route('/backward')
def moveBackward():
    enable_cors()
    wheelsSetup()

    print("Move backward start")

    GPIO.output([WHEELS_PIN1, WHEELS_PIN2], GPIO.HIGH)
    GPIO.output([WHEELS_PIN3], GPIO.LOW)
    time.sleep(TIMEOUT)

    GPIO.output([WHEELS_PIN1, WHEELS_PIN2, WHEELS_PIN3], GPIO.LOW)

    print("Move backward end")

    return template('index.html')

@route('/left')
def moveLeft():
    enable_cors()
    wheelsSetup()

    print("Move left start")

    GPIO.output([WHEELS_PIN1], GPIO.HIGH)
    GPIO.output([WHEELS_PIN2, WHEELS_PIN3], GPIO.LOW)
    time.sleep(TIMEOUT)

    GPIO.output([WHEELS_PIN1, WHEELS_PIN2, WHEELS_PIN3], GPIO.LOW)

    print("Move left end")

    return template('index.html')

@route('/right')
def moveRight():
    enable_cors()
    wheelsSetup()

    print("Move right start")

    GPIO.output([WHEELS_PIN2], GPIO.HIGH)
    GPIO.output([WHEELS_PIN1, WHEELS_PIN3], GPIO.LOW)
    time.sleep(TIMEOUT)

    GPIO.output([WHEELS_PIN1, WHEELS_PIN2, WHEELS_PIN3], GPIO.LOW)

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