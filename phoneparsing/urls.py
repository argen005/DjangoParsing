from django.contrib import admin
from django.urls import path
from phones import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('parse/myphone/', views.parse_myphone, name='parse_myphone'),
    path('parse/sulpak/', views.parse_sulpak, name='parse_sulpak'),
    path('parse/softech/', views.parse_softech, name='parse_softech'),
]

