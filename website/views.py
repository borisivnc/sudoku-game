from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from utils.sudoku_grid import render_sudoku
from solver.solver import solve
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import numpy as np
import cv2


def home(request):
    return render(request, "home.html", {})


def login_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        if request.POST.get('submit') == 'register':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
            messages.info(request, 'Failed to register')

        elif request.POST.get('submit') == 'login':
            username_ = request.POST.get('userName')
            pwd = request.POST.get('userPassword')

            user = authenticate(request, username=username_, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Email or password is incorrect')
                render(request, "login.html", {'form': form})

    return render(request, "login.html", {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')


def sudoku(request):
    return render(request, "sudoku_rules.html", {})


def upload_file(request):
    if request.method == 'POST':
        sudoku_grid = request.FILES.get("sudokuImage")
        form = UploadFileForm(sudoku_grid)
        if form.is_valid():
            grid = render_sudoku(cv2.imdecode(np.fromstring(sudoku_grid.read(), np.uint8), cv2.IMREAD_UNCHANGED))
            request.session['grid'] = grid
            return HttpResponseRedirect('correct-sudoku-grid')
    return render(request, "upload_file.html",  {})


def correct_sudoku(request):
    grid = request.session['grid']
    if request.method == 'POST':
        new_grid = request.POST.get("new_grid")
        final_grid = np.fromstring(new_grid, sep=',', dtype='int').reshape([9, 9]).tolist()
        request.session['grid'] = final_grid
        return HttpResponseRedirect('play-sudoku')
    return render(request, "correct_grid.html", {'grid': grid})


def play(request):
    grid = request.session['grid']
    if request.method == 'POST':
        final_grid = request.POST.get("final_grid")
        final_time = request.POST.get("final_time")
        grid_result = np.fromstring(final_grid, sep=',', dtype='int').reshape([9, 9]).tolist()
        final_result = solve(np.array(grid))
        print(final_result.tolist())
        print(grid_result)
        if final_result.tolist() == grid_result:
            print("Success!")
            request.session['result'] = "success"
        else:
            print("Fail!")
            request.session['result'] = "fail"

        print(final_time)
        request.session['final_grid'] = grid_result
        request.session['solve_grid'] = final_result.tolist()
        request.session['final_time'] = final_time
        return HttpResponseRedirect('result')
    return render(request, "play_sudoku.html", {'grid': grid})


def result(request):
    if 'final_time' not in request.session:
        return redirect('upload')
    timer = request.session['final_time']
    result = request.session['result']
    solve_grid = request.session['solve_grid']
    tps = timer.split(':')[0]
    return render(request, "result.html", {'timer': timer, 'result': result, 'solve_grid': solve_grid, 'tps': tps})
