import math

R = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1

a = dx*dx + dy*dy
b = 2*(x1*dx + y1*dy)
c = x1*x1 + y1*y1 - R*R

disc = b*b - 4*a*c

if disc < 0:
    length = 0.0
else:
    sqrt_disc = math.sqrt(disc)
    t1 = (-b - sqrt_disc) / (2*a)
    t2 = (-b + sqrt_disc) / (2*a)
    t_low = max(0, min(t1, t2))
    t_high = min(1, max(t1, t2))
    if t_high < t_low:
        length = 0.0
    else:
        length = (t_high - t_low) * math.hypot(dx, dy)

print(f"{length:.10f}")