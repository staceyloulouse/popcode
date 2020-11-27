import turtle

zippy=turtle.Turtle()
zippy.speed(0)
#zippy.begin_poly()

for i in range(4):
    
    if i%2==0:
        zippy.pencolor('green')
    else:
        zippy.pencolor("blue")
    for j in range(6):
        zippy.forward(100)
        zippy.right(60)
    zippy.forward(100)
    zippy.right(270)
       
   
#zippy.end_poly()

zippy.loop()