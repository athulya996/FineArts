
from django.urls import path

from artsapp import views, admin_views

urlpatterns = [

   path('', views.home, name='home'),
   path('login/', views.login, name='login'),
   path('admin_home/', views.admin_home, name='amin_home'),


   path('add_group/', admin_views.add_group, name='add_group'),
   path('view_group/', admin_views.view_group, name='view_group'),
   path('update_group/<int:id>/', admin_views.update_group, name='update_group'),
   path('delete_group/<int:id>/', admin_views.delete_group, name='delete_group'),
   path('register_teacher/', admin_views.register_teacher, name='register_teacher'),
   path('view_teacher/', admin_views.view_teacher, name='view_teacher'),
   path('update_teacher/<int:id>/', admin_views.update_teacher, name='update_teacher'),
   path('delete_teacher/<int:id>/', admin_views.update_group, name='update_group'),




]
