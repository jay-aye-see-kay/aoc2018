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
    if event[0]:
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
                change_minute = events[event_index][3]
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


sleepy_boi = guard_time_map[max_asleep[0]]

asleep_minutes = {time: 0 for time in range(0, 60)}

for times in sleepy_boi.values():
    for minute, value in times.items():
        asleep_minutes[minute] += value

max_minute = (0, 0)
for minute, value in asleep_minutes.items():
    if value > max_minute[1]:
        max_minute = (minute, value)

print("guard_id", max_asleep)
print("max_minute", max_minute)

guard_id_int = int(max_asleep[0][1:])
print('ans', guard_id_int * max_minute[0])
