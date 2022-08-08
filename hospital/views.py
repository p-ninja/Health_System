import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, DoctorUserCreationForm

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver

from .models import Patient, Doctor_Information


# Create your views here.

# function to return views for the urls


def hospital_home(request):
    return render(request, 'index-2.html')


def doctor_dashboard(request):
    return render(request, 'doctor-dashboard.html')


def doctor_profile(request):
    return render(request, 'doctor-profile.html')


def doctor_change_password(request):
    return render(request, 'doctor-change-password.html')


def change_password(request):
    return render(request, 'change-password.html')


def search(request):
    return render(request, 'search.html')


def doctor_profile_settings(request):
    return render(request, 'doctor-profile-settings.html')


def my_patients(request):
    return render(request, 'my-patients.html')


def add_billing(request):
    return render(request, 'add-billing.html')


def add_prescription(request):
    return render(request, 'add-prescription.html')


def appointments(request):
    return render(request, 'appointments.html')


def booking_success(request):
    return render(request, 'booking-success.html')


def booking(request):
    return render(request, 'booking.html')


def edit_billing(request):
    return render(request, 'edit-billing.html')


def edit_prescription(request):
    return render(request, 'edit-prescription.html')


def forgot_password(request):
    return render(request, 'forgot-password.html')


def patient_dashboard(request):
    return render(request, 'patient-dashboard.html')


def patient_profile(request):
    return render(request, 'patient-profile.html')


def privacy_policy(request):
    return render(request, 'privacy-policy.html')


def profile_settings(request):
    return render(request, 'profile-settings.html')


def schedule_timings(request):
    return render(request, 'schedule-timings.html')


# def authenticate_user(email, password):
#     try:
#         user = User.objects.get(email=email)
#     except User.DoesNotExist:
#         return None
#     else:
#         if user.check_password(password):
#             return user


def login_user(request):
    page = 'login'
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('hospital_home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User Logged out')
    return redirect('login')


# def register(request):
#     return render(request, 'register.html')


def registerPatient(request):
    page = 'patient-register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            # commit=False --> don't save to database yet (we have a chance to modify object)
            user = form.save(commit=False)
            # user.username = user.username.lower()  # lowercase username
            user.save()

            messages.success(request, 'User account was created!')

            # After user is created, we can log them in
            #login(request, user)
            return redirect('login')

        else:
            messages.error(
                request, 'An error has occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'register.html', context)


# @receiver(post_save, sender=Patient)
# def deleteUser(sender, instance, **kwargs):
#     try:
#         user = instance.user
#         user.delete()
#     except:
#         pass


def doctor_register(request):
    page = 'doctor-register'
    form = DoctorUserCreationForm()

    if request.method == 'POST':
        form = DoctorUserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            # commit=False --> don't save to database yet (we have a chance to modify object)
            user = form.save(commit=False)
            # user.username = user.username.lower()  # lowercase username
            user.save()

            messages.success(request, 'Doctor account was created!')

            # After user is created, we can log them in
            #login(request, user)
            return redirect('login')

        else:
            messages.error(
                request, 'An error has occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'doctor-register.html', context)
