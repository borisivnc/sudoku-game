from django.http import request
from django.shortcuts import render


def render_sudoku(array):
    # print('in script: array = {}'.format(array))
    grid_sudoku = [[8, -1, -1, -1, 1, -1, -1, -1, 9], [-1, 5, -1, 8, -1, 7, -1, 1, -1],
                   [-1,-1, 4, -1, 9, -1, 7, -1, -1], [-1, 6, -1, 7, -1, 1, -1, 2, -1],
                   [5, -1, 8, -1, 6, -1, 1, -1, 7], [-1, 1, -1, 5, -1, 2, -1, 9, -1],
                   [-1, -1, 7, -1, 4, -1, 6, -1, -1], [-1, 8, -1, 3, -1, 9, -1, 4, -1],
                   [3, -1, -1, -1, 5, -1, -1, -1, 8]];
    return grid_sudoku
