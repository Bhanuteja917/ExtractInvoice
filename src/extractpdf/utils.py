import os
import time
import calendar

def get_time_stamp():
    gmt = time.gmtime()
    ts = calendar.timegm(gmt)
    return ts

def check_input(input):
    non_existent_input = []
    for file in input:
        print(file)
        if not os.path.exists(file):
            non_existent_input.append(file)
    return non_existent_input

def complete_email(email):
        if email.endswith('.com'):
            return email
        else:
            email = email.split('@')
            if email[1].startswith('y'):
                return f'{email[0]}@yahoo.com'
            if email[1].startswith('h'):
                return f'{email[0]}@hotmail.com'
            if email[1].startswith('g'):
                return f'{email[0]}@gmail.com'
        return ''