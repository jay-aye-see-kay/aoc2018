data = open("data.txt")
freq_change_list = [int(change) for change in data]

freq_value = 0
freqs_seen = { freq_value: 1 }
found_duplicate = False

while not found_duplicate:
    for freq_change in freq_change_list:
        freq_value += freq_change
        if freq_value in freqs_seen:
            found_duplicate = True
            break
        else:
            freqs_seen[freq_value] = 1

print(freq_value)
