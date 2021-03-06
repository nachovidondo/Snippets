
from django.contrib.auth.views import logout_then_login
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required




urlpatterns = [
    path('',include('snippets.urls')),
    path('admin/', admin.site.urls),


]
