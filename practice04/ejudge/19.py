import math

R = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

def dist(a,b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def intersects_circle(A,B,R):
    x1,y1 = A
    x2,y2 = B
    dx = x2-x1
    dy = y2-y1
    a = dx*dx + dy*dy
    b = 2*(x1*dx + y1*dy)
    c = x1*x1 + y1*y1 - R*R
    disc = b*b - 4*a*c
    if disc < 0:
        return False
    sqrt_disc = math.sqrt(disc)
    t1 = (-b - sqrt_disc)/(2*a)
    t2 = (-b + sqrt_disc)/(2*a)
    return (0<=t1<=1) or (0<=t2<=1)

A = (x1,y1)
B = (x2,y2)
dAB = dist(A,B)

if not intersects_circle(A,B,R):
    print(f"{dAB:.10f}")
else:
    dA = math.hypot(x1,y1)
    dB = math.hypot(x2,y2)
    tanA = math.sqrt(dA**2 - R**2)
    tanB = math.sqrt(dB**2 - R**2)

    phiA = math.acos(R/dA)
    phiB = math.acos(R/dB)

    angleA = math.atan2(y1, x1)
    angleB = math.atan2(y2, x2)
    delta = abs(angleB - angleA)
    if delta > math.pi:
        delta = 2*math.pi - delta

    arc = delta - phiA - phiB
    if arc < 0:
        arc = 0

    length = tanA + tanB + R*arc
    print(f"{length:.10f}")