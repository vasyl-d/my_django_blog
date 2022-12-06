from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}

admin.site.register(Post, PostAdmin)