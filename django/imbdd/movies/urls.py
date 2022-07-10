from django.urls import path
from . import views
from .views import(
                MovieListView,              
)
urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movies'),
    path('movies/delete/<uuid:id>/', views.delete, name='delete'),
    path('movies/update/<uuid:id>', views.update, name='update'),
    path('movies/update/updaterecord/<uuid:id>', views.updaterecord, name='update'),
]