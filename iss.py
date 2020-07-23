#!/usr/bin/env python

__author__ = "Triston Reeves"
__assisted__ = "Keith Garcia/Ben McKenzie"

import requests
import turtle
import time


def get_astro():
    response = requests.get('http://api.open-notify.org/astros.json')
    return response.json()


def iss_location():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    return response.json()


def indianapolis():
    response = requests.get('http://api.open-notify.org/iss-pass.json',
                            params={'lat': '39.7684', 'lon': '-86.1581'})
    return response.json()


def mr_turtle():
    space = turtle.Turtle()
    n_pass = indianapolis()
    rise_time = time.ctime(n_pass["response"][1]["risetime"])
    show = turtle.Screen()
    show.setup(width=720, height=360, startx=0, starty=0)
    show.setworldcoordinates(-180, -90, 180, 90)
    show.bgpic('map.gif')
    show.register_shape('iss.gif')
    space.penup()
    space.goto(-86.1581, 39.7684)
    space.dot(4, "orange")
    space.color('red')
    space.shape("iss.gif")
    space.write(rise_time, align='right', font=("Courier", 14))
    location = iss_location()
    lon = float(location["iss_position"]["longitude"])
    lat = float(location["iss_position"]["latitude"])
    heading = space.towards(lon, lat)
    if heading > 0.0:
        space.setheading(heading)
        space.goto(lon, lat)
    show.exitonclick()
    return space


def main():
    astro = get_astro()
    print(f"Currently on the space station there are {astro['number']},\
          on the {astro['people'][0]['craft']}.")
    for astro in astro["people"]:
        print(f"Astronaut {astro['name']}")
    mr_turtle()


if __name__ == '__main__':
    main()
