
from django.urls import path
from . import views
from .views import IndexListView, SnippetDetailView,SnippetUpdateView,SnippetDeleteView,SnippetUserListView,SnippetLanguageListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView  



urlpatterns = [
    path('login/',LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name='login.html'), name='logout'),
    path('', login_required(IndexListView.as_view()), name='index'),
    path('snippets/detail/<int:pk>/',login_required(SnippetDetailView.as_view()), name='snippet'),
    path('snippets/edit/<int:pk>/', login_required(SnippetUpdateView.as_view()), name='snippet_edit'),
    path('snippets/user/', login_required(SnippetUserListView.as_view()), name='user_snippets'),
    path('snippets/language/',login_required(SnippetLanguageListView.as_view()),name ='language'),
    path('snippets/delete/<int:pk>',login_required( SnippetDeleteView.as_view()), name='snippet_delete'),
  
]