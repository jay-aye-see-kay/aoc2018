data = open("data.txt").readlines()[0].strip()


letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
pairs = []
for letter in letters:
    pairs.append("{}{}".format(letter, letter.upper()))
    pairs.append("{}{}".format(letter.upper(), letter))


def remove_pairs(polymer):
    initial_length = len(polymer)
    changed = False
    for pair in pairs:
        polymer = polymer.replace(pair, "")
    if len(polymer) != initial_length:
        changed = True
    return polymer, changed


def reduce_polymer(polymer):
    changed = True
    while changed:
        polymer, changed = remove_pairs(polymer)
    return polymer


print("5.1 ans", len(reduce_polymer(data)))


shortest_length = 1000000
for letter in letters:
    polymer = data.replace(letter, '').replace(letter.upper(), '')
    reduced_polymer = reduce_polymer(polymer)
    if shortest_length > len(reduced_polymer):
        shortest_length = len(reduced_polymer)

print('5.2 ans', shortest_length)
