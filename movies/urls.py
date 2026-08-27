from django.urls import path
from .views import home_page , movie_detail

app_name = 'movies'

urlpatterns = [
    path('index/',home_page,name='home_page'),
    path('<int:movie_id>/', movie_detail, name='movie_detail'),

]
