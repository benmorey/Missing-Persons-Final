from django.urls import path
from .views import landingPageView, tableView, personView


urlpatterns = [
    path('', landingPageView),
    path('table/', tableView, name='table'),
    path('table/<str:personId>', personView, name='personView'),
]
