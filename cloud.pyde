'''
Draw a bullseye in the centre of the screen
'''

def setup():
    size(640, 360)
    background(51)
    noStroke()
    noLoop()
    
def draw():
    drawCloud("#e6e9ef", 100, 300)
    drawCloud("#9ca5b7", 400, 200)
    drawCloud("##c4c7ce", width/2, height/2)
    
        
def drawCloud(colour, xloc, yloc):
    noStroke()
    ellipse(xloc, yloc/2, 50, 50)
    ellipse(xloc+30, yloc/2, 50, 50)
    ellipse(xloc+10, yloc/2-20, 50, 50)
            

    
        
