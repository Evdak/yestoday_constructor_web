from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, JsonResponse
from .services_getcourse import add_audio_to_getcourse_user_dict, add_notifications_to_student, delete_audio_from_getcourse_user_dict, show_getcourse_user_dict, get_audio_ids_from_getcourse_user_dict, add_student, book_lesson, unbook_lesson, book_lesson_teacher, unbook_lesson_teacher, get_lessons, get_lessons_today, get_lessons_teacher, get_lessons_today_teacher, get_available_lessons_teacher_by_student, get_available_lessons_teacher, get_info_for_student

from .tasks import send_notifications, delete_previous_zoom_meetings

from datetime import datetime
from django.utils import timezone
import re


def add_to_dict_view(request: HttpRequest, user_id: int, audio_id: int):
    return JsonResponse({"status": add_audio_to_getcourse_user_dict(user_id, audio_id)})


def delete_from_dict_view(request: HttpRequest, user_id: int, audio_id: int):
    return JsonResponse({"status": delete_audio_from_getcourse_user_dict(user_id, audio_id)})


def show_dict_view(request: HttpRequest, user_id: int):
    return JsonResponse({"status": show_getcourse_user_dict(user_id)})


def get_audio_ids_view(request: HttpRequest, user_id: int):
    return JsonResponse({"status": get_audio_ids_from_getcourse_user_dict(user_id)})


@csrf_exempt
def add_student_view(request: HttpRequest):
    user_id = request.GET.get('user_id')
    name = request.GET.get('name')
    surname = request.GET.get('surname')
    email = request.GET.get('email')
    teacher_id = request.GET.get('teacher_id')
    hours = request.GET.get('hours')

    s = []
    for t in hours.split():
        try:
            s.append(float(t))
        except ValueError:
            pass
    hours = sum(s)

    if not surname:
        surname = ' '

    if all((user_id, name, email, teacher_id, hours)):
        if add_student(user_id, name, surname, email, teacher_id, hours):
            return JsonResponse(
                {
                    "status": "OK",
                    "msg": "???????????? ??????????????????????????????"
                }
            )
        else:
            return JsonResponse(
                {
                    "status": "ERROR",
                    "msg": "?????????????????? ????????????, ???????????????????? ?????? ??????"
                }
            )
    else:
        return JsonResponse(
            {
                "status": "ERROR",
                "msg": "?????????????????????? ?????????????? ????????????"
            }
        )


@csrf_exempt
def book_lesson_view(request: HttpRequest):
    user_id = request.GET.get('user_id')
    date_time = request.GET.get('date_time')

    if all((user_id, date_time)):
        try:
            date_time = date_time.replace(' ', '+')
            date_time = timezone.datetime.fromisoformat(date_time)
        except Exception as err:
            return JsonResponse(
                {
                    "status": "ERROR",
                    "msg": "?????????????????????? ?????????????? ????????????",
                    "err": str(err)
                }
            )

        return JsonResponse(book_lesson(user_id, date_time))
    else:
        return JsonResponse(
            {
                "status": "ERROR",
                "msg": "?????????????????????? ?????????????? ????????????"
            }
        )


@csrf_exempt
def unbook_lesson_view(request: HttpRequest):
    user_id = request.GET.get('user_id')
    date_time = request.GET.get('date_time')

    if all((user_id, date_time)):
        try:
            date_time = date_time.replace(' ', '+')
            date_time = timezone.datetime.fromisoformat(date_time)
        except Exception as err:
            return JsonResponse(
                {
                    "status": "ERROR",
                    "msg": "?????????????????????? ?????????????? ????????????",
                    "err": str(err)
                }
            )

        return JsonResponse(unbook_lesson(user_id, date_time))
    else:
        return JsonResponse(
            {
                "status": "ERROR",
                "msg": "?????????????????????? ?????????????? ????????????"
            }
        )


@csrf_exempt
def book_lesson_teacher_view(request: HttpRequest):
    user_id = request.GET.get('user_id')
    date_time = request.GET.get('date_time')

    if all((user_id, date_time)):
        try:
            date_time = date_time.replace(' ', '+')
            date_time = timezone.datetime.fromisoformat(date_time)
            return JsonResponse(book_lesson_teacher(user_id, date_time))
        except Exception as err:
            return JsonResponse(
                {
                    "status": "ERROR",
                    "msg": "?????????????????????? ?????????????? ????????????",
                    "err": str(err)
                }
            )

    else:
        return JsonResponse(
            {
                "status": "ERROR",
                "msg": "?????????????????????? ?????????????? ????????????"
            }
        )


