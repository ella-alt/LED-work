import board
import neopixel

pixels = neopixel.NeoPixel(board.D18,20)

pixels[4] = (10,0,0)
