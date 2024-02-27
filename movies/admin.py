from django.contrib import admin

# Register your models here.

# Import our models to use with admin app

from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}

    list_display = ("title", "mainactor", "rating")

    list_filter = ("mainactor", "rating", )

# Register our models with the admin app

admin.site.register(Movie, MovieAdmin)