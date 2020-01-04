data = open("data.txt")

letter_count_list = []

for barcode in data:
    letter_count = {}
    for letter in barcode:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    letter_count_list.append(letter_count)

has2 = 0
has3 = 0

for letter_count in letter_count_list:
    barcode_has2 = False
    barcode_has3 = False
    for v in letter_count.values():
        if v == 2:
            barcode_has2 = True
        if v == 3:
            barcode_has3 = True
    if barcode_has2:
        has2 += 1
    if barcode_has3:
        has3 += 1


print(has2 * has3)
