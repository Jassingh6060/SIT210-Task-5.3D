import RPi.GPIO as GPIO
import time
from tkinter import *
import tkinter.font
from gpiozero import LED 

GPIO.setmode(RPi.GPIO.BOARD)

led = LED(18)
blink = time.sleep(0.25)

def mdot():
    led.on()
    time.sleep(blink)
    led.off()
    time.sleep(blink)


def mdash():
    led.on()
    time.sleep(4*blink)
    led.off()
    time.sleep(blink)


MORSE_CODE = {
    'A':'. _',
    'B':'_ . . .',
    'C':'_ . _ .',
    'D':'_ . .',
    'E':'.',
    'F':'. . _ .',
    'G':'_ _ .',
    'H':'. . . .',
    'I':'. .',
    'J':'. _ _ _',
    'K':'_ . _',
    'L':'. _ . .',
    'M':'_ _',
    'N':'_ .',
    'O':'_ _ _',
    'P':'. _ _ .',
    'Q':'_ _ . _',
    'R':'. _ .',
    'S':'. . .',
    'T':'_',
    'U':'. . _',
    'V':'. . . _',
    'W':'. _ _',
    'X':'_ . . _',
    'Y':'_ . _ _',
    'Z':'_ _ . .'
}


def Convert_to_morsecode(name):
    name = name.upper()
    ename = " "
    for name in name:
        ename += MORSE_CODE(i) + " "
        return ename


def Write():
    name = inputtxt.get(1.0, "end-1c") 
    ename = Convert_to_morsecode(name)
    print(ename)
    morsename = name
    if(len(name) >12):
       return 'invalid'
    else:
       return name



win = Tk()
win.title("Morse Code GUI")
win.geometry('400x200')

l = label(text = "covert name to Morse Code")
inputtxt = Text(win, height = 10, width = 20, bg = "light blue")
MorseButton = Button(win, height = 4, width = 20, text = "print", command = Convert_to_morsecode())
