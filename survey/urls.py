from django.urls import path

from . import views

app_name = 'survey'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
]
