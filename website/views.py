from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from utils.sudoku_grid import render_sudoku
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
            return HttpResponseRedirect('play-sudoku')
    return render(request, "upload_file.html",  {})


def play(request):
    grid = request.session['grid']
    return render(request, "play_sudoku.html", {'grid': grid})
