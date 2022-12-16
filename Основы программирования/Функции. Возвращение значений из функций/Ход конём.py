cells = [
    ["A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8"],
    ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],
    ["A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6"],
    ["A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5"],
    ["A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4"],
    ["A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3"],
    ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],
    ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"]
]

alf = [chr(i) for i in range(ord("A"), ord("H") + 1)]


def from_cell_to_coord(cell):
    return alf.index(cell[0]), int(cell[1]) - 1


def from_coord_to_cell(cooed):
    x, y = cooed
    return alf[x] + str(y + 1)


def possible_turns(cell):
    next_step = []
    x, y = from_cell_to_coord(cell)
    step_2 = [-2, 2]
    step_1 = [-1, 1]
    for i in step_1:
        for j in step_2:
            a, b = x + i, y + j
            if 0 <= a <= 7 and 0 <= b <= 7:
                next_step.append((a, b))
    for i in step_2:
        for j in step_1:
            a, b = x + i, y + j
            if 0 <= a <= 7 and 0 <= b <= 7:
                next_step.append((a, b))
    return sorted([from_coord_to_cell(i) for i in next_step])

