import turtle as tt

# point(x, y, angle)
# angle starts from +x axis. Angle > 0 is unti-clockwise

bgcol = (0, 0, 0)
pencol = 'white'
debugcol = 'green'

def resetpoint(p):
    tt.penup()
    tt.setpos(p[0], p[1])
    tt.pendown()
    tt.seth(p[2])

def currentpoint():
    x,y = tt.pos()
    h = tt.heading()
    return (x, y, h)

def Generate(A, B, L, gene, ratio, n):
    resetpoint(A)
    points = []

    #爬一遍这个线段的分形,但目的只是得到各个端点(当debugcol=bgcol即隐藏这段绘制)
    tt.pencolor(debugcol)
    for head in gene:
        if head == 'END':
            break
        else:
            head = int(head)

        if head < 0:
            tt.right(abs(head))
        else:
            tt.left(head)

        arrived = currentpoint()
        points.append(arrived)
        tt.forward(L * ratio)
    points.append(B)

    #只有最细的一层迭代需要真正的绘制
    if n == 1:
        resetpoint(A)
        tt.pencolor(pencol)
        for p in points:
            tt.setpos(p[0], p[1]) #draw call
    #过程迭代只是为了在每一个线段上继续分形
    else:
        i = 0
        while i < len(points) - 1:
            Generate(points[i], points[i+1], L * ratio, gene, ratio, n-1)
            i = i + 1

if __name__ == '__main__':
    tt.hideturtle() #hide the arrow
    tt.speed(10)
    tt.pensize(1)
    tt.colormode(255)
    tt.bgcolor(bgcol)

    A = (-500, 0, 0)
    B = (500, 0, 0)
    L = 1000
    gene = [0, 90, -90, -90, 90, -90, 90, 90, -90, 'END']
    ratio = 0.2
    n = 3
    
    resetpoint(A)
    Generate(A, B, L, gene, ratio, n)
    tt.done()