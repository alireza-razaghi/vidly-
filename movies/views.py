from django.shortcuts import render ,get_object_or_404
from .models import Movie 
# Create your views here.
def home_page(request):
    movies = Movie.objects.all()  # pylint: disable=no-member
    return render(request, 'index.html', {'movies': movies})

def movie_detail(_request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(_request, 'detail.html', {'movie': movie})
