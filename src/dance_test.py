from orbitlab import Orbit
import time
orbit = Orbit("100.82.252.30")

orbit.dance("")

orbit.set_rpm([10,-8])

time.sleep(5)

orbit.stop()