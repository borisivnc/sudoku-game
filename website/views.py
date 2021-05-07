from django.shortcuts import render


def home(request):
    return render(request, "home.html", {})


def sudoku(request):
    return render(request, "sudoku_rules.html", {})


def play(request):
    return render(request, "play_sudoku.html", {})


def login(request):
    return render(request, "login.html", {})


