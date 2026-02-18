import math

r = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1
a = dx*dx + dy*dy
b = 2*(dx*x1 + dy*y1)
c = x1*x1 + y1*y1 - r*r
disc = b*b - 4*a*c

if disc <= 0:
    print("0.0000000000")
else:
    sqrt_disc = math.sqrt(disc)
    t1 = (-b - sqrt_disc) / (2*a)
    t2 = (-b + sqrt_disc) / (2*a)
    t_min = max(0, min(t1, t2))
    t_max = min(1, max(t1, t2))
    if t_min >= t_max:
        print("0.0000000000")
    else:
        length = math.hypot(dx, dy) * (t_max - t_min)
        print(f"{length:.10f}")
