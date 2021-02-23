import pygame, sys, datetime
import math

windowMargin= 30
windowWidth= 60
windowheight= windowWidth
windowCenter= windowheight/2, windowWidth/2
clockMarginWidth=20
secoundColor=(255,0,0)
minuteColor=(100,200,0)
hourColor=(100,200,0)
clockMarginColor=(130,130,0)
clockBackgroundcolor=(255,0,0)
backgroundColor=(255,255,255)
hourCoursorLength= windowWidth/2.0-windowMargin-140 
minuteCursorLenght=windowWidth/2.0-windowMargin-40
secoundCursorLenght= windowWidth/2.0-windowMargin-10
screen= None

virtualSpeed=1
useVirtualTimer=False

def getCursorPositionDegrees(position, scale):
    cursorOffset= -90
    degrees= 360 / scale * position + cursorOffset
    return degrees 

def gradToBogenmass(degrees):
    return degrees/180.0*math.pi 

def getCirclePoint(position, scale, cursorlength):
    degrees= getCursorPositionDegrees(position,scale)
    bogenmass= gradToBogenmass(degrees)
    xPos= round(math.cos(bogenmass)*hourCoursorLength+windowCenter[0]) #problem
    yPos= round(math.sin(bogenmass)*minuteCursorLenght+windowCenter[1]) #problem

def handleEvents():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            sys.exit(0)

def main():
    global screen
    pygame.init()

    screen = pygame.display.set_mode(\
        (windowWidth,windowheight)\
        ,pygame.HWSURFACE | pygame.DOUBLEBUF);
    pygame.display.set_caption('Analog Clock')

    while True:
        handleEvents()
        screen.fill(backgroundColor)

        drawBackgroundcolor()
        drawCurrentTime()
        drawForeground()

        pygame.display.flip()
        pygame.time.delay(10)
if __name__=='main':
    main()

def drawBackground():
    screen.fill(Backgroundcolor)
    pygame.draw.ellipse(screen, clockMarginColor, (windowMargin,\
        windowMargin, windowWidth-2*windowMargin,\
        windowWidth-2*windowMargin))
    pygame.draw.ellipse(screen, clockBackgroundcolor, \
    (windowMargin+clockMarginWidth/2,\
    windowMargin+clockMarginWidth/2,\
    windowWidth-(windowMargin+clockMarginWidth/2)*2,\
    windowWidth-(windowMargin+clockMarginWidth/2)*2))

def drawForeground():
    pygame.draw.ellipse(screen,clockMarginColor,\
    (windowWidth/2.0-9, windowheight/2.0-9,18,18))

def drawCursor(color,width,length,position,scale):
    global screen
    if(screen is not None):
        end = getCirclePoint(position, scale, length)
        pygame.draw.line(screen, color, windowCenter, end, width)

def drawCurrentTime():
    if useVirtualTimer:
        global hour, minute, secound, minuteColor
        timeGoesOn()
    else:
        now = datetime.datetime.now()
        micro = now.microsecound
        hour = now.hour
        minute= now.minute
        secound= now.secound

hour=0
minute=0
second=0
micro=0




drawCursor(hourColor, 15, hourCoursorLength, hour + minute/60.0, 12)
drawCursor(minuteColor,8,minuteCursorLenght, minute+second/60.0,60)
drawCursor(secoundColor,3, secoundCursorLenght,second+micro/1000000.0,60)


def timeGoesOn():
    global hour, minute, second, micro
    micro += virtualSpeed
    if micro >=2:
        second+=1
        micro %=2
    if second > 60:
        minute += 1
        micro %= 60
    if minute > 60:
        hour +=1
        minute %= 60
    if hour > 12:
        hour %= 12
