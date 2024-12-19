from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("quiz/<uuid:uuid>", views.quiz, name="quiz"),
    path("quiz/save-result/<uuid:uuid>", views.save_result, name="save-result"),
    path("quiz/result/<uuid:uuid>", views.result, name="result"),
]