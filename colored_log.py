import os,sys,time
from colored import custom

JOINT = ' -- '

class stand_print_fun():
    green = custom('green', None, None)
    info = green[0] + JOINT + 'INFO' + JOINT + green[-1]
    red = custom('red', None, None)
    warn = red[0] + JOINT + 'WARN' + JOINT + red[-1]
    purple = custom('purple', None, None)
    test = purple[0] + JOINT + 'WARN' + JOINT + purple[-1]

def create_output(type):
    stand_put = getattr(T, type)
    def func(*args, Time=True):
        if Time:
            print( datetime() + stand_put + get_context(*args))
        else:
            print( stand_put + get_context(*args) )
    return func

T = stand_print_fun()
print_info = create_output('info')
print_warn = create_output('warn')
print_test = create_output('test')

def my_print(*args, fe=None, bk=None, dp=None, sep=' ', Time=True):
    style = custom(fe, bk, dp)
    custom_str = style[0] + get_context(*args, sep) + style[-1]
    if Time:
        print( datetime() + JOINT + custom_str)
    else:
        print( custom_str )

def datetime():
    return time.strftime('%Y-%m-%d %H:%M:%S')
    
def get_context(*args, sep=' '):
    return sep.join(map(str, args))