@csrf_exempt
def unbook_lesson_teacher_view(request: HttpRequest):
    user_id = request.GET.get('user_id')
    date_time = request.GET.get('date_time')

    if all((user_id, date_time)):
        try:
            date_time = date_time.replace(' ', '+')
            date_time = timezone.datetime.fromisoformat(date_time)
        except Exception as err:
            return JsonResponse(
                {
                    "status": "ERROR",
                    "msg": "?????????????????????? ?????????????? ????????????",
                    "err": str(err)
                }
            )

        return JsonResponse(unbook_lesson_teacher(user_id, date_time))
    else:
        return JsonResponse(
            {
                "status": "ERROR",
                "msg": "?????????????????????? ?????????????? ????????????"
            }
        )


@csrf_exempt
def get_lessons_view(request: HttpRequest):
    user_id = request.GET.get('user_id')
    if user_id:
        return JsonResponse(get_lessons(user_id=user_id))


@csrf_exempt
def get_lessons_today_view(request: HttpRequest):
    user_id = request.GET.get('user_id')
    date_time = request.GET.get('date_time')
    if all((user_id, date_time)):
        try:
            date_time = date_time.replace(' ', '+')
            date_time = timezone.datetime.fromisoformat(date_time)
            return JsonResponse(get_lessons_today(user_id=user_id, date_time=date_time))
        except Exception as err:
            return JsonResponse(
                {
                    "status": "ERROR",
                    "msg": "?????????????????????? ?????????????? ????????????",
                    "err": str(err)
                }
            )


@csrf_exempt
def get_lessons_teacher_view(request: HttpRequest):
    user_id = request.GET.get('user_id')
    if user_id:
        return JsonResponse(get_lessons_teacher(user_id=user_id))


@csrf_exempt
def get_available_lessons_teacher_by_student_view(request: HttpRequest):
    user_id = request.GET.get('user_id')
    if user_id:
        return JsonResponse(get_available_lessons_teacher_by_student(user_id=user_id))


@csrf_exempt
def get_available_lessons_teacher_view(request: HttpRequest):
    user_id = request.GET.get('user_id')
    if user_id:
        return JsonResponse(get_available_lessons_teacher(user_id=user_id))


@csrf_exempt
def get_lessons_teacher_today_view(request: HttpRequest):
    user_id = request.GET.get('user_id')
    date_time = request.GET.get('date_time')
    if all((user_id, date_time)):
        try:
            date_time = date_time.replace(' ', '+')
            date_time = timezone.datetime.fromisoformat(date_time)
            return JsonResponse(get_lessons_today_teacher(user_id=user_id, date_time=date_time))
        except Exception as err:
            return JsonResponse(
                {
                    "status": "ERROR",
                    "msg": "?????????????????????? ?????????????? ????????????",
                    "err": str(err)
                }
            )


@csrf_exempt
def get_info_for_student_view(request: HttpRequest):
    user_id = request.GET.get('user_id')
    if user_id:
        try:
            return JsonResponse(get_info_for_student(user_id=user_id))
        except Exception as err:
            return JsonResponse(
                {
                    "status": "ERROR",
                    "msg": "?????????????????????? ?????????????? ????????????",
                    "err": str(err)
                }
            )


@csrf_exempt
def send_notifications_view(requset: HttpRequest):
    send_notifications()
    return JsonResponse({"status": "OK"})


@csrf_exempt
def add_notifications_view(request: HttpRequest, getcourse_id: str, client_id: str):

    if all([getcourse_id, client_id]):
        try:
            return JsonResponse(add_notifications_to_student(getcourse_id, client_id))
        except Exception as err:
            return JsonResponse(
                {
                    "status": "ERROR",
                    "msg": "?????????????????? ????????????, ???????????????????? ?????? ?????? ?????? ???????????????????? ?? ??????????????????",
                }
            )

    else:
        return JsonResponse(
            {
                "status": "ERROR",
                "msg": "?????????????????????? ?????????????? ????????????, ???????????????????? ?????? ??????"
            }
        )


@csrf_exempt
def delete_previous_zoom_meetings_view(request: HttpRequest):
    delete_previous_zoom_meetings()
    return JsonResponse({"status": "OK"})
