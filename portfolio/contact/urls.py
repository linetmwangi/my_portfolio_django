from django.urls import path
from . import views
from .views import contact_view

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('contact/', contact_view, name='contact'),
    path('create/', views.contact_create, name='contact_create'),
    path('<int:pk>/update/', views.contact_update, name='contact_update'),
    path('<int:pk>/delete/', views.contact_delete, name='contact_delete'),
]
