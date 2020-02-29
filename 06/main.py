data = open("data.txt")

max_x = 0
max_y = 0
coordinates = []
for line in data:
    x_str, y_str = line.split(', ')
    x = int(x_str)
    y = int(y_str)
    coordinates.append((x, y))
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y


def get_nearest(x, y, coordinates):
    min_distance = 100000000000
    closest_coord = None
    equidistance = False
    for coord in coordinates:
        distance =  abs(x - coord[0]) + abs(y - coord[1])
        if min_distance > distance:
            min_distance = distance
            closest_coord = coord
            equidistance = False
        elif(min_distance == distance):
            equidistance = True
    if equidistance:
        return None
    return closest_coord


star_map = {}
coord_details = { coords: { "count": 1, "isInf": False } for coords in coordinates }

for x in range(0, max_x + 1):
    for y in range(0, max_y + 1):

        if (x, y) in coordinates:
            # when x, y is a coord
            if not x in star_map.keys():
                star_map[x] = {}
            star_map[x][y] = (x, y)

        else:
            # when x, y is empty space
            if not x in star_map.keys():
                star_map[x] = {}
            nearest_coord = get_nearest(x, y, coordinates)
            star_map[x][y] = nearest_coord
            if nearest_coord:
                coord_details[nearest_coord]["count"] += 1
                if x == 0 or x == max_x or y == 0 or y == max_y:
                    coord_details[nearest_coord]["isInf"] = True


print('coord_details', coord_details)


max_valid_count = 0
for coord, coord_detail in coord_details.items():
    if coord_detail["isInf"] == False and coord_detail["count"] > max_valid_count:
        max_valid_count = coord_detail["count"]

print('max_valid_count', max_valid_count)


# print('star_map', star_map)
