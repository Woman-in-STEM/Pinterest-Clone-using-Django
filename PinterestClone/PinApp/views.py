from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Board, Pin
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
import json

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        birthdate = request.POST['birthdate']
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('register')
        user = User.objects.create_user(username=email, password=password)
        user.save()
        messages.success(request, "Registration successful. Please log in.")
        return redirect('login')
    return render(request, 'login_register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('login')
    return render(request, 'login_register.html')


@login_required
def home(request):
    if request.user.is_authenticated:
        pins = Pin.objects.filter(board__user=request.user)  # Only pins of the signed-in user's boards
    else:
        pins = []  # Empty queryset if the user is not authenticated
    return render(request, "home.html", {'pins': pins})


@login_required
def profile(request):
    user = request.user
    boards = Board.objects.filter(user=user)
    pins = Pin.objects.filter(board__user=user)
    return render(request, 'profile.html', {'boards': boards, 'pins': pins})


@login_required
def create_board(request):
    if request.method == "POST":
        try:
            # Get the board name from the POST request
            data = json.loads(request.body)  # Parse JSON payload
            board_name = data.get("name")

            if not board_name:
                return JsonResponse({"error": "Board name cannot be empty."}, status=400)

            # Create a new Board instance
            Board.objects.create(name=board_name, user=request.user)

            # Return success response
            return JsonResponse({"message": "Board successfully created!"}, status=200)

        except Exception as e:
            # Handle unexpected errors
            return JsonResponse({"error": str(e)}, status=500)

    # Render the create_board.html page for GET requests
    return render(request, "create_board.html")


@login_required
def delete_board(request, board_id):
    board = get_object_or_404(Board, id=board_id, user=request.user)
    board.delete()
    return redirect("profile")


@login_required
def create_pin(request):
    if request.method == "POST":
        title = request.POST.get('title')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        board_id = request.POST.get('board')

        board = Board.objects.get(id=board_id, user=request.user)
        Pin.objects.create(title=title, image=image, description=description, board=board)
        
        messages.success(request, "Pin successfully created!")
        return redirect('create_pin')

    boards = Board.objects.filter(user=request.user)
    return render(request, 'create_pin.html', {'boards': boards})

@login_required
def delete_pin(request, pin_id):
    pin = get_object_or_404(Pin, id=pin_id, board__user=request.user)
    pin.delete()
    return redirect("profile")
