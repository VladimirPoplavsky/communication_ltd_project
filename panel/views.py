from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import PasswordResetView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views     # Used in urls.py
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.decorators import method_decorator
from django.views.generic import View, UpdateView, CreateView, DeleteView, ListView  # class based view

from .forms import ClientForm, PlanForm, RegisterForm, LoginForm
from .models import Plan, Userprofile


# Create your views here.

# Login Employee
class LoginEmployeeView(View):
    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            return redirect('panel')
        form = LoginForm()
        return render(request, 'panel/login.html', {'form': form})

    @staticmethod
    def post(request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('panel')
            else:
                form.add_error(None, 'Invalid username or password')

        return render(request, 'panel/login.html', {'form': form})


# Employee Logout
class UserLogoutView(View):
    @staticmethod
    def get(request):
        logout(request)
        messages.success(request, "logout successfully")
        return redirect(reverse_lazy('login'))


# Add Employee
class RegisterEmployeeView(View):
    @method_decorator(login_required(login_url="login"))
    def get(self, request):
        form = RegisterForm()
        return render(request, 'panel/register.html', {'form': form})

    @method_decorator(login_required(login_url="login"))
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            user = User.objects.create_user(first_name=first_name,
                                            last_name=last_name,
                                            username=username,
                                            email=email,
                                            password=password1)

            messages.success(request, f'Account created for {user.username}')

            return redirect('panel')

        return render(request, 'panel/register.html', {'form': form})


# Email Password Reset
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'panel/password_reset.html'
    email_template_name = 'panel/password_reset_email.html'
    subject_template_name = 'panel/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('login')


# Change Employee Password
@method_decorator(login_required(login_url='login'), name='dispatch')
class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'panel/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('panel')


# Main Screen Dashboard
@login_required(login_url="login")
def panel(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        # --
        user = Userprofile.objects.filter(user__icontains=search_query)
    else:
        user = Userprofile.objects.all()

    plans = Plan.objects.all()
    total_plan = plans.count()
    total_user = Userprofile.objects.all().count()

    page = request.GET.get('page')
    results = 5
    paginator = Paginator(user, results)
    try:
        user = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        user = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        user = paginator.page(page)

    left = (int(page) - 1)
    if left < 1:
        left = 1
    right = (int(page) + 2)
    if right > paginator.num_pages:
        right = paginator.num_pages + 1
    custom_range = range(left, right)

    context = {'plans': plans,
               'total_plan': total_plan,
               'user': user,
               'search_query': search_query,
               'paginator': paginator,
               'custom_range': custom_range,
               'total_user': total_user}

    return render(request, 'panel/panel.html', context)


# Get Plan List
@method_decorator(login_required(login_url='login'), name='dispatch')
class PlanListView(ListView):
    model = Plan
    template_name = 'panel/plans.html'
    context_object_name = 'plans'  # Set the name of the context variable to 'plans'


# Add a Plan
@method_decorator(login_required(login_url='login'), name='dispatch')
class AddPlanView(CreateView):
    form_class = PlanForm
    model = Plan
    template_name = 'panel/add_plan.html'
    success_url = reverse_lazy('panel')

    def form_valid(self, form):
        messages.success(self.request, "Plan created successfully")
        return super().form_valid(form)


# Delete a Plan
@method_decorator(login_required(login_url='login'), name='dispatch')
class DeletePlanView(DeleteView):
    model = Plan
    success_url = reverse_lazy('panel')

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, "Plan deleted successfully")
        return super().delete(request, *args, **kwargs)


# Update a Plan
@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdatePlanView(UpdateView):
    model = Plan
    form_class = PlanForm
    success_url = reverse_lazy('panel')
    template_name = 'panel/update_plan.html'
    pk_url_kwarg = 'pk'

    def form_valid(self, form):
        messages.info(self.request, 'Plan updated successfully')
        return super().form_valid(form)


# Add New Client
@method_decorator(login_required(login_url='login'), name='dispatch')
class AddClientView(CreateView):
    form_class = ClientForm
    template_name = 'panel/add_client.html'
    success_url = reverse_lazy('panel')

    def form_valid(self, form):
        messages.success(self.request, 'Client added successfully')
        return super().form_valid(form)


# Update Exist Client
@login_required(login_url="login")
def update_client(request, pk):
    try:
        user = Userprofile.objects.get(user=pk)
        form = ClientForm(instance=user)
        if request.method == 'POST':
            form = ClientForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
            messages.info(request, 'User updated successfully')
            return redirect('panel')
    except:
        print("Something went wrong")

    return render(request, 'panel/update_client.html', {'form': form})


# Delete a Client
@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteClientView(DeleteView):
    model = Userprofile
    success_url = reverse_lazy('panel')
    pk_url_kwarg = 'pk'

    def delete(self, request, *args, **kwargs):
        messages.info(self.request, 'User deleted successfully')
        return super().delete(request, *args, **kwargs)


# To View a Client Profile
@login_required(login_url="login")
def view_client(request, pk):
    user = Userprofile.objects.filter(user=pk)
    context = {'user': user}
    return render(request, 'panel/view_client.html', context)
