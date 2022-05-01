import sys

name=sys.argv[1]

print('hello world from .pyw file ' + name.upper())


countdown = 10

while countdown > 0:
    print ('CountDown = ', countdown)
    countdown = countdown - 1