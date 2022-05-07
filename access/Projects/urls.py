from django.urls import path, include
from . import views
app_name = 'Projects'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('contact/', views.contact, name='contact'),
]
