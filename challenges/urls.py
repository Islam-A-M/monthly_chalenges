from django.urls import path

from . import views
urlpatterns = [
   # path("january",views.index),
  #  path('january', views.january, name = 'home'),
  #  path('february', views.february ,name = 'february'),
  path("",views.index,name="index"),
  
  path("<int:month>",views.monthly_challenge_by_number, name='month-challenge-number'),
  path("<str:month>", views.monthly_challenge, name='month-challenge')
]
