#Based of off ispchr's work at https://github.com/ispchr/projectileMotionQuadraticDrag
import math
from matplotlib import pyplot as plt
#constants
g = 9.81
rho = 1.225
N= 1000
cd = .5

###############################################################
###     See notes for info on Runge-Katta method (RK4)      ###
###############################################################
class RK4:
    def __init__(self, coords, vel):
        self.coords = coords
        self.vel = vel
class startParam:
    def __init__(self,endTime,xVel,yVel,dragConst,stepSize):
        self.endTime = endTime
        self.xVel= xVel
        self.yVel = yVel
        self.dragConst = dragConst
        self.stepSize = stepSize


def ODEx0(u):
    return u
def ODEx1(dragConst,u,v):
    return -dragConst * u * math.sqrt(u*u+v*v)

def solverx(x,dragConst,u,v,h) -> RK4:
    lOne = h*ODEx0(u)
    kOne = h*ODEx1(dragConst,u,v)

    lTwo = h * ODEx0(u + kOne / 2.0)
    kTwo = h * ODEx1(dragConst, u + kOne / 2.0, v)

    lThree = h * ODEx0(u + kTwo / 2.0)
    kThree = h * ODEx1(dragConst, u + kTwo / 2.0, v) 

    lFour = h * ODEx0(u + kThree) 
    kFour = h * ODEx1(dragConst, u + kThree, v)

    x += (lOne / 6.0 + lTwo / 3.0 + lThree / 3.0 + lFour / 6.0)
    u += (kOne / 6.0 + kTwo / 3.0 + kThree / 3.0 + kFour / 6.0)

    X = RK4(coords=x,vel=u)
    return X


def ODEy0(v):
	return v
def ODEy1(dragConst,u,v):
	return -dragConst * v * math.sqrt(u * u + v * v) - g

def solvery(y,dragConst,u,v,h):
    lOne =  h * ODEy0(v)
    kOne = h * ODEy1(dragConst, u, v)

    lTwo = h * ODEy0(v + kOne / 2.0)
    kTwo = h * ODEy1(dragConst, u, v + kOne / 2.0)

    lThree =  h * ODEy0(v + kTwo / 2.0)
    kThree =  h * ODEy1(dragConst, u, v + kTwo / 2.0) 

    lFour = h * ODEy0(v + kThree)
    kFour = h * ODEy1(dragConst, u, v + kThree)

    y += (lOne / 6.0 + lTwo / 3.0 + lThree / 3.0 + lFour / 6.0)
    v += (kOne / 6.0 + kTwo / 3.0 + kThree / 3.0 + kFour / 6.0)

    Y = RK4(coords=y,vel=v)
    return Y


def calcFunc(initVel:float,diameter:float,mass:float,angle:float) -> startParam:
    end = 2 * initVel * math.sin(angle*math.pi/180)/g
    u = initVel*math.cos(angle*math.pi/180)
    v = initVel*math.sin(angle*math.pi/180)

    area = math.pi * diameter*diameter/4
    dragConst = cd*area*rho/(2.0*mass)

    h = end/N

    ans = startParam(end,u,v,dragConst,h)

    return ans



def main():
    print( "----------------------------------------------")
    print( "    Projectile Motion with Quadratic Drag    ")
    print( "		version 1.0    ")
    print( "----------------------------------------------")
    print( "Enter you Initial Conditions Below    ")


    # asking for different inputs from the user
    mass = float(input("Object Mass "))
    angle = float(input("Initial angle "))
    initVel = float(input("Initail velocity "))
    diameter = float(input("Object diameter "))
    x = float(input("Initial x positiion "))
    y = float(input("INital y position "))
    
    #calculates initial varaibles
    calccd = calcFunc(initVel,diameter,mass,angle)
    u = calccd.xVel
    v = calccd.yVel
    dragConst = calccd.dragConst
    h  = calccd.stepSize

    print( "----------------------------------------------")
    print( "Initializing Simulation ...")
    print( "End time = ",calccd.endTime," s")
    print( "Initial x - velocity = ",u," m/s")
    print( "Initial y - velocity = ",v," m/s")
    print( "Step size = ",h,' s')

    t = 0
    print( "----------------------------------------------")
    print("t\tx\ty")

    f = open("projectileCoords.txt","w+")
    x:RK4
    y:RK4
    xs =[]
    ys= []
    for i in range(N+1):
        if y < 0 :
            break

        for j in range(3):
            if j <1:
                f.write(str(t)+"\t")
                print(t,"\t", end="")
                t+=h

            elif (j<2):
                print(x,"\t",end = "")
                f.write(str(x)+"\t")
                X = solverx(x,dragConst,u,v,h)
                x  = X.coords
                u = X.vel
                xs.append(x)

            else:
                print(y,"\t")
                f.write(str(y)+"\n")
                Y = solvery(y,dragConst,u,v,h)
                y  = Y.coords
                v = Y.vel
                ys.append(y)
    
    f.close()
    plt.plot(xs,ys)
    plt.show()
    
if __name__ == "__main__":
    main()