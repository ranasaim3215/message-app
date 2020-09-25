from django.urls import path
from .views import MessegeView
urlpatterns = [
    path('',MessegeView.as_view(),name='home')
]