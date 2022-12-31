# An improved version of the "check" function found in the "Sudokum" Module
# customised by Syed-Taha-0 (Github)
# The original check function uses duplicate numbers to check if a grid has been...
# ... solved. That caused problems if the grid was empty, as it didn't check for...
# ...empty cells(0 cells). This problem has been fixed in this variant of the function
def check(list):
    zero_count = 0
    for r in range(9):
        tmp_set = set()
        dup = []
        for v in list[r]:
            if v == 0:
                zero_count += 1
            if v in tmp_set and v != 0:
                dup.append(v)
            tmp_set.add(v)
            if len(dup) > 0:
                pos = [(r, list[r].index(d)) for d in dup]
                return False, pos

    for c in range(9):
        solution_list = []
        dup = []
        for r in range(9):
            v = list[r][c]
            if v == 0:
                zero_count += 1
            if v in solution_list and v != 0:
                dup.append(v)
            solution_list.append(v)
            if len(dup) > 0:
                pos = [(solution_list.index(d), c) for d in dup]
                return False, pos

    for r in range(0, 9, 9 // 3):
        for c in range(0, 9, 9 // 3):
            solution_list = []
            dup = []
            for i in range(9):
                v = list[r + i // 3][c + i % 3]
                if v == 0:
                    zero_count += 1
                if v in solution_list and v != 0:
                    dup.append(v)
                solution_list.append(v)
                if len(dup) > 0:
                    pos = []
                    for d in dup:
                        i = solution_list.index(d)
                        pos.append((r + i // 3, c + i % 3))
                    return False, pos
    if zero_count == 0:
        return True, []
    return False, []
