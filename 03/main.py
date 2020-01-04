data = open("data.txt")


def parse_claim(string):
    _, _, offset, size = string.split(" ")
    x, y = offset[:-1].split(",")
    width, height = size.split("x")
    return {
        "x": int(x),
        "y": int(y),
        "width": int(width),
        "height": int(height),
    }

claim_map = {}

for claim_string in data:
    claim = parse_claim(claim_string)
    x_range = range(claim['x'], claim['x'] + claim['width'])
    y_range = range(claim['y'], claim['y'] + claim['height'])
    for x in x_range:
        for y in y_range:
            coord = (x, y)
            if coord in claim_map:
                claim_map[coord] += 1
            else:
                claim_map[coord] = 1

overlap_count = 0
for coord, count in claim_map.items():
    if count >= 2:
        overlap_count += 1

print('overlap_count', overlap_count)
