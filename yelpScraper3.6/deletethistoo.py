def g(x):
    y0 = x + 1
    y1 = x * 3
    y2 = y0 ** y1
    return {'y0': y0, 'y1': y1, 'y2': y2}


x = g(10)

print(x['y0'])