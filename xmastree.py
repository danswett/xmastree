import time
import datetime
import xmas_settings
import logging
from animations import *
import threading
from multiprocessing import Process
from neopixel import *
from webcolors import *
from colorcorrection import correctColor
from flask import Flask
from flask_ask import Ask, statement, convert_errors

# Define Flask
app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

processes = []

@ask.intent('TreeIntent', mapping={'status': 'status', 'pattern': 'pattern'})
def alexa_control(status, pattern):
    [x.terminate() for x in processes]
    if pattern in ['white']:
        p = Process(target=lightStrip, args=(strip, 'navajowhite', 'navajowhite', 30))
    if pattern in ['colors']:
        p = Process(target=xmasTheaterChase, args=(strip,))
    if pattern in ['blue fade']:
        p = Process(target=colorFade, args=(strip, 'navajowhite', 'royalblue', 40))
    if pattern in ['white fade']:
        p = Process(target=colorFade, args=(strip, 'navajowhite', 'navajowhite', 40))
    if pattern in ['blue']:
        p = Process(target=lightStrip, args=(strip, 'navajowhite', 'royalblue', 30))
    if pattern in ['rave']:
        p = Process(target=rainbowCycle, args=(strip,))
    if pattern in ['off']: resetStrip(strip)

    global processes
    processes.append(p)
    p.start()

    return statement('Setting tree to {}'.format(pattern))

# Main program logic follows:
if __name__ == '__main__':
	strip = Adafruit_NeoPixel(xmas_settings.LED_COUNT, xmas_settings.LED_PIN, xmas_settings.LED_FREQ_HZ, xmas_settings.LED_DMA, xmas_settings.LED_INVERT, xmas_settings.LED_BRIGHTNESS, xmas_settings.LED_CHANNEL, xmas_settings.LED_STRIP)
	strip.begin()

	print ('Press Ctrl-C to quit.')

        try:
            app.run(host='0.0.0.0', port=5000)
#                lightStrip(strip, 'navajowhite', 'royalblue', 30)
#                xmasTheaterChase(strip, 10)
#                xmasFade(strip,50, 10)
#                colorFade(strip, 'NavajoWhite', 50, 1200)

        except KeyboardInterrupt:
            resetStrip(strip)
