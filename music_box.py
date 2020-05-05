#import the libraries
import pygame
from gpiozero import Button, LED

#initiate pygame
pygame.init()

#setup the instruments
drum = pygame.mixer.Sound("/home/pi/gpio_music/samples/drum_tom_mid_hard.wav")
cymbal = pygame.mixer.Sound("/home/pi/gpio_music/samples/drum_cymbal_hard.wav")
snare = pygame.mixer.Sound("/home/pi/gpio_music/samples/drum_snare_hard.wav")
cowbell = pygame.mixer.Sound("/home/pi/gpio_music/samples/drum_cowbell.wav")

#setup the buttons
button_drum = Button(4)
button_cymbal = Button(17)
button_snare = Button(27)
button_cowbell = Button(22)

#setup the leds
led_drum = LED(21)
led_cymbal = LED(20)
led_snare = LED(16)
led_cowbell = LED(12)

#define what each button will do
def drum_play():
    drum.play()
    led_drum.on()

def cymbal_play():
    cymbal.play()
    led_cymbal.on()

def snare_play():
    snare.play()
    led_snare.on()

def cowbell_play():
    cowbell.play()
    led_cowbell.on()

#assign the functions to each button and make sure the leds go off when the buttons are released
button_drum.when_pressed = drum_play
button_drum.when_released = led_drum.off
button_cymbal.when_pressed = cymbal_play
button_cymbal.when_released = led_cymbal.off
button_snare.when_pressed = snare_play
button_snare.when_released = led_snare.off
button_cowbell.when_pressed = cowbell_play
button_cowbell.when_released = led_cowbell.off
