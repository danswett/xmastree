import time
import datetime
import xmas_settings
import logging
import animations
from neopixel import *
from webcolors import *
from colorcorrection import correctColor
from flask import Flask
from flask_ask import Ask, statement, convert_errors

# Define Flask
app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent('TreeIntent', mapping={'status': 'status', 'pattern': 'pattern'})

def alexa_control(status, pattern):
    if pattern in ['white']: lightStrip(strip, 'navajowhite', 'navajowhite', 30)
    if pattern in ['colors']: colorFade(strip, 'navajowhite', 'royalblue', 30, 1000)
    if pattern in ['blue']: lightStrip(strip, 'navajowhite', 'royalblue', 30)
    if pattern in ['off']: resetStrip(strip)

    return statement('Setting tree to {}'.format(pattern))


# LED colors:
xmasColorOld = ['red', 'gold', 'limegreen', 'cornflowerblue', \
        'darkorange','NavajoWhite']

xmasColor = ['red', 'royalblue', 'navajowhite', 'darkorange', 'limegreen']


# Main program logic follows:
if __name__ == '__main__':
	strip = Adafruit_NeoPixel(xmas_settings.LED_COUNT, xmas_settings.LED_PIN, xmas_settings.LED_FREQ_HZ, xmas_settings.LED_DMA, xmas_settings.LED_INVERT, xmas_settings.LED_BRIGHTNESS, xmas_settings.LED_CHANNEL, xmas_settings.LED_STRIP)
	strip.begin()

	print ('Press Ctrl-C to quit.')
        
        app.run(host='0.0.0.0', port=5000)

#        try:
#                lightStrip(strip, 'navajowhite', 'royalblue', 30)
#                xmasTheaterChase(strip, 10)
#                xmasFade(strip,50, 10)
#                colorFade(strip, 'NavajoWhite', 50, 1200)

#        except KeyboardInterrupt:
#            resetStrip(strip)
