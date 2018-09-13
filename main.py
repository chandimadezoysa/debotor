import RPi.GPIO as GPIO
import time, threading

from bottle import request, route, run, static_file, template, response

# start with BCM
GPIO.setmode(GPIO.BCM)

#WHEELS

WHEELS_PIN1 = 7
WHEELS_PIN2 = 8
WHEELS_PIN3 = 9
EYES_LEFT_PIN = 3
EYES_RIGHT_PIN = 2
ANTENNA = 4

TIMEOUT = 5
TIMEOUT_ANTENNA = 0.5


def setup_eyes():
    print("Eyes lights")
    GPIO.setup([EYES_LEFT_PIN, EYES_RIGHT_PIN], GPIO.OUT)
    GPIO.output([EYES_LEFT_PIN, EYES_RIGHT_PIN], GPIO.HIGH)
    return


def blink_antenna():
    GPIO.setup([ANTENNA], GPIO.OUT)
    while True:
       GPIO.output([ANTENNA], GPIO.HIGH)
       time.sleep(TIMEOUT_ANTENNA)
       GPIO.output([ANTENNA], GPIO.LOW)
       time.sleep(TIMEOUT_ANTENNA)
    return

def setup_antenna():

    threads = []
    for i in range(5):
       t = threading.Thread(target=blink_antenna)
       threads.append(t)
       t.start()
    time.sleep(TIMEOUT)


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


setup_eyes()
setup_antenna()
run(host='0.0.0.0', port=80)
