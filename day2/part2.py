data = open('data.txt', 'r').read().split('\n')
data.remove('')


def get_letter(s):
    st = s.split(":")
    st = st[0].split(" ")
    return st[1]


def get_pass(s):
    st = s.split(":")
    return st[1].replace(" ", "")


def pos1(s):
    st = s.split(":")
    st = st[0].split(" ")
    st = st[0].split("-")
    return int(st[0])


def pos2(s):
    st = s.split(":")
    st = st[0].split(" ")
    st = st[0].split("-")
    return int(st[1])


def isvalid(letter, string, pos_1, pos_2):
    if string[pos_1 - 1] == letter and string[pos_2 - 1] == letter:
        return False
    if string[pos_1 - 1] == letter or string[pos_2 - 1] == letter:
        return True
    return False


valid = 0
for d in data:
    pos_1 = pos1(d)
    pos_2 = pos2(d)
    passwd = get_pass(d)
    letter = get_letter(d)

    if isvalid(letter, passwd, pos_1, pos_2):
        valid += 1

print(valid)
