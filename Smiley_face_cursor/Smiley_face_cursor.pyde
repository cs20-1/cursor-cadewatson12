 # Cade Watson
 # Computer Science
 # October 2 
 # Smiley face cursor

def setup():
    size(500, 500)

def drawHead(x, y):
    background(255)
    ellipse(x, y, 200, 200)

def drawEyes(x, y):
    ellipse(x, y, 50, 50)
    ellipse(x + 80, y, 50, 50)

def drawPupils(x, y):
    ellipse(x, y, 10, 10)
    ellipse(x + 80, y, 10, 10)

def drawMouth(x, y):
    rect(x, y, 80, 40)

def draw():
    fill(238, 255, 0)
    drawHead(mouseX + 250, mouseY + 250)
    fill(255)
    drawEyes(mouseX + 210, mouseY + 225)
    fill(0)
    drawPupils(mouseX + 210, mouseX + 225)
    drawMouth(mouseX + 210, mouseY + 270)
