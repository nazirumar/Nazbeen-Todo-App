from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .form import TodoAppForm
from .models import TodoApp
# Create your views here.


class Index(CreateView):
    form_class = TodoAppForm
    model = TodoApp
    success_url ='/'
    template_name = 'index.html'
    def form_valid(self, form):
        form.save()
        print(form)
        return super().form_valid(form)
    def get(self, request):
        todo = TodoApp.objects.all()
        context ={
            'todo': todo
        }
        return render(request, self.template_name, context)




def todoAppDelete(request, pk):
    data = get_object_or_404(TodoApp, pk=pk) 
    data.delete()
    return redirect('/')



def todoappupdate(request, pk):
    data = get_object_or_404(TodoApp, pk=pk)
    form = TodoAppForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        return redirect('/')
    form = TodoAppForm(instance=data)
    form.fields['title'].widget.attrs['readonly'] = True
    context ={'form':form}
    return render(request, 'todo-update.html', context)
            


class TodoAppDetail(DetailView):
    model = TodoApp
    fields = '__all__'
    success_url = '/'
    template_name = 'index.html'