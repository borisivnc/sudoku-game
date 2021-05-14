from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from utils.sudoku_grid import render_sudoku
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, "home.html", {})


def login_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        if request.POST.get('submit') == 'register':
            form = CreateUserForm(request.POST)
            print(form.is_valid())
            print(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
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
            print("file:", sudoku_grid.read())
            render_sudoku(sudoku_grid)
            return HttpResponseRedirect('play-sudoku')
    return render(request, "upload_file.html", {})


def play(request):
    return render(request, "play_sudoku.html", {})
