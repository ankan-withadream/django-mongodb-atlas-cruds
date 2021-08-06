from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('comments', views.all_comments),
    path('movies', views.all_movies),
    path('users', views.all_users),

    path('add_comment', views.add_comment),
    path('add_movie', views.add_movie),
    path('add_user', views.add_user),

    path('update_comment/<str:name>', views.update_comment),
    path('update_movie/<str:title>', views.update_movie),
    path('update_user/<str:name>', views.update_user),

    path('delete_comment/<str:name>', views.delete_comment),
    path('delete_movie/<str:title>', views.delete_movie),
    path('delete_user/<str:name>', views.delete_user)
]
