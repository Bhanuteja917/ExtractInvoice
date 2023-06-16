import os
import time
import calendar

def get_time_stamp():
    gmt = time.gmtime
    ts = calendar.timegm
    return ts

def check_input(input):
    non_existent_input = []
    for file in input:
        if not os.path.exists(file):
            non_existent_input.append(file)
    return non_existent_input
