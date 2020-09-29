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
quantidade=int(input("Digite quantos pontos terá"))
for i in range(quantidade):
    if (i==0):
        print (i)
        print("digite x{}".format(i))
        x1=int(input())
        print("digite y{}".format(i))
        y1=int(input(""))
        ultimo1=x1 #será usado para voltar e fechar o polígono(x0)
        ultimo2=y1 #será usado pra voltar e fechar o polígono(y0)
        x.append(x1)
        x.append(y1)
    if (i==1):
        print("digite x{}".format(i))
        x1 = int(input())
        print("digite y{}".format(i))
        y1 = int(input(""))
        y.append(x1)
        y.append(y1)
        reta(x,y)
    if (i>1 and i!=quantidade-1):
        aux1=y[0]
        aux2=y[1]
        x[0]=aux1
        x[1]=aux2
        y.clear()
        print("digite x{}".format(i))
        x1 = int(input())
        print("digite y{}".format(i))
        y1 = int(input(""))
        y.append(x1)
        y.append(y1)
        reta(x, y)
    if(i==quantidade-1 and i!=0):
        aux1 = y[0]
        aux2 = y[1]
        x[0] = aux1
        x[1] = aux2
        y.clear()
        print("digite x{}".format(i))
        x1 = int(input())
        print("digite y{}".format(i))
        y1 = int(input(""))
        y.append(x1)
        y.append(y1)
        reta(x, y)
        # indo do ultimo ponto pro primeiro, para formar o polígono
        x[0] = y[0]
        x[1] = y[1]
        y[0]=ultimo1
        y[1]=ultimo2
        reta(x, y)
