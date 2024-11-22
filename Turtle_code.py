if __name__ == "__main__":
    from turtle import Screen, Turtle
    import turtle

    screen = Screen()
    screen.setup(600, 400)
    
    #window = turtle.Screen()
    #window.bgcolor("blue")

    roof = turtle.Turtle()
    roof.hideturtle()

    roof.teleport(-93.8, 21.5)
    x = [-93.8,-104,-111.3,-114.4,-122.8,-123.6,-129.4,-129,
    -115.5,-105,-68,-48.4,22,74,96.7,113,104.3,97,105.7,124,129.5,
    130,124.5,127.4,99.6,100,111.8,107.6,110.2,102.3,101.8,93,88.5,
    76.7,64.2,52.2,69,84.8,94.8,98.8,100.5,100,97.1,93.2,77.6,69.04,
    68.5,66.8,63,58.6,55.3,49.4,47.8,44,37.9,29.4,22.6,21.2,16.6,4.3,
    -2,-17.3,-25.8,-38.3,-44.7,-47.4,-49.7,-49.1,-47.6,-62.8,-73,-78,
    -79.2,-67.8,-62.4,-111.5,-110.8,-94.3,-80.7,-59.3,-51.3,-70.5,-85,-93.6]
   
    y = [21.5,3,-9.2,-26.7,-41.7,-61.3,-82,-139.4,-173.7,-205.5,
    -223,-223.5,-222,-211.3,-172,-108,-47.8,-23.4,-26.2,-24,-14,2.2,
    5.8,32.2,32.5,24.6,2.6,0.5,-9.5,-7.6,-14.3,-13.2,4,19.3,39.3,51.8,
    55.5,69.3,90,121.4,141,154.5,154.96,151.5,119.1,108.8,120.1,144.4,
    185,185.6,181.6,164.7,205.7,212.5,199.7,166,190.6,203.6,220.4,242.4,
    238.4,204.4,165.3,198,211.4,202.6,194.6,182,166.9,204.5,219.4,204.1,
    157.2,114.6,101.7,143.6,126,86.2,70.5,60.7,59.4,44.2,27.5,21.2]

    #line filled in with colour
    roof.begin_fill()
    #got the colour from this website: https://imagecolorpicker.com/
    roof.color("#fad432")
    for i in range(len(x)):
        roof.goto(x[i], y[i])
    roof.end_fill()
    
    #drawing an outline in black
    roof.pensize(3)
    roof.color("orange")
    for i in range(len(x)):
        roof.goto(x[i], y[i])
    roof.end_fill()
    
    #for vscode only
    screen.mainloop()

    
    
    screen = Screen()
    screen.setup(600, 400)
    
    #window = turtle.Screen()
    #window.bgcolor("blue")
    
    line = turtle.Turtle()
    line.hideturtle()

    line.teleport(-90.8, -212)
    x = [-90.8,-53.6,-54,-50.6,-45,-32]
    y = [-212,-184.5,-158.7,-138,-124.2,-115]    
   
    # x = [-129.2,-95.3,-79,-68.3,-19.1,27.6,53.35,] y = [-88.2,-50.3,-39.8,-30.2,-2.8,25.7,50.4]
    
    # x = [-103.7,-80,-61.2,-34.6,-23.8,-7,9.2] y = [3,13,29,43,50,55,62.8]

    #line filled in with colour
    line.begin_fill()
    #got the colour from this website: https://imagecolorpicker.com/
    line.color("#fad432")
    for i in range(len(x)):
        roof.goto(x[i], y[i])
    line.end_fill()

    #drawing an outline in black
    line.pensize(3)
    line.color("black")
    for i in range(len(x)):
        line.goto(x[i], y[i])
    line.end_fill()
    
    #for vscode only
    screen.mainloop()