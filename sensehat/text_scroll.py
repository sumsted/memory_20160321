#!/usr/bin/python
#from sense_hat import SenseHat
import sense_hat_client as sense

# sense = SenseHat()
sense.set_rotation(180, 0)
red = (255, 0, 0)
sense.show_message("One small step for Pi!", .1, (0, 255, 0), (255, 0, 255))
