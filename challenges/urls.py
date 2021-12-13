from django.urls import path

from . import views
urlpatterns = [
   # path("january",views.index),
  #  path('january', views.january, name = 'home'),
  #  path('february', views.february ,name = 'february'),
  path("<int:month>",views.monthly_challenge_by_number, name='month number'),
path("<str:month>", views.monthly_challenge, name='month')
]
