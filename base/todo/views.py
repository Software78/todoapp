from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render,redirect
from .models import Task
from django.views.generic import DeleteView,UpdateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, redirect_to_login
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def Index(request,):
    if request.user.is_authenticated == True:
        items = Task.objects.all()
        context = {'items':items}
        return render(request,'html/index.html',context)
    else:
        return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'html/signup.html', {'form': form})

def logout(request):
    logout(request)

class UpdateTask(UpdateView):
    model = Task
    fields = ['title','complete']
    context_object_name = 'item'
    template_name = 'html/update.html'
    success_url = reverse_lazy('index')

class DeleteTask(DeleteView):
    model = Task
    template_name = 'html/confirm_delete.html'
    success_url = reverse_lazy('index')

class CreateTask(CreateView):
    model = Task
    fields = ['title']
    template_name = 'html/index.html'
    success_url = reverse_lazy('index')