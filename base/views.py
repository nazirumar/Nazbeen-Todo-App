from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import CreateView, DeleteView, FormView
from .form import TodoAppForm
from .models import TodoApp
from django.urls import reverse_lazy

# Create your views here.


class Index(LoginRequiredMixin, CreateView):
    form_class = TodoAppForm
    model = TodoApp
    success_url ='/'
    context_object_name = 'todo'
    template_name = 'index.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Index, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['todo'] = self.model.objects.filter(user=self.request.user)
        return context


def todoappupdate(request, pk):
    data = get_object_or_404(TodoApp, pk=pk)
    form = TodoAppForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        return redirect('/')
    form = TodoAppForm(instance=data)
    form.fields['title'].widget.attrs['readonly'] = True
    form.fields['description'].widget.attrs={'rows': 2, 'cols': 20}
    context ={'form':form}
    return render(request, 'todo-update.html', context)
            
class DeleteView(LoginRequiredMixin, DeleteView):
    model = TodoApp
    context_object_name = 'todo'
    success_url ="/"
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)

class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, f' welcome {user.username} !!')

        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterPage, self).get(*args, **kwargs)



class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')

