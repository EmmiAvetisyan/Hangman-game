from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "date", "rating")
    list_display = ("title", "author", "date", "rating","text")

admin.site.register(Post, PostAdmin)
