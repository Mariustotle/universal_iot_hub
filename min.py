import RPi.GPIO as GPIO
import time

RELAY_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT, initial=GPIO.LOW)  # OFF

print("Relay should be OFF (red LED off).")
time.sleep(3)

GPIO.output(RELAY_PIN, GPIO.HIGH)  # ON
print("Relay ON (red LED should be ON).")
time.sleep(3)

GPIO.output(RELAY_PIN, GPIO.LOW)  # OFF
print("Relay OFF (red LED should be OFF).")
time.sleep(3)

GPIO.cleanup()
