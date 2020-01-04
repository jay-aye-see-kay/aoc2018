data = open("data.txt")


def parse_claim(string):
    id, _, offset, size = string.split(" ")
    x, y = offset[:-1].split(",")
    width, height = size.split("x")
    return (
        id[1:],
        {"x": int(x), "y": int(y), "width": int(width), "height": int(height)},
    )


claim_list = [parse_claim(claim_string) for claim_string in data]
claim_map = {}

for id, claim in claim_list:
    x_range = range(claim["x"], claim["x"] + claim["width"])
    y_range = range(claim["y"], claim["y"] + claim["height"])
    for x in x_range:
        for y in y_range:
            coord = (x, y)
            if coord in claim_map:
                claim_map[coord].append(id)
            else:
                claim_map[coord] = [id]

overlap_count = 0
for coord, id_list in claim_map.items():
    if len(id_list) >= 2:
        overlap_count += 1

print("overlap_count", overlap_count)


for id, claim in claim_list:
    claim_not_overlapping = True
    x_range = range(claim["x"], claim["x"] + claim["width"])
    y_range = range(claim["y"], claim["y"] + claim["height"])
    for x in x_range:
        for y in y_range:
            coord = (x, y)
            if len(claim_map[coord]) != 1:
                claim_not_overlapping = False
    if claim_not_overlapping:
        print('id', id)
