import time
import random
import json

while(1):
    with open("static/data.json", mode='w') as f:
        f.write(json.dumps([
            random.random(),
            random.random(),
            random.random(),
            random.random(),
            random.random(),
            random.random(),
            random.random()
        ]))
    time.sleep(3)