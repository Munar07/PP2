import math

r = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

def dist(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def tangent_length(p, r):
    d = math.hypot(p[0], p[1])
    if d < r:
        return 0.0, 0.0
    l = math.sqrt(d*d - r*r)
    angle = math.atan2(p[1], p[0])
    theta = math.acos(r/d)
    return l, angle, theta

p1 = (x1, y1)
p2 = (x2, y2)

d1, a1, t1 = tangent_length(p1, r)
d2, a2, t2 = tangent_length(p2, r)

# angles of tangent points
angles = [(a1 - t1, a2 - t2), (a1 - t1, a2 + t2), (a1 + t1, a2 - t2), (a1 + t1, a2 + t2)]

res = float('inf')
for ang1, ang2 in angles:
    # arc length along circle
    diff = abs(ang2 - ang1)
    diff = min(diff, 2*math.pi - diff)
    total = math.hypot(math.hypot(x1, y1)-r, 0) + math.hypot(math.hypot(x2, y2)-r, 0) + diff*r
    # more accurate: sum tangent lengths + arc
    total = math.sqrt(x1**2 + y1**2 - r**2) + math.sqrt(x2**2 + y2**2 - r**2) + diff * r
    res = min(res, total)

# check if segment doesn't cross circle
def crosses_circle():
    dx = x2 - x1
    dy = y2 - y1
    a = dx*dx + dy*dy
    b = 2*(x1*dx + y1*dy)
    c = x1*x1 + y1*y1 - r*r
    delta = b*b - 4*a*c
    if delta < 0:
        return False
    t1_root = (-b - math.sqrt(delta)) / (2*a)
    t2_root = (-b + math.sqrt(delta)) / (2*a)
    return (0 < t1_root < 1) or (0 < t2_root < 1)

if not crosses_circle():
    res = min(res, dist(p1, p2))

print(f"{res:.10f}")
