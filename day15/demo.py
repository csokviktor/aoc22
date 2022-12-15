def get_edges(sensor):
    sx, sy, d = sensor
    for dx in range(d + 2):
        dy = (d + 1) - dx
        for px, py in [(-1, 1), (1, -1), (1, 1), (-1, -1)]:
            x = sx + (dx * px)
            y = sy + (dy * py)
            yield (x, y)


print(set(get_edges((9, 16, 1))))
