from collections import namedtuple

 
 
def draw_line(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    a = dy / dx
    b = p1.y - a * p1.x
    points = []
    if dx > dy:
        for x in range(p1.x, p2.x, 1 if dx >= 0 else -1):
            y = round(a * x + b)
            points.append([x, y])
    else:
        for y in range(p1.y, p2.y, 1 if dy >= 0 else -1):
            x = round((y - b) / a)
            points.append([x, y])
    return points
 
 
Point = namedtuple('Point', 'x y')
p2 = Point(100, 100)
p1 = Point(120, 600)
print(draw_line(p1, p2))