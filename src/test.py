from orbitlab import Orbit

orbit = Orbit("100.117.140.948")

cnt = 0
while cnt < 5:
    print(orbit.current())
    cnt += 1

orbit.stop()

# orbit_client.stop()