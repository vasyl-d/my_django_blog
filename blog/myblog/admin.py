from django.contrib import admin

# Register your models here.
from .models import Post, FeedBack

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(FeedBack)