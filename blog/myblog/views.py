from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from .models import Post


class MainView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all() 
        paginator = Paginator(posts, 3) # 3 объекта на странице

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'myblog/home.html', context={
            'page_obj': page_obj
        })