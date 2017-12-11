from neopixel import *

# Twitter authentication
APP_KEY = 'qwRDV1THc5SSJnCEH05fUQJ4x'
APP_SECRET = '4LRzNc6UpP2vk4pKZf2lJFe2mTaBXiEp9gOJWBmsQQgHUnwRfe'
OAUTH_TOKEN = '23281923-WLiGj9oWcO2pwfLoU732AVo8fmMJIUzKUz0xQStSe'
OAUTH_TOKEN_SECRET = 'CTsTEdHviV33ti0f9gsSjKbRCAoNXckeA2QKHh06Z9j0n' 

# Search term
TERMS = 'twittertree'

# Database config
CONNECTION_STRING = "sqlite:///xmastweet.db"
CSV_NAME = "xmastweet.csv"
TABLE_NAME = "xmastweet"

# LED strip configuration:
LED_COUNT      = 350    # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering
