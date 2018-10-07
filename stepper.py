#Step 0: Preamble
#------------------------------------------------------------------------
#Program Title  : easy_stepper.py 
#Code Written by: Salty Scott
#Current Project: www.rowboboat.com
#This code is a very basic example of using python to control a spark fun
# easy driver.  The spark fun easy driver that I am using in this example
# is connected to a 42HS4013A4 stepper motor and my raspberry pi.  Pin 23
# is the direction control and pin 24 is the step control. 
# This program expects two arguments: direction and steps
#------------------------------------------------------------------------
 
#Step 1: Import necessary libraries 
#------------------------------------------------------------------------
import sys
import RPi.GPIO as gpio #https://pypi.python.org/pypi/RPi.GPIO more info
import time
#------------------------------------------------------------------------
 
#Step 2: Read arguements https://www.youtube.com/watch?v=kQFKtI6gn9Y
#------------------------------------------------------------------------
#read the direction and number of steps; if steps are 0 exit 
try: 
   	steps = int(float(sys.argv[2]))
	direction = sys.argv[1]

except:
    steps = 0
 
#print which direction and how many steps 
print("You told me to turn %s %s steps.") % (direction, steps)
#------------------------------------------------------------------------
 
 
#Step 3: Setup the raspberry pi's GPIOs
#------------------------------------------------------------------------
#use the broadcom layout for the gpio
gpio.setmode(gpio.BCM)
#GPIO23 = Direction
#GPIO24 = Step
gpio.setup(23, gpio.OUT)
gpio.setup(24, gpio.OUT)
gpio.setup(27, gpio.OUT)
gpio.setup(17, gpio.OUT)
#------------------------------------------------------------------------
 
 
#Step 4: Set direction of rotation
#set the output to true for left and false for right
if direction == 'left':
    gpio.output(23, True)
    gpio.output(17, True)
elif direction == 'right':
    gpio.output(24, False)
    gpio.output(27, False)
#------------------------------------------------------------------------
 
 
#Step 5: Setup step counter and speed control variables
#------------------------------------------------------------------------
#track the numebr of steps taken
StepCounter = 0
 
#waittime controls speed
WaitTime = 0.0025
#------------------------------------------------------------------------
 
 
#Step 6: Let the magic happen

#------------------------------------------------------------------------
# Start main loop
while StepCounter < steps:
 
    #turning the gpio on and off tells the easy driver to take one step
    gpio.output(24, True)
    gpio.output(27, True)
    gpio.output(24, False)
    gpio.output(27, False)
    StepCounter += 1
 
    #Wait before taking the next step...this controls rotation speed
    time.sleep(WaitTime)
#------------------------------------------------------------------------
 
 
#Step 7: Clear the GPIOs so that some other program might enjoy them
#------------------------------------------------------------------------
#relase the GPIO
gpio.cleanup()
#------------------------------------------------------------------------

