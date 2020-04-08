import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import turtle
import time

wn = turtle.Screen()
wn.title("Stoplights")
wn.bgcolor("black")

pen = turtle.Turtle()
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(-30, 60)
pen.pendown()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)

red_light = turtle.Turtle()
red_light.shape("circle")
red_light.color("grey")
red_light.penup()
red_light.goto(0, 40)

yellow_light = turtle.Turtle()
yellow_light.shape("circle")
yellow_light.color("grey")
yellow_light.penup()
yellow_light.goto(0, 0)

green_light = turtle.Turtle()
green_light.shape("circle")
green_light.color("grey")
green_light.penup()
green_light.goto(0, -40)


im = cv2.imread('cars_4.jpeg')
bbox, label, conf = cv.detect_common_objects(im)
output_image = draw_bbox(im, bbox, label, conf)
plt.imshow(output_image)
plt.show()
print('Number of cars in the image is ' + str(label.count('car')))
if str(label.count('bus')) > '10':
    red_light.color("red")
    time.sleep(5)
    exit(0)

elif str(label.count('bus')) == '10':
    yellow_light.color("yellow")
    time.sleep(2)
    exit(0)

else:
    green_light.color("bus")
    time.sleep(2)
    exit(0)

wn.mainloop()





