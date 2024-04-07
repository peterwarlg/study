import time
from config import joints


def real_loop():
    while 1:
        joints[0] += 1
        time.sleep(1)