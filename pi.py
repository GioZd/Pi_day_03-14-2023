'''
from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
'''
import matplotlib.pyplot as plt
import numpy as np
import random as rd
import math as mt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def ranpoint_distanced(self, d = 1):
        theta = rd.choice(list(np.linspace(0, 2*mt.pi, 200)))
        return Point(
            self.x + mt.cos(theta),
            self.y + mt.sin(theta)
            )

plt.xlim(-4, 4)
plt.ylim(-4, 4)
#plt.grid(b=True, which='major', axis='x')
for x in range(-5,5):
    plt.axvline(x = x, color = 'blue')

count_red = 0
count_green = 0
count_total = int(input('No di iterazioni: '))

for i in range(count_total):
    a = Point(rd.uniform(-3, 3), rd.uniform(-3, 3))
    b = a.ranpoint_distanced()
    xs = np.array([a.x, b.x])
    ys = np.array([a.y, b.y])
    if mt.floor(a.x) != mt.floor(b.x):
        plt.plot(xs, ys, color = 'red')
        count_red += 1
    else:
        plt.plot(xs, ys, color = 'springgreen')
        count_green += 1

    count_total = count_red + count_green
    # plt.text(0,3, str(count_green), c = 'springgreen', size = 12)
    # plt.text(0,2, f'{count_red}', c= 'red', size = 12)
    plt.text(3.5,3.5,str(count_green),
         fontsize=20,
         color="springgreen",
         verticalalignment ='top', 
         horizontalalignment ='center',
         bbox ={'facecolor':'white'}
        )  
    plt.text(3.5,2.5,str(count_red),
         fontsize=20,
         color="red",
         verticalalignment ='top', 
         horizontalalignment ='center',
         bbox ={'facecolor':'white'}
        )  
    plt.text(3.5,1.5,str(count_total),
         fontsize=20,
         color="blue",
         verticalalignment ='top', 
         horizontalalignment ='center',
         bbox ={'facecolor':'white'}
        )  
    approx_pi = (2*(count_total))/count_red
    conclusions = f"2×{count_total}:{count_red}=\n{approx_pi:.3f}"
    plt.text(3.5,0.5, conclusions,
         fontsize=12,
         #color="blue",
         verticalalignment ='top', 
         horizontalalignment ='center',
         bbox ={'facecolor':'white'}
        )  

plt.show()