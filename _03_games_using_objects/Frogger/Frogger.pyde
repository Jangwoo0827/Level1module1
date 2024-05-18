
def setup():
    global frog_x, frog_y
    global carx, cary
    global carxx, caryy
    global carxxx, caryyy
    carx = 400
    cary = 300
    carxx = 200
    caryy = 400
    carxxx = 100
    caryyy = 200
    frog_x = 400
    frog_y = 540
    Car(carx, cary, 70, 5)
    Car(carxx, caryy, 100, 10)
    Car(carxxx, caryyy, 100, 20)
    # 1. Use the size function to set the size of your sketch
    size(800, 600)
    # 2. Create 2 global variables for the background and the frog
    # using the loadImage("frog.png") function. For example:
    global bg
    bg = loadImage("froggerBackground.png")
    global frog
    frog = loadImage("frog.png")
    # global bg, frog
    # bg = loadImage("froggerBackground.png")
    bg.resize(800, 600)
    frog.resize (50, 50)
    # 3. Use the resize method to set the size of the background variable
    # to the width and height of the sketch. Resize the frog to an
    # appropriate size.
def draw():
    global frog_x, frog_y,carx, carxx, carxxx
    # 4. Use the background function to draw the background
    background(bg)
    # 5. Use the image function to draw the frog.
    # Run the program and check the background and frog are displayed.
    image(frog, frog_x, frog_y)
    # 6. Create global frog_x and frog_y variables in the setup function
    # and use them when drawing the frog. You will also have to put the
    # following in the draw function:
    # global frog_x, frog_y
    carx+= 5
    carxx+=10
    carxxx+=20
    if carx > 800:
        carx = 0
    if carxx > 800:
        carxx = 0
    if carxxx > 800:
        carxxx = 0
    if mousePressed:
        frog_y-=5
    if not mousePressed:
        frog_y+=2
    # 7. Use the Car class below to create a global car object in the
    # setup function and call the update and draw functions here.
    car = Car(carx, cary, 70, 5)
    car.update()
    car.draw()
    car1 = Car(carxx, caryy, 100, 10)
    car1.update()
    car1.draw()
    car2 = Car(carxxx, caryyy, 30, 10)
    car2.update()
    car2.draw()
    image(frog, frog_x, frog_y)
    # 8. Create an intersects method that checks whether the frog collides
    # with the car. If there's a collision, move the frog back to the starting
    # point.
    intersect()

def intersect():
    global frog_x, frog_y
    global carx, carxx, carxxx, cary, caryy, caryyy
    # if (frog_x > carx and frog_x < carx+70 and frog_y < cary) or (frog_x > carxx and frog_x < carxx+100 and frog_y < caryy) or (frog_x > carxxx and frog_x < carxxx+30 and frog_y < caryyy):
    #     print("Got hit")
    #     frog_x = 400
    #     frog_y = 540
    #     image(frog, frog_x, frog_y)
    if (frog_x > carx and frog_x < carx+70 and frog_y > cary and frog_y < cary+23.333333333333333):
        print("Got hit 70")
        frog_x = 400
        frog_y = 540
        image(frog, frog_x, frog_y)
    elif (frog_x > carxx and frog_x < carxx+100 and frog_y > caryy and frog_y < caryy+33.333333333):
        print("Got hit 100")
        frog_x = 400
        frog_y = 540
        image(frog, frog_x, frog_y)
    elif(frog_x > carxxx and frog_x < carxxx+30 and frog_y > caryyy and frog_y < caryyy+10):
        print("Got hit 30")
        frog_x = 400
        frog_y = 540
        image(frog, frog_x, frog_y)
    # 9. Create more car objects of different lengths, speed, and size
    
class Car:
    def __init__(self, x, y, length, speed):
        self.x = x
        self.y = y
        self.length = length
        self.speed = speed
        
        self.car_image = loadImage("carRight.png")
        if self.speed < 0:
            self.car_image = loadImage("carLeft.png")
        
        self.car_image.resize(self.length, self.length / 3)
        
    def draw(self):
        image(self.car_image, self.x, self.y)
    
    def update(self):
        self.x += self.speed
        
        if self.x > width:
            self.x = -self.length
            
        if self.x < -self.length:
            self.x = width
