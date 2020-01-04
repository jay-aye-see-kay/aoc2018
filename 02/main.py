data = open("data.txt")
barcode_list = [barcode for barcode in data]


def barcode_match(barcode1, barcode2):
    diff_count = 0
    for i, char1 in enumerate(barcode1):
        char2 = barcode2[i]
        if char1 != char2:
            diff_count += 1
    return diff_count == 1


for barcode1 in barcode_list:
    for barcode2 in barcode_list:
        if barcode1 == barcode2:
            continue
        match = barcode_match(barcode1, barcode2)
        if match:
            print("barcode1", barcode1)
            print("barcode2", barcode2)
            break
