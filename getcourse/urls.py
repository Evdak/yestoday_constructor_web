from django.urls import path
from . import views

urlpatterns = [
    path('add_to_dict/<int:user_id>/<int:audio_id>/',
         views.add_to_dict_view, name='add_to_dict'),
    path('delete_from_dict/<int:user_id>/<int:audio_id>/',
         views.delete_from_dict_view, name='delete_from_dict'),
    path('show_dict/<int:user_id>/',
         views.show_dict_view, name='show_dict'),
    path('get_audio_ids_from_dict/<int:user_id>/',
         views.get_audio_ids_view, name='get_audio_ids_from_getcourse_user_dict'),
    path('add_student',
         views.add_student_view, name='add_student'),
    path('book_lesson',
         views.book_lesson_view, name='book_lesson'),
    path('unbook_lesson',
         views.unbook_lesson_view, name='unbook_lesson'),
    path('book_lesson_teacher',
         views.book_lesson_teacher_view, name='book_lesson_teacher'),
    path('unbook_lesson_teacher',
         views.unbook_lesson_teacher_view, name='unbook_lesson_teacher'),
    path('get_lessons',
         views.get_lessons_view, name='get_lessons'),
    path('get_lessons_today',
         views.get_lessons_today_view, name='get_lessons_today'),
    path('get_available_lessons_teacher_by_student',
         views.get_available_lessons_teacher_by_student_view, name='get_available_lessons_teacher_by_student'),
    path('get_available_lessons_teacher',
         views.get_available_lessons_teacher_view, name='get_available_lessons_teacher'),
    path('get_lessons_teacher',
         views.get_lessons_teacher_view, name='get_lessons_teacher_view'),
    path('get_lessons_teacher_today',
         views.get_lessons_teacher_today_view, name='get_lessons_teacher_today_view'),
    path('get_info_for_student',
         views.get_info_for_student_view, name='get_info_for_student_view'),
    path('send_notifications',
         views.send_notifications_view, name='send_notifications_view'),
    path('add_notifications',
         views.add_notifications_view, name='add_notifications_view'),
]
