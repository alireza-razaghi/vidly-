from django.contrib import admin

from .models import Genre, Movie

class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_per_page = 10

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'release_year', 'number_in_stock', 'daily_rate']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    list_per_page = 10

# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)