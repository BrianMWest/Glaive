import glaive
import time

glaive.init()

params = glaive.params()
period = float(params['period']) if 'period' in params else 0

while True:
    time.sleep(period)
    glaive.send({
        "message": "Hello, there!",
    })

glaive.close()
