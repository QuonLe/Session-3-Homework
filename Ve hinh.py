from turtle import *
speed(-1)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(3,8):
    pensize(2)
    pencolor(colors[i-3])
    for x in range(i):
        forward(100)
        left(360/i)

pencolor("white")
setposition(-100,-100)

for x in range(1,6):
    pencolor(colors[x-1])
    fillcolor(colors[x-1])
    begin_fill()
    for i in range(2):
        forward(50)
        right(90)
        forward(100)
        right(90)
    forward(50)
    end_fill()
mainloop()

