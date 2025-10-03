from orbitlab import Orbit
from orbitlab.orbit_utils.face_ids import FaceId

orbit = Orbit("100.82.252.30")

face_change = False

while True:
    try:
        akim = orbit.current()
        print(akim)
        if akim > 3.0:
            if not face_change:
                orbit.change_face(FaceId.ERROR)
                orbit.set_rgb([0, 0, 255])
                face_change = True
                # orbit.text_to_speech("WARNING! Robot Hit the wall!")
                orbit.play_song("cannon in d")
        else:
            if face_change:
                face_change = False
                orbit.change_face(FaceId.BREATHE)
                orbit.set_rgb([0, 255, 0])

    except KeyboardInterrupt:
        break
orbit.stop()