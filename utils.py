from collections import namedtuple

RBGMAX = 255
HLSMAX = [360, 100., 100.]

# https://support.microsoft.com/pt-br/help/29240/how-to-converting-colors-between-rgb-and-hls-hbs


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


def rbg_to_hls(rbg_values: dict):
    # https://www.rapidtables.com/convert/color/rgb-to-hsl.html
    _r = rbg_values['red'] / RBGMAX
    _g = rbg_values['green'] / RBGMAX
    _b = rbg_values['blue'] / RBGMAX

    c_max = max(_r, _g, _b)
    c_min = min(_r, _g, _b)
    delta = c_max - c_min

    lightness = (c_max + c_min) / 2
    hue = 0.
    saturation = 0.

    if delta != 0.:
        saturation = delta / (1 - abs(2 * lightness - 1))

    if c_max == _r:
        hue = 60 * (((_g - _b) / delta) % 6)
    elif c_max == _g:
        hue = 60 * (((_b - _r) / delta) + 2.)
    elif c_max == _b:
        hue = 60 * (((_r - _g) / delta) + 4.)

    return {'hue': hue, 'lightness': lightness, 'saturation': saturation}


def hls_to_rbg():
    pass


def color_conversion():
    pass


test_color = {'red': 0, 'green': 0, 'blue': 255}
print(rbg_to_hls(test_color))