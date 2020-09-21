import time
import random
import json

while(1):
    with open("/home/tobiuo0203/static/data.json", mode='w') as f:
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