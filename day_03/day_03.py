from aocd import data

NORTH = '^'
SOUTH = 'v'
EAST = '>'
WEST = '<'

x, y = 0, 0
gifts = 1
visited = [(0, 0)]

for char in data[::2]:
    if char == NORTH:
        dx, dy = 0, 1
    elif char == SOUTH:
        dx, dy = 0, -1
    elif char == EAST:
        dx, dy = 1, 0
    elif char == WEST:
        dx, dy = -1, 0
    x += dx
    y += dy
    location = x, y
    if location not in visited:
        gifts += 1
        visited.append(location)

x, y = 0, 0
for char in data[1::2]:
    if char == NORTH:
        dx, dy = 0, 1
    elif char == SOUTH:
        dx, dy = 0, -1
    elif char == EAST:
        dx, dy = 1, 0
    elif char == WEST:
        dx, dy = -1, 0
    x += dx
    y += dy
    location = x, y
    if location not in visited:
        gifts += 1
        visited.append(location)

print(gifts)
