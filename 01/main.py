data = open("data.txt")

freq_value = 0

for freq_change in data:
    freq_value += int(freq_change)

print(freq_value)
