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


polymer = data
changed = True
while changed:
    polymer, changed = remove_pairs(polymer)

print("1.1 ans", len(polymer))
