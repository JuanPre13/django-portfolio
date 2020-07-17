from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_blogs, name='allblogs'),
    path('<int:id_blog>/', views.show_blog, name='detail')

] 
