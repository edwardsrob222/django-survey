from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    # path('signup/', views.SignUpView.as_view(), name='signup'),
    path('', views.IndexView.as_view(), name='index'),
    path('all/', views.CreateView.as_view(), name='create'),
]
