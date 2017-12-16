import time
import datetime
import xmas_settings
import logging
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


# Define functions which animate LEDs in various ways.
def lightStrip(strip, color1, color2, brightness):
    for i in range(strip.numPixels()):
        if i % 2 == 0:
            strip.setPixelColor(i, correctColor(color2))
        else:
            strip.setPixelColor(i, correctColor(color1))
    strip.setBrightness(brightness)
    strip.show()

def colorWipe(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, correctColor(color))
        strip.show()
        time.sleep(wait_ms/1000.0)

def xmasWipe(strip, wait_ms=50):
    j = 0
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, correctColor(xmasColor[j]))
        strip.show()
        time.sleep(wait_ms/1000.0)
        if j < 5:
            j += 1
        else:
            j = 0

def xmasFade(strip, brightness, fades, wait_ms=50):
    c = 0
    q = 0
    for j in range(strip.numPixels()):
        strip.setPixelColor(j, correctColor(xmasColor[c]))
        if c < 4:
            c += 1
        else:
            c = 0
    for e in range(fades):
        for i in range(q, brightness):
            strip.setBrightness(i)
            strip.show()
            time.sleep(wait_ms/1000.0)
            
        for i in reversed(range(brightness)):
            if i == 15:
                q = i
                break
            else:
                strip.setBrightness(i)
                strip.show()
                time.sleep(wait_ms/1000.0)

def colorFade(strip, color1, color2, brightness, fades, wait_ms=50):
    q = 0
    for i in range(strip.numPixels()):
        if i % 2 == 0:
            strip.setPixelColor(i, correctColor(color2))
        else:
            strip.setPixelColor(i, correctColor(color1))
   
    for e in range(fades):
        for i in range(q, brightness):
            strip.setBrightness(i)
            strip.show()
            time.sleep(wait_ms/1000.0)
            
        for i in reversed(range(brightness)):
            if i == 15:
                q = i
                break
            else:
                strip.setBrightness(i)
                strip.show()
                time.sleep(wait_ms/1000.0)


def xmasChase(strip, wait_ms=50):
    j=0
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, correctColor(xmasColor[j]))
        strip.setPixelColor(i-1, Color(0,0,0))
        strip.setBrightness(255)
        strip.show()
        time.sleep(wait_ms/1000.0)
        if j < 4:
            j += 1
        else:
            j = 0

def xmasTheaterChase(strip, iterations, wait_ms=150):
# Movie theater light style chaser animation.
        strip.setBrightness(50)
        c = 0
        for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
                            strip.setPixelColor(i+q, correctColor(xmasColor[c]))
                            if c < 4:
                                c += 1
                            else:
                                c = 0

			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def theaterChase(strip,color,  wait_ms=100, iterations=10):
# Movie theater light style chaser animation.
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, correctColor(color))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def wheel(pos):
# Generate rainbow colors across 0-255 positions.
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
# Draw rainbow that fades across all pixels at once.
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
# Draw rainbow that uniformly distributes itself across all pixels.
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
# Rainbow movie theater light style chaser animation.
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def clearWipe(strip, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0))
        strip.show()
        time.sleep(wait_ms/1000.0)

def resetStrip(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0))
    strip.show()

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
