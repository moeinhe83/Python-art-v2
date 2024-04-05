# A beautiful design with Python - Part 2

# Library
from turtle import * 
import colorsys

# Background Color
bgcolor('black')
tracer(5)
h = 0.8 

# Design Code
for i in range(200):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    begin_fill()
    forward(i)
    left(5)
    backward(i*1.5)
    circle(i*0.5, 100)
    end_fill()
    h += 2.008
done()


# Create By Moein Heshmati
# Finish