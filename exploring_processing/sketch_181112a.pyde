x = 0
y = 0
def setup():
    global sat_img
    global back_img
    
    size(630,385)
    sat_img = loadImage("sakura2.png")
    back_img = loadImage("fuji.png")
    
def draw():
    background(back_img)
    image(sat_img, 50, 50, 300, 250)

    global x
    
    if x >= 385:
        x = 0
    x += 3
    
    stroke("#f7f4f2")
    strokeWeight(3)
    fill("#ffe2ee")
    ellipse(600-x/2, x, 25, 50)
    
    noStroke()
    fill("#c6edf2")
    rect(y,50, 30, 30)
    
def mouseClicked():
    global y
    y += 30
    if y >= 630:
        y = 0
    
