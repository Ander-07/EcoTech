
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from app_doacao_coleta import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')),
    path('', lambda request: redirect('/auth/login/')),
    path('plataforma/', include('plataforma.urls')),
    path('coleta/', views.coleta, name='coleta')
]
