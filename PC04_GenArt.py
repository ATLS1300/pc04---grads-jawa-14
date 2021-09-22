#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 09:17:35 2021

@author: nolan

This code creates a generative art piece of rain over a coral reef. The reef is made out of interlocked octagons. 
With each generation, the octagons randomly change color to create a living reef. Every time you visit, it has
changed. As for the rain, not only does it change color with each "visit," but the positions of the drops vary,
conveying a sense of constant motion.  

"""
import turtle
import random

turtle.colormode(255)
turtle.tracer(0)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h)


#Rainbow Rain

rain = turtle.Turtle()
rain.up()
rain.pensize(1)
rain.right(90)

#For loop creating 500 randomly placed rain drops (vertical lines) of varied colors.
#The colors and placement are random because the integers for the position and RGB values are all randomly generated using random.randint() 
for drop in range(500):
    rain.goto(random.randint(-300,300),random.randint(-300,300))
    rain.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    rain.down()
    rain.forward(5)
    rain.up()
    
rain.hideturtle()


#Ocean

water = turtle.Turtle()
water.up()
water.color(227,246,253)
water.goto(-300,0)
water.down()
water.begin_fill()
water.goto(300,0)
water.goto(300,-300)
water.goto(-300,-300)
water.goto(-300,0)
water.end_fill()


#Waves

#Nested for loops to create sixty 60-60-60 traingles in a row with sides 10 pixels long (the waves).
for wave in range(60):
    water.left(60)
    water.begin_fill()
    for side in range(2):
        water.forward(10)
        water.right(120)
    water.forward(10)
    water.end_fill()
    water.right(180)
    water.forward(10)
    

#Coral
#Pattern of octagons based off of modified Sergio Laureano-Rivera's pseudocode

coral = turtle.Turtle()
coral.up()
coral.goto(-300,-300)

#Nested for loops to create 20 rows of 100 interlocked hexagons (side length 6) of random colors.
#This forms the coral reef.
for row in range(20):
    coral.down()
    for shape in range (100):
        coral.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        for side in range(8):
            coral.forward(6)
            coral.left(45)
        coral.forward(6)
    coral.up()
    coral.back(600)
    coral.left(90)
    coral.forward(10)
    coral.right(90)

# "Put a bow on it"
panel.update()
turtle.done()




