def reta (p0, p1):
    x0, y0 = p0
    x1, y1 = p1

    dx = abs(x1-x0)
    dy = abs(y1-y0)
    if x0 < x1:
        sx = 1
    else:
        sx = -1


    if y0 < y1:
        sy = 1
    else:
        sy = -1
    err = dx-dy

    while True:
        print (x0, y0)
        if x0 == x1 and y0 == y1:
            return

        e2 = 2*err
        if e2 > -dy:
            err = err - dy
            x0 = x0 + sx
        if e2 < dx:
            err = err + dx
            y0 = y0 + sy

x = []
y = []
x1=int(input("Digite x1"))
x2=int(input("Digite x2"))
x.append(x1)
x.append(x2)
y1=int(input("Digite y1"))
y2=int(input("Digite y2"))
y.append(y1)
y.append(y2)
reta (x, y)
