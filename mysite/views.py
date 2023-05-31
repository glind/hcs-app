from django.shortcuts import  render, redirect
from .forms import RegistrationForm, RegistrationUpdateForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from bootstrap_modal_forms.generic import BSModalCreateView

from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db import transaction


from django.contrib import messages


def register(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        try:
            with transaction.atomic():
                # Create a new user object
                user = form.save()
                
                messages.info(request, "You are now Registered, please login.")
                redirect("/login")
                
                
        except Exception as e:
            error_message = str(e)
            form.add_error(None, error_message)  # Add the error to non-field errors
            messages.error(request, error_message)  # Optional: Add the error to messages framework

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = RegistrationUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
        messages.info(request, "You have not Registered as Bounty Hunter or Setter, please contact support.")
    else:
        form = RegistrationUpdateForm(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'register_update.html', context)


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user, backend='django.contrib.auth.backends.ModelBackend')
				messages.info(request, "You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("/")


