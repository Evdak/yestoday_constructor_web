from django.http import HttpRequest, JsonResponse
from .services_getcourse import add_audio_to_getcourse_user_dict, delete_audio_from_getcourse_user_dict, show_getcourse_user_dict, get_audio_ids_from_getcourse_user_dict


def add_to_dict(request: HttpRequest, user_id: int, audio_id: int):
    return JsonResponse({"status": add_audio_to_getcourse_user_dict(user_id, audio_id)})


def delete_from_dict(request: HttpRequest, user_id: int, audio_id: int):
    return JsonResponse({"status": delete_audio_from_getcourse_user_dict(user_id, audio_id)})


def show_dict(request: HttpRequest, user_id: int):
    return JsonResponse({"status": show_getcourse_user_dict(user_id)})


def get_audio_ids(request: HttpRequest, user_id: int):
    return JsonResponse({"status": get_audio_ids_from_getcourse_user_dict(user_id)})
