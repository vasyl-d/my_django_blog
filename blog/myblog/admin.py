from django.contrib import admin

# Register your models here.
from .models import Post, FeedBack, Tag, Comment

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}

admin.site.register(Post, PostAdmin)
admin.site.register(FeedBack)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)