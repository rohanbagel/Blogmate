from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.index, name= "blog-index"),
    #path('profile/', views.profile, name='users-profile'),
    path('post_detail/', views.post_detail, name = "blog-post-detail")
    
    
]
