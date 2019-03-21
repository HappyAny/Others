import RPi.GPIO as GPIO
from datetime import datetime 
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(21, GPIO.FALLING)
for loop in range(0,30):
    a=0
    b=[]
    while a<=35:
        if GPIO.event_detected(21):
            b.append(datetime.now())
            a=a+1
    #print(b)
    s=''
    count=0
    for count in range(0,35):
        if (b[count+1]-b[count]).microseconds<1500:
            s=s+'0'
        elif (b[count+1]-b[count]).microseconds>1500 and (b[count+1]-b[count]).microseconds<2500 :
            s=s+'1'
    print(s)
    time.sleep(2)
GPIO.cleanup()
