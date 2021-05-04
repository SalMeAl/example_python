#!/usr/bin/python 
import sys
LED3_PATH = "/sys/class/leds/beaglebone:green:usr3"

def writeLED(fileName, value, path=LED3_PATH):
    """This function writes a passed value to the file and into the path"""
    fo = open(path + fileName,"w")
    fo.write(value)
    fo.close()
    return

def removeTrigger():
    """This function sets to an empty state"""
    writeLED("/trigger", "none")
    return

#Application begins:
print("Starting the LED Python Script") 
if len(sys.argv)!=2:
    print("Wrong number of arguments")
    sys.exit(2)

if sys.argv[1]=="on":
    print("LED is on")
    removeTrigger()
    writeLED("/brightness", "1")
elif sys.argv[1]=="off":
    print("LED is off")
    removeTrigger()
    writeLED(fileName="/brightness", value="0")
elif sys.argv[1]=="flash":
    print("LED is flashing")
    removeTrigger()
    writeLED(fileName="/trigger", value="timer")
    writeLED(fileName="/delay_on", value="50")
    writeLED(fileName="/delay_off", value="50")
else:
    print("Wrong command")

print("End of Script")
