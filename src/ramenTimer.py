#coding: utf-8

import wiringpi as pi
import time
import sys

LED_PIN = 23
SW_PIN = 24
BUZZER_PIN = 18
pi.wiringPiSetupGpio()
pi.pinMode(LED_PIN, pi.OUTPUT)
pi.pinMode(SW_PIN, pi.INPUT)
pi.pullUpDnControl(SW_PIN, pi.PUD_UP)
pi.pinMode(BUZZER_PIN, pi.OUTPUT)

button = False


try:
    while True:
        if (pi.digitalRead(SW_PIN) == pi.LOW):
            pi.digitalWrite(LED_PIN, pi.HIGH)
            button = True
            t = time.time()
        else:
            pi.digitalWrite(LED_PIN, pi.LOW)
        time.sleep(0.1)

        while button:
            c = time.time()
            if c - t >= 180:
                pi.digitalWrite(BUZZER_PIN,pi.HIGH)
                time.sleep(10)
                pi.digitalWrite(LED_PIN, pi.LOW)
                pi.digitalWrite(BUZZER_PIN,pi.LOW)
                button = False
            else:
                if (pi.digitalRead(SW_PIN) == pi.LOW):
                    pi.digitalWrite(LED_PIN,pi.LOW)
                    button = False
                pi.digitalWrite(LED_PIN,pi.HIGH)
        pi.digitalWrite(BUZZER_PIN,pi.LOW)


except KeyboardInterrupt:
  pi.digitalWrite(BUZZER_PIN, pi.LOW)
  pi.digitalWrite(LED_PIN,pi.LOW)
  sys.exit(0)

