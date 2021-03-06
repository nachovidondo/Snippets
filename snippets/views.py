
from django.contrib.auth.views import LoginView
from django.db.models.base import Model
from django.views.generic.edit import DeleteView
from snippets.forms import SnippetForm
from django.shortcuts import render,redirect,reverse
from .models import Language, Snippet
from django.views.generic import ListView,DetailView,UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login,logout


class IndexListView(ListView):
    model = Snippet
    template_name =  'index.html'
    context_object_name = 'snippets'
    queryset= Snippet.objects.filter(public=True)
   
class SnippetDetailView(DetailView):
    model = Snippet
    template_name  = 'snippets/snippet.html'
    

class SnippetUserListView(ListView, LoginRequiredMixin):
    model = Snippet
    template_name = 'snippets/user_snippets.html'
    
    def get_queryset(self):
        return Snippet.objects.filter(user=self.request.user)
   

class SnippetLanguageListView(ListView):
    model = Snippet
    template_name ='snippets/snippet_language.html'
    
    def get_queryset(self):
        qs= Snippet.objects.filter(public=True)
        language_id = self.request.GET.get('lang')
        if language_id:
            qs = qs.filter(language__id = language_id)
            
        return qs    

class SnippetUpdateView(UpdateView):
    model = Snippet
    template_name = 'snippets/snippet_edit.html'
    form_class = SnippetForm
    success_url = reverse_lazy('index')
   
class SnippetDeleteView(DeleteView,LoginRequiredMixin):
    model = Snippet
    success_url = reverse_lazy('index')
    def get_queryset(self):
        return Snippet.objects.filter(user=self.request.user)
 



   


   







            
     