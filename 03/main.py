data = open("data.txt")


def parse_claim(string):
    id, _, offset, size = string.split(" ")
    x, y = offset[:-1].split(",")
    width, height = size.split("x")
    x_range = range(int(x), int(x) + int(width))
    y_range = range(int(y), int(y) + int(height))
    coord_list = []
    for x in x_range:
        for y in y_range:
            coord_list.append((x, y))
    return id[1:], coord_list


claim_list = [parse_claim(claim_string) for claim_string in data]
claim_map = {}

for id, coord_list in claim_list:
    for coord in coord_list:
        if coord in claim_map:
            claim_map[coord].append(id)
        else:
            claim_map[coord] = [id]

overlap_count = 0
for coord, id_list in claim_map.items():
    if len(id_list) >= 2:
        overlap_count += 1

print("overlap_count", overlap_count)


for id, coord_list in claim_list:
    claim_not_overlapping = True
    for coord in coord_list:
        if len(claim_map[coord]) != 1:
            claim_not_overlapping = False
    if claim_not_overlapping:
        print("id", id)
