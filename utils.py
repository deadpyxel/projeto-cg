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

    # _r = round(_r, 2)
    # _g = round(_g, 2)
    # _b = round(_b, 2)

    c_max = max(_r, _g, _b)
    c_min = min(_r, _g, _b)
    print(f'MAX: {c_max} MIN:{c_min}')
    delta = c_max - c_min

    lightness = (c_max + c_min) / 2
    print(f'L: {lightness}')
    hue = 0.
    saturation = 0.

    if c_max != c_min:
        saturation = delta / (c_max + c_min) if lightness < 0.5 else float(
            delta / (2.0 - delta))

    if c_max == _r:
        hue = 60 * ((_g - _b) / delta)
    elif c_max == _g:
        hue = 60 * (((_b - _r) / delta) + 2.)
    elif c_max == _b:
        hue = 60 * (((_r - _g) / delta) + 4.)

    if hue < 0.:
        hue += 360.

    hue = hue / 360 * 240
    saturation *= 240
    lightness *= 240
    return {'hue': hue, 'lightness': lightness, 'saturation': saturation}


def hls_to_rbg(hls_values: dict):
    # https://www.rapidtables.com/convert/color/hsl-to-rgb.html

    # normalization
    _h = 360 * hls_values['hue'] / 240
    _s = hls_values['saturation'] / 240
    _l = hls_values['lightness'] / 240

    if _s == 0.:
        val = 255 / 100
        return {'red': val, 'green': val, 'blue': val}

    t1 = float(_l * (1. + _s)) if _l < 0.5 else (_l + _s) - (_l + _s)
    t2 = 2.0 * _l - t1

    _h = _h / 360
    _rgb = _r, _g, _b = _h + 1. / 3, _h, _h + 1. / 3

    for ch in _rgb:
        if ch < 0:
            ch += 1
        elif ch > 1:
            ch -= 1

        if 6 * ch < 1:
            ch = t2 + (t1 - t2) * 6 * ch
        elif 2 * ch < 1:
            ch = t1
        elif 3 * ch < 2:
            ch = float(t2 + ((t1 - t2) * (2 / 3 - ch) * 6))
        else:
            ch = t2

        ch = round(ch * RBGMAX)
        print(ch)
    print(_rgb)
    return {'red': _rgb[0], 'green': _rgb[1], 'blue': _rgb[2]}


def color_conversion():
    pass


test_color = {'red': 24, 'green': 98, 'blue': 118}
hls = rbg_to_hls(test_color)
print(hls)
print(hls_to_rbg(hls))

# Point = namedtuple('Point', 'x y')
# p2 = Point(100, 100)
# p1 = Point(120, 600)
# print(draw_line(p1, p2))