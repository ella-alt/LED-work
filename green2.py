import board
import neopixel

pixels = neopixel.NeoPixel(board.D18,20)

pixels[1] = (0,128,0)
