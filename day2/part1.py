data = open('data.txt', 'r').read().split('\n')
data.remove('')


def get_letter(s):
    st = s.split(":")
    st = st[0].split(" ")
    return st[1]


def get_pass(s):
    st = s.split(":")
    return st[1]


def get_min(s):
    st = s.split(":")
    st = st[0].split(" ")
    st = st[0].split("-")
    return int(st[0])


def get_max(s):
    st = s.split(":")
    st = st[0].split(" ")
    st = st[0].split("-")
    return int(st[1])


def get_count(letter, string):
    count = 0
    for l in string:
        if l == letter:
            count += 1
    return count


valid = 0
for d in data:
    minim = get_min(d)
    maxim = get_max(d)
    passw = get_pass(d)
    letter = get_letter(d)

    count = get_count(letter, passw)
    if count >= minim and count <= maxim:
        valid += 1

print(valid)
