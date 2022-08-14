from django.urls import path
from . import views


urlpatterns = [
    path('add_to_dict/<int:user_id>/<int:audio_id>/',
         views.add_to_dict, name='add_to_dict'),
    path('delete_from_dict/<int:user_id>/<int:audio_id>/',
         views.delete_from_dict, name='delete_from_dict'),
    path('show_dict/<int:user_id>/',
         views.show_dict, name='show_dict'),
    path('get_audio_ids_from_dict/<int:user_id>/',
         views.get_audio_ids, name='get_audio_ids_from_getcourse_user_dict')
]
