import random


def scrambler():
    moves = ["L", "L2", "L'",
            "R", "R2", "R'",
            "F", "F2", "F'",
            "B", "B2", "B'",
            "U", "U2", "U'",
            "D", "D2", "D'"]

    cnt = 0
    output = []
    prev = 'ZZ'

    while cnt < 15:
        pos = random.randrange(18)
        if moves[pos][0] != prev[0]:
            output.append(moves[pos])
            prev = moves[pos]
            cnt += 1
            
    print('Here is a scramble for you. Solve Fast!!')
    print()
    print(' '.join(output))


if __name__ == '__main__':
    scrambler()