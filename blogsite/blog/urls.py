from django.urls import path
from .views import postslist, postdetail

urlpatterns = [
    path('', postslist.as_view(), name='post'),
    path('<slug:slug>/', postdetail.as_view(), name='post_detail'),
]



