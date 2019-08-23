from collections import namedtuple

RBGMAX = 255
HLSMAX = [360, 1., 1.]

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


def hls_to_rbg(hls_values: dict):
    # https://www.rapidtables.com/convert/color/hsl-to-rgb.html
    c = (1 - abs(2 * hls_values['lightness'] - 1) * hls_values['saturation'])
    x = c * (1 - abs((hls_values['hue'] / 60.) % 2 - 1))
    m = hls_values['lightness'] - c / 2.

    _r, _g, _b = 0, 0, 0
    if 0. < hls_values['hue'] < 60.:
        _r, _g, _b = c, x, 0
    elif 60. <= hls_values['hue'] < 120.:
        _r, _g, _b = x, c, 0
    elif 120. <= hls_values['hue'] < 180.:
        _r, _g, _b = 0, c, x
    elif 180. <= hls_values['hue'] < 240.:
        _r, _g, _b = 0, x, c
    elif 240. <= hls_values['hue'] < 300.:
        _r, _g, _b = x, 0, c
    elif 300. <= hls_values['hue'] < 360.:
        _r, _g, _b = c, 0, x

    rbg = {
        'red': (_r + m) * 255,
        'green': (_g + m) * 255,
        'blue': (_b + m) * 255
    }
    return rbg


def color_conversion():
    pass


test_color = {'red': 0, 'green': 0, 'blue': 255}
hls = rbg_to_hls(test_color)
print(hls)
print(hls_to_rbg(hls))

# Point = namedtuple('Point', 'x y')
# p2 = Point(100, 100)
# p1 = Point(120, 600)
# print(draw_line(p1, p2))