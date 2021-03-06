data = open("data.txt")
timestamps = sorted(list(data))


def parse_timestamp(timestamp):
    datetime, text = timestamp.replace("[", "").split("] ")
    date, time = datetime.split(" ")
    _, minute = time.split(":")
    id = None
    if "Guard #" in text:
        _, id, _, _ = text.split(" ")

    return (id, text, date, minute)


event_list = [parse_timestamp(timestamp) for timestamp in timestamps]

per_guard_per_day = []

for event in event_list:
    if event[0]:  # only has first field if new guard or day
        per_guard_per_day.append([event])
    else:
        per_guard_per_day[-1].append(event)

guard_time_map = {}

for events in per_guard_per_day:
    if len(events) == 1:
        continue
    guard_id = events[0][0]
    is_asleep = 0
    change_minute = int(events[1][3])
    times = {}
    event_index = 1
    event_range = len(events)
    date = events[1][2]
    for minute in range(0, 60):
        if minute == change_minute:
            is_asleep = (is_asleep + 1) % 2
            event_index += 1
            if event_index < event_range:
                change_minute = int(events[event_index][3])
        times[minute] = is_asleep
    if guard_id in guard_time_map:
        guard_time_map[guard_id][date] = times
    else:
        guard_time_map[guard_id] = {date: times}

guard_asleep_minutes = {}
max_asleep = ("", 0)
for guard_id, guard_times in guard_time_map.items():
    time_asleep = 0
    for k, times in guard_times.items():
        time_asleep += sum(times.values())
    guard_asleep_minutes[guard_id] = time_asleep
    if time_asleep > max_asleep[1]:
        max_asleep = (guard_id, time_asleep)


def get_max_sleepy_minute(guard_id, guard_time_map):
    guard_times = guard_time_map[guard_id]

    # sum all minutes into one dict
    asleep_minutes = {time: 0 for time in range(0, 60)}
    for times in guard_times.values():
        for minute, value in times.items():
            asleep_minutes[minute] += value

    # find the sleepiest minute
    max_minute = (0, 0)
    for minute, value in asleep_minutes.items():
        if value > max_minute[1]:
            max_minute = (minute, value)

    return max_minute


sleepiest_guard_id = max_asleep[0]
max_minute = get_max_sleepy_minute(sleepiest_guard_id, guard_time_map)

guard_id_int = int(max_asleep[0][1:])
print("part1 ans", guard_id_int * max_minute[0])

overall_max_min = (0, 0, '') # (minute, value, guard_id)
for guard_id in guard_time_map.keys():
    minute, value = get_max_sleepy_minute(guard_id, guard_time_map)
    if value > overall_max_min[1]:
        overall_max_min = (minute, value, guard_id)

guard_id_int = int(overall_max_min[2][1:])
print("part2 ans", guard_id_int * overall_max_min[0])
