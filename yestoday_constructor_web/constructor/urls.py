from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz1',
         views.quiz1, name='quiz1'),
    path('quiz2',
         views.quiz2, name='quiz2'),
    path('quiz3',
         views.quiz3, name='quiz3'),
    path('quiz4',
         views.quiz4, name='quiz4'),
    path('quiz5',
         views.quiz5, name='quiz5'),
    path('quiz6',
         views.quiz6, name='quiz6'),
    path('quiz7',
         views.quiz7, name='quiz7'),
    path('quiz8',
         views.quiz8, name='quiz8'),
    path('quiz9',
         views.quiz9, name='quiz9'),
    path('audio',
         views.audio, name='audio'),
    path('cards',
         views.cards, name='cards'),
    path('quizphoto',
         views.quizphoto, name='quizphoto'),
    path('translate',
         views.translate, name='translate'),
    path('translateNew',
         views.translate_new, name='translateNew'),
    path('audio_tts',
         views.audio_tts, name='audio_tts'),
    path('video',
         views.video, name='video'),
    path('quizOrder',
         views.quizOrder, name='quizOrder'),
    path('stt',
         views.stt, name='stt'),
    path('quiztable',
         views.quiztable, name='quiztable'),
    path('audioQuiz5',
         views.audioQuiz5, name='audioQuiz5'),
    path('textAudio',
         views.textAudio, name='textAudio'),
    path('start',
         views.start_view, name='start_view'),
    path('nextslide',
         views.nextslide_view, name='nextslide_view'),
    path('end',
         views.end_view, name='end_view'),
]
