import time
import datetime
import dataset
import json
import xmas_settings
from twython import TwythonStreamer
from neopixel import *
from webcolors import *
from sqlalchemy.exc import ProgrammingError

db = dataset.connect(xmas_settings.CONNECTION_STRING)

# LED colors:
xmasColor = ['red', 'yellow', 'green', 'cornflowerblue', \
        'darkorange','magenta']

gammaTable = [int(pow(float(i) / 255.0, 2.8) * 255.0) for i in range(256)]

# Setup callbacks from Twython Streamer
class twitterStream(TwythonStreamer):

    def on_success(self, data):
        
        tweet_id = data['id']
        tweet_author = data['user']['screen_name']
        tweet_fullname = data['user']['name']
        tweet_timestamp = float(data['timestamp_ms'])
        tweet_friendscount = data['user']['friends_count']
        tweet_text = data['text']
        tweet_convertedtime = datetime.datetime.fromtimestamp(tweet_timestamp/1000.0)


        table = db[xmas_settings.TABLE_NAME]
        try:
            table.insert(dict(
                tweet_id=tweet_id,
                author=tweet_author,
                name=tweet_fullname,
                time=tweet_convertedtime,
                friends=tweet_friendscount,
                text=tweet_text,
            ))
        
        except ProgrammingError as err:
            print(err)

        if 'text' in data:
            print data['text'].encode('utf-8')
            newtweet = data['text'].encode('utf-8')
            newtweet = newtweet.lower()
            newtweet = newtweet.replace(xmas_settings.TERMS, '')
            newtweet = newtweet.replace('#', '')
            theaterChase(strip, Color(255,255,255))
            xmasChase(strip)
            xmasFade(strip, 30)

    def on_error(self, status_code, data):
        print status_code

# Define functions which animate LEDs in various ways.
def lightLetter(position, color):
        strip.setPixelColor(position, color)
        strip.show()

def colorWipe(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        currentColor = name_to_rgb(color)
        colorR = gammaTable[currentColor[0]]
        colorG = gammaTable[currentColor[1]]
        colorB = gammaTable[currentColor[2]]

        strip.setPixelColor(i, Color(colorG,colorR,colorB))
        strip.show()
        time.sleep(wait_ms/1000.0)

def xmasWipe(strip, wait_ms=50):
    j = 0
    for i in range(strip.numPixels()):
        currentColor = name_to_rgb(xmasColor[j])
        colorR = gammaTable[currentColor[0]]
        colorG = gammaTable[currentColor[1]]
        colorB = gammaTable[currentColor[2]]

        strip.setPixelColor(i, Color(colorG, colorR, colorB))
        strip.setBrightness(80)
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
        currentColor = name_to_rgb(xmasColor[c])
        colorR = gammaTable[currentColor[0]]
        colorG = gammaTable[currentColor[1]]
        colorB = gammaTable[currentColor[2]]
        strip.setPixelColor(j, Color(colorG, colorR, colorB))
        if c < 5:
            c += 1
        else:
            c = 0
    for e in range(fades):
        for i in range(q, brightness):
            strip.setBrightness(i)
            strip.show()
            time.sleep(wait_ms/1000.0)
            
        for i in reversed(range(brightness)):
            if i == 10:
                q = i
                break
            else:
                strip.setBrightness(i)
                strip.show()
                time.sleep(wait_ms/1000.0)


def xmasChase(strip, wait_ms=50):
    j=0
    for i in range(strip.numPixels()):
        currentColor = name_to_rgb(xmasColor[j])
        colorR = gammaTable[currentColor[0]]
        colorG = gammaTable[currentColor[1]]
        colorB = gammaTable[currentColor[2]]

        strip.setPixelColor(i, Color(colorG, colorR, colorB))
        strip.setPixelColor(i-1, Color(0,0,0))
        if i == 149:
            strip.setPixelColor(i, Color(0,0,0))
        strip.setBrightness(255)
        strip.show()
        time.sleep(wait_ms/1000.0)
        if j < 5:
            j += 1
        else:
            j = 0


def theaterChase(strip, color, wait_ms=50, iterations=10):
# Movie theater light style chaser animation.
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
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

        try:
            xmasFade(strip,60, 1200)
#            stream = twitterStream(xmas_settings.APP_KEY, xmas_settings.APP_SECRET, xmas_settings.OAUTH_TOKEN, xmas_settings.OAUTH_TOKEN_SECRET)
#            tweet = stream.statuses.filter(track=xmas_settings.TERMS)

        except KeyboardInterrupt:
            resetStrip(strip)
