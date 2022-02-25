
from django.urls import path

from artsapp import views, admin_views, teacher_views, student_views

urlpatterns = [

   path('', views.home, name='home'),
   path('login/', views.login_view, name='login'),
   path('logout_view/', views.logout_view, name='logout_view'),



   # admin
   path('admin_home/', admin_views.admin_home, name='admin_home'),
   path('welcome/', admin_views.welcome, name='welcome'),
   path('add_group/', admin_views.add_group, name='add_group'),
   path('view_group/', admin_views.view_group, name='view_group'),
   path('update_group/<int:id>/', admin_views.update_group, name='update_group'),
   path('delete_group/<int:id>/', admin_views.delete_group, name='delete_group'),
   path('register_teacher/', admin_views.register_teacher, name='register_teacher'),
   path('view_teacher/', admin_views.view_teacher, name='view_teacher'),
   path('update_teacher/<int:user_id>/', admin_views.update_teacher, name='update_teacher'),
   path('delete_teacher/<int:user_id>/', admin_views.delete_teacher, name='delete_teacher'),
   path('register_student/', admin_views.register_student, name='register_student'),
   path('view_student/', admin_views.view_student, name='view_student'),
   path('assign_group/<int:user_id>/', admin_views.assign_group, name='assign_group'),
   path('update_student/<int:user_id>/', admin_views.update_student, name='update_student'),
   path('delete_student/<int:user_id>/', admin_views.delete_student, name='delete_student'),
   path('add_program/', admin_views.add_program, name='add_program'),
   path('view_program/', admin_views.view_program, name='view_program'),
   path('update_program/<int:id>/', admin_views.update_program, name='update_program'),
   path('delete_program/<int:id>/', admin_views.delete_program, name='delete_program'),
   path('program_register/', admin_views.program_register, name='program_register'),
   path('result_list/', admin_views.result_list, name='result_list'),
   path('view_result/<int:id>/', admin_views.view_result, name='view_result'),
   path('score_board/', admin_views.score_board, name='score_board'),



   path('teacher_home/', teacher_views.teacher_home, name='teacher_home'),
   path('welcome_teacher/', teacher_views.welcome_teacher, name='welcome_teacher'),
   path('members/', teacher_views.members, name='members'),
   path('program_views/', teacher_views.program_views, name='program_views'),
   path('program_updates/<int:id>/', teacher_views.program_updates, name='program_updates'),
   path('add_program_teacher/', teacher_views.add_program_teacher, name='add_program_teacher'),
   path('teacher_register/', teacher_views.teacher_register, name='teacher_register'),
   path('program_result/', teacher_views.program_result, name='program_result'),
   path('add_result/<int:id>/', teacher_views.add_result, name='add_result'),
   path('result_teacher/', teacher_views.result_teacher, name='result_teacher'),
   path('results/<int:id>/', teacher_views.results, name='results'),
   path('scoreboard/', teacher_views.scoreboard, name='scoreboard'),


   path('student_home/', student_views.student_home, name='student_home'),
   path('welcome_student/', student_views.welcome_student, name='welcome_student'),
   path('group_view/', student_views.group_view, name='group_view'),
   path('program_student/', student_views.program_student, name='program_student'),
   path('register_program/<int:id>/', student_views.register_program, name='register_program'),
   path('registered_program/', student_views.registered_program, name='registered_program'),
   path('result_student/', student_views.result_student, name='result_student'),
   path('results_program/<int:id>/', student_views.results_program, name='results_program'),
   path('student_scoreboard/', student_views.student_scoreboard, name='student_scoreboard'),






]
