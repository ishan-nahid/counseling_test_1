from django.shortcuts import render, redirect
from .forms import User_form, LoginForm
from app_1.models import User


def go_index(request):
    if request.method == "POST":
        form = User_form(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()

            try:
                return redirect('login')
            except Exception as e:
                print("Redirect Exception:", str(e))
        else:
            print("Form errors:", form.errors) 
    else:
        form = User_form()

    return render(request, 'sign_up.html')

def welcome(request):
    return render(request, 'welcome.html')

def profile(request):
    return render(request, 'profile.html')

def student_profile(request):
    return render(request, 'student_profile.html')

def faculty_profile(request,name, id, role):
    context = {
        'name': name,
        'id': id,
        'role': role,
    }
    return render(request, 'faculty_profile.html', context)

from django.urls import reverse
# from django.contrib.auth.hashers import check_password

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                print('not email here')
                user = None

            if user and user.password == password:

                ## just experiment
                # stored_hashed_password = user.password
                # password_matches = check_password(password, stored_hashed_password)
                # if password_matches == True:
                #     print('matches')
                # else:
                #     print('not matches')

                user_data = {
                    'name': f"{user.first_name} {user.last_name}",
                    'id': user.user_id,
                    'role': user.role,
                }

                if user_data['role'] == 'faculty':
                    return redirect(reverse('faculty', args=[user_data['name'], user_data['id'], user_data['role']]))
                else:
                    return redirect('student', {'user_data': user_data})
            else:
                print('pass not match')
                form.add_error(None, 'Invalid email or password')
    else:
        form = LoginForm()

    return render(request, 'login.html')

    