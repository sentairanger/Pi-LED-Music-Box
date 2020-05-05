# Pi-LED-Music-Box
This is an extension of a Raspberry Pi Projects guide where you use buttons to play music

## Overview

This is based on this [project](https://projects.raspberrypi.org/en/projects/gpio-music-box) where you play music by pressing buttons.

### Needed Items

To replicate this project on your own you will need the following:

* A Raspberry Pi (Can be any Pi as long as it has 40 GPIO pins)
* A suitable Micro USB or USB-C Power Supply (Pi 4 uses USB-C)
* Jumper Wires
* Resistors (Can be any value above 150 Ohms)
* Breadboards
* HDMI cable
* Keyboard/Mouse
* Buttons
* Micro SD card
* [Raspbian](https://www.raspberrypi.org/downloads/raspbian/)

### Setting up the Breadboards

If you have a large breadboard you can use it as you'll need to connect 4 LEDs and 4 Buttons. The link I provided shows you how to wire the buttons on to the Pi. To wire the LEDs, you can use [this](https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins) to help you. All you need is to repeat the process three times and you're good. It helps to have a common ground so be sure to add one ground lede to help you save on ground pins. Same with the buttons. Once you have that be sure to connect the wires to the pins on the Pi. You can use any of the other GPIO pins that are not in the code provided. Just be sure to alter the code as needed.

### Setting up the Code

Before you begin, make sure you have a Micro SD card to install Raspbian. First, plug it in to your SD card reader and then download the image from the link provided. Then, use a utility like etcher or the official imaging software provided by the foundation. Once you do that write the image and then eject your card. Insert it into your Pi and then follow the setup instructions. If you already have Raspbian on your Pi you can skip these steps and just start with the code. First, clone this repository and then change to the directory of the repo by typing `cd Pi-LED-Music-Box`. Make sure you have followed the instructions from the project site to ensure you have copied the flac files into a custom directory and use ffmpeg to covert them into wav files. Then type `python musicbox.py` and then try the buttons out. Be sure that you wired everything correctly and that you can hear the music. You can use any other sound you want or even add more buttons to make it more interesting. 
