from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),

    path('create/', views.create, name='create'),

    path('<int:post_id>/create/comment/', views.comment_create, name='comment_create'),

    path('<int:post_id>/comment/<int:id>/delete/', views.delete, name='delete'),

    path('<int:id>/update/', views.update, name='update'),
]