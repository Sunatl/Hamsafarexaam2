from django.views.generic import CreateView,DeleteView,DetailView,UpdateView,ListView
from .models import *
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template import loader

# views.py
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def user_logout(request):
    logout(request) 
    return render(request, 'registration/log_out.html') 



class UserListView(ListView):
    model = User
    template_name = 'list_u.html'
    
class UserDetailView(DetailView):
    model = User
    template_name = 'detail_u.html'
    
class UserCreateView(CreateView):
    model = User
    template_name = 'create_u.html'
    fields = ['fullname','username','email','phone',"image"]
    success_url = reverse_lazy('list_u') 
    
    
class UserUpdateView(UpdateView):
    model = User
    template_name = 'update_u.html'
    fields = ['fullname','username','email','phone',"image"]
    success_url = reverse_lazy('list_u') 
    
    
class UserDeleteView(DeleteView):
    model = User
    template_name = 'delete_u.html'
    success_url = reverse_lazy('list_u') 
    
def base(request):
    template = loader.get_template("base.html")
    return HttpResponse(template.render())
def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

    

    
    
    
# Talant

class TalantListView(ListView):
    model = CompanionRequest
    template_name = 'list_m.html'
    
class TalantDetailView(DetailView):
    model = CompanionRequest
    template_name = 'detail_m.html'
    
class TalantCreateView(CreateView):
    model = CompanionRequest
    template_name = 'create_m.html'
    fields = ['user','trip','start_location','end_location','date','description']
    success_url = reverse_lazy('list_m') 
    

class TalantUpdateView(UpdateView):
    model = CompanionRequest
    template_name = 'update_m.html'
    fields = ['user','trip','start_location','end_location','date','description']
    success_url = reverse_lazy('list_m') 
    
    
class TalantDeleteView(DeleteView):
    model = CompanionRequest
    template_name = 'delete_m.html'
    success_url = reverse_lazy('list_m') 
    
    
    


# Aplication 
class AplicationListView(ListView):
    model = Trip
    template_name = 'list_o.html'
    
class AplicationDetailView(DetailView):
    model = Trip
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["vakansi"] = CompanionRequest.objects.filter(trip = self.kwargs['pk'])
        return context
    template_name = 'detail_o.html'
    
class AplicationCreateView(CreateView):
    model = Trip
    template_name = 'create_o.html'
    fields = ['user','image','start_location','end_location','date','description']
    success_url = reverse_lazy('list_o') 
    
    
class AplicationUpdateView(UpdateView):
    model = Trip
    template_name = 'update_o.html'
    fields = ['user','image','start_location','end_location','date','description']
    success_url = reverse_lazy('list_o') 
    
    
class AplicationDeleteView(DeleteView):
    model = Trip
    template_name = 'delete_o.html'
    success_url = reverse_lazy('list_o') 