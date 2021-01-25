from sense_hat import SenseHat

sense = SenseHat()

c1 = (252, 186, 3)
c2 = (3, 252, 173)
c3 = (4, 25, 214)

leds = [
  c1, c2, c3, c1, c3, c2, c1, c2,
  c1, c2, c3, c1, c3, c2, c1, c2,
  c1, c2, c3, c1, c3, c2, c1, c2,
  c1, c2, c3, c1, c3, c2, c1, c2,
  c1, c2, c3, c1, c3, c2, c1, c2,
  c1, c2, c3, c1, c3, c2, c1, c2,
  c1, c2, c3, c1, c3, c2, c1, c2,
  c1, c2, c3, c1, c3, c2, c1, c2,
]

sense.set_pixels(leds)
sleep(5)
