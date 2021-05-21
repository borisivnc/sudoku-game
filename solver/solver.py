from copy import deepcopy
import numpy as np

def solve(grid):
    candidates = filter(grid)
    grid = fill_singles(grid, candidates)
    if is_solution(grid):
        return grid
    if not is_valid_grid(grid):
        return None
    return guess(grid, candidates)

def filter(grid):
    test_grid = grid.copy()
    candidates = get_candidates(grid)
    filtered_candidates = deepcopy(candidates)
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for candidate in candidates[i][j]:
                    test_grid[i][j] = candidate
                    if not is_valid_grid(fill_singles(test_grid)):
                        filtered_candidates[i][j].remove(candidate)
                    test_grid[i][j] = 0
    return filtered_candidates

def guess(grid, candidates=None):
    grid = grid.copy()
    if not candidates:
        candidates = get_candidates(grid)
    min_len = sorted(list(set(map(
       len, np.array(candidates, dtype=object).reshape(1,81)[0]))))[1]
    for i in range(9):
        for j in range(9):
            if len(candidates[i][j]) == min_len:
                for guess in candidates[i][j]:
                    grid[i][j] = guess
                    solution = solve(grid)
                    if solution is not None:
                        return solution
                    grid[i][j] = 0

def get_candidates(grid : np.ndarray) -> list:
    def subgrid_index(i : int, j : int) -> int:
        return (i//3) * 3 + j // 3
    subgrids = get_subgrids(grid)
    grid_candidates = []
    for i in range(9):
        row_candidates = []
        for j in range(9):
            row = set(grid[i])
            col = set(grid[:, j])
            sub = set(subgrids[subgrid_index(i, j)])
            common = row | col | sub
            candidates = set(range(10)) - common
            if not grid[i][j]:
                row_candidates.append(list(candidates))
            else:
                row_candidates.append([grid[i][j]])
        grid_candidates.append(row_candidates)
    return grid_candidates

def get_subgrids(grid):
    subgrids = []
    for box_i in range(3):
        for box_j in range(3):
            subgrid = []
            for i in range(3):
                for j in range(3):
                    subgrid.append(grid[3*box_i + i][3*box_j + j])
            subgrids.append(subgrid)
    return np.array(subgrids)

def fill_singles(grid, candidates=None):
    grid = grid.copy()
    if not candidates:
        candidates = get_candidates(grid)
    any_fill = True
    while any_fill:
        any_fill = False
        for i in range(9):
            for j in range(9):
                if len(candidates[i][j]) == 1 and grid[i][j] == 0:
                    grid[i][j] = candidates[i][j][0]
                    candidates = merge(get_candidates(grid), candidates)
                    any_fill = True
    return grid

def merge(candidates_1, candidates_2):
    candidates_min = []
    for i in range(9):
        row = []
        for j in range(9):
            if len(candidates_1[i][j]) < len(candidates_2[i][j]):
                row.append(candidates_1[i][j][:])
            else:
                row.append(candidates_2[i][j][:])
        candidates_min.append(row)
    return candidates_min

def create_grid(puzzle_str):
    lines = puzzle_str.replace(' ','').replace('\n','')
    digits = list(map(int, lines))
    grid = np.array(digits).reshape(9,9)
    return grid

def is_valid_grid(grid):
    candidates = get_candidates(grid)
    for i in range(9):
        for j in range(9):
            if len(candidates[i][j]) == 0:
                return False
    return True

def is_solution(grid):
    if np.all(np.sum(grid, axis=1) == 45) and \
       np.all(np.sum(grid, axis=0) == 45) and \
       np.all(np.sum(get_subgrids(grid), axis=1) == 45):
        return True
    return False

if __name__ == '__main__':
    puzzle = [ '043080250600000000000001094900004070000608000010200003820500000000000005034090710',
        '100920000524010000000000070050008102000000000402700090060000000000030945000071006',
        '800010009050807010004090700060701020508060107010502090007040600080309040300050008',
        '000604700706000009000005080070020093800000005430010070050200000300000208002301000',
        '530070000600195000098000060800060003400803001700020006060000280000419005000080079']
    for p in puzzle:
        print(solve(create_grid(p)))
