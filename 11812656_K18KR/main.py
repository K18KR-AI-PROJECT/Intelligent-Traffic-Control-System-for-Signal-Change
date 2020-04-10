import Stoplight_frame as sf
import number as nb
import time
import turtle

sf.stoplight()

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

for i in range(1, 6):

    no_of_car = nb.calc_car(f"car{i}.jpeg")

    if  no_of_car > 9:
        red_light.color("red")
        time.sleep(1)
        red_light.color("grey")
        yellow_light.color("yellow")
        time.sleep(1)
        yellow_light.color("grey")
        green_light.color("green")
        time.sleep(1)
        green_light.color("grey")

    elif no_of_car == 9:
        yellow_light.color("yellow")
        time.sleep(1)
        yellow_light.color("grey")
        green_light.color("green")
        time.sleep(1)
        green_light.color("grey")

    else:
        green_light.color("green")
        time.sleep(1)
        green_light.color("grey")

    time.sleep(1)

exit(0)
wn.mainloop()



