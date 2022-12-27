from django.urls import path
from .views import MainView, PostDetailView, SignUpView, SignInView, FeedBackView, SuccessView, SearchResultsView, TagView, del_comment
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('blog/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout',),
    path('contact/', FeedBackView.as_view(), name='contact'),
    path('contact/success/', SuccessView.as_view(), name='success'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('tag/<slug>/', TagView.as_view(), name="tag"), 
    path('comment/<int:comment_id>/delete/', del_comment, name='del_comment')
]