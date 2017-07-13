import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIN = 21
GPIO.setup(PIN, GPIO.OUT)

while True:
    try:
        GPIO.output(PIN, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(PIN, GPIO.LOW)
        time.sleep(2)
    except KeyboardInterrupt:
	GPIO.cleanup()

GPIO.cleanup()

