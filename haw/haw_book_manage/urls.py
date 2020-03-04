from django.urls import path
from . import views

app_name = 'haw'
urlpatterns = [
    path('', views.top, name='top'),
    path('create', views.create, name='create'),
    path('update/<int:book_id>', views.update, name='update'),
    path('delete/<int:book_id>', views.delete, name='delete'),
]
